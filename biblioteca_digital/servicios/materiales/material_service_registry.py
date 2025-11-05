"""Registro centralizado de servicios de materiales."""

from __future__ import annotations

from typing import Dict, Iterable, Optional, TYPE_CHECKING, Union

from biblioteca_digital import constantes
from biblioteca_digital.entidades.materiales.material import Material
from biblioteca_digital.patrones.singleton.singleton_meta import SingletonMeta

from .audiolibro_service import AudiolibroService
from .ebook_service import EbookService
from .libro_service import LibroService
from .materiales_service import MaterialService
from .revista_service import RevistaService


if TYPE_CHECKING:
    from biblioteca_digital.entidades.usuarios.membresia import Membresia


class MaterialServiceRegistry(metaclass=SingletonMeta):
    """Patrón Registry + Singleton para acceder a servicios por tipo."""

    def __init__(self) -> None:
        self._servicios: Dict[str, MaterialService] = {
            constantes.TIPO_MATERIAL_LIBRO: LibroService(),
            constantes.TIPO_MATERIAL_REVISTA: RevistaService(),
            constantes.TIPO_MATERIAL_EBOOK: EbookService(),
            constantes.TIPO_MATERIAL_AUDIOLIBRO: AudiolibroService(),
        }

    def registrar_servicio(
        self, tipo_material: str, servicio: MaterialService
    ) -> None:
        self._servicios[tipo_material] = servicio

    def obtener_servicio(
        self, material_o_tipo: Union[Material, str]
    ) -> MaterialService:
        tipo = (
            material_o_tipo.tipo
            if isinstance(material_o_tipo, Material)
            else material_o_tipo
        )
        try:
            return self._servicios[tipo]
        except KeyError as exc:
            raise ValueError(f"No existe servicio registrado para {tipo}") from exc

    def obtener_dias_prestamo(
        self, material: Material, membresia: Optional["Membresia"] = None
    ) -> int:
        servicio = self.obtener_servicio(material)
        return servicio.calcular_dias_prestamo(membresia)

    def calcular_fecha_vencimiento(
        self,
        material: Material,
        membresia: Optional["Membresia"],
        fecha_referencia=None,
    ):
        servicio = self.obtener_servicio(material)
        return servicio.calcular_fecha_vencimiento(material, membresia, fecha_referencia)

    def tipos_registrados(self) -> Iterable[str]:
        return self._servicios.keys()

    def obtener_descripcion(self, material: Material) -> str:
        servicio = self.obtener_servicio(material)
        return servicio.descripcion(material)


__all__ = ["MaterialServiceRegistry"]
