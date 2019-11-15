from modules.debug import debugClass
import socket

class comUdpClass:
    def __init__(self,port=10000,ip="127.0.0.1"):
        self.port = port
        self.ip   = ip
        self.buff = 1024
        self.udpSock=0
        pass

    def sendUdpMsg(self,msg):
        self.udpSock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM) # UDP socket
        debugClass.v2("enviando datos por udp ip={} puerto={} mensaje={}".format(self.ip,self.port,msg))
        self.udpSock.settimeout(1)
        self.udpSock.sendto(msg.encode(),(self.ip, self.port))                      # envia el mensaje
        return self.udpSock.recv(self.buff)                                         # espera una respuesta

    def loopSendRcv(self,msg):
        try:
            return self.sendUdpMsg(msg)
        except socket.timeout:
            debugClass.v1("udp: timeout esperando respuesta del server")
            self.udpSock.close()
            return b'tout'

