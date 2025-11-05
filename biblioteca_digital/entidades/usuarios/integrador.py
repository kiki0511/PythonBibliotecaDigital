"""
Archivo integrador generado automaticamente
Directorio: /Users/pc_joaco/Desktop/Facu/3-Diseno_de_sistema/PythonBibliotecaDigital/biblioteca_digital/entidades/usuarios
Fecha: 2025-11-05 09:05:45
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: membresia.py
# Ruta: /Users/pc_joaco/Desktop/Facu/3-Diseno_de_sistema/PythonBibliotecaDigital/biblioteca_digital/entidades/usuarios/membresia.py
# ================================================================================

"""Modelo de membresía de usuario."""

from __future__ import annotations

from dataclasses import dataclass

from biblioteca_digital import constantes
from biblioteca_digital.patrones.strategy.impl.multa_estandar_strategy import (
    MultaEstandarStrategy,
)
from biblioteca_digital.patrones.strategy.impl.multa_reducida_strategy import (
    MultaReducidaStrategy,
)
from biblioteca_digital.patrones.strategy.impl.sin_multa_strategy import SinMultaStrategy
from biblioteca_digital.patrones.strategy.multa_strategy import MultaStrategy

_ESTRATEGIAS: dict[str, MultaStrategy] = {
    constantes.TIPO_MEMBRESIA_BASICA: MultaEstandarStrategy(),
    constantes.TIPO_MEMBRESIA_ESTANDAR: MultaReducidaStrategy(),
    constantes.TIPO_MEMBRESIA_PREMIUM: SinMultaStrategy(),
}

_DIAS_PRESTAMO: dict[str, int] = {
    constantes.TIPO_MEMBRESIA_BASICA: 7,
    constantes.TIPO_MEMBRESIA_ESTANDAR: 14,
    constantes.TIPO_MEMBRESIA_PREMIUM: 30,
}


@dataclass(frozen=True)
class Membresia:
    """Representa una membresía con políticas de préstamo y multa."""

    tipo: str
    dias_prestamo: int
    estrategia_multa: MultaStrategy

    def calcular_multa(self, dias_retraso: int) -> float:
        return self.estrategia_multa.calcular_multa(dias_retraso)

    @classmethod
    def crear(cls, tipo: str) -> "Membresia":
        tipo_normalizado = tipo.capitalize()
        if tipo_normalizado not in _ESTRATEGIAS:
            raise ValueError(f"Tipo de membresía inválido: {tipo}")
        return cls(
            tipo=tipo_normalizado,
            dias_prestamo=_DIAS_PRESTAMO[tipo_normalizado],
            estrategia_multa=_ESTRATEGIAS[tipo_normalizado],
        )

    def __str__(self) -> str:
        return self.tipo


__all__ = ["Membresia"]


# ================================================================================
# ARCHIVO 2/2: usuario.py
# Ruta: /Users/pc_joaco/Desktop/Facu/3-Diseno_de_sistema/PythonBibliotecaDigital/biblioteca_digital/entidades/usuarios/usuario.py
# ================================================================================

"""Entidad que representa a los usuarios de la biblioteca."""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import List, TYPE_CHECKING

from .membresia import Membresia

if TYPE_CHECKING:
    from biblioteca_digital.entidades.prestamos.prestamo import Prestamo
    from biblioteca_digital.entidades.prestamos.reserva import Reserva

_EMAIL_REGEX = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


@dataclass
class Usuario:
    """Modelo de dominio para usuarios registrados."""

    dni: int
    nombre: str
    email: str
    membresia: Membresia
    prestamos_activos: List["Prestamo"] = field(default_factory=list, init=False)
    reservas_activas: List["Reserva"] = field(default_factory=list, init=False)

    def __post_init__(self) -> None:
        if self.dni <= 0:
            raise ValueError("El DNI debe ser un entero positivo.")
        if not self.nombre:
            raise ValueError("El nombre no puede estar vacío.")
        if not _EMAIL_REGEX.match(self.email):
            raise ValueError(f"Email inválido: {self.email}")

    def calcular_multa(self, dias_retraso: int) -> float:
        return self.membresia.calcular_multa(dias_retraso)

    def registrar_prestamo(self, prestamo: "Prestamo") -> None:
        if prestamo not in self.prestamos_activos:
            self.prestamos_activos.append(prestamo)

    def cerrar_prestamo(self, prestamo: "Prestamo") -> None:
        if prestamo in self.prestamos_activos:
            self.prestamos_activos.remove(prestamo)

    def agregar_reserva(self, reserva: "Reserva") -> None:
        if reserva not in self.reservas_activas:
            self.reservas_activas.append(reserva)

    def remover_reserva(self, reserva: "Reserva") -> None:
        if reserva in self.reservas_activas:
            self.reservas_activas.remove(reserva)

    def __str__(self) -> str:
        return (
            f"Usuario: {self.nombre} (DNI: {self.dni}) - {self.membresia.tipo}"
        )


__all__ = ["Usuario"]


