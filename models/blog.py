from pydantic import BaseModel

class BlogModel(BaseModel):
    """
    Pydantic BaseModel for defining the structure of a blog document.

    Attributes:
        title (str): The title of the blog.
        sub_title (str): The sub-title or summary of the blog.
        content (str): The main content of the blog.
        author (str): The author of the blog.
        tags (list): List of tags associated with the blog.
        likes (int): The number of likes for the blog. Defaults to 0.
        dislikes (int): The number of dislikes for the blog. Defaults to 0.
        comments (list): List of comments associated with the blog. Defaults to an empty list.
    """
    title: str
    sub_title: str
    content: str
    author: str
    tags: list
    likes: int = 0  # Default value for likes
    dislikes: int = 0  # Default value for dislikes
    comments: list = []  # Default value for comments

class UpdateBlogModel(BaseModel):
    """
    Pydantic BaseModel for defining the structure of an update request for a blog.

    Attributes:
        title (str): The updated title of the blog.
        sub_title (str): The updated sub-title of the blog.
        content (str): The updated content of the blog.
        author (str): The updated author of the blog.
        tags (list): The updated list of tags associated with the blog.
    """
    title: str = None
    sub_title: str = None
    content: str = None
    author: str = None
    tags: list = None

class CommentModel(BaseModel):
    """
    Pydantic BaseModel for defining the structure of a comment.

    Attributes:
        author (str): The author of the comment.
        content (str): The content of the comment.
    """
    author: str
    content: str
