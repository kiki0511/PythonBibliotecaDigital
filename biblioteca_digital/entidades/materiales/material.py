"""Modelos de materiales disponibles en la biblioteca."""

from __future__ import annotations

from typing import Optional

from biblioteca_digital import constantes


class Material:
    """Modelo base para cualquier material bibliográfico."""

    TIPO: str = "Material"

    def __init__(self, titulo: str, autor: str, codigo: Optional[str] = None) -> None:
        self.titulo = titulo
        self.autor = autor
        slug = self.titulo.lower().replace(" ", "-")
        self.codigo = codigo or f"{self.TIPO.lower()}-{slug}"
        self.estado = constantes.ESTADO_MATERIAL_DISPONIBLE

    @property
    def tipo(self) -> str:
        return self.TIPO

    def esta_disponible(self) -> bool:
        return self.estado == constantes.ESTADO_MATERIAL_DISPONIBLE

    def marcar_prestado(self) -> None:
        self.estado = constantes.ESTADO_MATERIAL_PRESTADO

    def marcar_disponible(self) -> None:
        self.estado = constantes.ESTADO_MATERIAL_DISPONIBLE

    def marcar_reservado(self) -> None:
        self.estado = constantes.ESTADO_MATERIAL_RESERVADO

    def marcar_en_mantenimiento(self) -> None:
        self.estado = constantes.ESTADO_MATERIAL_EN_MANTENIMIENTO

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(titulo='{self.titulo}', autor='{self.autor}')"

    def __str__(self) -> str:
        return f"{self.tipo}: {self.titulo} - {self.autor}"

    def descripcion_detallada(self) -> str:
        return str(self)


__all__ = ["Material"]
