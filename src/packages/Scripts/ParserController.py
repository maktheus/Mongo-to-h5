
import sys
import json
import h5py
import pandas as pd
import numpy as np

sys.path.append("/home/muchoa/code/cetelli/Mongo_to_h5/src")
from packages.Database.databaseController import getAllDataFromCollection

payload = []

def getPayload():
    dataFromDataBase = getAllDataFromCollection()
    for doc in dataFromDataBase:
        payload.append(doc.get("payload"))

    return payload

def transformPayloadToJson():
    payloadJson = []
    payload = getPayload()
    for sample in payload:
        #sample to json
        payloadJson.append(json.loads(sample))
    return payloadJson

def jsonSeparation():
    payloadJson = transformPayloadToJson()
    payloadJsonHex = []
    payloadJsonWise = []

    for json in payloadJson:
        # se payloadJson possuir inletPressure colocar dentro do hexJson
        if type(json) == dict:
            payloadJsonHex.append(json)
        # se possuir 74FE48FFFF6D8845 colocar dentro do wiseJson
        elif type(json) == list:
            payloadJsonWise.append(json)
    
    return payloadJsonHex, payloadJsonWise 

def jsonToH5():
    payloadJsonHex, payloadJsonWise = jsonSeparation()
    
    payloadHexNumeric = []
    payloadWiseNumeric = []

    for item in payloadJsonHex:
        # se nao tive 'cpu':  na listacontinuar o loop
        if 'cpu' not in item:
            print(list(item.values()))
            payloadHexNumeric.append(list(item.values()))

    for item in payloadJsonWise:
        print(list(item.values()))
        payloadWiseNumeric.append(list(item.values()))

    #criar arquivo h5
    hexH5 = h5py.File("src/dump/hex.h5", "w")
    wiseH5 = h5py.File("wise.h5", "w")



import h5py

def jsonToCsv():

    payloadJsonHex, payloadJsonWise = jsonSeparation()
    #retirar os valores que tivemrem cpu
    payloadJsonHex = [item for item in payloadJsonHex if 'cpu' not in item]


    #criar arquivo csv
    hexCsv = pd.DataFrame(payloadJsonHex)
    wiseCsv = pd.DataFrame(payloadJsonWise)

    hexCsv.to_csv("src/dump/hex.csv",index=False)
    wiseCsv.to_csv("src/dump/wise.csv",index=False)

    # #colocar tudo dentro de um csv
    # payloadCsv = pd.DataFrame(payloadJson)
    # payloadCsv.to_csv("payload.csv",index=False)


def main():
    jsonToCsv()
    jsonToH5()
    

if __name__ == "__main__":
    main()