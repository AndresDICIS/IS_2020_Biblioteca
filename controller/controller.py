from model.model import Model
from view.view import View

class Controller:
    """
    ************************************************
    * Controlador de la base de datos de biblioteca*
    ************************************************
    """
    def __init__(self):
        self.model = Model()
        self.view = View()

    def start(self):
        self.view.start()
        self.menu_principal()
    
    """
    ************************************************
    *             Controles Generales              *
    ************************************************
    """
    def menu_principal(self):
        opcion = '0'
        while opcion != '7':
            self.view.menu_principal()
            self.view.opcion('7')
            opcion = input()
            if opcion == '1':
                self.menu_prestamos()
            elif opcion == '2':
                self.menu_usuarios()
            elif opcion == '3':
                self.menu_libros()
            elif opcion == '4':
                self.menu_postal()
            elif opcion == '5':
                self.menu_seccion()
            elif opcion == '6':
                self.menu_secciones_libros()
            elif opcion == '7':
                self.view.end()
            else: 
                self.view.opcion_invalida()
        return
    
    def actualizar_listas(self, fs, vs):
        campos = []
        valores = []
        for f, v in zip(fs,vs):
            if v != '':
                campos.append(f+' = %s')
                valores.append(v)
        return campos, valores

    """
    ************************************************
    *       Controles para Codigos postales        *
    ************************************************
    """
    def menu_postal(self):
        opcion = '0'
        while opcion != '7':
            self.view.menu_postal()
            self.view.opcion('7')
            opcion = input()
            if opcion == '1':
                self.insert_postal()
            elif opcion == '2':
                self.leer_todos_postal()
            elif opcion == '3':
                self.leer_postal()
            elif opcion == '4':
                self.leer_todos_postal_ciudad()
            elif opcion == '5':
                self.actualizar_postal()
            elif opcion == '6':
                self.borrar_postal()
            elif opcion == '7':
                return
            else: 
                self.view.opcion_invalida()
        return

    def pregunta_cp(self):
        self.view.preguntar('Colonia: ')
        colonia = input()
        self.view.preguntar('Ciudad: ')
        ciudad = input()
        self.view.preguntar('Estado: ')
        estado = input()
        return [colonia, ciudad, estado]
    
    def insert_postal(self):
        self.view.preguntar('Codigo Postal: ')
        i_cp = input()
        colonia, ciudad, estado = self.pregunta_cp()
        salida = self.model.insert_postal(i_cp, colonia, ciudad, estado)
        if salida == True:
            self.view.Ok(i_cp, 'agrego')
        else:
            if salida.errno == 1062:
                self.view.error('El codigo postal esta repetido.')
            else:
                self.view.error('No se pudo agregar el codigo, revise.')
        return
    
    def leer_postal(self):
        self.view.preguntar('CP: ')
        i_cp = input()
        codigo = self.model.leer_postal(i_cp)
        if type(codigo) == tuple:
            self.view.mostrar_cabecera_cp(' Datos del codigo '+i_cp+' ')
            self.view.mostrar_cp(codigo)
            self.view.mostrar_separador_cp()
            self.view.mostrar_pie_cp()
        else:
            if codigo == None:
                self.view.error('El codigo postal no existe')
            else:
                self.view.error('Problema al leer el codigo, revise')
        return

    def leer_todos_postal(self):
        cps = self.model.leer_todos_postal()
        if type(cps) == list:
            self.view.mostrar_cabecera_cp(' Todos los CPs ')
            for cp in cps:
                self.view.mostrar_cp(cp)
                self.view.mostrar_separador_cp()
            self.view.mostrar_pie_cp()
        else:
            self.view.error('Problema al leer el codigo, revise')
        return

    def leer_todos_postal_ciudad(self):
        self.view.preguntar('Ciudad: ')
        ciudad = input()
        cps = self.model.leer_todos_postal_ciudad(ciudad)
        if type(cps) == list:
            self.view.mostrar_cabecera_cp(' CPs para la ciudad de '+ciudad+' ')
            for cp in cps:
                self.view.mostrar_cp(cp)
                self.view.mostrar_separador_cp()
            self.view.mostrar_pie_cp()
        else:
            self.view.error('Problema al leer el codigo, revise')
        return

    def actualizar_postal(self):
        self.view.preguntar('Codigo Postal a modificar: ')
        i_cp = input()
        cp = self.model.leer_postal(i_cp)
        if type(cp) == tuple:
            self.view.mostrar_cabecera_cp(' Datos del codigo '+ i_cp+' ')
            self.view.mostrar_cp(cp)
            self.view.mostrar_separador_cp()
            self.view.mostrar_pie_cp()
        else:
            if  cp == None:
                self.view.error('El Codigo no existe')
            else:
                self.view.error('Problema al leer el codigo, revise')
            return
        self.view.mensaje('Ingresa los valores a modificar (Vacio para dejarlo igual): ')
        todos_valores = self.pregunta_cp()
        campos, valores = self.actualizar_listas(['colonia', 'ciudad', 'estado'], todos_valores)
        valores.append(i_cp)
        valores = tuple(valores)
        salida = self.model.actualizar_postal(campos, valores)
        if salida == True:
            self.view.Ok(i_cp, 'Actualizo')
        else:
            self.view.error('No se pudo actualizar el CP, Revise.')
        return 

    def borrar_postal(self):
        self.view.preguntar('CP a borrar: ')
        i_cp = input()
        count = self.model.borrar_postal(i_cp)
        if count != 0:
            self.view.Ok(i_cp, 'Borro')
        else:
            if count == 0:
                self.view.error('El CP no existe')
            else:
                self.view.error('Problema al leer el codigo, revise.')

    """
    ************************************************
    *           Controles para Seccion             *
    ************************************************
    """

    def menu_seccion(self):
        opcion = '0'
        while opcion != '6':
            self.view.menu_seccion()
            self.view.opcion('6')
            opcion = input()
            if opcion == '1':
                self.insert_seccion()
            elif opcion == '2':
                self.leer_todos_seccion()
            elif opcion == '3':
                self.leer_descripcion_porNombre()
            elif opcion == '4':
                self.actualizar_descripcion_seccion()
            elif opcion == '5':
                self.borrar_seccion()
            elif opcion == '6':
                return
            else: 
                self.view.opcion_invalida()
        return
    
    def pregunta_seccion(self):
        self.view.preguntar('Nombre de la seccion: ')
        nombre = input()
        self.view.preguntar('Descripcion de la seccion: ')
        descripcion = input()
        return [nombre, descripcion]
    
    def insert_seccion(self):
        nombre, descripcion = self.pregunta_seccion()
        salida = self.model.insert_seccion(nombre, descripcion)
        if salida == True:
            self.view.Ok(nombre, 'agrego')
        else:
            if salida.errno == 1062:
                self.view.error('El nombre de la seccion esta repetido.')
            else:
                self.view.error('No se pudo agregar la seccion, revise.')
        return

    def leer_todos_seccion(self):
        secciones = self.model.leer_todos_seccion()
        if type(secciones) == list:
            self.view.mostrar_cabecera_seccion(' Todos las secciones ')
            for seccion in secciones:
                self.view.mostrar_seccion(seccion)
                self.view.mostrar_separador_seccion()
            self.view.mostrar_pie_seccion()
        else:
            self.view.error('Problema al leer la seccion, revise')
        return

    def leer_descripcion_porNombre(self):
        self.view.preguntar('Nombre de la seccion: ')
        i_nombre = input()
        descripcion = self.model.leer_descripcion_porNombre(i_nombre)
        if type(descripcion) == tuple:
            self.view.mostrar_cabecera_seccion('Descripcion de '+i_nombre+' ')
            self.view.mostrar_seccion(descripcion)
            self.view.mostrar_separador_seccion()
            self.view.mostrar_pie_seccion()
        else:
            if descripcion == None:
                self.view.error('El nombre de la seccion no existe')
            else:
                self.view.error('Problema al leer el nombre, revise')
        return


    def actualizar_descripcion_seccion(self):
        self.view.preguntar('Nombre de la seccion: ')
        nombre = input()
        self.view.preguntar('Nueva descripcion: ')
        i_descripcion = input()
        salida = self.model.actualizar_descripcion_seccion(i_descripcion, nombre)
        if salida == True:
            self.view.Ok(nombre, 'actualizo')
        else:
            self.view.error('No se pudo actualizar la seccion, revise.')
        return
    
    def borrar_seccion(self):
        self.view.preguntar('Nombre de la seccion: ')
        nombre = input()
        salida = self.model.borrar_seccion(nombre)
        if salida == True:
            self.view.Ok(nombre, 'borro')
        else:
            self.view.error('No se pudo borrar la seccion, revise.')
        return


    """
    ************************************************
    *           Controles para Usuarios            *
    ************************************************
    """

    def menu_usuarios(self):
        opcion = '0'
        while opcion != '7':
            self.view.menu_usuarios()
            self.view.opcion('7')
            opcion = input()
            if opcion == '1':
                self.insert_usuario()
            elif opcion == '2':
                self.leer_todo_usuario()
            elif opcion == '3':
                self.leer_usuario_porNombreApellido()
            elif opcion == '4':
                self.leer_usuario_porEmail()
            elif opcion == '5':
                self.actualizar_usuario()
            elif opcion == '6':
                self.borrar_usuario()
            elif opcion == '7':
                return
            else: 
                self.view.opcion_invalida()
        return

    def pregunta_usuario(self):
        self.view.preguntar('Nombre: ')
        nombre = input()
        self.view.preguntar('Primer apellido: ')
        apellido_1 = input()
        self.view.preguntar('Segundo apellido: ')
        apellido_2 = input()
        self.view.preguntar('Email: ')
        email = input()
        self.view.preguntar('Telefono: ')
        telefono = input()
        self.view.preguntar('Calle: ')
        calle = input()
        self.view.preguntar('Codigo Postal: ')
        cp = input()
        return [nombre, apellido_1, apellido_2, email, telefono, calle, cp]
    
    def insert_usuario(self):
        nombre, apellido_1, apellido_2, email, telefono, calle, cp = self.pregunta_usuario()
        salida = self.model.insert_usuario(nombre, apellido_1, apellido_2, email, telefono, calle, cp)
        if salida == True:
            self.view.Ok(nombre, 'agrego')
        else:
            if salida.errno == 1062:
                self.view.error('El usuario esta repetido.')
            else:
                self.view.error('No se pudo agregar el usuario, revise.')
        return
    
    def leer_todo_usuario(self):
        usuarios = self.model.leer_todo_usuario()
        if type(usuarios) == list:
            self.view.mostrar_cabecera_usuarios('Todos los usuarios')
            for usuario in usuarios:
                self.view.mostrar_usuarios(usuario)
                self.view.mostrar_separador_usuarios()
            self.view.mostrar_pie_usuarios()
        else:
            self.view.error('Problema al leer los usuarios, revise')
        return

    def leer_usuario_porNombreApellido(self):
        self.view.preguntar('Nombre del usuario: ')
        nombre = input()
        self.view.preguntar('Primer apellido del usuario: ')
        apellido = input()
        usuarios  = self.model.leer_usuario_porNombreApellido(nombre, apellido)
        if type(usuarios) == list:
            self.view.mostrar_cabecera_usuarios('Todos los Usuarios')
            for usuario in usuarios:
                self.view.mostrar_usuarios(usuario)
                self.view.mostrar_separador_usuarios()
            self.view.mostrar_pie_usuarios()
        else:
            self.view.error('Problema al mostrar los libros, revise')
        return

    def leer_usuario_porEmail(self):
        self.view.preguntar('Email del usuario: ')
        email = input()
        usuario  = self.model.leer_usuario_porEmail(email)
        if type(usuario) == tuple:
            self.view.mostrar_cabecera_usuarios('Datos del email '+email+' ')
            self.view.mostrar_usuarios(usuario)
            self.view.mostrar_separador_usuarios()
            self.view.mostrar_pie_usuarios()
        else:
            if usuario == None:
                self.view.error('El email de usuario no existe')
            else:
                self.view.error('Problema al leer el email, revise')
        return

    def actualizar_usuario(self):
        self.view.preguntar('Email del usuario a modificar: ')
        email = input()
        usuario = self.model.leer_usuario_porEmail(email)
        if type(usuario) == tuple:
            self.view.mostrar_cabecera_usuarios('Datos del email '+email+' ')
            self.view.mostrar_usuarios(usuario)
            self.view.mostrar_separador_usuarios()
            self.view.mostrar_pie_usuarios()
        else:
            if usuario == None:
                self.view.error('El email de usuario no existe')
            else:
                self.view.error('Problema al leer el email, revise')
            return
        self.view.mensaje('Ingrese los valores a modificar (vacio para dejarlo igual):')
        todos_valores = self.pregunta_usuario()
        campos, valores = self.actualizar_listas(['nombre', 'apellido_1', 'apellido_2', 'email', 'telefono', 'calle', 'u_cp'], todos_valores)
        valores.append(email)
        valores = tuple(valores)
        salida = self.model.actualizar_usuario(campos, valores)
        if salida == True:
            self.view.Ok(email, 'actualizo')
        else:
            self.view.error('No se pudo actualizar el usuario, revise')
        return

    def borrar_usuario(self):
        self.view.preguntar('Email del cliente a borrar: ')
        email = input()
        count = self.model.borrar_usuario(email)
        if count != 0:
            self.view.Ok(email, 'borro')
        else:
            if count == 0:
                self.view.error('El email no existe')
            else:
                self.view.error('Problema al borrar el usuario, revise')
        return

    """
    ************************************************
    *            Controles para Libros             *
    ************************************************
    """
    def menu_libros(self):
        opcion = '0'
        while opcion != '7':
            self.view.menu_libros()
            self.view.opcion('7')
            opcion = input()
            if opcion == '1':
                self.insert_libros()
            elif opcion == '2':
                self.leer_libros()
            elif opcion == '3':
                self.leer_libros_titulo()
            elif opcion == '4':
                self.leer_libros_autor()
            elif opcion == '5':
                self.leer_libros_seccion()
            elif opcion == '6':
                self.actualizar_libro()
            elif opcion == '7':
                self.borrar_libro()
            elif opcion == '8':
                return
            else: 
                self.view.opcion_invalida()
        return

    def pregunta_libro(self):
        self.view.preguntar('Titulo: ')
        titulo = input()
        self.view.preguntar('Editorial: ')
        editorial = input()
        self.view.preguntar('Edicion: ')
        edicion = input()
        self.view.preguntar('Autor: ')
        autor = input()
        return [titulo, editorial, edicion, autor]

    def insert_libros(self):
        titulo, editorial, edicion, autor = self.pregunta_libro()
        salida = self.model.insert_libros(titulo, editorial, edicion, autor)
        if salida == True:
            self.view.Ok(titulo, 'agrego')
        else:
            self.view.error('No se pudo agregar el libro, revise.')
        return
    
    def leer_libros(self):
        libros = self.model.leer_libros()
        if type(libros) == list:
            self.view.mostrar_cabecera_libros('Todos los libros')
            for libro in libros:
                self.view.mostrar_libros(libro)
                self.view.mostrar_separador_libros()
            self.view.mostrar_pie_libros()
        else:
            self.view.error('Problema al mostrar los libros, revise')
        return
    
    def leer_libros_titulo(self):
        self.view.preguntar('Titulo del libro: ')
        titulo = input()
        libros = self.model.leer_libros_titulo(titulo)
        if type(libros) == list:
            self.view.mostrar_cabecera_libros('Todos los libros')
            for libro in libros:
                self.view.mostrar_libros(libro)
                self.view.mostrar_separador_libros()
            self.view.mostrar_pie_libros()
        else:
            self.view.error('Problema al mostrar los libros, revise')
        return
    
    def leer_libros_autor(self):
        self.view.preguntar('Autor de los libros: ')
        autor = input()
        libros = self.model.leer_libros_autor(autor)
        if type(libros) == list:
            self.view.mostrar_cabecera_libros('Todos los libros')
            for libro in libros:
                self.view.mostrar_libros(libro)
                self.view.mostrar_separador_libros()
            self.view.mostrar_pie_libros()
        else:
            self.view.error('Problema al mostrar los libros, revise')
        return

    def leer_libros_seccion(self):
        self.view.preguntar('Seccion de los libros: ')
        seccion = input()
        libros = self.model.leer_libros_seccion(seccion)
        if type(libros) == list:
            self.view.mostrar_cabecera_libros('Todos los libros')
            for libro in libros:
                self.view.mostrar_libros(libro)
                self.view.mostrar_separador_libros()
            self.view.mostrar_pie_libros()
        else:
            self.view.error('Problema al mostrar los libros, revise')
        return
    
    def actualizar_libro(self):
        self.view.preguntar('Id del libro a modificar: ')
        id_libro = input()
        libro = self.model.leer_libro_id(id_libro)
        if type(libro) == tuple:
            self.view.mostrar_cabecera_libros('Datos del libro '+id_libro+' ')
            self.view.mostrar_libros_actualizar(libro)
            self.view.mostrar_separador_libros()
            self.view.mostrar_pie_libros()
        else:
            if libro == None:
                self.view.error('El libro no existe')
            else:
                self.view.error('Problema con el libro, revise')
            return
        self.view.mensaje('Ingrese los valores a modificar (vacio para dejarlo igual): ')
        todos_valores = self.pregunta_libro()
        campos, valores = self.actualizar_listas(['titulo', 'editorial', 'edicion', 'autor'], todos_valores)
        valores.append(id_libro)
        valores = tuple(valores)
        salida = self.model.actualizar_libro(campos, valores)
        if salida == True:
            self.view.Ok('', 'actualizo')
        else:
            self.view.error('No se pudo actualizar el libro, revise')
        return
        
    def borrar_libro(self):
        self.view.preguntar('Id del libro a borrar: ')
        libro_id = input()
        count = self.model.borrar_libro(libro_id)
        if count != 0:
            self.view.Ok('', 'borro')
        else:
            if count == 0:
                self.view.error('El libro no existe')
            else:
                self.view.error('Problema al borrar el libro, revise')
        return
    
    """
    ************************************************
    *           Controles para Prestamos           *
    ************************************************
    """
    def menu_prestamos(self):
        opcion = '0'
        while opcion != '7':
            self.view.menu_prestamos()
            self.view.opcion('7')
            opcion = input()
            if opcion == '1':
                self.insert_prestamo()
            elif opcion == '2':
                self.leer_prestamo_email()
            elif opcion == '3':
                self.leer_prestamo_entregado('Si')
            elif opcion == '4':
                self.leer_prestamo_entregado('No')
            elif opcion == '5':
                self.leer_prestamo_fecha_prest()
            elif opcion == '6':
                self.leer_prestamo_fecha_entrega()
            elif opcion == '7':
                self.actualizar_prestamo()
            elif opcion == '8':
                self.borrar_prestamo()
            elif opcion == '9':
                return
            else: 
                self.view.opcion_invalida()
        return

    def pregunta_prestamo(self):
        self.view.preguntar('ID del usuario: ')
        id_usuario = input()
        self.view.preguntar('ID del libro: ')
        id_libro = input()
        self.view.preguntar('Fecha de prestamo formato(yyyy-mm-dd): ')
        fecha_prestamo = input()
        self.view.preguntar('Fecha de entrega formato(yyyy-mm-dd): ')
        fecha_entrega = input()
        self.view.preguntar('Entregado? (Si/No): ')
        entregado = input()
        return [id_usuario, id_libro, fecha_prestamo, fecha_entrega, entregado]

    def insert_prestamo(self):
        id_usuario, id_libro, fecha_prestamo, fecha_entrega, entregado = self.pregunta_prestamo()
        salida = self.model.insert_prestamo(id_usuario, id_libro, fecha_prestamo, fecha_entrega, entregado)
        if salida == True:
            self.view.Ok('', 'agrego')
        else:
            self.view.error('No se pudo agregar el prestamo, revise.')
        return



    def leer_prestamo_email(self):
        self.view.preguntar('Email del usuario:' )
        email = input()
        prestamos = self.model.leer_prestamo_email(email)
        if type(prestamos) == list:
            self.view.mostrar_cabecera_prestamos('Todos los prestamos')
            for prestamo in prestamos:
                self.view.mostrar_prestamos(prestamo)
                self.view.mostrar_separador_prestamos()
            self.view.mostrar_pie_prestamos()
        else:
            self.view.error('Problema al mostrar los prestamos, revise')
        return

    def leer_prestamo_entregado(self, entregado):
        prestamos = self.model.leer_prestamo_entregado(entregado)
        if type(prestamos) == list:
            self.view.mostrar_cabecera_prestamos('Todos los prestamos')
            for prestamo in prestamos:
                self.view.mostrar_prestamos(prestamo)
                self.view.mostrar_separador_prestamos()
            self.view.mostrar_pie_prestamos()
        else:
            self.view.error('Problema al mostrar los prestamos, revise')
        return

    def leer_prestamo_fecha_prest(self):
        self.view.preguntar('Fecha de los prestamos formato(yyyy-mm-dd): ')
        fecha_prestamo = input()
        prestamos = self.model.leer_prestamo_fecha_prest(fecha_prestamo)
        if type(prestamos) == list:
            self.view.mostrar_cabecera_prestamos('Todos los prestamos')
            for prestamo in prestamos:
                self.view.mostrar_prestamos(prestamo)
                self.view.mostrar_separador_prestamos()
            self.view.mostrar_pie_prestamos()
        else:
            self.view.error('Problema al mostrar los prestamos, revise')
        return

    def leer_prestamo_fecha_entrega(self):
        self.view.preguntar('Fecha de las entregas formato(yyyy-mm-dd): ')
        fecha_entrega = input()
        prestamos = self.model.leer_prestamo_fecha_entrega(fecha_entrega)
        if type(prestamos) == list:
            self.view.mostrar_cabecera_prestamos('Todos los prestamos')
            for prestamo in prestamos:
                self.view.mostrar_prestamos(prestamo)
                self.view.mostrar_separador_prestamos()
            self.view.mostrar_pie_prestamos()
        else:
            self.view.error('Problema al mostrar los prestamos, revise')
        return

    def actualizar_prestamo(self):
        self.view.preguntar('Id del prestamo a modificar: ')
        id_prestamo = input()
        prestamo = self.model.leer_prestamo_id(id_prestamo)
        if type(prestamo) == tuple:
            self.view.mostrar_cabecera_prestamos('Datos del prestamo '+id_prestamo+' ')
            self.view.mostrar_prestamos(prestamo)
            self.view.mostrar_separador_prestamos()
            self.view.mostrar_pie_prestamos()
        else:
            if prestamo == None:
                self.view.error('El prestamo no existe')
            else:
                self.view.error('Problema con el prestamo, revise')
            return
        self.view.mensaje('Ingrese los valores a modificar (vacio para dejarlo igual): ')
        todos_valores = self.pregunta_prestamo()
        campos, valores = self.actualizar_listas(['p_usr_id', 'p_libro_id', 'fecha_prest', 'fecha_entrega', 'entregado'], todos_valores)
        valores.append(id_prestamo)
        valores = tuple(valores)
        salida = self.model.actualizar_prestamo(campos, valores)
        if salida == True:
            self.view.Ok('', 'actualizo')
        else:
            self.view.error('No se pudo actualizar el prestamo, revise')
        return
        
    def borrar_prestamo(self):
        self.view.preguntar('Id del prestamo a borrar: ')
        id_prestamo = input()
        count = self.model.borrar_prestamo(id_prestamo)
        if count != 0:
            self.view.Ok('', 'borro')
        else:
            if count == 0:
                self.view.error('El prestamo no existe')
            else:
                self.view.error('Problema al borrar el prestamo, revise')
        return


    """
    ************************************************
    *       Controles para libros-Secciones        *
    ************************************************
    """
    def menu_secciones_libros(self):
        opcion = '0'
        while opcion != '7':
            self.view.menu_secciones_libros()
            self.view.opcion('7')
            opcion = input()
            if opcion == '1':
                self.insertar_LibroSeccion()
            elif opcion == '2':
                self.leer_LibroSeccion()
            elif opcion == '3':
                self.leer_SeccionLibro()
            elif opcion == '4':
                self.actualizar_LibroSeccion()
            elif opcion == '5':
                self.borrar_LibroSeccion()
            elif opcion == '6':
                return
            else: 
                self.view.opcion_invalida()
        return

    def pregunta_libroseccion(self):
        self.view.preguntar('Id de la seccion: ')
        id_seccion = input()
        self.view.preguntar('Id del libro: ')
        id_libro = input()
        return [id_seccion, id_libro]
    
    def insertar_LibroSeccion(self):
        id_seccion, id_libro = self.pregunta_libroseccion()
        salida = self.model.insertar_LibroSeccion(id_seccion, id_libro)
        if salida == True:
            self.view.Ok('', 'agrego')
        else:
            self.view.error('No se pudo agregar la relacion, revise.')
        return


    def leer_LibroSeccion(self):
        self.view.preguntar('Titulo del libro: ')
        titulo = input()
        secciones = self.model.leer_LibroSeccion(titulo)
        if type(secciones) == list:
            self.view.mostrar_cabecera_secciones_libros('Todas las secciones')
            for seccion in secciones:
                self.view.mostrar_secciones_libros(seccion)
                self.view.mostrar_separador_secciones_libros()
            self.view.mostrar_pie_secciones_libros()
        else:
            self.view.error('Problema al mostrar las secciones, revise')
        return


    def leer_SeccionLibro(self):
        self.view.preguntar('Seccion: ')
        seccion = input()
        titulos = self.model.leer_SeccionLibro(seccion)
        if type(titulos) == list:
            self.view.mostrar_cabecera_secciones_libros('Todas las secciones')
            for titulo in titulos:
                self.view.mostrar_secciones_libros(titulo)
                self.view.mostrar_separador_secciones_libros()
            self.view.mostrar_pie_secciones_libros()
        else:
            self.view.error('Problema al mostrar las secciones, revise')
        return


    def actualizar_LibroSeccion(self):
        self.view.preguntar('Id de la seccion: ')
        id_seccion = input()
        self.view.preguntar('Id del libro relacionado: ')
        id_libro = input()
        relacion = self.model.leer_una_relacion(id_seccion, id_libro)
        if type(relacion) == tuple:
            self.view.mostrar_cabecera_secciones_libros('Datos de la relacion '+id_seccion+' ')
            self.view.mostrar_secciones_libros(relacion)
            self.view.mostrar_separador_secciones_libros()
            self.view.mostrar_pie_secciones_libros()
        else:
            if relacion == None:
                self.view.error('la relacion no existe')
            else:
                self.view.error('Problema con la relacion, revise')
            return
        self.view.mensaje('Ingrese los valores a modificar (vacio para dejarlo igual): ')
        todos_valores = self.pregunta_libroseccion()
        campos, valores = self.actualizar_listas(['ls_seccion_id', 'ls_libro_id'], todos_valores)
        valores.append(id_seccion)
        valores.append(id_libro)
        valores = tuple(valores)
        salida = self.model.actualizar_LibroSeccion(campos, valores)
        if salida == True:
            self.view.Ok('', 'actualizo')
        else:
            self.view.error('No se pudo actualizar la relacion, revise')
        return
        
    def borrar_LibroSeccion(self):
        self.view.preguntar('Id de la seccion: ')
        id_seccion = input()
        self.view.preguntar('Id del libro relacionado: ')
        id_libro = input()
        count = self.model.borrar_LibroSeccion(id_seccion, id_libro)
        if count != 0:
            self.view.Ok('', 'borro')
        else:
            if count == 0:
                self.view.error('La relacion no existe')
            else:
                self.view.error('Problema al borrar la relacion, revise')
        return




