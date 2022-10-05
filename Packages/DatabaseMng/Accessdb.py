import pymongo
from pymongo import MongoClient # Oggetto che permette di connettersi al DB

# Connessione al DB
client = MongoClient('localhost', 27017)

# Carico il database
db = client.NoteAPP

db.collection_names
for collection in db.list_collection_names():
    print(collection)
    A = db.get_collection(collection)
    B = A.find_one({"Object_name":"Name_1"})
    A.insert_one({"Object_name":"Name_1","Price":"Price_1","Link":"Link_1"})

# Accedo alla collection persone
persone_coll = db.persone


# Find all the document
p = persone_coll.find({"Object_name":"Name_1"},{"Price":"Price_1"},{"Link":"Link_1"})

for person in p:
    print(person)

res = persone_coll.update_one({"nome":"Pasquale"}, {"$set":{"pensiero":"Sono un ingegnere meccatronico \n" * 2}})

# Print all thoughts Buonocore has
p = persone_coll.find({"cognome":"Buonocore"})
for pers in p:
    if "pensiero" in list(pers.keys()):
        print(pers["pensiero"])
