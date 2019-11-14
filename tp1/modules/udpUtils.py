from modules.debug import debugClass
import socket

class comUdpClass:
    def __init__(self,port=10000,ip="127.0.0.1"):
        self.port = port
        self.ip   = ip
        self.buff = 1024
        pass

    def sendUdpMsg(self,msg):
        udpSock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM) # UDP socket
        debugClass.print("enviando datos por udp ip={} puerto={} mensaje={}".format(self.ip,self.port,msg))
        udpSock.sendto(msg.encode(),(self.ip, self.port))                      # envia el mensaje
        udpSock.settimeout(1)
        return udpSock.recv(self.buff)                                         # espera una respuesta

    def loopSendRcv(self,msg):
        try:
            return self.sendUdpMsg(msg)
        except socket.timeout:
            print("error de timeout")
        finally:
            print("cierro socket udp")

