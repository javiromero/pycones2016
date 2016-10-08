"""
Estructura que almacena la informacion de lugares.
"""

from lugares.modelos import Aeropuerto


AEROPUERTOS = (
    Aeropuerto(nombre='Adolfo Suárez Madrid-Barajas', codigo_iata='MAD'),
    Aeropuerto(nombre='Barcelona-El Prat', codigo_iata='BAR'),
    Aeropuerto(nombre='Palma de Mallorca', codigo_iata='PMI'),
    Aeropuerto(nombre='Malaga-Costa del Sol', codigo_iata='AGP'),
    Aeropuerto(nombre='Alicante-Elche', codigo_iata='ALC'),
    Aeropuerto(nombre='Ibiza', codigo_iata='IBZ'),
    Aeropuerto(nombre='Valencia', codigo_iata='VLC'),
    Aeropuerto(nombre='Gran Canaria', codigo_iata='LPA,'),
    Aeropuerto(nombre='Tenerife Sur', codigo_iata='TFS,'),
    Aeropuerto(nombre='Lanzarote', codigo_iata='ACE,'),
)

LUGARES = {
    'aeropuerto': AEROPUERTOS,
}
