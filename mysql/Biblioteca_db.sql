DROP DATABASE library;
CREATE DATABASE IF NOT EXISTS library;
USE library;

CREATE TABLE IF NOT EXISTS libros(
	libro_id INT NOT NULL AUTO_INCREMENT,
    titulo VARCHAR(45) NOT NULL,
    editorial VARCHAR(45) NOT NULL,
    edicion INT NOT NULL NOT NULL, 
    autor VARCHAR (80) NOT NULL,
    PRIMARY KEY (libro_id)
)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS seccion(
	seccion_id INT NOT NULL AUTO_INCREMENT,
    nombre_seccion VARCHAR(45) UNIQUE NOT NULL,
    descripcion VARCHAR(255) NOT NULL,
    PRIMARY KEY (seccion_id)
)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS codigo_postal(
    cp VARCHAR(6) NOT NULL,
    colonia VARCHAR(45) NOT NULL,
    ciudad VARCHAR(45) NOT NULL,
    estado VARCHAR(45) NOT NULL,
    PRIMARY KEY(cp)
)ENGINE=INNODB;


CREATE TABLE IF NOT EXISTS usuarios(
	usr_id INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(45) NOT NULL,
	apellido_1 VARCHAR(45) NOT NULL,
    apellido_2 VARCHAR(45) NOT NULL,
    email VARCHAR(45) UNIQUE NOT NULL,
    telefono VARCHAR(10) NOT NULL,
    calle VARCHAR(45) NOT NULL,
    u_cp VARCHAR(6) NOT NULL,
	PRIMARY KEY (usr_id),
    CONSTRAINT fk_u_cp
    FOREIGN KEY (u_cp)
    REFERENCES codigo_postal(cp)
    ON DELETE CASCADE
    ON UPDATE CASCADE
)ENGINE=INNODB;

CREATE TABLE IF NOT EXISTS prestamos(
	prest_id INT NOT NULL AUTO_INCREMENT,
    p_usr_id INT NOT NULL,
    p_libro_id INT NOT NULL,
    fecha_prest DATE NOT NULL,
    fecha_entrega DATE NOT NULL,
    entregado ENUM('Si', 'No') NOT NULL,
    PRIMARY KEY(prest_id),
    CONSTRAINT fk_p_usr_id
    FOREIGN KEY (p_usr_id)
    REFERENCES usuarios(usr_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
    CONSTRAINT fk_p_libro_id
    FOREIGN KEY (p_libro_id)
    REFERENCES libros(libro_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
)ENGINE=INNODB;

CREATE TABLE IF NOT EXISTS libro_seccion(
	ls_seccion_id INT NOT NULL,
    ls_libro_id INT NOT NULL,
    PRIMARY KEY(ls_seccion_id, ls_libro_id),
    CONSTRAINT fk_ls_seccion_id
    FOREIGN KEY (ls_seccion_id)
    REFERENCES seccion(seccion_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
    CONSTRAINT fk_ls_libro_id
    FOREIGN KEY (ls_libro_id)
    REFERENCES libros(libro_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
)ENGINE=INNODB;
