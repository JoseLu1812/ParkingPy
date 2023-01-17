class Cliente:

    def __init__(self,tipo,matricula):
        self._tipo = tipo
        self._matricula = matricula

        @property
        def matricula(self):
            return self.__matricula

        @matricula.setter
        def matricula(self, matricula):
            self.__matricula = matricula

        @property
        def tipo(self):
            return self.__tipo

        @tipo.setter
        def tipo(self, tipo):
            self.__tipo = tipo
