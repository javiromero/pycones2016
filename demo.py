#!/usr/bin/env python3

from lugares.datos import LUGARES
from lugares.utiles import busca_volumen_pasajeros


def main():
    """Actualiza los aeropuertos con el volumen de pasajeros anual."""
    # import ipdb; ipdb.set_trace()
    aeropuertos = LUGARES['aeropuerto']
    actualizados = 0

    for aeropuerto in aeropuertos:
        if not aeropuerto.volumen:
            nuevo_volumen = busca_volumen_pasajeros(aeropuerto.codigo_iata)
            aeropuerto.volumen = nuevo_volumen
            actualizados += 1

    print("Actualizados {}".format(actualizados))

if __name__ == '__main__':
    main()
