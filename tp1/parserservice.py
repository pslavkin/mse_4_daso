from   modules.debugModule    import debugClass
from   modules.exchangeModule import *
from   modules.signalModule   import *

class Main:
    def __init__(self,ip="localhost",startPort=10000,tout=1,config="config.txt"):                # recibo los parametros de configuracion
        flag = Event()                                                                           # este es el Event que usare para comunicar el main con las tareas para poder apagarlas
        signalClass(flag)                                                                        # registro el signal SIGINT y le paso el flag que usare para parar las tareas
        self.sendExchangeInstances = []                                                          # lista de tareas
        for i in range(3):                                                                       # decido que sean 3 tareas.
            self.sendExchangeInstances.append(                                                   # voy agregando los id de las tareas creadas a la lista para luego poder hacer el joun cuando estas terminen
                    sendExchangeClass(                                                           # aca instancio la tarea con los parametros
                        ip         = ip,
                        port       = startPort+i,                                                # incremento el puerto de salida
                        tout       = tout*(i+1),                                                 # incremento en 1 el tout para que queden desincronizadas
                        flag       = flag,                                                       # le paso el flag que usaremos para comunicarnos
                        config     = config.partition(".")[0]+str(i)+".txt",                     # el archivo de configuracion de la forma "configX.txt"
                        threadName = "tarea "+str(i)                                             # nombre de fantasia
                    )
            )
            self.sendExchangeInstances[i].start()                                                # arranco cada tarea
            debugClass.vx(2,"tarea {} creada id={}".format(i,id(self.sendExchangeInstances[i]))) # debug muestro el ID de cada una

    def main(self):
        for i in self.sendExchangeInstances:                                                     # para todas las tareas creadas
            i.join()                                                                             # espero bloqueando a que terminann con un join
            debugClass.vx(2,"tarea {} terminada id={}".format(i.name,id(i)))                     # debug
        debugClass.vx(2,"programa principal terminado id={}".format(id(self)))                   # debug de fin de programa

debugClass.verbose = 2                                                                           # nivel de debug para la muestra de mensajes
Main(ip="127.0.0.1",startPort=10000,tout=1,config="config/config.txt").main()                           # instancio la clase Main y lanzo el miembro main().. la instancia no la guardo porque no la necesito
