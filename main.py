import json
import sys
f = open('config.json')
token = json.load(f)["token"]
f.close()
if token == "YOUR TOKEN GOES HERE":
    print("You have not changed your token. Please set it in config.json")
    sys.exit()
