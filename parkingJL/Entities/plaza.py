class Plaza:

    def __init__(self, numero, tipoPlaza, disponibilidad):
        self._numero = numero
        self._tipoPlaza = tipoPlaza
        self._disponibilidad = disponibilidad

    def __str__(self):
        return "Plaza Nº" + self._num + ", Para" + self._tipoPlaza + ". \nDisponibilidad: " + self._disponibilidad + "."

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, numero):
        self._numero = numero

    @property
    def tipoPlaza(self):
        return self._tipoPlaza

    @numero.setter
    def tipoPlaza(self, tipoPlaza):
        self._tipoPlaza = tipoPlaza

    @property
    def disponiblidad(self):
        return self._disponiblidad

    @numero.setter
    def disponiblidad(self, disponiblidad):
        self._disponiblidad = disponiblidad