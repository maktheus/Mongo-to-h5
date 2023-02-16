import json
import subprocess
from ParserController import payloadWise

def payloadWiseParser():
    res = []
    for item in payloadWise():
        payload = item.get("payload")
        time = item.get("time")
        payload = json.loads(payload)
        payloadRaw = payload[6]["vs"]
        payloadDecodifier = subprocess.run(["src/packages/Scripts/decoder/main-linux", payloadRaw], stdout=subprocess.PIPE)
        # to json
        # payloadDecodifier = subprocess.run(["src/packages/Scripts/decoder/main-linux", payloadRaw], stdout=subprocess.PIPE)
        payloadDecodifier = payloadDecodifier.stdout.decode("utf-8")
        payloadDecodifier = json.loads(payloadDecodifier)
        res.append({"payload": payloadDecodifier, "time": time})
    return res


    
        
def main():
    payloadWiseParser()

if __name__ == "__main__":
    main()
        

    