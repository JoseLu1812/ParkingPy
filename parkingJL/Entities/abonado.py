from Entities.cliente import Cliente


class Abonado(Cliente):

    def __init__(self, pin, matricula, nombre, apellidos, dni, visa, tipoAbono, tipovehiculo, plaza, email, fechaSubs, fechaCanc):
        super().__init__(matricula, tipovehiculo)
        self.__pin = pin
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__dni = dni
        self.__email = email
        self.__visa = visa
        self.__tipoAbono = tipoAbono
        self.__fechaSubs = fechaSubs
        self.__fechaCanc = fechaCanc
        self.__plaza = plaza
        self.__pin = pin

    def __str__(self):
        return

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, dni):
        self.__dni = dni

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def apellidos(self):
        return self.__apellidos

    @apellidos.setter
    def apellidos(self, apellidos):
        self.__apellidos = apellidos

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def tarjeta(self):
        return self.__visa

    @tarjeta.setter
    def tarjeta(self, visa):
        self.__visa = visa

    @property
    def tipoAbono(self):
        return self.__tipoAbono

    @tipoAbono.setter
    def tipoAbono(self, tipoAbono):
        self.__tipoAbono = tipoAbono

    @property
    def fechaSubs(self):
        return self.__fechaSubs

    @fechaSubs.setter
    def fechaSubs(self, fechaSubs):
        self.__fechaSubs = fechaSubs

    @property
    def fechaCanc(self):
        return self.__fechaCanc

    @fechaCanc.setter
    def fechaCanc(self, fechaCanc):
        self.__fechaCanc = fechaCanc

    @property
    def activo(self):
        return self.__activo

    @activo.setter
    def activo(self, activo):
        self.__activo = activo

    @property
    def plaza(self):
        return self.__plaza

    @plaza.setter
    def plaza(self, plaza):
        self.__plaza = plaza

    @property
    def pin(self):
        return self.__pin

    @pin.setter
    def pin(self, pin):
        self.__pin = pin

