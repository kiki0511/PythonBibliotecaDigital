"""Excepciones base del dominio de la biblioteca digital."""


class BibliotecaException(Exception):
    """Excepción base para el dominio del sistema de biblioteca."""

    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message


__all__ = ["BibliotecaException"]
