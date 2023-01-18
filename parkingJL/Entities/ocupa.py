from datetime import datetime
class Ocupa:

    def __init__(self, plaza, cliente, pin, entrada=datetime.now(), salida=None, costeTotal=None, activo=True):
        self.__plaza = plaza
        self.__cliente = cliente
        self.__pin = pin
        self.__entrada = entrada
        self.__salida = salida
        self.__activo = activo
        self.__costeTotal = costeTotal

    @property
    def plaza(self):
        return self.__plaza

    @plaza.setter
    def plaza(self, plaza):
        self.__plaza = plaza

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente

    @property
    def pin(self):
        return self.__pin

    @pin.setter
    def pin(self, pin):
        self.__pin = pin

    @property
    def entrada(self):
        return self.__entrada

    @entrada.setter
    def entrada(self, entrada):
        self.__entrada = entrada

    @property
    def salida(self):
        return self.__salida

    @salida.setter
    def salida(self, salida):
        self.__salida = salida

    @property
    def activo(self):
        return self.__activo

    @activo.setter
    def activo(self, activo):
        self.__activo = activo

    @property
    def costeTotal(self):
        return self.__costeTotal

    @costeTotal.setter
    def costeTotal(self, costeTotal):
        self.__costeTotal = costeTotal