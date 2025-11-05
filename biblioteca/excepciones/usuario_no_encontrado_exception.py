"""
Excepción para usuario no encontrado.
"""

from biblioteca_digital.excepciones.biblioteca_exception import BibliotecaException


class UsuarioNoEncontradoException(BibliotecaException):
    """
    Excepción lanzada cuando no se encuentra un usuario en el sistema.
    """

    def __init__(self, dni: int):
        """
        Inicializa la excepción.

        Args:
            dni: DNI del usuario no encontrado
        """
        self._dni = dni
        mensaje = f"Usuario con DNI {dni} no encontrado en el sistema"
        super().__init__(mensaje)

    def get_dni(self) -> int:
        """Retorna el DNI del usuario no encontrado."""
        return self._dni