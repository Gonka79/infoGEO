import geoip2.database
import socket
import os

# Ruta a la base de datos GeoIP local (asegúrate de que esté en la misma carpeta o especifica la ruta correcta)
geoip_db = 'GeoLite2-City.mmdb'

# Verificar si la base de datos existe
if not os.path.isfile(geoip_db):
    print(f"Error: No se encontró la base de datos '{geoip_db}'. Asegúrate de que el archivo está en la misma carpeta que el script.")
    exit()

# Crear una instancia de Reader para leer la base de datos
try:
    reader = geoip2.database.Reader(geoip_db)
except Exception as e:
    print(f"Error al abrir la base de datos '{geoip_db}': {e}")
    exit()

def buscar_geoip(ip_o_dominio):
    try:
        # Resolver el dominio a una IP si se ingresa un dominio
        try:
            ip = socket.gethostbyname(ip_o_dominio)
            print(f"Dominio '{ip_o_dominio}' resuelto a IP: {ip}")
        except socket.gaierror:
            # Si no es un dominio válido, se asume que es una IP
            ip = ip_o_dominio

        # Obtener la información de la IP usando el lector que ya está abierto
        response = reader.city(ip)

        # Imprimir la información geográfica
        print(f"\nInformación Geográfica para la IP: {ip}")
        print(f"País: {response.country.name if response.country.name else 'N/A'}")
        print(f"Código ISO del País: {response.country.iso_code if response.country.iso_code else 'N/A'}")
        print(f"Continente: {response.continent.name if response.continent.name else 'N/A'}")
        print(f"Código del Continente: {response.continent.code if response.continent.code else 'N/A'}")
        print(f"Región: {response.subdivisions.most_specific.name if response.subdivisions.most_specific.name else 'N/A'}")
        print(f"Código ISO de la Región: {response.subdivisions.most_specific.iso_code if response.subdivisions.most_specific.iso_code else 'N/A'}")
        print(f"Ciudad: {response.city.name if response.city.name else 'N/A'}")
        print(f"Latitud: {response.location.latitude if response.location.latitude else 'N/A'}")
        print(f"Longitud: {response.location.longitude if response.location.longitude else 'N/A'}")
        print(f"Código Postal: {response.postal.code if response.postal.code else 'N/A'}")
        print(f"Zona Horaria: {response.location.time_zone if response.location.time_zone else 'N/A'}")
        print(f"Precisión del Radio (km): {response.location.accuracy_radius if response.location.accuracy_radius else 'N/A'}")
        print(f"Código de Conexión Móvil (MCC): {response.traits.mobile_country_code if hasattr(response.traits, 'mobile_country_code') else 'N/A'}")
        print(f"Código de Red Móvil (MNC): {response.traits.mobile_network_code if hasattr(response.traits, 'mobile_network_code') else 'N/A'}")
        print(f"Nombre de la Organización/ISP: {response.traits.organization if hasattr(response.traits, 'organization') else 'N/A'}")
        print(f"Proveedor de Servicios de Internet (ISP): {response.traits.isp if hasattr(response.traits, 'isp') else 'N/A'}")
        print(f"Autónomo del Sistema (ASN): {response.traits.autonomous_system_number if hasattr(response.traits, 'autonomous_system_number') else 'N/A'}")
        print(f"Nombre del Autónomo del Sistema (AS): {response.traits.autonomous_system_organization if hasattr(response.traits, 'autonomous_system_organization') else 'N/A'}")
        print(f"Es una conexión de uso satelital: {'Sí' if response.traits.is_satellite_provider else 'No'}")

    except geoip2.errors.AddressNotFoundError:
        print(f"No se encontró información para la IP: {ip_o_dominio}")
    except Exception as e:
        print(f"Error al obtener información para la IP/dominio '{ip_o_dominio}': {e}")

if __name__ == "__main__":
    try:
        while True:
            entrada = input("\nIntroduce la dirección IP o el dominio que deseas buscar (o 'salir' para finalizar): ")
            if entrada.lower() == 'salir':
                break
            buscar_geoip(entrada)
    except KeyboardInterrupt:
        print("\nPrograma finalizado por el usuario.")
    finally:
        # Cerrar el lector al final del programa
        reader.close()
