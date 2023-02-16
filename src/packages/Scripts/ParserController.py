
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
        dataPayload = doc.get("payload")
        dataTime = doc.get("timestamp")

        data = {
            "time": dataTime,
            "payload": dataPayload
        }

        payload.append(data)

    return payload

        
def dataSeparation():
    data = getPayload()
    payloadWise = []
    payloadHex = []
    payloadKS = []
    for item in data:
        payload = item.get("payload")
        time = item.get("time")
        data = {
            "time": time,
            "payload": payload
        }
        # se tiver bn na str retirar [ ] e separar por virgula
        if "bn" in payload and "74FE48FFFF6D8845" in payload:
           payloadWise.append(data)
        elif "bn" in payload and "74FE48FFFF6D8845" not in payload:
            payloadKS.append(data)
        else:
            payloadHex.append(data)
        
    return payloadWise, payloadHex, payloadKS


def payloadWise():
    payloadWise = dataSeparation()[0]

    return payloadWise

def payloadHex():
    payloadHex = dataSeparation()[1]
    return payloadHex

def payloadKS():
    payloadKS = dataSeparation()[2]
    return payloadKS
            

# def jsonToH5():
#     payloadJsonHex, payloadJsonWise = jsonSeparation()
    
#     payloadHexNumeric = []
#     payloadWiseNumeric = []

#     for item in payloadJsonHex:
#         # se nao tive 'cpu':  na listacontinuar o loop
#         if 'cpu' not in item:
#             print(list(item.values()))
#             payloadHexNumeric.append(list(item.values()))

#     for item in payloadJsonWise:
#         print(list(item.values()))
#         payloadWiseNumeric.append(list(item.values()))

#     #criar arquivo h5
#     hexH5 = h5py.File("src/dump/hex.h5", "w")
#     wiseH5 = h5py.File("wise.h5", "w")



# import h5py

# def jsonToCsv():

#     payloadJsonHex, payloadJsonWise = jsonSeparation()
#     #retirar os valores que tivemrem cpu
#     payloadJsonHex = [item for item in payloadJsonHex if 'cpu' not in item]


#     #criar arquivo csv
#     hexCsv = pd.DataFrame(payloadJsonHex)
#     wiseCsv = pd.DataFrame(payloadJsonWise)

#     hexCsv.to_csv("src/dump/hex.csv",index=False)
#     wiseCsv.to_csv("src/dump/wise.csv",index=False)

#     # #colocar tudo dentro de um csv
#     # payloadCsv = pd.DataFrame(payloadJson)
#     # payloadCsv.to_csv("payload.csv",index=False)


def main():
    a ,b ,c = dataSeparation()
    
    
    # jsonToH5()
    # jsonToCsv()
    

if __name__ == "__main__":
    main()