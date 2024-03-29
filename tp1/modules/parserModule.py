from   modules.debugModule import debugClass
import json

class parserClass:
    def __init__(self,configFileName="config.txt"):                        # por defecto sin debug y config.txt como arvhivo que dice que archivo contiene el cambio de moneda
        self.readCsvPath(configFileName)                                   # asigno el nombre del archivo csv

    def readCsvPath(self,configFileName):                                  # lee del configFileName la ruta al csv para extraer los datos de cambio
        with open(configFileName,"r") as fileStream:
            self.csvFileName=fileStream.readline().strip()
            debugClass.vx(1,"csv file assigned={}".format(self.csvFileName)) # comantario de debug

    def cvs2json(self):
        with open(self.csvFileName,"r") as fileStream:                     # abro archivo para lectura usando with
            jsonMsgList=[]                                                 # lista vacia que la ire llenando con items de tipo dicctionario
            fileStream.readline()                                          # me salteo la 1er linea que tiene un encabezado
            for line in fileStream:                                        # para todas las lineas del archivo
                stringList=line.strip().split(",")                         # separo la linea en una lista de palabras sueltas separadas por coma
                jsonMsgList.append ({ "id":     stringList[0] ,            # armo un duccionario con los value:key utilizando las palabras que se extrajeron del archivo
                                      "value1": stringList[2] ,
                                      "value2": stringList[3] ,
                                      "name":   stringList[1] })
            jsonString=json.dumps(jsonMsgList)                             # una vez lista la lista de diccionarios, los convierto a un string de json y es lo que devuelvo
            debugClass.vx(3,"jsonString extraido={}".format(jsonString))     # print debug de los que obtengo y devuelvo
            return jsonString
