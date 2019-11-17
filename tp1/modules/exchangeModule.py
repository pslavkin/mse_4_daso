from   modules.debugModule    import debugClass
from   modules.udpUtilsModule import *
from   modules.parserModule   import *
from   threading              import (Thread,Event)

class sendExchangeClass(Thread):                                                        # implemento la logica de envio de datos heredera de Thread porque la voy a lanzar desde el main
    def __init__(self,ip,port,tout,flag,config,threadName):
        self.flag           = flag                                                      # me guardo el flag(Event) que estare monitoreando en la terea para decidir cuando terminar
        self.tout           = tout                                                      # es el tiempo entre peticiones
        self.parserInstance = parserClass(configFileName=config)                        # creo una instancia del parser que usare para leer los datos del archivo cada vez que tenga que mandar
        self.comUdpInstance = comUdpClass(ip=ip, port=port)                             # creo una instancia de udp, que se encarga de la logica de mantener un socket activo y devolverme si recibio o no el ack desde el server
        super().__init__()                                                              # inicializo al padre
        super().setName(threadName)                                                     # le asigno un nombre de fantasia a la tarea para identificarla facilmente

    def run(self):
        goodAck = 0
        badAck  = 0
        while True:
            ans = self.comUdpInstance.sendUdpMsg(                                       # usando la instancia de udp envio un mensaje con:
                        self.parserInstance.                                            # usando la instancia del parser asociada a un archivo de config asociado a un csv parseo:
                            cvs2json()                                                  # lo que sale de convertir el csv a json
                    )                                                                   # la respuesta la guardo en ans, para ver si el server respondio o no
            if ans==b'OK':                                                              # si respondio OK, incremento en uno los exitos, sino
               goodAck+=1
            else:
                badAck+=1                                                               # incremento en uno los fallos
            debugClass.vx(1,"{} goodAck={} badAck={}".format(self.name,goodAck,badAck)) # debug
            if self.flag.wait(self.tout)==True:                                         # aca monitoreo el flag para ver si hay una peticion de cierre, mientras espero un tiempo sin hacer nada
                exit(0)                                                                 # si hay una peticion cierro
