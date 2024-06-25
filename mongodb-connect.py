from pymongo import MongoClient

url = "mongodb://test:testpassword@localhost:27017"

client = MongoClient(url)

database = client['training']

collection = database['users']

record = {
    'first_name': 'person 1',
    'last_name': 'dummy',
    'tags': [
        'neighbour',
        'employed'
    ]
}

collection.insert_one(record)

for user in collection.find():
    print(user)
