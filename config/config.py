# Import necessary modules
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Define the MongoDB Atlas connection URI
password = ""  # Replace this with your actual password
uri = f"mongodb+srv://satyajeetkadu:{password}@saty.cuqjy72.mongodb.net/?retryWrites=true&w=majority"

# Create a new MongoClient instance and connect to the MongoDB Atlas server
client = MongoClient(uri, server_api=ServerApi('1'))

# Access the 'Blogging' database in the connected MongoDB instance
db = client.Blogging

# Define collections within the 'Blogging' database
blogs_collection = db['blogs']  # Collection to store blog documents
comments_collection = db['comments']  # Collection to store comment documents
likes_collection = db['likes']  # Collection to store like and dislike documents

# Send a ping to confirm a successful connection to the MongoDB server
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
