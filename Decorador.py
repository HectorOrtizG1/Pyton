def decora(f):
    def envuelve():
        print('Estoy a punto de ejecutar la funcion')
        f()
        print('Termine de ejecutar la funcion')
    return envuelve

@decora  #@Decora, decora la funcion principal
def hola():
    print('Hola mundo!')

hola()
