"""
Entidad Audiolibro del sistema.
Representa un audiolibro o libro narrado.
"""

from biblioteca_digital.entidades.materiales.material import Material


class Audiolibro(Material):
    """
    Representa un audiolibro.
    Incluye información sobre duración y narrador.
    """

    def __init__(
        self,
        id_material: int,
        titulo: str,
        autor: str,
        duracion_minutos: int,
        narrador: str
    ):
        """
        Inicializa un audiolibro.

        Args:
            id_material: ID único del material
            titulo: Título del audiolibro
            autor: Autor del contenido
            duracion_minutos: Duración total en minutos
            narrador: Nombre del narrador

        Raises:
            ValueError: Si duracion_minutos es inválido
        """
        super().__init__(id_material, titulo, autor)

        if duracion_minutos <= 0:
            raise ValueError("La duración debe ser mayor a cero")

        self._duracion_minutos = duracion_minutos
        self._narrador = narrador

    def get_duracion_minutos(self) -> int:
        """Retorna la duración en minutos."""
        return self._duracion_minutos

    def get_narrador(self) -> str:
        """Retorna el nombre del narrador."""
        return self._narrador

    def __str__(self) -> str:
        """Representación en string."""
        horas = self._duracion_minutos // 60
        minutos = self._duracion_minutos % 60
        return f"Audiolibro: {self.get_titulo()} - {self.get_autor()} ({horas}h {minutos}min, narrado por {self._narrador})"