"""
Entidad base Material del sistema.
Clase abstracta que define la interfaz para todos los materiales.
"""

from abc import ABC
from biblioteca_digital.constantes import ESTADO_MATERIAL_DISPONIBLE


class Material(ABC):
    """
    Clase base abstracta para materiales bibliográficos.
    Define la interfaz común para todos los tipos de materiales.
    """

    def __init__(self, id_material: int, titulo: str, autor: str):
        """
        Inicializa un material.

        Args:
            id_material: ID único del material
            titulo: Título del material
            autor: Autor del material

        Raises:
            ValueError: Si el ID es inválido
        """
        if id_material <= 0:
            raise ValueError("El ID del material debe ser un número positivo")

        self._id_material = id_material
        self._titulo = titulo
        self._autor = autor
        self._estado = ESTADO_MATERIAL_DISPONIBLE

    def get_id_material(self) -> int:
        """Retorna el ID del material."""
        return self._id_material

    def get_titulo(self) -> str:
        """Retorna el título del material."""
        return self._titulo

    def get_autor(self) -> str:
        """Retorna el autor del material."""
        return self._autor

    def get_estado(self) -> str:
        """Retorna el estado actual del material."""
        return self._estado

    def set_estado(self, estado: str) -> None:
        """
        Establece el estado del material.

        Args:
            estado: Nuevo estado del material
        """
        self._estado = estado

    def esta_disponible(self) -> bool:
        """
        Verifica si el material está disponible para préstamo.

        Returns:
            True si está disponible, False en caso contrario
        """
        return self._estado == ESTADO_MATERIAL_DISPONIBLE

    def __str__(self) -> str:
        """Representación en string."""
        return f"{self._titulo} - {self._autor} [{self._estado}]"

    def __repr__(self) -> str:
        """Representación técnica."""
        return f"Material(id={self._id_material}, titulo='{self._titulo}')"