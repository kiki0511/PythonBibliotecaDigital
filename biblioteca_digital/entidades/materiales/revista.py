"""Entidad Revista."""

from __future__ import annotations

from typing import Optional

from biblioteca_digital import constantes

from .material import Material


class Revista(Material):
    """Revista periódica disponible en la biblioteca."""

    TIPO: str = constantes.TIPO_MATERIAL_REVISTA

    def __init__(
        self,
        titulo: str,
        autor: str,
        numero_edicion: str,
        periodicidad: str,
        codigo: Optional[str] = None,
    ) -> None:
        super().__init__(titulo=titulo, autor=autor, codigo=codigo)
        self.numero_edicion = numero_edicion
        self.periodicidad = periodicidad

    def __str__(self) -> str:
        return f"Revista: {self.titulo} #{self.numero_edicion} - {self.periodicidad}"

    def descripcion_detallada(self) -> str:
        return f"Revista #{self.numero_edicion}, Periodicidad: {self.periodicidad}"


__all__ = ["Revista"]
