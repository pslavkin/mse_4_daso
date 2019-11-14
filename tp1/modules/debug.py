class debugClass:
    def __init__(self):
        pass

    enable=False
    @staticmethod
    def print(msg):                                   # funcion para mostrar mensajes en pantalla pero con un switch de debug para prender o apagar al instanciar la clase
        if debugClass.enable == True:
            print(msg)

