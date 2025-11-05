"""
Excepción para errores de persistencia.
"""

from enum import Enum
from biblioteca_digital.excepciones.biblioteca_exception import BibliotecaException


class TipoOperacion(Enum):
    """Tipos de operaciones de persistencia."""
    GUARDAR = "GUARDAR"
    CARGAR = "CARGAR"
    ELIMINAR = "ELIMINAR"


class PersistenciaException(BibliotecaException):
    """
    Excepción lanzada cuando ocurre un error en operaciones de persistencia.
    """

    def __init__(self, mensaje: str, nombre_archivo: str, tipo_operacion: TipoOperacion):
        """
        Inicializa la excepción.

        Args:
            mensaje: Mensaje descriptivo del error
            nombre_archivo: Nombre del archivo involucrado
            tipo_operacion: Tipo de operación que falló
        """
        self._nombre_archivo = nombre_archivo
        self._tipo_operacion = tipo_operacion
        mensaje_completo = f"{mensaje} - Archivo: {nombre_archivo} - Operación: {tipo_operacion.value}"
        super().__init__(mensaje_completo)

    def get_nombre_archivo(self) -> str:
        """Retorna el nombre del archivo."""
        return self._nombre_archivo

    def get_tipo_operacion(self) -> TipoOperacion:
        """Retorna el tipo de operación."""
        return self._tipo_operacion