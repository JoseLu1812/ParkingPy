class TipoPlaza:

    def __init__(self, nombre, porcentaje, tarifa):
        self.__nombre = nombre
        self.__porcentaje = porcentaje
        self.__tarifa = tarifa

    def __str__(self):
        return

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo

    @property
    def porcentaje(self):
        return self.__porcentaje

    @porcentaje.setter
    def porcentaje(self, porcentaje):
        self.__porcentaje = porcentaje

    @property
    def tarifa(self):
        return self.__tarifa

    @tarifa.setter
    def tarifa(self, tarifa):
        self.__tarifa = tarifa
