import requests,json

def obtenerIpDesdeDominio(dominio):
    print("--------------Dominio ->"+str(dominio)+"-------------------")
    resultadoBusqueda = requests.get("https://networkcalc.com/api/dns/lookup/"+str(dominio))
    if resultadoBusqueda.json()['records'] != None:
        for i in range(len(resultadoBusqueda.json()['records']['A'])):
            ip =(resultadoBusqueda.json()["records"]["A"][i]["address"])
            resultadoRegion = requests.get("https://ipinfo.io/"+str(ip)+"/json")
            print("la region de la ip ->"+str(ip)+" es "+str(resultadoRegion.json()))


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
    resultadoEmails =requests.get("https://api.hunter.io/v2/domain-search?domain="+ str(dominio)+"&api_key=8cc2d69ade4968c5888e775128e02c2fa176e8d3")
    print(json.dumps(resultadoEmails.json(),indent=4))
    if resultadoEmails.json()['data']['emails']!= None:
        for correo in range (len(resultadoEmails.json()["data"]["emails"])):
            print("correo ; "+ str(resultadoEmails.json()["data"]["emails"][correo]["value"]))
for dominio in dominios_empresas:
 obtenerIpDesdeDominio(dominio)
    obtenerEmailsDesdeDominio("dersa.com")