"""Modelo de datos para notificaciones del sistema."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict


@dataclass(frozen=True)
class Notificacion:
    """Mensaje generado por el sistema ante un evento relevante."""

    tipo: str
    mensaje: str
    destinatario: str
    metadata: Dict[str, Any] = field(default_factory=dict)
    fecha: datetime = field(default_factory=datetime.now)


__all__ = ["Notificacion"]
