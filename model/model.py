from mysql import connector

class Model:
    """
    ***********************************************
    * Modelo para la base de datos de la libreria *
    ***********************************************
    """
    def __init__(self, config_db_file = 'config.txt'):
        self.config_db_file = config_db_file
        self.config_db = self.read_config_db()
        self.connect_to_db()
    
    def read_config_db(self):
        d = {}
        with open(self.config_db_file,) as f_r:
            for line in f_r:
                (key, val) = line.strip().split(':')
                d[key] = val
        return d

    def connect_to_db(self):
        self.cnx = connector.connect(**self.config_db)
        self.cursor = self.cnx.cursor()

    def close_db(self):
        self.cnx.close()

    """
    **********************
    *  Codigos Postales  *
    **********************
    """

    def insert_postal(self, cp, colonia, ciudad, estado):
        try:
            consulta_sql = 'INSERT INTO codigo_postal (`cp`, `colonia`, `ciudad`, `estado`) VALUES (%s, %s, %s, %s)'
            valores = (cp, colonia, ciudad, estado)
            self.cursor.execute(consulta_sql, valores)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def leer_postal(self, cp):
        try:
            consulta_sql = 'SELECT * FROM codigo_postal WHERE cp = %s'
            valores = (cp,)
            self.cursor.execute(consulta_sql, valores)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def leer_todos_postal(self):
        try:
            consulta_sql = 'SELECT * FROM codigo_postal'
            self.cursor.execute(consulta_sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def leer_todos_postal_ciudad(self, ciudad):
        try:
            consulta_sql = 'SELECT * FROM codigo_postal WHERE ciudad = %s'
            valores = (ciudad,)
            self.cursor.execute(consulta_sql, valores)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def actualizar_postal(self, campos, valores):
        try:
            consulta_sql = 'UPDATE codigo_postal SET '+','.join(campos)+' WHERE cp = %s'
            self.cursor.execute(consulta_sql, valores)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err 

    def borrar_postal(self, cp):
        try:
            consulta_sql = 'DELETE FROM codigo_postal WHERE cp = %s'
            valores = (cp,)
            self.cursor.execute(consulta_sql, valores)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    """
    **********************
    *     seccion        *
    **********************
    """

    def insert_seccion(self, nombre, descripcion):
        try:
            consulta_sql = 'INSERT INTO seccion (`nombre_seccion`,`descripcion`) VALUES(%s, %s)'
            valores = (nombre, descripcion)
            self.cursor.execute(consulta_sql, valores)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def leer_todos_seccion(self):
        try:
            consulta_sql = 'SELECT * FROM seccion'
            self.cursor.execute(consulta_sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def leer_seccion_porId(self, seccion_id):
        try:
            consulta_sql = 'SELECT * FROM seccion WHERE seccion_id = %s'
            valores = (seccion_id,)
            self.cursor.execute(consulta_sql, valores)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
    
    def leer_descripcion_porNombre(self, nombre):
        try: 
            consulta_sql = 'SELECT * FROM seccion WHERE nombre_seccion = %s'
            valores = (nombre,)
            self.cursor.execute(consulta_sql, valores)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def actualizar_descripcion_seccion(self,nueva_descripcion, nombre):
        try:
            consulta_sql = 'UPDATE seccion SET descripcion = %s WHERE nombre_seccion = %s'
            valores = (nueva_descripcion, nombre)
            self.cursor.execute(consulta_sql, valores)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    """
    def actualizar_nombre_seccion(self, nuevo_nombre, seccion_id):
        try:
            consulta_sql = 'UPDATE seccion SET nombre = %s WHERE seccion_id = %s'
            valores = (nuevo_nombre, seccion_id)
            self.cursor.execute(consulta_sql, valores)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    """
   
    def borrar_seccion(self, nombre):
        try:
            consulta_sql = 'DELETE FROM seccion WHERE nombre_seccion = %s'
            valores = (nombre,)
            self.cursor.execute(consulta_sql, valores)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err
    """
    **********************
    *     Usuarios       *
    **********************
    """

    def insert_usuario(self, nombre, apellido1, apellido2, email, telefono, calle, cp):
        try:
            consulta_sql = 'INSERT INTO usuarios (`nombre`, `apellido_1`, `apellido_2`, `email`, `telefono`, `calle`, `u_cp`) VALUES(%s, %s, %s, %s, %s, %s, %s)'
            valores = (nombre, apellido1, apellido2, email, telefono, calle, cp)
            self.cursor.execute(consulta_sql, valores)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def leer_todo_usuario(self):
        try: 
            consulta_sql = 'SELECT U.usr_id, U.nombre, U.apellido_1, U.apellido_2, U.email, U.telefono, U.calle, U.u_cp, CP.colonia, CP.ciudad \
            FROM usuarios U, codigo_postal CP WHERE U.u_cp = CP.cp'
            self.cursor.execute(consulta_sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err 

    def leer_usuario_porNombreApellido(self, nombre, apellido1):
        try: 
            consulta_sql = 'SELECT U.usr_id, U.nombre, U.apellido_1, U.apellido_2, U.email, U.telefono, U.calle, U.u_cp, CP.colonia, CP.ciudad \
            FROM usuarios U, codigo_postal CP \
            WHERE U.nombre = %s AND U.apellido_1 = %s AND CP.cp = U.u_cp'
            valores = (nombre, apellido1)
            self.cursor.execute(consulta_sql, valores)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err 
    
    def leer_usuario_porEmail(self, email):
        try: 
            consulta_sql = 'SELECT U.usr_id, U.nombre, U.apellido_1, U.apellido_2, U.email, U.telefono, U.calle, U.u_cp, CP.colonia, CP.ciudad \
            FROM usuarios U, codigo_postal CP \
            WHERE U.email = %s AND CP.cp = U.u_cp'
            valores = (email, )
            self.cursor.execute(consulta_sql, valores)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err 
    
    def actualizar_usuario(self, campos, valores):
        try:
            consulta_sql = 'UPDATE usuarios SET '+','.join(campos)+' WHERE email = %s'
            self.cursor.execute(consulta_sql, valores)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err 
    
    def borrar_usuario(self, email):
        try:
            consulta_sql = 'DELETE FROM usuarios WHERE email = %s'
            valores = (email, )
            self.cursor.execute(consulta_sql, valores)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    **********************
    *       Libros       *
    **********************
    """
    def insert_libros(self, titulo, editorial, edicion, autor):
        try:
            consulta_sql = 'INSERT INTO libros (`titulo`, `editorial`, `edicion`, `autor`) VALUES(%s, %s, %s, %s)'
            valores = (titulo, editorial, edicion, autor)
            self.cursor.execute(consulta_sql, valores)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def leer_libros(self):
        try:
            consulta_sql = 'SELECT L.libro_id, L.titulo, L.editorial, L.edicion, L.autor, S.nombre_seccion, S.descripcion \
            FROM libros L, seccion S, libro_seccion LS \
            WHERE LS.ls_libro_id = L.libro_id AND S.seccion_id = LS.ls_seccion_id'
            self.cursor.execute(consulta_sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def leer_libro_id(self, libro_id):
        try:
            consulta_sql = 'SELECT libro_id, titulo, editorial, edicion, autor FROM libros WHERE libro_id = %s'
            valores = (libro_id, )
            self.cursor.execute(consulta_sql, valores)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            self.cnx.rollback()
            return err



    def leer_libros_titulo(self, titulo):
        try:
            consulta_sql = 'SELECT L.libro_id, L.titulo, L.editorial, L.edicion, L.autor, S.nombre_seccion, S.descripcion \
            FROM libros L, seccion S, libro_seccion LS \
            WHERE L.titulo = %s AND LS.ls_libro_id = L.libro_id AND S.seccion_id = LS.ls_seccion_id'
            valores = (titulo, )
            self.cursor.execute(consulta_sql, valores)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def leer_libros_autor(self, autor):
        try:
            consulta_sql = 'SELECT L.libro_id, L.titulo, L.editorial, L.edicion, L.autor, S.nombre_seccion, S.descripcion \
            FROM libros L, seccion S, libro_seccion LS \
            WHERE L.autor = %s AND LS.ls_libro_id = L.libro_id AND S.seccion_id = LS.ls_seccion_id'
            valores = (autor, )
            self.cursor.execute(consulta_sql, valores)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def leer_libros_seccion(self, seccion):
        try:
            consulta_sql = 'SELECT L.libro_id, L.titulo, L.editorial, L.edicion, L.autor, S.nombre_seccion, S.descripcion \
            FROM libros L, seccion S, libro_seccion LS \
            WHERE S.nombre_seccion = %s AND L.libro_id = LS.ls_libro_id  AND LS.ls_seccion_id = S.seccion_id'
            valores = (seccion, )
            self.cursor.execute(consulta_sql, valores)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def actualizar_libro(self, campos, valores):
        try:
            consulta_sql = 'UPDATE libros SET '+','.join(campos)+' WHERE libro_id = %s'
            self.cursor.execute(consulta_sql, valores)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err 

    def borrar_libro(self, libro_id):
        try:
            consulta_sql = 'DELETE FROM libros WHERE libro_id = %s'
            valores = (libro_id,)
            self.cursor.execute(consulta_sql, valores)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    """
    **********************
    *      Prestamos     *
    **********************
    """
    def insert_prestamo(self, p_usr_id, p_libro_id, fecha_prest, fecha_entrega, entregado):
        try:
            consulta_sql = 'INSERT INTO prestamos (`p_usr_id`, `p_libro_id`, `fecha_prest`, `fecha_entrega`, `entregado`) VALUES(%s, %s, %s, %s, %s)'
            valores = (p_usr_id, p_libro_id, fecha_prest, fecha_entrega, entregado)
            self.cursor.execute(consulta_sql, valores)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def leer_prestamo_id(self, prest_id):
        try:
            consulta_sql = 'SELECT P.prest_id, L.titulo, U.nombre, U.apellido_1, U.apellido_2, L.edicion, P.fecha_prest, \
            P.fecha_entrega, P.entregado FROM prestamos P, libros L, usuarios U WHERE  P.prest_id = %s AND P.p_usr_id = U.usr_id \
            AND L.libro_id = P.p_libro_id'
            valores = (prest_id, )
            self.cursor.execute(consulta_sql, valores)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            self.cnx.rollback
            return err

    def leer_prestamo_email(self, email):
        try:
            consulta_sql = 'SELECT P.prest_id, L.titulo, U.nombre, U.apellido_1, U.apellido_2, L.edicion, P.fecha_prest, \
            P.fecha_entrega, P.entregado FROM prestamos P, libros L, usuarios U WHERE U.email = %s AND P.p_usr_id = U.usr_id \
            AND L.libro_id = P.p_libro_id'
            valores = (email, )
            self.cursor.execute(consulta_sql, valores)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            self.cnx.rollback
            return err

    def leer_prestamo_entregado(self, entregado):
        try:
            consulta_sql = 'SELECT P.prest_id, L.titulo, U.nombre, U.apellido_1, U.apellido_2, L.edicion, P.fecha_prest, \
            P.fecha_entrega, P.entregado FROM prestamos P, libros L, usuarios U WHERE P.entregado = %s AND U.usr_id = P.p_usr_id  \
            AND L.libro_id = P.p_libro_id'
            valores = (entregado, )
            self.cursor.execute(consulta_sql, valores)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
                self.cnx.rollback
                return err

    def leer_prestamo_fecha_entrega(self, fecha_entrega):
        try:
            consulta_sql = 'SELECT P.prest_id, L.titulo, U.nombre, U.apellido_1, U.apellido_2, L.edicion, P.fecha_prest, \
            P.fecha_entrega, P.entregado FROM prestamos P, libros L, usuarios U WHERE P.fecha_entrega = %s AND U.usr_id = P.p_usr_id  \
            AND L.libro_id = P.p_libro_id'
            valores = (fecha_entrega, )
            self.cursor.execute(consulta_sql, valores)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
                self.cnx.rollback
                return err

    def leer_prestamo_fecha_prest(self, fecha_prest):
        try:
            consulta_sql = 'SELECT P.prest_id, L.titulo, U.nombre, U.apellido_1, U.apellido_2, L.edicion, P.fecha_prest, \
            P.fecha_entrega, P.entregado FROM prestamos P, libros L, usuarios U WHERE P.fecha_prest = %s AND U.usr_id = P.p_usr_id  \
            AND L.libro_id = P.p_libro_id'
            valores = (fecha_prest, )
            self.cursor.execute(consulta_sql, valores)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
                self.cnx.rollback
                return err

    def actualizar_prestamo(self, campos, valores):
        try:
            consulta_sql = 'UPDATE prestamos SET '+','.join(campos)+' WHERE prest_id = %s'
            self.cursor.execute(consulta_sql, valores)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err 
    
    def borrar_prestamo(self, prest_id):
        try:
            consulta_sql = 'DELETE FROM prestamos WHERE prest_id = %s'
            valores = (prest_id,)
            self.cursor.execute(consulta_sql, valores)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    **********************
    *  Libro-Secciones   *
    **********************
    """

    def insertar_LibroSeccion(self, ls_seccion_id, ls_libro_id):
        try:
            consulta_sql = 'INSERT INTO libro_seccion (`ls_seccion_id`, `ls_libro_id`) VALUES (%s, %s)'
            valores = (ls_seccion_id, ls_libro_id)
            self.cursor.execute(consulta_sql, valores)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def leer_LibroSeccion(self, titulo):
        try:
            consulta_sql = 'SELECT L.titulo, S.nombre_seccion, S.descripcion FROM seccion S, libros L, libro_seccion LS \
            WHERE L.titulo = %s AND L.libro_id = LS.ls_libro_id AND S.seccion_id = LS.ls_seccion_id' 
            valores = (titulo, )
            self.cursor.execute(consulta_sql, valores)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def leer_SeccionLibro(self, nombre_seccion):
        try:
            consulta_sql = 'SELECT L.titulo, S.nombre_seccion, S.descripcion FROM seccion S, libros L, libro_seccion LS \
            WHERE S.nombre_seccion = %s AND L.libro_id = LS.ls_libro_id AND S.seccion_id = LS.ls_seccion_id' 
            valores = (nombre_seccion, )
            self.cursor.execute(consulta_sql, valores)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def leer_una_relacion(self, id_seccion, id_libro):
        try:
            consulta_sql = 'SELECT ls_libro_id, ls_seccion_id FROM libro_seccion \
            WHERE ls_seccion_id = %s AND ls_libro_id = %s' 
            valores = (id_seccion, id_libro)
            self.cursor.execute(consulta_sql, valores)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def actualizar_LibroSeccion(self, campos, valores):
        try:
            consulta_sql = 'UPDATE libro_seccion SET '+','.join(campos)+' WHERE ls_seccion_id = %s AND ls_libro_id = %s'
            self.cursor.execute(consulta_sql, valores)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err 
    
    def borrar_LibroSeccion(self, ls_seccion_id, ls_libro_id):
        try:
            consulta_sql = 'DELETE FROM libro_seccion WHERE ls_seccion_id = %s AND ls_libro_id = %s'
            valores = (ls_seccion_id, ls_libro_id)
            self.cursor.execute(consulta_sql, valores)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    