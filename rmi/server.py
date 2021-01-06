import Pyro.core

# Clase para crear servidor RMI usando Pyro
class Servidor(Pyro.core.ObjBase):
    def __init__(self):
        Pyro.core.ObjBase.__init__(self)

    # Metodo invocar desde cliente
    def saludar(self, name):
        print("Saludando...\n")
        saludo = "Hola %s \n" % name
        return saludo

# Funcion py para ejecutar Servidor
def main():
    try:
        Pyro.core.initServer()       # Inicar server
        demonio = Pyro.core.Daemon() # Iniciar Daemon
        uri     = demonio.connect(Servidor(), "servidor")
        print("El servidor de Hola Mundo:", uri)
        demonio.requestLoop()        # Mantener activo el servidor
    except:
        demonio.disconnect(uri.objectID) # En caso de error, cerrar servidor


if __name__ == "__main__":
    main()
