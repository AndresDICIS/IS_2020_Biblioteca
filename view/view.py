class View:
    """
    ******************************************
    * Vista para base de datos de Biblioteca *
    ******************************************
    """

    def start(self):
        print("======================================")
        print("=Bienvenido al sistema de Biblioteca.=")
        print("======================================")

    def end(self):
        print("======================================")
        print("=        Sistema cerrado             =")
        print("======================================")
    
    def menu_principal(self):
        print("======================================")
        print("=           Menu Principal           =")
        print("======================================")
        print('1.- Prestamos')
        print('2.- Usuarios')
        print('3.- Libros')
        print('4.- Codigos Postales')
        print('5.- Secciones')
        print('6.- Relacion de libros y secciones')
        print('7.- Salir')

    def opcion(self, last):
        print('Selecciona una opcion (1-'+last+'): ', end = '')

    def opcion_invalida(self):
        print('¡Opcion no valida!\nIntente de nuevo')
    
    def preguntar(self, output):
        print(output, end = '')
    
    def mensaje(self, output):
        print(output)
    
    def Ok(self, id, op):
        print('+'*(len(str(id))+len(op)+24))
        print('+ ¡'+ str(id)+' se '+op+' correctamente! +')
        print('+'*(len(str(id))+len(op)+24))

    def error(self, err):
        print(' ¡Error! '.center(len(err)+4,'-'))
        print('- '+err+' -')
        print('-'*(len(err)+4))

    """
    ******************************************
    *     Vista para codigos postales        *
    ******************************************
    """

    def menu_postal(self):
        print("======================================")
        print("=          Codigos Postales          =")
        print("======================================")
        print('1.- Agregar codigo postal')
        print('2.- Mostrar todos los codigos postales')
        print('3.- Mostrar informacion por codigo postal')
        print('4.- Mostrar informacion por ciudad')
        print('5.- Actualizar codigo postal')
        print('6.- Borrar codigo postal')
        print('7.- Regresar')
    
    def mostrar_cp(self, record):
        print(f'{record[0]:<6}|{record[1]:<45}|{record[2]:<45}|{record[3]:<45}')
        
    
    def mostrar_cabecera_cp(self, header):
        print(header.center(141, '*'))
        print('CP'.ljust(6)+'|'+'Colonia'.ljust(45)+'|'+'Ciudad'.ljust(45)+'|'+'Estado'.ljust(45))
        print('-'*141)
    
    def mostrar_separador_cp(self):
        print('-'*141)

    def mostrar_pie_cp(self):
        print('*'*141)

    """
    ******************************************
    *           Vista para Seccion           *
    ******************************************
    """

    def menu_seccion(self):
        print("======================================")
        print("=             Secciones              =")
        print("======================================")
        print('1.- Agregar nueva seccion')
        print('2.- Mostrar todas las secciones')
        print('3.- Mostrar seccion por nombre')
        print('4.- Actualizar seccion')
        print('5.- Borrar seccion')
        print('6.- Regresar')
    
    def mostrar_seccion(self, record):
        print('ID: ', record[0])
        print('Nombre: ', record[1])
        print('Descripcion: ', record[2])
    
    def mostrar_cabecera_seccion(self, header):
        print(header.center(58, '*'))
        print('-'*58)

    def mostrar_separador_seccion(self):
        print('-'*58)

    def mostrar_pie_seccion(self):
        print('*'*58)


    """
    ******************************************
    *           Vista para Usuarios           *
    ******************************************
    """
    def menu_usuarios(self):
        print("======================================")
        print("=             Usuarios               =")
        print("======================================")
        print('1.- Agregar nuevo usuario')
        print('2.- Mostrar todos los usuarios')
        print('3.- Mostrar usuario por nombre y apellido')
        print('4.- Mostrar usuario por email')
        print('5.- Actualizar usuario')
        print('6.- Borrar usuario')
        print('7.- Regresar')
    
    def mostrar_usuarios(self, record):
        print('ID: ', record[0])
        print('Nombre: ', record[1] + ' '+ record[2] + ' ' + record[3])
        print('Email: ', record[4])
        print('Telefono: ', record[5])
        print('Calle: ', record[6])
        print('Codigo Postal: ', record[7])
        print('Colonia: ', record[8])
        print('Ciudad: ', record[9])
    
    def mostrar_cabecera_usuarios(self, header):
        print(header.center(63, '*'))
        print('-'*63)

    def mostrar_separador_usuarios(self):
        print('-'*63)

    def mostrar_pie_usuarios(self):
        print('*'*63)

    
    """
    ******************************************
    *           Vista para Libros           *
    ******************************************
    """
    def menu_libros(self):
        print("======================================")
        print("=               Libros               =")
        print("======================================")
        print('1.- Agregar nuevo libro')
        print('2.- Mostrar todos los libros')
        print('3.- Mostrar libros por titulo')
        print('4.- Mostrar libros por autor')
        print('5.- Mostrar libros por seccion')
        print('6.- Actualizar libro')
        print('7.- Borrar libro')
        print('8.- regresar')
    
    def mostrar_libros(self, record):
        print('ID: ', record[0])
        print('Titulo: ', record[1])
        print('Editorial: ', record[2])
        print('Edicion: ', record[3])
        print('Autor: ', record[4])
        print('Seccion: ', record[5])
        print('Descripcion: ', record[6])

    def mostrar_libros_actualizar(self, record):
        print('ID: ', record[0])
        print('Titulo: ', record[1])
        print('Editorial: ', record[2])
        print('Edicion: ', record[3])
        print('Autor: ', record[4])
    
    def mostrar_cabecera_libros(self, header):
        print(header.center(63, '*'))
        print('-'*63)

    def mostrar_separador_libros(self):
        print('-'*63)

    def mostrar_pie_libros(self):
        print('*'*63)

    """
    ******************************************
    *           Vista para Prestamos         *
    ******************************************
    """
    def menu_prestamos(self):
        print("======================================")
        print("=              Prestamos             =")
        print("======================================")
        print('1.- Agregar nuevo prestamo')
        print('2.- Mostrar prestamos por email')
        print('3.- Mostrar prestamos entregados')
        print('4.- Mostrar prestamos por entregar')
        print('5.- Mostrar prestamos por fecha de prestamo')
        print('6.- Mostrar prestamos por fecha de entrega')
        print('7.- Actualizar prestamo')
        print('8.- Borrar prestamo')
        print('9.- regresar')
    
    def mostrar_prestamos(self, record):
        print('ID del Prestamo: ', record[0])
        print('Titulo: ', record[1])
        print('Nombre del usuario: ', record[2] + ' '+ record[3] + ' ' + record[4])
        print('Edicion: ', record[5])
        print('Prestado del: ', record[6]) 
        print(' al ', record[7])
        print('Entregado?: ', record[8])
    
    def mostrar_cabecera_prestamos(self, header):
        print(header.center(63, '*'))
        print('-'*155)

    def mostrar_separador_prestamos(self):
        print('-'*155)

    def mostrar_pie_prestamos(self):
        print('*'*155)

    """
    ******************************************
    * Vista para la relacion libro-secciones *
    ******************************************
    """

    def menu_secciones_libros(self):
            print("======================================")
            print("=      Secciones de los libros       =")
            print("======================================")
            print('1.- Agregar nueva relacion')
            print('2.- Mostrar las secciones a las que pertenece un libro')
            print('3.- Mostrar los libros de una seccion')
            print('4.- Actualizar relacion')
            print('5.- Borrar relacion')
            print('6.- regresar')
    
    def mostrar_secciones_libros(self, record):
        print(f'{record[0]:<45}|{record[1]:<255}')
    
    def mostrar_cabecera_secciones_libros(self, header):
        print(header.center(78, '*'))
        print('Titulo'.ljust(45)+' '+'Seccion'.ljust(45))
        print('-'*78)

    def mostrar_separador_secciones_libros(self):
        print('-'*78)

    def mostrar_pie_secciones_libros(self):
        print('*'*78)
