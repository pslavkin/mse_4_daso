from modules.debugModule import debugClass
import socket

class comUdpClass:
    def __init__(self,port=10000,ip="127.0.0.1"):
        self.port    = port                                                             # creo miembros de la clase con los datos que usare en los metodos
        self.ip      = ip                                                               # ip y puerto
        self.buff    = 1024                                                             # buffer de recepcion tipico
        self.udpSock = None                                                             # cro un miembro vacio que sera la instancia de la conexion
        self.resetSocket()                                                              # configuro el socket con los datos

    def resetSocket(self):
        if self.udpSock!=None:
            self.udpSock.close()
        self.udpSock = socket.socket(family = socket.AF_INET, type = socket.SOCK_DGRAM) # creo la instancia del socket
        self.udpSock.settimeout(1)                                                      # esto me permite no quedarme bloqueado para siempre esperando un feedback del server y actuar en consecuencia en un looop

    def sendUdpMsg(self,msg):
        debugClass.vx(3,"enviando datos por udp ip={} puerto={} len={}".format(self.ip,self.port,len(msg)))
        debugClass.vx(3,"mensaje={}".format(msg))
        self.udpSock.sendto(msg.encode(),(self.ip, self.port))                          # envia el mensaje
        try:
            return self.udpSock.recv(self.buff)                                         # me 'siento' a esperar la respuesta pero con un timeout ya seteado para ese socket dentro del try, si anda bien directamente return
        except socket.timeout:                                                          # capturo con except el error socket.timeout que es un error que esta definido en la biblioteca socket
            debugClass.vx(3,"udp: timeout esperando respuesta del server")              # mensaje de debug de error de recepcton
            self.resetSocket()                                                          # como fallo, al resetear el socket cambio los puertos de origen para que no quede enganchado siempre a los mismos puertos...origen:destino es una opcion.. podria seguir siempre con los mismos...(el destino siempre es el mismo, pero el origen es aleatorio y se cambia al rearmar el socket)
            return b'tout'                                                              # me invento un mensaje de error
