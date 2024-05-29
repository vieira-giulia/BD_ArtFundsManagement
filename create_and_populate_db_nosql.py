from pymongo import MongoClient
import json

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['db_nosql'] 

# In case you run this more than once and need to delete the database before you create it again
client.drop_database(db)

# Create artists collection
artists_collection = db['artists']

# Populate artists collection
artists_data = [
    { "_id": 101, "name": "ArtistA", "dateInit": "2010-01-01", "dateEnd": None },
    { "_id": 102, "name": "ArtistB", "dateInit": "2015-05-10", "dateEnd": "2022-12-31" }
]

artists_collection.insert_many(artists_data)

# Create artistic objects collection
artistic_objects_collection = db['artisticObjects']

# Populate artistics objects collection
artistic_objects_data = [
    { "_id": 1, "name": "Painting", "theme": "Nature", "genre": "Landscape", "year": 2022, "typeArt": "Oil", "material": "Canvas", "authorID": 101, "executorID": 201, "owner": "Private" },
    { "_id": 2, "name": "Sculpture", "theme": "Abstract", "genre": "Modern", "year": 2021, "typeArt": "Marble", "material": "Stone", "authorID": 102, "executorID": 202, "owner": "Museum" }
]

artistic_objects_collection.insert_many(artistic_objects_data)

# Create users collection
users_collection = db['users']

# Populate users collection
users_data = [
    { "_id": 1, "name": "UserA", "email": "usera@example.com" },
    { "_id": 2, "name": "UserB", "email": "userb@example.com" }
]

users_collection.insert_many(users_data)

# Create user visits logs collection
logs_collection = db['logs']

# Populate user visits logs collection
logs_data = [
    { "date": "2023-01-01T10:00:00", "objectID": 1, "artistID": 101 },
    { "date": "2023-01-02T14:30:00", "objectID": 2, "artistID": 102 }
]

logs_collection.insert_many(logs_data)

# Exporto JSONs to make things easier to be seen outside MongoDB for this project
# This is not actually necessary or recommended, but makes it easier to illustrate 
# the data format proposed
artists = list(artists_collection.find())
objects = list(artistic_objects_collection.find())
users = list(users_collection.find())
logs = list(users_collection.find())


# Close the connection
client.close()

# Export JSONs
with open('artists.json', 'w') as json_file:
    json.dump(artists, json_file, indent=2)

with open('artistic_objects.json', 'w') as json_file:
    json.dump(objects, json_file, indent=2)

with open('users.json', 'w') as json_file:
    json.dump(users, json_file, indent=2)

with open('logs.json', 'w') as json_file:
    json.dump(logs, json_file, indent=2)
