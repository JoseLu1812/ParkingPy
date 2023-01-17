class TipoPlaza:

    def __init__(self, tipo, porcentaje, tarifa):
        self._tipo = tipo
        self._porcentaje = porcentaje
        self._tarifa = tarifa

    def __str__(self):
        return

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

    @property
    def porcentaje(self):
        return self._porcentaje

    @porcentaje.setter
    def porcentaje(self, porcentaje):
        self._porcentaje = porcentaje

    @property
    def tarifa(self):
        return self._tarifa

    @tarifa.setter
    def tarifa(self, tarifa):
        self._tarifa = tarifa
