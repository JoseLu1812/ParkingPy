from datetime import datetime

from Entities.abonado import Abonado
from Entities.cliente import Cliente
from Entities.disponibilidad import Disponibilidad
from Entities.ocupa import Ocupa
from Entities.plaza import Plaza
from Entities.tipoAbono import TipoAbono
from Entities.tipoPlaza import TipoPlaza
from Entities.tipoVehiculo import TipoVehiculo

import pickle


listaTiposVehiculo = [TipoVehiculo.TURISMO, TipoVehiculo.MOTOCICLETA, TipoVehiculo.MOVILIDAD_REDUCIDA]
archivoTipoVehi = open('Datos/tipoVehiculo.pickle', 'w')
pickle.dump(listaTiposVehiculo, archivoTipoVehi)
pickle.dump(archivoTipoVehi)


tipoAb1 = "Mensual", 25.0, 30
tipoAb2 = "Trimestral", 70, 90
tipoAb3 = "Semestral", 130, 180
tipoAb4 = "Anual", 200, 360

listaTipoAbono = [tipoAb1, tipoAb2, tipoAb3, tipoAb4]
archivoTipoAbo = open('Datos/tipoAbono.pickle', 'w')
pickle.dump(listaTipoAbono, archivoTipoAbo)
archivoTipoAbo.close(archivoTipoAbo)


listaDisponi = [Disponibilidad.LIBRE, Disponibilidad.OCUPADA, Disponibilidad.ABONO_LIBRE, Disponibilidad.ABONO_OCUPADA]
archivoDisp = open('Datos/disponibilidad.pickle', 'w')
pickle.dump(listaDisponi, archivoDisp)
pickle.close(archivoDisp)


ab1 = Abonado(1416, "C2997MGL", "Julia", "Estévez García", "53988776W", "4857 5895 3113 8392", tipoAb1, TipoVehiculo.MOTOCICLETA, "26", "julita@gmail.com", datetime(2022,12,12), datetime(2023,1,11))
ab2 = Abonado(9897, "7840FNM", "Federico", "Jiménez Márquez", "P8960559F", "4308 6780 1801 8386", tipoAb4, TipoVehiculo.TURISMO, "11", "fedejimar@gmail.com", datetime(2022,3,31), datetime(2023,3,30))
ab3 = Abonado(5274, "1337CLF", "Alberto", "Lupión González", "60367310S", "4849 2533 9794 7138", tipoAb2, TipoVehiculo.MOVILIDAD_REDUCIDA, "2", "albertitolupi@gmail.com", datetime(2022,11,8), datetime(2023,2,7))
ab4 = Abonado(5274, "7067CNJ", "Carlos", "Sánchez López", "72345767A", "4415 0343 0425 8080", tipoAb3, TipoVehiculo.TURISMO, "2", "albertitolupi@gmail.com", datetime(2022,11,8), datetime(2023,2,7))


listaAbonado = [ab1, ab2, ab3]
archivoAbonado =  open('Datos/abonado.pickle', 'w')
pickle.dump(listaAbonado, archivoAbonado)
pickle.close(archivoAbonado)





