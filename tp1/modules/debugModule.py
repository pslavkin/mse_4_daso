class debugClass:
    def __init__(self):
        pass

    verbose=0
    @staticmethod
    def vx(x,msg):
        if debugClass.verbose >= x:
            print(msg)
