class TipoPlaza:

    def __init__(self, nombre, porcentaje, tarifa, numPlazas):
        self.__nombre = nombre
        self.__porcentaje = porcentaje
        self.__tarifa = tarifa
        self.__numPlazas = numPlazas


    def __str__(self):
        return

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

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

    @property
    def numPlazas(self):
        return self.__numPlazas

    @numPlazas.setter
    def numPlazas(self, numPlazas):
        self.__numPlazas = numPlazas
