class Cliente:

    def __init__(self,tipoVehiculo,matricula):
        self._tipoVehiculo = tipoVehiculo
        self._matricula = matricula

    def __str__(self):
        return

    @property
    def matricula(self):
            return self.__matricula

    @matricula.setter
    def matricula(self, matricula):
            self.__matricula = matricula

    @property
    def tipoVehiculo(self):
            return self.__tipoVehiculo

    @tipoVehiculo.setter
    def tipo(self, tipoVehiculo):
            self.__tipoVehiculo = tipoVehiculo
