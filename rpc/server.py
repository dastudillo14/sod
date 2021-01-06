from xmlrpc.server import SimpleXMLRPCServer
import os

# Iniciar Servidor Localmente en el puerto 9000
server = SimpleXMLRPCServer(
    ('localhost', 9000),
    logRequests=True,
)

# Exponer funcion
def listar_contenido(dir_name):    
    return os.listdir(dir_name)

# Registrar funcion en el servidor
server.register_function(listar_contenido)

# Crear Execpcion para poder cerrar Servidor
try:
    print('Control-C para salir')
    server.serve_forever() # Mantener activo el servidor.
except KeyboardInterrupt:
    print('Saliendo...')