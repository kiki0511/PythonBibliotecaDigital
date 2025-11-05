"""
Constantes del sistema de biblioteca digital.
Define valores fijos utilizados en toda la aplicación.
"""

# Días de préstamo por tipo de material
DIAS_PRESTAMO_LIBRO = 14
DIAS_PRESTAMO_REVISTA = 7
DIAS_PRESTAMO_EBOOK = 21
DIAS_PRESTAMO_AUDIOLIBRO = 10

# Multas por tipo de membresía (por día de retraso)
MULTA_BASICA_POR_DIA = 2.00
MULTA_ESTANDAR_POR_DIA = 1.00
MULTA_PREMIUM_POR_DIA = 0.00

# Días de anticipación para notificación de vencimiento
DIAS_NOTIFICACION_VENCIMIENTO = 3

# Tipos de membresía
TIPO_MEMBRESIA_BASICA = "Basica"
TIPO_MEMBRESIA_ESTANDAR = "Estandar"
TIPO_MEMBRESIA_PREMIUM = "Premium"

# Tipos de materiales
TIPO_MATERIAL_LIBRO = "Libro"
TIPO_MATERIAL_REVISTA = "Revista"
TIPO_MATERIAL_EBOOK = "eBook"
TIPO_MATERIAL_AUDIOLIBRO = "Audiolibro"

# Estados de préstamos
ESTADO_PRESTAMO_ACTIVO = "Activo"
ESTADO_PRESTAMO_DEVUELTO = "Devuelto"
ESTADO_PRESTAMO_VENCIDO = "Vencido"

# Estados de reservas
ESTADO_RESERVA_PENDIENTE = "Pendiente"
ESTADO_RESERVA_NOTIFICADA = "Notificada"
ESTADO_RESERVA_COMPLETADA = "Completada"
ESTADO_RESERVA_CANCELADA = "Cancelada"

# Estados de materiales
ESTADO_MATERIAL_DISPONIBLE = "Disponible"
ESTADO_MATERIAL_PRESTADO = "Prestado"
ESTADO_MATERIAL_RESERVADO = "Reservado"
ESTADO_MATERIAL_EN_MANTENIMIENTO = "En Mantenimiento"

# Persistencia
DIRECTORIO_DATA = "data"
EXTENSION_DATA = ".dat"

# Tipos de notificaciones
TIPO_NOTIF_PRESTAMO = "PRESTAMO"
TIPO_NOTIF_DEVOLUCION = "DEVOLUCION"
TIPO_NOTIF_RESERVA = "RESERVA"
TIPO_NOTIF_MULTA = "MULTA"
TIPO_NOTIF_VENCIMIENTO = "VENCIMIENTO"