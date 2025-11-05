"""
Entidad eBook del sistema.
Representa un libro digital.
"""

from biblioteca_digital.entidades.materiales.material import Material


class eBook(Material):
    """
    Representa un libro digital (eBook).
    Incluye información sobre formato y tamaño.
    """

    def __init__(
        self,
        id_material: int,
        titulo: str,
        autor: str,
        formato: str,
        tamanio_mb: float
    ):
        """
        Inicializa un eBook.

        Args:
            id_material: ID único del material
            titulo: Título del eBook
            autor: Autor del eBook
            formato: Formato del archivo (PDF, EPUB, MOBI, etc.)
            tamanio_mb: Tamaño del archivo en megabytes

        Raises:
            ValueError: Si tamanio_mb es inválido
        """
        super().__init__(id_material, titulo, autor)

        if tamanio_mb <= 0:
            raise ValueError("El tamaño debe ser mayor a cero")

        self._formato = formato
        self._tamanio_mb = tamanio_mb

    def get_formato(self) -> str:
        """Retorna el formato del eBook."""
        return self._formato

    def get_tamanio_mb(self) -> float:
        """Retorna el tamaño en megabytes."""
        return self._tamanio_mb

    def __str__(self) -> str:
        """Representación en string."""
        return f"eBook: {self.get_titulo()} - {self.get_autor()} ({self._formato}, {self._tamanio_mb}MB)"