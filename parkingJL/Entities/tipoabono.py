class TipoAbono:

    def __init__(self, tipo, precio, caducidad):
        self.__tipo = tipo
        self.__precio = precio
        self.__caducidad = caducidad

    def __str__(self):
        return

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, precio):
        self._precio = precio

    @property
    def caducidad(self):
        return self._caducidad

    @caducidad.setter
    def caducidad(self, caducidad):
        self._caducidad = caducidad
