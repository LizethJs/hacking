import requests
import json

def obtenerIpDesdeDominio(dominio):
    """
    Obtiene la dirección IP asociada a un dominio y luego obtiene la región geográfica de esa IP.
    
    :param dominio: Nombre del dominio (por ejemplo, 'avn.com.co').
    """
    print("--------------Dominio ->" + str(dominio) + "-------------------")
    
    # Realiza una búsqueda DNS para el dominio usando la API de NetworkCalc
    resultadoBusqueda = requests.get("https://networkcalc.com/api/dns/lookup/" + str(dominio))
    
    # Verifica si hay registros de tipo 'A' en la respuesta JSON
    if resultadoBusqueda.json()['records'] is not None:
        # Recorre cada registro 'A' para obtener la dirección IP
        for i in range(len(resultadoBusqueda.json()['records']['A'])):
            ip = resultadoBusqueda.json()["records"]["A"][i]["address"]
            
            # Realiza una búsqueda de información de IP usando la API de ipinfo.io
            resultadoRegion = requests.get("https://ipinfo.io/" + str(ip) + "/json")
            
            # Imprime la región de la IP obtenida
            print("La región de la IP ->" + str(ip) + " es " + str(resultadoRegion.json()))

def obtenerEmailsDesdeDominio(dominio):
    """
    Obtiene una lista de direcciones de correo electrónico asociadas a un dominio usando la API de Hunter.
    
    :param dominio: Nombre del dominio (por ejemplo, 'dersa.com').
    """
    # Realiza una búsqueda de correos electrónicos usando la API de Hunter
    resultadoEmails = requests.get("https://api.hunter.io/v2/domain-search?domain=" + str(dominio) + "&api_key=8cc2d69ade4968c5888e775128e02c2fa176e8d3")
    
    # Imprime la respuesta JSON de la API en un formato legible
    print(json.dumps(resultadoEmails.json(), indent=4))
    
    # Verifica si hay correos electrónicos en la respuesta JSON
    if resultadoEmails.json()['data']['emails'] != None:
        # Recorre cada correo electrónico y lo imprime
        for correo in range(len(resultadoEmails.json()["data"]["emails"])):
            print("correo: " + str(resultadoEmails.json()["data"]["emails"][correo]["value"]))

# Itera sobre cada dominio en la lista y obtiene la IP para cada dominio
for dominio in dominios_empresas:
    obtenerIpDesdeDominio(dominio)  # Obtiene y muestra la región de la IP para cada dominio

# Obtiene y muestra los correos electrónicos asociados a un dominio específico
obtenerEmailsDesdeDominio("dersa.com.co")  # Obtiene correos electrónicos para 'ducati.com'

