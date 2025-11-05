"""Servicio para la persistencia de usuarios en disco."""

from __future__ import annotations

import pickle
from pathlib import Path
from typing import Optional

from biblioteca_digital import constantes
from biblioteca_digital.entidades.usuarios.usuario import Usuario
from biblioteca_digital.excepciones.persistencia_exception import PersistenciaException


class UsuarioService:
    """Gestiona la serialización y deserialización de usuarios."""

    def __init__(self, base_path: Optional[Path] = None) -> None:
        raiz_proyecto = Path(__file__).resolve().parents[3]
        self._data_dir = (base_path or raiz_proyecto / constantes.DIRECTORIO_DATA)
        self._data_dir.mkdir(exist_ok=True)

    def _obtener_ruta(self, identificador: str) -> Path:
        nombre = identificador.strip()
        if not nombre:
            raise PersistenciaException("Nombre de archivo vacío.")
        return self._data_dir / f"{nombre}{constantes.EXTENSION_DATA}"

    def guardar_usuario(self, usuario: Usuario, identificador: Optional[str] = None) -> Path:
        ruta = self._obtener_ruta(identificador or usuario.nombre)
        try:
            with ruta.open("wb") as archivo:
                pickle.dump(usuario, archivo)
        except OSError as exc:
            raise PersistenciaException(str(exc)) from exc
        return ruta

    def cargar_usuario(self, identificador: str) -> Usuario:
        ruta = self._obtener_ruta(identificador)
        try:
            with ruta.open("rb") as archivo:
                usuario: Usuario = pickle.load(archivo)
        except FileNotFoundError as exc:
            raise PersistenciaException(f"No existe archivo {ruta.name}") from exc
        except OSError as exc:
            raise PersistenciaException(str(exc)) from exc
        return usuario
