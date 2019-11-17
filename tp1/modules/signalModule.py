from modules.debugModule import debugClass
import signal

class signalClass:
    staticFlag=None                                            # es estatica porque no depende de ninguna instancia, es solo para mantener una copia del flag(Event) dentro de la clase
    def __init__(self,flag):
        signalClass.staticFlag=flag                            # me guardo el flag que lo usara el Handler  para parar las tareas cuando se oproma C-c
        debugClass.vx(2,"registro signal SIGINT")
        signal.signal(signal.SIGINT,signalClass.handlerSIGINT) #

    @staticmethod
    def handlerSIGINT(sig,frame):
        debugClass.vx(3,"SIGINT handler sig={}".format(sig))
        debugClass.vx(3,"frame={}".format(frame))
        signalClass.staticFlag.set()                           # seteando este flag, todas las tareas terminaran de manera ordenada
