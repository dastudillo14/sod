import xmlrpc.client

# Crear conexion con el servidor 
proxy = xmlrpc.client.ServerProxy('http://localhost:9000')

# Llamar funcion listar contenido y pasar directorio que deseo mostrar su informacion
DIRECTORITO_TEST = '/home/dantee/Documentos/DIRECTORIO_PRUEBA_SOD'
print('Contenido >>>',proxy.listar_contenido(DIRECTORITO_TEST))