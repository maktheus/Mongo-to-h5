import json
from ParserController import payloadHex

def payloadHexParser():
    res =[]
    for item in payloadHex():
        payload = item.get("payload")
        time = item.get("time")
        payload = json.loads(payload)
        res.append({"payload": payload, "time": time})

    return res

def main():
    payloadHexParser()

if __name__ == "__main__":
    main()
