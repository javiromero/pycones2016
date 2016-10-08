"""
Modelos personalizados para lugares
"""


class Aeropuerto:

    def __init__(self, **kwargs):
        for name, value in kwargs.items():
            self.__dict__[name] = value

    def __getattr__(self, name):
        try:
            value = self.__dict__[name]
        except KeyError:
            value = 0
        return value

    def __repr__(self):
        return 'Aeropuerto({})'.format(self.__dict__)
