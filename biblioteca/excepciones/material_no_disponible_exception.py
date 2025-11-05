"""
Excepción para material no disponible.
"""

from biblioteca_digital.excepciones.biblioteca_exception import BibliotecaException


class MaterialNoDisponibleException(BibliotecaException):
    """
    Excepción lanzada cuando se intenta prestar un material no disponible.
    """

    def __init__(self, id_material: int, titulo: str):
        """
        Inicializa la excepción.

        Args:
            id_material: ID del material no disponible
            titulo: Título del material
        """
        self._id_material = id_material
        self._titulo = titulo
        mensaje = f"Material no disponible para préstamo: {titulo} (ID: {id_material})"
        super().__init__(mensaje)

    def get_id_material(self) -> int:
        """Retorna el ID del material."""
        return self._id_material

    def get_titulo(self) -> str:
        """Retorna el título del material."""
        return self._titulo