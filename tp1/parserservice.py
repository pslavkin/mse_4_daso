from   modules.debug    import debugClass
from   modules.udpUtils import *
import json
import sys
import os
import time

class parserClass:
    def __init__(self,configFileName="config.txt"):                           # por defecto sin debug y config.txt como arvhivo que dice que archivo contiene el cambio de moneda
        self.readCsvPath(configFileName)                                      # asigno el nombre del archivo csv

    def readCsvPath(self,configFileName):                                     # lee del configFileName la ruta al csv para extraer los datos de cambio
        with open(configFileName,"r") as fileStream:
            self.csvFileName=fileStream.readline().strip()
            debugClass.v1("csv file assigned={}".format(self.csvFileName)) # comantario de debug

    def cvs2json(self):
        with open(self.csvFileName,"r") as fileStream:                        # abro archivo para lectura usando with
            jsonMsgList=[]                                                    # lista vacia que la ire llenando con items de tipo dicctionario
            fileStream.readline()                                             # me salteo la 1er linea
            for line in fileStream:                                           # para todas las lineas del archivo
                stringList=line.strip().split(",")                            # separo la linea en una lista de palabras sueltas separadas por coma
                jsonMsgList.append ({ "id":     stringList[0] ,               # armo un duccionario con los value:key utilizando las palabras que se extrajeron del archivo
                                      "value1": stringList[2] ,
                                      "value2": stringList[3] ,
                                      "name":   stringList[1] })
            jsonString=json.dumps(jsonMsgList)                                # una vez lista la lista de diccionarios, los convierto a un string de json y es lo que devuelvo
            debugClass.v3("jsonString extraido={}".format(jsonString))      # print debug de los que obtengo y devuelvo
            return jsonString

class Main:
    def __init__(self,ip="localhost",tout=1):
        self.port = 10000
        print("puerto parametro={} tipo={} int={}".format(sys.argv[1],type(sys.argv[1]), int(sys.argv[1])))
        
        try:
            self.port = int(sys.argv[1])
            debugClass.v1("Puerto elegido= {}".format(self.port))
        except:
            debugClass.v1("Puerto incorrecto")
            exit(1)
        self.ip   = ip
        self.tout = tout
        self.main()

    def main(self):
        goodAck           = 0
        badAck            = 0
        parserInstance    = parserClass(configFileName = "config.txt")
        while True:
            ans = comUdpClass(ip=self.ip,port=self.port).loopSendRcv(parserInstance.cvs2json())
            if ans==b'OK':
               goodAck+=1 
            else:
                badAck+=1 
            debugClass.v1("goodAck={} badAck={}".format(goodAck,badAck))
            time.sleep(self.tout)

debugClass.verbose = 1
Main(ip="127.0.0.1",tout=1)
