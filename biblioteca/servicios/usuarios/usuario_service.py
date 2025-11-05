"""
Servicio para persistencia de usuarios.
"""

import os
import pickle
from typing import Optional
from biblioteca_digital.entidades.usuarios.usuario import Usuario
from biblioteca_digital.excepciones.persistencia_exception import (
    PersistenciaException,
    TipoOperacion
)
from biblioteca_digital.constantes import DIRECTORIO_DATA, EXTENSION_DATA


class UsuarioService:
    """
    Servicio para guardar y cargar usuarios del disco.
    Usa serialización con Pickle.
    """

    def guardar_usuario(self, usuario: Usuario) -> str:
        """
        Guarda un usuario en disco.

        Args:
            usuario: Usuario a guardar

        Returns:
            Ruta del archivo creado

        Raises:
            PersistenciaException: Si ocurre un error al guardar
        """
        # Crear directorio si no existe
        if not os.path.exists(DIRECTORIO_DATA):
            os.makedirs(DIRECTORIO_DATA)

        nombre_archivo = f"{usuario.get_nombre()}{EXTENSION_DATA}"
        ruta_completa = os.path.join(DIRECTORIO_DATA, nombre_archivo)

        try:
            with open(ruta_completa, 'wb') as archivo:
                pickle.dump(usuario, archivo)
            print(f"Usuario {usuario.get_nombre()} guardado en {ruta_completa}")
            return ruta_completa
        except Exception as e:
            raise PersistenciaException(
                f"Error al guardar usuario: {str(e)}",
                nombre_archivo,
                TipoOperacion.GUARDAR
            )

    def cargar_usuario(self, nombre: str) -> Usuario:
        """
        Carga un usuario desde disco.

        Args:
            nombre: Nombre del usuario (usado como nombre de archivo)

        Returns:
            Usuario cargado

        Raises:
            PersistenciaException: Si ocurre un error al cargar
        """
        nombre_archivo = f"{nombre}{EXTENSION_DATA}"
        ruta_completa = os.path.join(DIRECTORIO_DATA, nombre_archivo)

        if not os.path.exists(ruta_completa):
            raise PersistenciaException(
                f"Archivo no encontrado",
                nombre_archivo,
                TipoOperacion.CARGAR
            )

        try:
            with open(ruta_completa, 'rb') as archivo:
                usuario = pickle.load(archivo)
            print(f"Usuario {nombre} cargado desde {ruta_completa}")
            return usuario
        except Exception as e:
            raise PersistenciaException(
                f"Error al cargar usuario: {str(e)}",
                nombre_archivo,
                TipoOperacion.CARGAR
            )