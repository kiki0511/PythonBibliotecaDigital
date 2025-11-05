"""
Entidad Revista del sistema.
Representa una revista o publicación periódica.
"""

from biblioteca_digital.entidades.materiales.material import Material


class Revista(Material):
    """
    Representa una revista o publicación periódica.
    Incluye información sobre edición y periodicidad.
    """

    def __init__(
        self,
        id_material: int,
        titulo: str,
        autor: str,
        numero_edicion: int,
        periodicidad: str
    ):
        """
        Inicializa una revista.

        Args:
            id_material: ID único del material
            titulo: Título de la revista
            autor: Editor o autor principal
            numero_edicion: Número de la edición
            periodicidad: Frecuencia de publicación (Semanal, Mensual, etc.)

        Raises:
            ValueError: Si numero_edicion es inválido
        """
        super().__init__(id_material, titulo, autor)

        if numero_edicion <= 0:
            raise ValueError("El número de edición debe ser mayor a cero")

        self._numero_edicion = numero_edicion
        self._periodicidad = periodicidad

    def get_numero_edicion(self) -> int:
        """Retorna el número de edición."""
        return self._numero_edicion

    def get_periodicidad(self) -> str:
        """Retorna la periodicidad de la revista."""
        return self._periodicidad

    def __str__(self) -> str:
        """Representación en string."""
        return f"Revista: {self.get_titulo()} #{self._numero_edicion} - {self._periodicidad}"