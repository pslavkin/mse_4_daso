class debugClass:
    def __init__(self):
        pass

    verbose=0
    @staticmethod
    def v1(msg):                                   # funcion para mostrar mensajes en pantalla pero con un switch de debug para prender o apagar al instanciar la clase
        if debugClass.verbose >= 1:
            print(msg)
    def v2(msg):                                   # funcion para mostrar mensajes en pantalla pero con un switch de debug para prender o apagar al instanciar la clase
        if debugClass.verbose >= 2:
            print(msg)
    def v3(msg):                                   # funcion para mostrar mensajes en pantalla pero con un switch de debug para prender o apagar al instanciar la clase
        if debugClass.verbose >= 3:
            print(msg)
    def vx(x,msg):
        if debugClass.verbose >= x:
            print(msg)
