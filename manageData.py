import json

def writeData(obj):
    with open("database.json", "a+") as writeToFile:
        tobj = obj.__dict__
        json.dump(tobj,writeToFile)

def readData():
    data = []
    with open("database.json", "r+") as readFromFile:
        for line in readFromFile:
            data.append(json.loads(line))
    return data