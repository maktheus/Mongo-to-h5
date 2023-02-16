import json
from ParserController import payloadKS

def payloadKSParser():
    res =[]
    for item in payloadKS():
        payload = item.get("payload")
        time = item.get("time")
        payload = json.loads(payload)
        
        res.append({"payload": payload, "time": time})

    return res


def main():
    payloadKSParser()

if __name__ == "__main__":
    main()