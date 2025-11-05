"""
Excepción base del sistema de biblioteca digital.
"""


class BibliotecaException(Exception):
    """
    Excepción base para el sistema de biblioteca.
    Todas las excepciones específicas deben heredar de esta.
    """

    def __init__(self, mensaje: str):
        """
        Inicializa la excepción.

        Args:
            mensaje: Mensaje descriptivo del error
        """
        self._mensaje = mensaje
        super().__init__(self._mensaje)

    def get_mensaje(self) -> str:
        """Retorna el mensaje de error."""
        return self._mensaje