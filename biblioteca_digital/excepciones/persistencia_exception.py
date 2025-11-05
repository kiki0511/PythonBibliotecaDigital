"""Excepción para errores de persistencia."""

from .biblioteca_exception import BibliotecaException


class PersistenciaException(BibliotecaException):
    """Se lanza ante errores de lectura o escritura en disco."""

    def __init__(self, message: str) -> None:
        super().__init__(f"Error de persistencia: {message}")


__all__ = ["PersistenciaException"]
