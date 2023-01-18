class Views:

    def inicio(self):
        print('Escoja una opción de acceso mediante su Nº: \n\n' +
            '1. Zona Cliente.\n' +
            '2. Zona Administración\n\n')
    def menuCliente(self):

        print('¿Qué operación desea realizar?\n\n' +
              '1. Depositar vehículo\n' +
              '2. Retirar vehículo\n' +
              '3. Depositar abonados\n'+
              '4. Retirar abonados\n\n')

    def menuAdministrador(self):
        print('¿Qué operación desea realizar?\n\n' +
              '1. Estado del parking\n' +
              '2. Facturación\n' +
              '3. Consulta abonados\n' +
              '4. Abonos\n' +
              '5. Caducidad de abonos\n\n')

