"""
Archivo integrador generado automaticamente
Directorio: /Users/pc_joaco/Desktop/Facu/3-Diseno_de_sistema/PythonBibliotecaDigital/biblioteca_digital/excepciones
Fecha: 2025-11-05 09:05:45
Total de archivos integrados: 4
"""

# ================================================================================
# ARCHIVO 1/4: biblioteca_exception.py
# Ruta: /Users/pc_joaco/Desktop/Facu/3-Diseno_de_sistema/PythonBibliotecaDigital/biblioteca_digital/excepciones/biblioteca_exception.py
# ================================================================================

"""Excepciones base del dominio de la biblioteca digital."""


class BibliotecaException(Exception):
    """Excepción base para el dominio del sistema de biblioteca."""

    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message


__all__ = ["BibliotecaException"]


# ================================================================================
# ARCHIVO 2/4: material_no_disponible_exception.py
# Ruta: /Users/pc_joaco/Desktop/Facu/3-Diseno_de_sistema/PythonBibliotecaDigital/biblioteca_digital/excepciones/material_no_disponible_exception.py
# ================================================================================

"""Excepción específica para materiales no disponibles."""

from typing import Optional

from .biblioteca_exception import BibliotecaException


class MaterialNoDisponibleException(BibliotecaException):
    """Se lanza cuando se intenta operar con un material no disponible."""

    def __init__(self, material_id: Optional[str] = None) -> None:
        mensaje = (
            f"Material no disponible para préstamo o reserva: {material_id}"
            if material_id
            else "Material no disponible para préstamo o reserva."
        )
        super().__init__(mensaje)


__all__ = ["MaterialNoDisponibleException"]


# ================================================================================
# ARCHIVO 3/4: persistencia_exception.py
# Ruta: /Users/pc_joaco/Desktop/Facu/3-Diseno_de_sistema/PythonBibliotecaDigital/biblioteca_digital/excepciones/persistencia_exception.py
# ================================================================================

"""Excepción para errores de persistencia."""

from .biblioteca_exception import BibliotecaException


class PersistenciaException(BibliotecaException):
    """Se lanza ante errores de lectura o escritura en disco."""

    def __init__(self, message: str) -> None:
        super().__init__(f"Error de persistencia: {message}")


__all__ = ["PersistenciaException"]


# ================================================================================
# ARCHIVO 4/4: usuario_no_encontrado_exception.py
# Ruta: /Users/pc_joaco/Desktop/Facu/3-Diseno_de_sistema/PythonBibliotecaDigital/biblioteca_digital/excepciones/usuario_no_encontrado_exception.py
# ================================================================================

"""Excepción para operaciones con usuarios inexistentes."""

from typing import Optional

from .biblioteca_exception import BibliotecaException


class UsuarioNoEncontradoException(BibliotecaException):
    """Se lanza cuando no se encuentra un usuario en el sistema."""

    def __init__(self, dni: Optional[int] = None) -> None:
        mensaje = (
            f"Usuario con DNI {dni} no encontrado." if dni else "Usuario no encontrado."
        )
        super().__init__(mensaje)


__all__ = ["UsuarioNoEncontradoException"]


