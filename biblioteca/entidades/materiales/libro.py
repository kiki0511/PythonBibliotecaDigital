"""
Entidad Libro del sistema.
Representa un libro físico de la biblioteca.
"""

from biblioteca_digital.entidades.materiales.material import Material


class Libro(Material):
    """
    Representa un libro físico.
    Incluye información específica como ISBN, editorial y número de páginas.
    """

    def __init__(
        self,
        id_material: int,
        titulo: str,
        autor: str,
        isbn: str,
        editorial: str,
        num_paginas: int
    ):
        """
        Inicializa un libro.

        Args:
            id_material: ID único del material
            titulo: Título del libro
            autor: Autor del libro
            isbn: Código ISBN
            editorial: Editorial que publicó el libro
            num_paginas: Número de páginas

        Raises:
            ValueError: Si num_paginas es inválido
        """
        super().__init__(id_material, titulo, autor)

        if num_paginas <= 0:
            raise ValueError("El número de páginas debe ser mayor a cero")

        self._isbn = isbn
        self._editorial = editorial
        self._num_paginas = num_paginas

    def get_isbn(self) -> str:
        """Retorna el ISBN del libro."""
        return self._isbn

    def get_editorial(self) -> str:
        """Retorna la editorial del libro."""
        return self._editorial

    def get_num_paginas(self) -> int:
        """Retorna el número de páginas."""
        return self._num_paginas

    def __str__(self) -> str:
        """Representación en string."""
        return f"Libro: {self.get_titulo()} - {self.get_autor()} (ISBN: {self._isbn})"