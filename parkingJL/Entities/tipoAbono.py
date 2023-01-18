class TipoAbono:

    def __init__(self, nombre, precio, caducidad):
        self.__nombre = nombre
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
        return self.__precio

    @precio.setter
    def precio(self, precio):
        self.__precio = precio

    @property
    def caducidad(self):
        return self.__caducidad

    @caducidad.setter
    def caducidad(self, caducidad):
        self.__caducidad = caducidad
