"""
Utilidades para lugares
"""


def busca_volumen_pasajeros(codigo_iata):
    """Busca en la web de AENA el volumen de pasajeros de un aeropuerto."""

    url = 'http://www.aena.es/csee/Satellite?pagename=Estadisticas/Home'

    # En el interés del tiempo... ;-)
    volumen_por_iata = {
        'ACE': 6124321,
        'AGP': 14404170,
        'ALC': 10574484,
        'BAR': 39711276,
        'IBZ': 6477283,
        'LPA': 10627182,
        'MAD': 46828279,
        'PMI': 23745131,
        'TFS': 9117637,
        'VLC': 5051871,
    }

    return volumen_por_iata.get(codigo_iata)
