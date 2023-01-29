from datetime import datetime, timedelta

from Entities.abonado import Abonado
from Entities.cliente import Cliente
from Entities.disponibilidad import Disponibilidad
from Entities.ocupa import Ocupa
from Entities.plaza import Plaza
from Entities.tipoAbono import TipoAbono
from Entities.tipoPlaza import TipoPlaza
from Entities.tipoVehiculo import TipoVehiculo

import pickle

def service():

    
    open("Datos/tipoAbono.p", "w").close()
    open("Datos/plaza.p", "w").close()
    open("Datos/cliente.p", "w").close()
    open("Datos/ocupa.p", "w").close()
    open("Datos/tipoVehiculo.p", "w").close()


    numPlazas = 200
    plazasTurismos = TipoPlaza(TipoVehiculo.TURISMO, 0.12, 70)
    plazasMotos = TipoPlaza(TipoVehiculo.MOTOCICLETA, 0.08, 15)
    plazasReducidas = TipoPlaza(TipoVehiculo.MOVILIDAD_REDUCIDA, 0.10, 15)
    tiposPlazas = [plazasTurismos, plazasMotos, plazasReducidas]
    archivoTipoPlaza = open("Datos/tipoPlaza.p", "wb")
    pickle.dump(tiposPlazas, archivoTipoPlaza)


    listaTiposVehiculo = [TipoVehiculo.TURISMO, TipoVehiculo.MOTOCICLETA, TipoVehiculo.MOVILIDAD_REDUCIDA]
    archivoTipoVehi = open('Datos/tipoVehiculo.p', 'w')
    pickle.dump(listaTiposVehiculo, archivoTipoVehi)
    pickle.dump(archivoTipoVehi)


    tipoAb1 = "Mensual", 25.0, 30
    tipoAb2 = "Trimestral", 70, 90
    tipoAb3 = "Semestral", 130, 180
    tipoAb4 = "Anual", 200, 360

    listaTipoAbono = [tipoAb1, tipoAb2, tipoAb3, tipoAb4]
    archivoTipoAbo = open('Datos/tipoAbono.p', 'w')
    pickle.dump(listaTipoAbono, archivoTipoAbo)
    archivoTipoAbo.close(archivoTipoAbo)


    listaDisponi = [Disponibilidad.LIBRE, Disponibilidad.OCUPADA, Disponibilidad.ABONO_LIBRE, Disponibilidad.ABONO_OCUPADA]
    archivoDisp = open('Datos/disponibilidad.p', 'w')
    pickle.dump(listaDisponi, archivoDisp)
    pickle.close(archivoDisp)


    plazas = []
    for tipoP in tiposPlazas:
        idX += 100
        tipoP.numPlazas = int(numPlazas * (tipoP.porcentaje / 100))
        for i in range(tipoP.numPlazas):
            plazas.append(Plaza(idX + i, tipoP))

    clientes = []
    c1 = Cliente(TipoVehiculo.MOVILIDAD_REDUCIDA, "71439DNF")
    c2 = Cliente(TipoVehiculo.MOTOCICLETA, "L7878KLC")
    c3 = Cliente(TipoVehiculo.MOTOCICLETA, "L8582MSD")
    ab1 = Abonado(1416, "C2997MGL", "Julia", "Estévez García", "53988776W", "4857 5895 3113 8392", tipoAb1, TipoVehiculo.MOTOCICLETA, "26", "julita@gmail.com", datetime(2022,12,12), datetime(2023,1,11))
    ab2 = Abonado(9897, "7840FNM", "Federico", "Jiménez Márquez", "P8960559F", "4308 6780 1801 8386", tipoAb4, TipoVehiculo.TURISMO, "11", "fedejimar@gmail.com", datetime(2022,3,31), datetime(2023,3,30))
    ab3 = Abonado(5274, "1337CLF", "Alberto", "Lupión González", "60367310S", "4849 2533 9794 7138", tipoAb2, TipoVehiculo.MOVILIDAD_REDUCIDA, "2", "albertitolupi@gmail.com", datetime(2022,11,8), datetime(2023,2,7))
    ab4 = Abonado(5274, "7067CNJ", "Carlos", "Sánchez López", "72345767A", "4415 0343 0425 8080", tipoAb3, TipoVehiculo.TURISMO, "2", "albertitolupi@gmail.com", datetime(2022,11,8), datetime(2023,2,7))

    clientes.append(c1)
    clientes.append(c2)
    clientes.append(c3)
    clientes.append(ab1)
    clientes.append(ab2)
    clientes.append(ab3)
    clientes.append(ab4)
    plazas[25].disponibilidad = Disponibilidad.ABONO_LIBRE

    ocupas = []
    entrada = datetime.now() - timedelta(days=2, hours=1, minutes=15)
    salida = datetime.now() - timedelta(days=2)
    tiempoEstacionado = divmod((salida - entrada).total_seconds(), 60)[0]
    ocupacion1 = Ocupa(plazas[3], c1, ab1.pin, datetime.now() - timedelta(days = 10), timedelta(days = 8), 0, False)
    ocupacion2 = Ocupa(plazas[0], c2, 763248, entrada, salida, tiempoEstacionado * plazas[0].tipoPlaza.tarifa, False)
    ocupas.append(ocupacion1)
    ocupas.append(ocupacion2)

    archivoPlazas = open("Datos/plaza.p", "wb")
    pickle.dump(plazas, archivoPlazas)
    archivoPlazas.close()

    archivoOcupa = open("Datos/ocupa.p", "wb")
    pickle.dump(ocupas, archivoOcupa)
    archivoOcupa.close()

    archivoClientes = open("Datos/cliente.p", "wb")
    pickle.dump(clientes, archivoClientes)
    archivoClientes.close()








