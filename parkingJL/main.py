from datetime import datetime, timedelta
import random
import pickle
import time
from threading import Thread

from Entities.abonado import Abonado
from Entities.cliente import Cliente
from Entities.disponibilidad import Disponibilidad
from Entities.ocupa import Ocupa
from Entities.tipoVehiculo import TipoVehiculo
from Views.views import Views


archivoAbono = open("Datos/tipoAbono.p", "rb")
archivoPlaza = open("Datos/plaza.p", "rb")
archivoCliente = open("Datos/cliente.p", "rb")
archivoOcupa = open("Datos/ocupa.p", "rb")
archivoTipoPlaza = open("Datos/tipoPlaza.p", "rb")


abonos = pickle.load(archivoAbono)
plazas = pickle.load(archivoPlaza)
clientes = pickle.load(archivoCliente)
ocupas = pickle.load(archivoOcupa)
tipoPlazas = pickle.load(archivoTipoPlaza)


archivoAbono.close()
archivoPlaza.close()
archivoCliente.close()
archivoOcupa.close()
archivoTipoPlaza.close()


def persistCollections():
    on = True
    while on:
        i=0
        while i < 300:
            if mainThread.is_alive():
                time.sleep(1)
                i += 1
            else:
                i = 300
                on = False

        open("Persistence/tipoAbono.p", "w").close()
        open("Persistence/ocupa.p", "w").close()
        open("Persistence/plaza.p", "w").close()
        open("Persistence/cliente.p", "w").close()
        open("Persistence/tipoPlaza.p", "w").close()

        archivoAbono = open("Persistence/tipoAbonos.pickle", "wb")
        pickle.dump(abonos, archivoAbono)
        archivoAbono.close()
        archivoTipoPlaza = open("Persistence/tipoVehiculo.p", "wb")
        pickle.dump(tipoPlazas, archivoTipoPlaza)
        archivoTipoPlaza.close()
        archivoPlaza = open("Persistence/plaza.p", "wb")
        pickle.dump(plazas, archivoPlaza)
        archivoPlaza.close()
        archivoOcupa = open("Persistence/ocupa.p", "wb")
        pickle.dump(ocupas, archivoOcupa)
        archivoOcupa.close()
        archivoCliente = open("Persistence/cliente.p", "wb")
        pickle.dump(clientes, archivoCliente)
        archivoCliente.close()


def main():

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

            while x != 0:
                Views.menuCliente()

                try:
                    x = input()
                except:
                    print('Indique un número válido: ')

                if x == 1:
                    plazasDisp = [plaza for plaza in plazas if plaza.estado == Disponibilidad.LIBRE]
                    turismoDisp = len([plaza for plaza in plazasDisp if plaza.tipoPlaza.tipo == TipoVehiculo.TURISMO])
                    motosDisp = len([plaza for plaza in plazasDisp if plaza.tipoPlaza.tipo == TipoVehiculo.MOTOCICLETA])
                    movRedDisp = len([plaza for plaza in plazasDisp if plaza.tipoPlaza.tipo == TipoVehiculo.MOVILIDAD_REDUCIDA])
                    if len(plazasDisp) > 0:
                        Views.imprimirPlazasDisp(plazasDisp, turismoDisp, motosDisp, movRedDisp)
                        Views.menuTipoVehiculo()
                        try:
                            x2 = list(TipoVehiculo)[int(input()) - 1]
                            if (x2 == TipoVehiculo.TURISMO and turismoDisp > 0) or (x2 == TipoVehiculo.MOTOCICLETA and motosDisp > 0) or (x2 == TipoVehiculo.MOVILIDAD_REDUCIDA and movRedDisp > 0) :
                                matricula = input("Introduzca su matrícula: ")
                                plaza = [plaza for plaza in plazasDisp if plaza.tipoPlaza.tipo == tipoVehiculo][0]
                                plaza.estado = Disponibilidad.OCUPADA
                                plazaOcupada = Ocupa(plaza, Cliente(matricula, tipoVehiculo), random.randint(100000, 999999))
                                ocupas.append(plazaOcupada)
                                print(f"- Matricula: {plazaOcupada.cliente.matricula}")
                                print(f"- Id: {plazaOcupada.plaza.numero}")
                                print(f"- Pin: {plazaOcupada.pin}")
                            else:
                                print("No hay plazas disponibles")
                        except:
                            print("Introduzca una opción válida")
                    else:
                        print("No hay plazas disponibles")

                elif x == 2:
                    try:
                        matricula = input("Introduzca su matrícula: ")
                        numPlaza = int(input("Escriba el número de plaza: "))
                        pin = int(input("Pin: "))
                        ocupas = [ocupa for ocupa in ocupas if ocupa.plaza.numero == numPlaza and ocupa.cliente.matricula == matricula and ocupa.pin == pin]
                        if(len(ocupa) >= 1):
                            ocupa = ocupas[0]
                            ocupa.activo = False
                            ocupa.salida = datetime.now()
                            tiempo = divmod((ocupa.salida - ocupa.entrada).total_seconds(), 60)[0]
                            ocupa.costeTotal = ocupa.plaza.tipoPlaza.tarifa * tiempo
                            ocupa.plaza.estado = Disponibilidad.LIBRE
                            print(f"- Coste final: {ocupa.costeTotal}€")
                        else:
                            print("No se encuentra el vehículo...")
                    except:
                        print("Datos erróneos. Indiquelos de nuevo: ")

                elif x == 3:
                    dni = input("Introduzca su dni: ")
                    matricula = input("Escriba su matrícula: ")
                    try:
                        cliente = next(cliente for cliente in clientes if isinstance(cliente, Abonado) and cliente.activo and cliente.matricula == matricula and cliente.dni == dni)
                        print(f"Adelante...")
                        print(f"Su plaza es: {cliente.plaza.numero}")
                        cliente.plaza = [plaza for plaza in plazas if plaza.numero == cliente.plaza.numero][0]
                        cliente.plaza.disponilidad = Disponibilidad.ABONO_OCUPADA
                        ocupas.append(Ocupa(cliente.plaza, cliente, cliente.pin, costeTotal=0))
                    except:
                        print("Vehículo no encontrado...")

                elif x == 4:
                    dni = input("Introduzca su dni: ")
                    matricula = input("Escriba su matrícula: ")
                    pin = input("Pin: ")
                    try:
                        ocupa = next(ocupa for ocupa in ocupas if ocupa.activo and ocupa.pin == int(pin) and ocupa.cliente.matricula == matricula and ocupa.cliente.dni == dni)
                        print("¡Hasta luego. Vuelva pronto!")
                        cliente.plaza.disponibilidad = Disponibilidad.ABONO_LIBRE
                        ocupa.activo = False
                    except:
                        print("Vehículo no encontrado...")

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
                    Views.menuAbonados()
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

                            Views.menuTipoVehiculo()
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
                            Views.menuModifAbonado()
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
                                    cadAntigua = abonado.fechaCanc
                                    abonado.fechaCanc = cadAntigua + timedelta(
                                        days=30 * abonado.tipoAbono.caducidad)
                                    print(f"El Abono {abonado.tipoAbono.tipo} a nombre de {abonado.nombre} {abonado.apellidos} ha sido actualizado.")
                                    print(f"\t- Nueva Fecha de Cancelación: {abonado.fechaCanc}")
                            except:
                                print('Indique un número válido: ')

                        except:
                            print('DNI no encontrado o no válido...')
                            print('Introduzca un DNI de nuevo: ')

                    elif y2 == 3:
                        dni = input("Indique el DNI: ")
                        try:
                            abonado = next(
                                cliente for cliente in clientes if isinstance(cliente, Abonado) and cliente.dni == dni)
                            if abonado.activo:
                                Views.confirmarBaja()
                                i = int(input())
                                if i == 1:
                                    abonado.plaza = [plaza for plaza in plazas if plaza.id == abonado.plaza.id][0]
                                    abonado.plaza.estado = Disponibilidad.LIBRE
                                    print("Cliente dado de baja...")
                            else:
                                print("El cliente indicado no consta de ningún abono...")
                        except:
                            print("Cliente no encontrado...")

                elif y == 5:
                    Views.menuCadAbonos()
                    try:
                        y2 = int(input())
                    except:
                        print("Por favor introduzca un número.")

                    if y2 == 1:
                        month = int(input("Indique el nº del mes que quiere consultar: "))
                        year = int(input("Indique el año que quiere consultar: "))
                        aCaducar = [cliente for cliente in clientes if isinstance(cliente, Abonado) and cliente.fechaCanc.month == month and cliente.fechaCanc.year == year]
                        Views.imprimirClientesACaducar(aCaducar)
                        if len(aCaducar) == 0: print("No hay ningún cliente cuyo abono caduque en ese mes.")

                    elif y2 == 2:
                        aCaducar = [cliente for cliente in clientes if isinstance(cliente, Abonado) and cliente.fechaCanc > datetime.now() and cliente.fechaCanc < datetime.now() + timedelta(days = 10)]
                        Views.imprimirClientesACaducar(aCaducar)
                        if len(aCaducar) == 0: print("No hay ningún cliente cuyo abono caduque en 10 días.")


mainThread = Thread(target=main)
persistenceThread = Thread(target=persistCollections)
mainThread.start()
persistenceThread.start()

