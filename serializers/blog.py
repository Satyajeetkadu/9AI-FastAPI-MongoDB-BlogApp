from bson import ObjectId
from config.config import likes_collection

# one doc 
def DecodeBlog(doc) -> dict:

    return {
        "_id" : str(doc["_id"]) ,
        "title" : doc["title"] ,
        "sub_title" : doc["sub_title"] ,
        "content" : doc["content"] ,
        "author" : doc["author"] ,
        "date" : doc["date"],

    }


# all blogs 
def DecodeBlogs(docs) -> list:
    return [DecodeBlog(doc) for doc in docs]

def DecodeComment(comment) -> dict:
    return {
        "_id": str(comment["_id"]),
        "author": comment["author"],
        "content": comment["content"],
        "created_at": comment["created_at"]
    }