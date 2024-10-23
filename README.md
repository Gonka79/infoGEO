# IP Geolocation Tool with MaxMind GeoLite2

This project allows you to obtain detailed geographical information about IP addresses using the local **GeoLite2-City** database from MaxMind and the `geoip2` library for Python. The script resolves a domain or IP and prints data such as country, city, region, coordinates, internet service provider, and more.

## Features
- Detailed IP information, including country, city, region, postal code, ISP, and more.
- Resolves domain names to IP addresses.
- Uses a local database for fast and unlimited queries.

## Requirements
- Python 3.x
- `geoip2` and `socket` libraries to perform geographic lookups.
- **GeoLite2-City.mmdb** database downloaded from MaxMind. You can download it for free [here](https://dev.maxmind.com/geoip/geolite2-free-geolocation-data).

## Installation
1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/repository-name.git
   cd repository-name
   ```

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv myenv
   source myenv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Place the `GeoLite2-City.mmdb` database in the project folder.

## Usage
Run the script to enter a domain or IP address and get geographical information:

```bash
python3 infoGEO.py
```

The script will prompt you to enter an IP address or domain. It will display detailed geographical information about the entered IP, such as:
- Country and ISO code
- Continent and continent code
- Region and city
- Latitude and longitude
- Internet service provider (ISP)

## Contributions
Contributions are welcome. You can fork the repository and submit a Pull Request with improvements or corrections.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

# Herramienta de Geolocalización de IPs con MaxMind GeoLite2

Este proyecto permite obtener información geográfica detallada de direcciones IP usando la base de datos local **GeoLite2-City** de MaxMind y la librería `geoip2` para Python. El script resuelve un dominio o IP e imprime datos como país, ciudad, región, coordenadas, proveedor de servicios de internet, y más.

## Características
- Información detallada de IPs, incluyendo país, ciudad, región, código postal, ISP, y más.
- Resuelve nombres de dominio a direcciones IP.
- Uso de base de datos local para consultas rápidas y sin limitaciones.

## Requisitos
- Python 3.x
- `geoip2` y `socket` para realizar las consultas geográficas.
- Base de datos **GeoLite2-City.mmdb** descargada de MaxMind. Puedes descargarla de forma gratuita [aquí](https://dev.maxmind.com/geoip/geolite2-free-geolocation-data).

## Instalación
1. Clonar el repositorio:

   ```bash
   git clone https://github.com/tu-usuario/nombre-del-repositorio.git
   cd nombre-del-repositorio
   ```

2. Crear un entorno virtual y activar:

   ```bash
   python3 -m venv myenv
   source myenv/bin/activate
   ```

3. Instalar las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Colocar la base de datos `GeoLite2-City.mmdb` en la carpeta del proyecto.

## Uso
Ejecuta el script para ingresar un dominio o dirección IP y obtener información geográfica:

```bash
python3 infoGEO.py
```

El script te solicitará que ingreses una dirección IP o un dominio. Se mostrará la información geográfica detallada de la IP ingresada, como:
- País y código ISO
- Continente y código del continente
- Región y ciudad
- Latitud y longitud
- Proveedor de servicios de internet (ISP)

## Contribuciones
Las contribuciones son bienvenidas. Puedes hacer un fork del repositorio y enviar un Pull Request con mejoras o correcciones.

## Licencia
Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.

