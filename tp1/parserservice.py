import os
import time
import json


class parser:
    csvFileName=""

    def __init__(self):
        pass
    
    @staticmethod
    def readCsvPath():
        with open("config.txt","r") as fileStream:
            parser.csvFileName=fileStream.readline().strip()
            print("csv file assigned={}".format(parser.csvFileName))


    def cvs2json(self):
        with open(parser.csvFileName,"r") as fileStream:
            jsonMsgList=[]
            fileStream.readline()
            for line in fileStream:
                stringList=line.strip().split(",")
                jsonMsgList.append ({ "id":     stringList[0] ,
                                      "value1": stringList[2] ,
                                      "value2": stringList[3] ,
                                      "name":   stringList[1] })
            udpMsg=json.dumps(jsonMsgList)
            print(udpMsg)

class com:
    def __init__(self):
        pass
    
parser.readCsvPath()
p=parser()
p.cvs2json()
