"""
Entidad Membresía del sistema.
Representa un tipo de membresía con sus características.
"""


class Membresia:
    """
    Representa un tipo de membresía en la biblioteca.
    Cada membresía tiene diferentes privilegios y días de préstamo.
    """

    def __init__(self, tipo: str, dias_prestamo: int, descripcion: str):
        """
        Inicializa una membresía.

        Args:
            tipo: Tipo de membresía (Basica, Estandar, Premium)
            dias_prestamo: Días de préstamo base permitidos
            descripcion: Descripción de la membresía

        Raises:
            ValueError: Si días de préstamo es inválido
        """
        if dias_prestamo <= 0:
            raise ValueError("Los días de préstamo deben ser mayores a cero")

        self._tipo = tipo
        self._dias_prestamo = dias_prestamo
        self._descripcion = descripcion

    def get_tipo(self) -> str:
        """Retorna el tipo de membresía."""
        return self._tipo

    def get_dias_prestamo(self) -> int:
        """Retorna los días de préstamo base."""
        return self._dias_prestamo

    def get_descripcion(self) -> str:
        """Retorna la descripción de la membresía."""
        return self._descripcion

    def __str__(self) -> str:
        """Representación en string."""
        return f"Membresía {self._tipo} - {self._dias_prestamo} días"

    def __repr__(self) -> str:
        """Representación técnica."""
        return f"Membresia(tipo='{self._tipo}', dias={self._dias_prestamo})"