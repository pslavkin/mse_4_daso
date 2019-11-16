from   modules.debugModule    import debugClass
from   modules.udpUtilsModule import *
from   modules.signalModule import *
from   modules.parserModule import *
import threading
import json
import sys
import os
import time


class changeClass(threading.Thread):
    def __init__(self):
        super().__init__()
        pass

    def run(self):
        for i in range(10):
            print ("hola")
            time.sleep(1)

class Main:
    def __init__(self,ip="localhost",tout=1):
        signalClass.signalRegisterSIGINT()
        try:
            self.port = int(sys.argv[1])
            debugClass.v1("Puerto elegido= {}".format(self.port))
        except:
            debugClass.v1("Puerto incorrecto")
            exit(1)
        self.ip             = ip
        self.tout           = tout
        self.parserInstance = parserClass(configFileName = "config.txt")
        self.comUdpInstance = comUdpClass(ip             = self.ip,port = self.port)

    def main(self):
        goodAck = 0
        badAck  = 0
        while True:
            ans = self.comUdpInstance.sendUdpMsg(self.parserInstance.cvs2json())
            if ans==b'OK':
               goodAck+=1
            else:
                badAck+=1
            debugClass.v1("goodAck={} badAck={}".format(goodAck,badAck))
            time.sleep(self.tout)

debugClass.verbose = 1
changeInstance=changeClass()
changeInstance.start()

#Main(ip="127.0.0.1",tout=1).main()
