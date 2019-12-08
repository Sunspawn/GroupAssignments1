import json

def writeData(obj):
    with open("database.json", "a+") as writeToFile:
        tobj = obj.__dict__
        json.dump(tobj,writeToFile)

