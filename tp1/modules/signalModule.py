import signal
from modules.debugModule import debugClass

class signalClass:
    def __init__(self):
        pass

    @staticmethod
    def handlerSIGINT(sig,frame):
        debugClass.vx(1,"SIGINT handler sig={}".format(sig))
        debugClass.vx(1,"frame={}".format(frame))
        exit(1)

    @staticmethod
    def signalRegisterSIGINT():
        debugClass.vx(1,"registro signal SIGINT")
        signal.signal(signal.SIGINT,signalClass.handlerSIGINT)

