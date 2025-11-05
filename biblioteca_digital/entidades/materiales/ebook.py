"""Entidad eBook."""

from __future__ import annotations

from typing import Optional

from biblioteca_digital import constantes

from .material import Material


class Ebook(Material):
    """Libro digital con metadatos de formato."""

    TIPO: str = constantes.TIPO_MATERIAL_EBOOK

    def __init__(
        self,
        titulo: str,
        autor: str,
        formato: str,
        tamano_mb: float,
        codigo: Optional[str] = None,
    ) -> None:
        super().__init__(titulo=titulo, autor=autor, codigo=codigo)
        self.formato = formato
        self.tamano_mb = tamano_mb

    def __str__(self) -> str:
        return f"eBook: {self.titulo} - {self.autor} ({self.formato}, {self.tamano_mb:.1f}MB)"

    def descripcion_detallada(self) -> str:
        return f"eBook formato {self.formato}, {self.tamano_mb:.1f}MB"


__all__ = ["Ebook"]
