import pymongo
from pymongo import MongoClient # Oggetto che permette di connettersi al DB
import json

with open('Packages/Configuration/DataBase_Structure.json') as json_file:
    DataBase_Configuration = json.load(json_file)

# Connessione al DB
client = MongoClient('localhost', 27017)

# Creo un database
db = client.NoteAPP

for collection in db.list_collection_names():
    if not db.get_collection(collection).count_documents({}):
        db.get_collection(collection).insert_one(DataBase_Configuration[collection][0])



# persone_coll.insert_one(p2)


print('ciao')

