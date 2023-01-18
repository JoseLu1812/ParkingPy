class Plaza:

    def __init__(self, numero, tipoPlaza, disponibilidad):
        self.__numero = numero
        self.__tipoPlaza = tipoPlaza
        self.__disponibilidad = disponibilidad

    def __str__(self):
        return f"Plaza Nº" + self.__num + ", Para" + self.__tipoPlaza + ". \nDisponibilidad: " + self.__disponibilidad + "."

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    @property
    def tipoPlaza(self):
        return self.__tipoPlaza

    @numero.setter
    def tipoPlaza(self, tipoPlaza):
        self.__tipoPlaza = tipoPlaza

    @property
    def disponiblidad(self):
        return self.__disponiblidad

    @numero.setter
    def disponiblidad(self, disponiblidad):
        self.__disponiblidad = disponiblidad