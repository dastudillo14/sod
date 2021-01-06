import Pyro.core
import os

# Clase para crear Cliente
class Cliente(object):
    def __init__(self):
        self.servidor = Pyro.core.getProxyForURI("PYROLOC://localhost:7766/servidor")# Instanciar servidor
    # Metodo para llamar al metodo "saludar" del servidor
    def cli(self, name):
        nom = self.servidor.saludar(name)
        print(nom)

Pyro.core.initClient() # Iniciar cliente
client    =  Cliente() # Instancia cliente

def main():
    os.system("clear")
    while True:                                          # Mantener cliclo para solicitar saludo y saludar n veces
       n = raw_input("Ingrese un nombre para saludar: ") # Ingresar por consola un texto cualquier
       client.cli(n)                                     # Metodo del cliente que se comunica con el servidor, y presenta saludo.

if __name__=="__main__":
    main()