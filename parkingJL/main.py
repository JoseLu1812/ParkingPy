from datetime import datetime, timedelta
import random
import time
import pickle

from Entities.abonado import Abonado
from Entities.cliente import Cliente
from Entities.disponibilidad import Disponibilidad
from Entities.ocupa import Ocupa
from Entities.plaza import Plaza
from Entities.tipoAbono import TipoAbono
from Entities.tipoPlaza import TipoPlaza
from Entities.tipoVehiculo import TipoVehiculo
from Views.views import Views


archivoAbono = open("Datos/tiposAbono.pickle", "rb")
archivoPlaza = open("Datos/plaza.pickle", "rb")
archivoCliente = open("Datos/cliente.pickle", "rb")
archivoOcupa = open("Datos/ocupa.pickle", "rb")

abonos = pickle.load(archivoAbono)
plazas = pickle.load(archivoPlaza)
clientes = pickle.load(archivoCliente)
ocupas = pickle.load(archivoOcupa)

archivoAbono.close()
archivoPlaza.close()
archivoCliente.close()
archivoOcupa.close()


def Main():

    i = -1

    while i != 0:

        x = -1
        x2 = -1
        y = -1
        y2 = -1
        y3 = -1
        print(Views.inicio())

        try:
            select = int(input())
        except:
            print('Indique un número válido: ')

        if select == 1:
            Views.menuCliente()
            x = input()
            if x == 1:

            elif x == 2:

            elif x == 3:

            elif x == 4:

            elif x == 5:

            else:
                pass


        elif select == 2:
            Views.menuAdministrador()
            while y != 0:
                try:
                    y = int(input())
                except:
                    print('Indique un número válido: ')
                if y == 1:
                    plazasDisp = len([plaza for plaza in plazas if plaza.estado == Disponibilidad.LIBRE])
                    porcentaje = (200 - plazasDisp) / (200 / 100)
                    print(
                        f"Plazas disponibles: {plazasDisp}" +
                        f"Porcentaje de ocupación: {porcentaje}%")
                    Views.imprimirPlazas(plazas)

                elif y == 2:
                    try:
                        print("Introduzca la fecha de inico a consultar: ")
                        yearIni = input("Año: ")
                        monthIni = input("Mes: ")
                        dayIni = input("Día: ")
                        hourIni = input("Hora: ")
                        minIni = input("Minutos: ")
                        ini = datetime(int(yearIni), int(monthIni), int(dayIni), int(hourIni),
                                          int(minIni))
                        print("Introduzca la fecha de fin a consultar: ")
                        yearFin = input("Año: ")
                        monthFin = input("Mes: ")
                        dayFin = input("Día: ")
                        hourFin = input("Hora: ")
                        minFin = input("Minutos: ")
                        fin = datetime(int(yearFin), int(monthFin), int(dayFin), int(hourFin), int(minFin))
                        pagos = [ocupa for ocupa in ocupas if (not ocupa.activo) and (
                                    ocupa.costeTotal > 0 and ocupa.salida < fin and ocupa.salida > ini)]
                        Views.imprimirPagos(pagos)
                    except:
                        print(
                            "Indique las fechas correctamente, escribiendo el año, mes, dia, y horas con números.")

                elif y == 3:
                    abonados = [cliente for cliente in clientes if isinstance(cliente, Abonado) and cliente.activo]
                    Views.imrpimirAbonados(abonados)

                elif y == 4:
                    Views.imprimirMenuAbonados()
                    try:
                        y2 = int(input())
                    except:
                        print('Indique un número válido: ')

                    if y2 == 1:
                        dni = input("Dni: ")
                        nombre = input("Nombre: ")
                        apellidos = input("Apellidos: ")
                        email = input("Email: ")

                        try:
                            print("Seleccione el tipo de abono: ")
                            for i, abono in enumerate(abonos):
                                print(f"{i+1}. {abono.nombre} = {abono.precio}€")
                            tipoAbono = abonos[int(input()) - 1]
                            visa = input("Tarjeta de Crédito: ")

                            Views.printMenuTipoVehiculo()
                            tipoVehiculo = list(TipoVehiculo)[int(input()) - 1]
                            matricula = input("Matrícula: ")
                            plaza = next(plaza for plaza in plazas if plaza.estado == Disponibilidad.LIBRE and plaza.tipoPlaza.tipo == tipoVehiculo)
                            pin = random.randint(100000, 999999)

                            nuevoCliente = Abonado(pin, matricula, nombre, apellidos, dni, tipoVehiculo, dni, visa, tipoAbono, plaza, email, datetime.now(), datetime.now() + timedelta(days = 30 * tipoAbono.caducidad))
                            clientes.append(nuevoCliente)
                            plaza.estado = Disponibilidad.ABONO_LIBRE
                            print("Abonado creado con éxito.")
                        except:
                            print('Indique un número válido: ')

                    elif y2 == 2:
                        dni = input("Indique el DNI: ")
                        try:
                            abonado = next(cliente for cliente in clientes if
                                           isinstance(cliente, Abonado) and cliente.activo and cliente.dni == dni)
                            Views.imprimirMenuModifAbonado()
                            y3 = int(input())

                            try:

                                if y3 == 1:
                                    print(
                                        "Introduzca los datos a continuación, para mantener el actual, simplemente pulse intro.")
                                    abonado.dni = input(f"Abonado:\n" +
                                                        f"- Dni actual: {abonado.dni}): ") or abonado.dni
                                    abonado.nombre = input(
                                        f"- Nombre actual: {abonado.nombre}): ") or abonado.nombre
                                    abonado.apellidos = input(
                                        f"- Apellidos actual: {abonado.apellidos}): ") or abonado.apellidos
                                    abonado.email = input(f"Email actual: {abonado.email}): ") or abonado.email
                                    abonado.matricula = input(
                                        f"- Matricula actual: {abonado.matricula}): ") or abonado.matricula
                                    abonado.tarjeta = input(
                                        f"- Tarjeta actual: {abonado.tarjeta}): ") or abonado.tarjeta

                                elif y3 == 2:
                                    cadAntigua = abonado.fechaCancelacion
                                    abonado.fechaCanc = cadAntigua + timedelta(
                                        days=30 * abonado.tipoAbono.caducidad)
                                    print(f"El Abono {abonado.tipoAbono.tipo} a nombre de {abonado.nombre} {abonado.apellidos} ha sido actualizado.")
                                    print(f"\t- Nueva Fecha de Cancelación: {abonado.fechaCanc}")
                            except:
                                print('Indique un número válido: ')

                        except:
                            print('DNI no encontrado o no válido...')
                            print('Introduzca un DNI de nuevo: ')

        else:
            pass

