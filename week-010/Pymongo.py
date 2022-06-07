import pymongo
from pymongo import MongoClient
from pymongo import collection
import certifi

cluster = MongoClient('mongodb+srv://dylanpicart:K!ngdomhearts2!@cluster0.avicd.mongodb.net/demo?retryWrites=true&w=majority', tlsCAFile=certifi.where())
db = cluster['demo']
collection = db['student']

'''d1 = {"ID":1,"name":"Dylan","email":"dylanpicart@mail.adelphi.edu"}
collection.insert_one(d1)
d2 = {"ID":2,"name":"Sonali", "email":"sonali@gmail.com"}
d3 = {"ID":3,"name":"Fahmid", "email":"fahmid@gmail.com"}
# for multiple insertion
collection.insert_many([d2, d3])'''

# To print out the names in the database
'''result = collection.find()
for res in result:
    print(res["name"])'''
    
# To find individual element in the database
'''result = collection.find({'name':'Sonali'})
for res in result:
    print(res["ID"])
# For more of the elements of the person
res = collection.find_one({"ID": 2})
print(res)'''

collection.update_many({"ID":1}, {"$set":{"name":'Dylan'}})

# deleting data
# collection.delete_one({"ID":1})

