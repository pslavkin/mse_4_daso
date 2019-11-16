from modules.debugModule import debugClass
import socket

class comUdpClass:
    def __init__(self,port=10000,ip="127.0.0.1"):
        self.port    = port
        self.ip      = ip
        self.buff    = 1024
        self.udpSock = None
        self.resetSocket()

    def resetSocket(self):
        if self.udpSock!=None:
            self.udpSock.close()
        self.udpSock = socket.socket(family = socket.AF_INET, type = socket.SOCK_DGRAM) # UDP socket
        self.udpSock.settimeout(1)

    def sendUdpMsg(self,msg):
        debugClass.v1("enviando datos por udp ip={} puerto={} len={}".format(self.ip,self.port,len(msg)))
        debugClass.v3("mensaje={}".format(msg))
        self.udpSock.sendto(msg.encode(),(self.ip, self.port))                      # envia el mensaje
        try:
            return self.udpSock.recv(self.buff)
        except socket.timeout:
            debugClass.v1("udp: timeout esperando respuesta del server")
            self.resetSocket()  #al resetear el socket cambio los puertos de salida para que no quede enganchado siempre a los mismos puertos...es una opcion.. podria seguir siempre con los mismos...
            return b'tout'
