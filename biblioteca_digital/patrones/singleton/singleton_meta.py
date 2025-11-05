"""Metaclase para implementar el patrón Singleton thread-safe."""

from __future__ import annotations

from threading import RLock
from typing import Any, Dict, Type


class SingletonMeta(type):
    """Metaclase que garantiza una única instancia por clase."""

    _instances: Dict[Type, Any] = {}
    _lock: RLock = RLock()

    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        if cls not in cls._instances:
            with cls._lock:
                if cls not in cls._instances:
                    cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


__all__ = ["SingletonMeta"]
