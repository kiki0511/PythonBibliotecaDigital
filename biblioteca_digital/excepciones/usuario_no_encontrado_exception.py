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
