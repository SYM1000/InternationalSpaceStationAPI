import requests # importamos la libreria que nos permite hacer solicitudes web

#servidor al que hacemos la llamada
server = "http://api.open-notify.org/"
#Direccion del servidor de la que obtenemos la informacion
endpoint = "iss-now.json"

#Generamos la solicitud
response = requests.get(server+endpoint)

# Revisamos el estado de la solicitud
print(response)
