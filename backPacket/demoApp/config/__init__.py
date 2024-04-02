import os
import json

def getConfig():
    configIndex = {}
    configDir = os.path.dirname(__file__)
    configFiles = os.listdir(configDir)
    for configFile in configFiles:
        if(configFile.split('.')[-1] == "json"):
            filePath = "{}/{}".format(configDir,configFile)
            jsonData = readJson(filePath)
            keyName = configFile.split('.')[0]
            configIndex[keyName] = jsonData
    return configIndex


def readJson(inputPath):
    with open(inputPath) as file_r:
        jsonData = json.load(file_r)
    return jsonData

if __name__ == '__main__':
    getConfig()