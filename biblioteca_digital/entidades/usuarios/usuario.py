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
