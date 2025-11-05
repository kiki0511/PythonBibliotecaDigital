"""Entidad Libro que extiende Material."""

from __future__ import annotations

from typing import Optional

from biblioteca_digital import constantes

from .material import Material


class Libro(Material):
    """Representa un libro físico tradicional."""

    TIPO: str = constantes.TIPO_MATERIAL_LIBRO

    def __init__(
        self,
        titulo: str,
        autor: str,
        isbn: str,
        editorial: Optional[str] = None,
        paginas: Optional[int] = None,
        codigo: Optional[str] = None,
    ) -> None:
        super().__init__(titulo=titulo, autor=autor, codigo=codigo)
        self.isbn = isbn
        self.editorial = editorial
        self.paginas = paginas

    def __str__(self) -> str:
        detalles = [f"ISBN: {self.isbn}"]
        if self.paginas is not None:
            detalles.append(f"{self.paginas} páginas")
        if self.editorial:
            detalles.append(f"Editorial: {self.editorial}")
        det_str = ", ".join(detalles)
        return f"Libro: {self.titulo} - {self.autor} ({det_str})"

    def descripcion_detallada(self) -> str:
        partes = [f"Libro ISBN: {self.isbn}"]
        if self.paginas is not None:
            partes.append(f"{self.paginas} páginas")
        if self.editorial:
            partes.append(f"Editorial: {self.editorial}")
        return ", ".join(partes)


__all__ = ["Libro"]
