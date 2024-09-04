#Este archivo opciones.py, se crea con la finalidad de escribir ciertas funciones que
#no necesitan ser heredadas por los modelos, pero si para ser utilizadas como opciones en el
#Estos modulos de opciones seran llamados en el archivo modelos.py

opciones_estado = (
    ('Operativo', 'Operativo'),
    ('Inactivo', 'Inactivo')
)

# ________________________________________________________________________________________________________________________________________________________

opciones_activos = (
    ('All In One', 'All In One'),
    ('Notebook', 'Notebook'),
    ('Notebook Avanzado', 'Notebook Avanzado'),
    ('Pc de Escritorio', 'Pc de Escritorio'),
    ('Mini Pc', 'Mini Pc'),
    ('Proyector', 'Proyector')
)

# ________________________________________________________________________________________________________________________________________________________

opciones_marca_all_in_one = (
    ('HP', 'HP'),
    ('Lenovo', 'Lenovo'),
    ('Apple', 'Apple')
)

# ________________________________________________________________________________________________________________________________________________________

opciones_marca_notebook = (
    ('Dell', 'Dell'),
    ('HP', 'HP'),
    ('Lenovo', 'Lenovo'),
)


# ________________________________________________________________________________________________________________________________________________________
opciones_marca_mini_pc = (
    ('Intel', 'Intel'),
)

# ________________________________________________________________________________________________________________________________________________________

opciones_marca_proyector = (
    ('Epson', 'Epson'),
)

# ________________________________________________________________________________________________________________________________________________________
opciones_marca_azotea =(
    ('A0LFCL', 'A0LFCL'),
    ('Apple', 'Apple'),
    ('HP', 'HP'),
    ('Lenovo', 'Lenovo'),
    ('Dell', 'Dell'),
)


# ________________________________________________________________________________________________________________________________________________________
opciones_marca_bodega_adr = (
    ('Apple', 'Apple'),
    ('Epson', 'Epson'),
    ('HP', 'HP'),
    ('Lenovo', 'Lenovo'),
    ('Panasonic', 'Panasonic'),
    ('Viewsonic', 'Viewsonic'),
)


# ________________________________________________________________________________________________________________________________________________________
opciones_sala_All_In_One = (
    ('LC-01', 'LC-01'),
    ('LC-02', 'LC-02'),
    ('LC-04', 'LC-04'),
    ('LC-05', 'LC-05'),
    ('LC-06', 'LC-06'),
    ('LC-07', 'LC-07'),
    ('LC-08', 'LC-08'),
    ('LC-09', 'LC-09'),
    ('LC-10', 'LC-10'),
    ('205 B', '205 B'),
    ('301 C', '301 C'),
    ('302 C', '302 C'),
    ('303 C', '303 C'),
    ('311 C', '311 C'),
    ('403 C', '403 C'),
    ('Biblioteca', 'Biblioteca'),
    ('Sala de profesores', 'Sala de profesores'),
    ('Co Work', 'Co Work'),
    ('Fabrica 4310', 'Fabrica 4310'),
)
# ________________________________________________________________________________________________________________________________________________________


opciones_ubicacion_all_in_one_admin = (
    ('Biblioteca', 'Biblioteca'),
    ('Bodega', 'Bodega'),
    ('Capacitación', 'Capacitación'),
    ('CoWork', 'Cowork'),
    ('DACOM', 'DACOM'),
    ('DAE', 'DAE'),
    ('DAF', 'DAF'),
    ('DAC', 'DAC'),
    ('Dirección', 'Dirección'),
    ('Dirección Gastronomía', 'Dirección Gastronomía'),
    ('Direción Mecánica', 'Dirección Mecánica'),
    ('Logística', 'Logística'),
    ('Pañol Construcción (sala 107B)', 'Pañol Construcción (sala 107B)'),
    ('Pañol Electrónica', 'Pañol Electrónica'),
    ('Pañol Gastronomía', 'Pañol Gastronomía'),
    ('Pañol Mecánica', 'Pañol Mecánica'),
    ('Sala CCTV Guardias Dunas', 'Sala CCTV Guardias Dunas'),
    ('Sala Profesores', 'Sala Profesores'),
    ('SubDirector Académico', 'SubDirector Académico'),
    ('Tutoría', 'Tutoría')
)

# ________________________________________________________________________________________________________________________________________________________

opciones_ubicacion_notebook = (
    ('ADR', 'ADR'),
    ('Biblioteca', 'Biblioteca'),
    ('Bodega', 'Bodega'),
    ('Bodega Principal', 'Bodega Principal'),
    ('Capacitación', 'Capacitación'),
    ('Coordinación Docente', 'Coordinación Docente'),
    ('DAC', 'DAC'),
    ('DACOM', 'DACOM'),
    ('DAE', 'DAE '),
    ('DAF', 'DAF'),
    ('Domicilio', 'Domicilio'),
    ('Fabríca 4310', 'Fabríca 4310'),
    ('Hall Guardias', 'Hall Guardias'),
    ('Oficína Gastronomía', 'Oficína Gastronomía'),
    ('Oficína Mecánica', 'Oficína Mecánica'),
    ('Oficína Minería', 'Oficína Minería'),
    ('Oficína RRHH', 'Oficína RRHH'),
    ('Tutoría', 'Tutoría')
)

# ________________________________________________________________________________________________________________________________________________________

opciones_ubicacion_mini_pc = (
    ('DACOM', 'DACOM'),
    ('DAE', 'DAE'),
    ('DAF', 'DAF'),
    ('Edf A Piso 1 Ascensor','Edf A Piso 1 Ascensor'),
    ('Edf A Piso 1 Biblioteca', 'Edf A Piso 1 Biblioteca'),
    ('Edf A Piso 1 Coordinación', 'Edf A Piso 1 Coordinación'),
    ('Edf A Piso 2 Ascensor', 'Edf A Piso 2 Ascensor'),
    ('Edf A Piso 2 Escalera', 'Edf A Piso 2 Escalera'),
    ('Edf A Piso 2 Tutoría', 'Edf A Piso 2 Tutoría'),
    ('Edf A Piso 3 Ascensor', 'Edf A Piso 3 Ascensor'),
    ('Edf A Piso 3 Nodo (derecho)', 'Edf A Piso 3 Nodo (derecho)'),
    ('Edf B Piso 1 Mecánica', 'Edf B Piso 1 Mecánica'),
    ('Edf C Piso 3 Sala clase', 'Edf C Piso 3 Sala clase'),
    ('Edf C Piso 4 Casino (fuera)', 'Edf C Piso 4 Casino (fuera)'),
    ('Edf C Piso 5 Sala clase', 'Edf C Piso 5 Sala clase'),
    ('Edf C Piso 6 Sala clase', 'Edf C Piso 6 Sala clase'),
    ('Totem (fuera de oficina ADR)', 'Totem (fuera de oficina ADR)')
)

# ________________________________________________________________________________________________________________________________________________________

opciones_ubicacion_proyector = (
  ('LC-01', 'LC-01'),
  ('LC-02', 'LC-02'),
  ('LC-03', 'LC-03'),
  ('LC-04', 'LC-04'),
  ('LC-05', 'LC-05'),
  ('LC-06', 'LC-06'),
  ('LC-07', 'LC-07'),
  ('LC-08', 'LC-08'),
  ('LC-09', 'LC-09'),
  ('LC-10', 'LC-10'),

  ('201 A', '201 A'),
  ('202 A', '202 A'),
  ('203 A', '203 A'),
  ('204 A', '204 A'),
  ('205 A', '205 A'),
  ('206 A', '206 A'),
  ('207 A', '207 A'),
  ('208 A', '208 A'),
  ('301 A', '301 A'),
  ('302 A', '302 A'),
  ('303 A', '303 A'),
  ('304 A', '304 A'),
  ('305 A', '305 A'),
  ('306 A', '306 A'),

  ('103 B', '103 B'),
  ('105 B', '105 B'),
  ('112 B', '112 B'),
  ('203 B', '203 B'),
  ('205 B', '205 B'),
  ('206 B', '206 B'),

  ('301 C', '301 C'),
  ('302 C', '302 C'),
  ('303 C', '303 C'),
  ('304 C', '304 C'),
  ('305 C', '305 C'),
  ('306 C', '306 C'),
  ('307 C', '307 C'),
  ('308 C', '308 C'),
  ('309 C', '309 C'),
  ('310 C', '310 C'),
  ('311 C', '311 C'),
  ('312 C', '312 C'),
  ('313 C', '313 C'),
  ('314 C', '314 C'),
  ('315 C', '315 C'),
  ('316 C', '316 C'),
  ('317 C', '317 C'),
  ('318 C', '318 C'),
  ('319 C', '319 C'),
  ('320 C', '320 C'),
  ('401 C', '401 C'),
  ('403 C', '403 C'),
  ('501 C', '501 C'),
  ('502 C', '502 C'),
  ('503 C', '503 C'),
  ('504 C', '504 C'),
  ('505 C', '505 C'),
  ('506 C', '506 C'),
  ('508 C', '508 C'),
  ('509 C', '509 C'),
  ('510 C', '510 C'),
  ('511 C', '511 C'),
  ('512 C', '512 C'),
  ('513 C', '513 C'),
  ('514 C', '514 C'),
  ('516 C', '516 C'),
  ('517 C', '517 C'),

  ('601 C', '601 C'),
  ('602 C', '602 C'),
  ('603 C', '603 C'),
  ('604 C', '604 C'),
  ('605 C', '605 C'),
  ('606 C', '606 C'),
  ('607 C', '607 C'),
  ('608 C', '608 C'),
  ('609 C', '609 C'),
  ('610 C', '610 C'),
  ('611 C', '611 C'),
  ('612 C', '612 C'),
  ('613 C', '613 C'),
  ('614 C', '614 C'),
  ('615 C', '615 C'),
  ('DAE (Sala Reuniones)','DAE (Sala Reuniones)'),
  ('DAE (Zócalo)', 'DAE (Zócalo)'),
  ('Fábrica 4310', 'Fábrica 4310'),

)

# ________________________________________________________________________________________________________________________________________________________

opciones_estado_activo = (
    ('Bueno', 'Bueno'),
    ('Malo', 'Malo'),
    ('Con Detalles', 'Con Detalles'),
)

opciones_edificio = (
    ('Edificio A Tirana', 'Edificio A Tirana'),
    ('Edificio B Mecánica', 'Edificio B Mecánica'),
    ('Edificio C Dunas', 'Edificio C Dunas'),
)