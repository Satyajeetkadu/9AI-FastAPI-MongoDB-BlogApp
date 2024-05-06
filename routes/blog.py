from fastapi import APIRouter, HTTPException
from models.blog import BlogModel, UpdateBlogModel, CommentModel
from config.config import blogs_collection, comments_collection,likes_collection
from serializers.blog import DecodeBlogs, DecodeBlog,DecodeComment
import datetime
from bson import ObjectId


blog_root = APIRouter()

# post request 
@blog_root.post("/new/blog")
def NewBlog(doc:BlogModel):
    doc = dict(doc)
    current_date = datetime.date.today()
    doc["date"] = str(current_date )
    
    res = blogs_collection.insert_one(doc)

    doc_id = str(res.inserted_id )

    return {
        "status" : "ok" ,
        "message" : "Blog posted successfully" , 
        "_id" : doc_id
    }
    

# getting blogs 
@blog_root.get("/all/blogs")
def AllBlogs():
    res =  blogs_collection.find() 
    decoded_data = DecodeBlogs(res)

    for blog in decoded_data:
        blog["likes"] = []
        blog["dislikes"] = []
        blog["comments"] = []

    return {
        "status": "ok" , 
        "data" : decoded_data
    }


@blog_root.get("/blog/{_id}") 
def Getblog(_id:str) :
    res = blogs_collection.find_one({"_id" : ObjectId(_id) }) 
    decoded_blog = DecodeBlog(res)
    return {
        "status" : "ok" ,
        "data" : decoded_blog
    }


# update blog 
@blog_root.patch("/update/{_id}")
def UpdateBlog(_id: str , doc:UpdateBlogModel):
    req = dict(doc.model_dump(exclude_unset=True)) 
    blogs_collection.find_one_and_update(
       {"_id" : ObjectId(_id) } ,
       {"$set" : req}
    )

    return {
        "status" : "ok" ,
        "message" : "blog updated successfully"
    }


# delete blog 
@blog_root.delete("/delete/{_id}")
def  DeleteBlog(_id : str):
    blogs_collection.find_one_and_delete(
        {"_id" : ObjectId(_id)}
    )

    return {
        "status" : "ok" ,
        "message" : "Blog deleted succesfully"
    }

@blog_root.post("/blog/{blog_id}/comment")
def create_comment(blog_id: str, comment: CommentModel):
    # Ensure the blog exists
    blog = blogs_collection.find_one({"_id": ObjectId(blog_id)})
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")

    # Add the comment to the comments collection
    comment_doc = comment.dict()
    comment_doc["blog_id"] = blog_id
    comment_doc["created_at"] = datetime.datetime.utcnow()
    res = comments_collection.insert_one(comment_doc)

    return {
        "status": "ok",
        "message": "Comment added successfully",
        "_id": str(res.inserted_id)
    }
def get_comments(blog_id: str):
    # Retrieve comments for the specified blog
    comments = comments_collection.find({"blog_id": blog_id})

    # Decode and return the comments
    decoded_comments = [DecodeComment(comment) for comment in comments]
    return {"status": "ok", "data": decoded_comments}

# Like a blog
@blog_root.post("/blog/{_id}/like")
def LikeBlog(_id: str):
    likes_collection.insert_one({"blog_id": ObjectId(_id), "like": True})
    return {"message": "Blog liked successfully"}

# Dislike a blog
@blog_root.post("/blog/{_id}/dislike")
def DislikeBlog(_id: str):
    likes_collection.insert_one({"blog_id": ObjectId(_id), "like": False})
    return {"message": "Blog disliked successfully"}