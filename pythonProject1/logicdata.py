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

# Lista de dominios de empresas con sus respectivas etiquetas
dominios_empresas = [
    "avn.com.co",        # Avianca
    "bancolombia.com",   # Bancolombia
    "eci.com",           # Éxito
    "cemexcol.com",      # Cemex Colombia
    "alpina.com",        # Alpina
    "bavaria.com.co",    # Bavaria
    "sura.com",          # Grupo Sura
    "nexura.com",        # Nexura (Grupo Aval)
    "cajacopi.co",       # Cajacopi
    "terpel.com",        # Terpel
    "postobon.com",      # Postobón
    "une.com.co",        # UNE (ahora parte de Tigo)
    "tigo.com.co",       # Tigo
    "carvajal.com",      # Carvajal
    "grupopromotora.com",# Promotora de Seguridad
    "conavi.com.co",     # Conavi
    "bancoomeva.com",    # Bancoomeva
    "gruposura.com",     # Grupo Sura
    "hipotecaria.com",   # Hipotecaria
    "lagranaventura.com",# La Gran Aventura
    "ferreteriaferraz.com", # Ferretería Ferraz
    "sodimac.com.co",    # Sodimac
    "baloto.com",        # Baloto
    "tuscal.com",        # Tuscal
    "grupoaval.com",    # Grupo Aval
    "grupoexito.com",   # Grupo Éxito
    "santoangel.com.co", # Santo Ángel
    "tropicanafm.com",   # Tropicana
    "prisa.com",         # Prisa Radio
    "rappi.com",         # Rappi
    "codensa.com.co",    # Codensa
]

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
    if resultadoEmails.json()['data']['emails'] is not None:
        # Recorre cada correo electrónico y lo imprime
        for correo in range(len(resultadoEmails.json()["data"]["emails"])):
            print("Correo: " + str(resultadoEmails.json()["data"]["emails"][correo]["value"]))

# Itera sobre cada dominio en la lista y obtiene la IP y correos electrónicos
for dominio in dominios_empresas:
    obtenerIpDesdeDominio(dominio)
    obtenerEmailsDesdeDominio(dominio)
