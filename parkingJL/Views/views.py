class Views:

    def inicio(self):
        print('Escoja una opción de acceso mediante su Nº: \n\n' +
            '0. Salir\n' +
            '1. Zona Cliente.\n' +
            '2. Zona Administración\n\n')
    def menuCliente(self):

        print('¿Qué operación desea realizar?\n\n' +
              '0. Salir\n' +
              '1. Depositar vehículo\n' +
              '2. Retirar vehículo\n' +
              '3. Depositar abonados\n'+
              '4. Retirar abonados\n\n')

    def menuAdministrador(self):
        print('¿Qué operación desea realizar?\n\n' +
              '0. Salir\n' +
              '1. Estado del parking\n' +
              '2. Facturación\n' +
              '3. Consulta abonados\n' +
              '4. Abonos\n' +
              '5. Caducidad de abonos\n\n')

    def imprimirPlazas(self, plaza):
        pos = 1
        for plaza in plaza:
            if pos < 5:
                print(f"- {plaza.id} ---> {plaza.estado.value} -")
                pos += 1
            else:
                print(f"- {plaza.id} ---> {plaza.estado.value} -")
                pos = 1

    def imprimirPagos(self, pagos):
        for pago in pagos:
            print(
                f"Plaza {pago.plaza.numero}:\n" +
                f"\t\t - {pago.plaza.tipoPlaza.tipo.value}) "
                f"\t\t - {pago.entrada.strftime('%d/%m/%Y, %H:%M:%S')} hasta {pago.salida.strftime('%d/%m/%Y, %H:%M:%S')} "
                f"\t\t - Total = {pago.costeTotal} €")

    def imrpimirAbonados(self, abonados):
        if len(abonados) == 0:
            print("No hay abonados...")
        for abonado in abonados:
            print(
                f"{abonado.nombre} {abonado.apellidos}: "
                f"\t -Suscripcion: {abonado.tipoAbono.tipo}"
                f"\t -Fecha de Caducidad:  {abonado.fechaCanc.strftime('%d de %B del %Y')}")

    def imrprimirMenuTipoVehiculo(self):
        print("Seleccione el tipo del vehículo: ")
        print("1. Turismo.")
        print("2. Motocicleta.")
        print("3. Vehículo para personas con movilidad reducida.")

    def imprimirMenuAbonados(self):
        print("1. Alta de abonado")
        print("2. Modificación de datos del abonado")
        print("3. Baja del abonado")

    def imprimirMenuModifAbonado(self):
        print("1. Modificar datos del cliente")
        print("2. Renovar abono")

    def imprimirPlazasDisp(self, plazasDisp, dispTurismo, dispMoto, dispMovRed):
        print(f"Plazas Disponibles Totales: {len(plazasDisp)}")
        print(
            f"- Plazas disponibles para turismos:\t" if dispTurismo > 0 else "0")
        print(
            f"- Plazas disponibles para motos:\t" if dispMoto > 0 else "0")
        print(
            f"- Plazas disponibles para vehículos para personas con movilidad reducidad:\t" if dispMovRed > 0 else "0")









