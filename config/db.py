from pymongo import MongoClient
from bson.binary import UuidRepresentation


conn=MongoClient("mongodb+srv://sofkau:contra@clustersofkau.8kil0mz.mongodb.net/userspython?retryWrites=true&w=majority",uuidRepresentation='standard')
       
    
