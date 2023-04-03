import pymongo
import json
from dotenv import load_dotenv
import os

load_dotenv()


# Recuperar as variáveis de ambiente
MONGO_URL = os.getenv("MONGO_URL")
MONGO_DB = os.getenv("MONGO_DB")
MONGO_COLLECTION = os.getenv("MONGO_COLLECTION")


def ConnectToMongoDataBase():
    # Conectar ao banco de dados
    client = pymongo.MongoClient(MONGO_URL)
    db = client[MONGO_DB]
    collection = db[MONGO_COLLECTION]

    return collection


def getAllDataFromCollection():
    collection = ConnectToMongoDataBase()
    # without object id
    docs = collection.find({}, {"_id": False})
    return docs


def SaveDataInFile():
    docs = getAllDataFromCollection()
    with open("src/packages/Database/out/dados.txt", "w") as outfile:
        for doc in docs:
            outfile.write(str(doc))
            outfile.write("\n")
