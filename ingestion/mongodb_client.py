from pymongo import MongoClient
from bson.objectid import ObjectId

class MongoDBClient:
    def __init__(self, uri, database_name, collection_name):
        self.client = MongoClient(uri)
        self.db = self.client[database_name]
        self.collection = self.db[collection_name]

    def save_data(self, data):
        result = self.collection.insert_one(data)
        return str(result.inserted_id)
    
    def get_data(self, document_id):
        return self.collection.find_one({"_id", ObjectId(document_id)})