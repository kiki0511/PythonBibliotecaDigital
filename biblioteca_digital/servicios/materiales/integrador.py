"""
Archivo integrador generado automaticamente
Directorio: /Users/pc_joaco/Desktop/Facu/3-Diseno_de_sistema/PythonBibliotecaDigital/biblioteca_digital/servicios/materiales
Fecha: 2025-11-05 09:05:45
Total de archivos integrados: 6
"""

# ================================================================================
# ARCHIVO 1/6: audiolibro_service.py
# Ruta: /Users/pc_joaco/Desktop/Facu/3-Diseno_de_sistema/PythonBibliotecaDigital/biblioteca_digital/servicios/materiales/audiolibro_service.py
# ================================================================================

"""Servicio para audiolibros."""

from __future__ import annotations

from biblioteca_digital.constantes import DIAS_PRESTAMO_AUDIOLIBRO

from .materiales_service import MaterialService


class AudiolibroService(MaterialService):
    """Aplica las políticas de préstamos a los audiolibros."""

    def __init__(self) -> None:
        super().__init__(dias_prestamo_base=DIAS_PRESTAMO_AUDIOLIBRO)


__all__ = ["AudiolibroService"]


# ================================================================================
# ARCHIVO 2/6: ebook_service.py
# Ruta: /Users/pc_joaco/Desktop/Facu/3-Diseno_de_sistema/PythonBibliotecaDigital/biblioteca_digital/servicios/materiales/ebook_service.py
# ================================================================================

"""Servicio específico para eBooks."""

from __future__ import annotations

from biblioteca_digital.constantes import DIAS_PRESTAMO_EBOOK

from .materiales_service import MaterialService


class EbookService(MaterialService):
    """Gestiona las reglas de préstamo para libros digitales."""

    def __init__(self) -> None:
        super().__init__(dias_prestamo_base=DIAS_PRESTAMO_EBOOK)


__all__ = ["EbookService"]


# ================================================================================
# ARCHIVO 3/6: libro_service.py
# Ruta: /Users/pc_joaco/Desktop/Facu/3-Diseno_de_sistema/PythonBibliotecaDigital/biblioteca_digital/servicios/materiales/libro_service.py
# ================================================================================

"""Servicio específico para libros."""

from __future__ import annotations

from biblioteca_digital.constantes import DIAS_PRESTAMO_LIBRO

from .materiales_service import MaterialService


class LibroService(MaterialService):
    """Gestiona reglas de préstamo para libros físicos."""

    def __init__(self) -> None:
        super().__init__(dias_prestamo_base=DIAS_PRESTAMO_LIBRO)


__all__ = ["LibroService"]


# ================================================================================
# ARCHIVO 4/6: material_service_registry.py
# Ruta: /Users/pc_joaco/Desktop/Facu/3-Diseno_de_sistema/PythonBibliotecaDigital/biblioteca_digital/servicios/materiales/material_service_registry.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 5/6: materiales_service.py
# Ruta: /Users/pc_joaco/Desktop/Facu/3-Diseno_de_sistema/PythonBibliotecaDigital/biblioteca_digital/servicios/materiales/materiales_service.py
# ================================================================================

"""Servicios base para operaciones sobre materiales."""

from __future__ import annotations

from abc import ABC
from datetime import datetime, timedelta
from typing import Optional, TYPE_CHECKING

from biblioteca_digital.excepciones.material_no_disponible_exception import (
    MaterialNoDisponibleException,
)

if TYPE_CHECKING:
    from biblioteca_digital.entidades.materiales.material import Material
    from biblioteca_digital.entidades.usuarios.membresia import Membresia


class MaterialService(ABC):
    """Servicio base reutilizable por los distintos tipos de materiales."""

    def __init__(self, dias_prestamo_base: int) -> None:
        self._dias_prestamo_base = dias_prestamo_base

    def validar_disponibilidad(self, material: "Material") -> None:
        if not material.esta_disponible():
            raise MaterialNoDisponibleException(material.codigo)

    def calcular_fecha_vencimiento(
        self,
        material: "Material",
        membresia: Optional["Membresia"],
        fecha_referencia: Optional[datetime] = None,
    ) -> datetime:
        dias = self.calcular_dias_prestamo(membresia)
        fecha_referencia = fecha_referencia or datetime.now()
        return fecha_referencia + timedelta(days=dias)

    def calcular_dias_prestamo(self, membresia: Optional["Membresia"]) -> int:
        if membresia:
            return min(self._dias_prestamo_base, membresia.dias_prestamo)
        return self._dias_prestamo_base

    def prestar(self, material: "Material") -> None:
        self.validar_disponibilidad(material)
        material.marcar_prestado()

    def devolver(self, material: "Material") -> None:
        material.marcar_disponible()

    def descripcion(self, material: "Material") -> str:
        return material.descripcion_detallada()


__all__ = ["MaterialService"]


# ================================================================================
# ARCHIVO 6/6: revista_service.py
# Ruta: /Users/pc_joaco/Desktop/Facu/3-Diseno_de_sistema/PythonBibliotecaDigital/biblioteca_digital/servicios/materiales/revista_service.py
# ================================================================================

"""Servicio específico para revistas."""

from __future__ import annotations

from biblioteca_digital.constantes import DIAS_PRESTAMO_REVISTA

from .materiales_service import MaterialService


class RevistaService(MaterialService):
    """Gestiona el ciclo de vida de las revistas."""

    def __init__(self) -> None:
        super().__init__(dias_prestamo_base=DIAS_PRESTAMO_REVISTA)


__all__ = ["RevistaService"]


