# Historias de Usuario - Sistema de Gestión de Biblioteca Digital

**Proyecto**: BibliotecaDigital  
**Versión**: 1.0.0  
**Fecha**: Noviembre 2025  
**Metodología**: User Story Mapping

---

## Índice

1. [Historias de Usuario Principales](#historias-de-usuario-principales)
   - [US-001: Registrar Usuario en el Sistema](#us-001-registrar-usuario-en-el-sistema)
   - [US-002: Prestar Material Bibliográfico](#us-002-prestar-material-bibliográfico)
   - [US-003: Devolver Material y Calcular Multas](#us-003-devolver-material-y-calcular-multas)
   - [US-004: Reservar Material No Disponible](#us-004-reservar-material-no-disponible)
   - [US-005: Recibir Notificaciones de Eventos](#us-005-recibir-notificaciones-de-eventos)
2. [Historias Técnicas (Patrones de Diseño)](#historias-técnicas-patrones-de-diseño)
   - [US-TECH-001: Implementar Singleton para UsuarioManager](#us-tech-001-implementar-singleton-para-usuariomanager)
   - [US-TECH-002: Implementar Factory Method para Materiales](#us-tech-002-implementar-factory-method-para-materiales)
   - [US-TECH-003: Implementar Observer Pattern para Notificaciones](#us-tech-003-implementar-observer-pattern-para-notificaciones)
   - [US-TECH-004: Implementar Strategy Pattern para Cálculo de Multas](#us-tech-004-implementar-strategy-pattern-para-cálculo-de-multas)
   - [US-TECH-005: Implementar Registry Pattern para Dispatch Polimórfico](#us-tech-005-implementar-registry-pattern-para-dispatch-polimórfico)

---

## Historias de Usuario Principales

### US-001: Registrar Usuario en el Sistema

**Como** administrador de biblioteca  
**Quiero** registrar nuevos usuarios con diferentes tipos de membresía  
**Para** controlar el acceso y privilegios de cada usuario

#### Criterios de Aceptación

- [x] Permitir crear un usuario con DNI (entero positivo), nombre, email y tipo de membresía (Básica, Estándar, Premium).
- [x] Validar unicidad del DNI dentro del gestor.
- [x] Configurar automáticamente las políticas de préstamo y multa según la membresía.
- [x] Validar formato de email.
- [x] Posibilitar la persistencia del usuario en disco.

#### Detalles Técnicos

**Clase**: `Usuario` (`biblioteca_digital/entidades/usuarios/usuario.py`)  
**Servicio**: `UsuarioManager` (`biblioteca_digital/servicios/usuarios/usuario_manager.py`)

**Código de ejemplo**:
```python
from biblioteca_digital.servicios.usuarios.usuario_manager import UsuarioManager

usuario_manager = UsuarioManager.get_instance()
usuario = usuario_manager.registrar_usuario(
    dni=12345678,
    nombre="Juan Perez",
    email="juan@email.com",
    tipo_membresia="Premium",
)
```

**Validaciones**:
```python
usuario_manager.registrar_usuario(12345678, "Otro", "otro@email.com", "Basica")
# ValueError: Usuario con DNI 12345678 ya existe.

usuario_manager.registrar_usuario(87654321, "Maria", "maria@email.com", "Oro")
# ValueError: Tipo de membresía inválido: Oro
```

**Trazabilidad**: `main.py` líneas 92-117.

---

### US-002: Prestar Material Bibliográfico

**Como** bibliotecario  
**Quiero** registrar préstamos de materiales a usuarios  
**Para** llevar control de qué materiales están prestados y a quién

#### Criterios de Aceptación

- [x] Permitir prestar Libro, Revista, eBook y Audiolibro con reglas específicas por tipo.
- [x] Impedir prestar un material mientras esté marcado como prestado.
- [x] Generar fecha de vencimiento basada en el tipo de material y la membresía del usuario.
- [x] Registrar usuario, material, fecha de préstamo y fecha de vencimiento.
- [x] Cambiar el estado del material a “Prestado”.

#### Detalles Técnicos

**Clase**: `Prestamo` (`biblioteca_digital/entidades/prestamos/prestamo.py`)  
**Servicio**: `PrestamoService` (`biblioteca_digital/servicios/prestamo/prestamo_service.py`)  
**Factory**: `MaterialFactory` (`biblioteca_digital/patrones/factory/material_factory.py`)

**Código de ejemplo**:
```python
from biblioteca_digital.patrones.factory.material_factory import MaterialFactory
from biblioteca_digital.servicios.prestamo.prestamo_service import PrestamoService

libro = MaterialFactory.crear_material(
    tipo="Libro",
    titulo="Cien años de soledad",
    autor="Gabriel García Márquez",
    isbn="978-3-16-148410-0",
)

prestamo_service = PrestamoService.get_instance()
prestamo = prestamo_service.realizar_prestamo(usuario, libro)
print(prestamo.fecha_vencimiento.date())
```

**Validaciones**:
```python
prestamo_service.realizar_prestamo(otro_usuario, libro)
# MaterialNoDisponibleException: Material no disponible para préstamo o reserva: libro-...
```

**Trazabilidad**: `main.py` líneas 176-195 y `biblioteca_digital/servicios/materiales/materiales_service.py`.

---

### US-003: Devolver Material y Calcular Multas

**Como** bibliotecario  
**Quiero** registrar devoluciones de materiales y calcular multas automáticamente  
**Para** mantener control del inventario y cobrar penalizaciones por retrasos

#### Criterios de Aceptación

- [x] Registrar fecha de devolución y poner el material en estado “Disponible”.
- [x] Calcular días de retraso a partir de la fecha real de devolución.
- [x] Calcular multa según la estrategia asociada a la membresía del usuario.
- [x] Notificar al usuario si se generó una multa.
- [x] Al liberar el material, notificar a reservas en espera.

#### Detalles Técnicos

**Servicio**: `PrestamoService.registrar_devolucion()`  
**Strategy**: `MultaStrategy` (`biblioteca_digital/patrones/strategy/multa_strategy.py` y `impl/`)

**Código de ejemplo**:
```python
from datetime import datetime

multa = prestamo_service.registrar_devolucion(prestamo, fecha=datetime.now())
print(f"Multa generada: ${multa:.2f}")
```

**Ejemplos**:
```python
usuario_basico.calcular_multa(5)   # 10.00
usuario_estandar.calcular_multa(5) # 5.00
usuario_premium.calcular_multa(5)  # 0.00
```

**Trazabilidad**: `main.py` líneas 198-210.

---

### US-004: Reservar Material No Disponible

**Como** usuario de biblioteca  
**Quiero** reservar un material que está prestado actualmente  
**Para** ser notificado cuando esté disponible

#### Criterios de Aceptación

- [x] Registrar usuario, material, fecha y estado de la reserva.
- [x] Mantener las reservas en cola FIFO por material.
- [x] Permitir cancelar, notificar y completar reservas.
- [x] Al liberar el material, notificar al primer usuario de la cola.

#### Detalles Técnicos

**Clase**: `Reserva` (`biblioteca_digital/entidades/prestamos/reserva.py`)  
**Servicio**: `ReservaService` (`biblioteca_digital/servicios/prestamo/reserva_service.py`)

**Código de ejemplo**:
```python
from biblioteca_digital.servicios.prestamo.reserva_service import ReservaService

reserva_service = ReservaService.get_instance()
reserva = reserva_service.crear_reserva(usuario_estandar, revista)
reserva_service.notificar_disponibilidad(revista)
```

**Trazabilidad**: `main.py` líneas 212-223.

---

### US-005: Recibir Notificaciones de Eventos

**Como** usuario de biblioteca  
**Quiero** recibir notificaciones sobre eventos relevantes  
**Para** estar informado de vencimientos, disponibilidad y multas

#### Criterios de Aceptación

- [x] Notificar préstamos registrados, devoluciones, reservas disponibles, vencimientos y multas.
- [x] Incluir tipo de evento, mensaje, destinatario y metadatos básicos.
- [x] Permitir múltiples observadores suscribibles dinámicamente.
- [x] Utilizar una implementación tipo-segura del patrón Observer.

#### Detalles Técnicos

**Clase**: `Notificacion` (`biblioteca_digital/notificaciones/notificacion.py`)  
**Servicio**: `NotificacionService` (`biblioteca_digital/notificaciones/notificacion_service.py`)

**Código de ejemplo**:
```python
from biblioteca_digital.notificaciones.notificacion_service import NotificacionService
from biblioteca_digital.patrones.observer.observer import Observer

class ConsoleNotifier(Observer):
    def actualizar(self, notificacion):
        print(f"[NOTIFICACION] {notificacion.mensaje}")

notif_service = NotificacionService()
notif_service.agregar_observador(ConsoleNotifier())

prestamo_service.realizar_prestamo(usuario, libro)
prestamo_service.registrar_devolucion(prestamo)
```

**Trazabilidad**: `main.py` líneas 150-171 y 198-210.

---

## Historias Técnicas (Patrones de Diseño)

### US-TECH-001: Implementar Singleton para UsuarioManager

**Como** arquitecto de software  
**Quiero** garantizar una única instancia del gestor de usuarios  
**Para** mantener consistencia en el registro de usuarios

#### Criterios de Aceptación

- [x] Implementar patrón Singleton thread-safe mediante metaclase.
- [x] Inicialización perezosa y bloqueo reentrante (`RLock`).
- [x] Proveer método `get_instance()` para acceso global.
- [x] Asegurar un único diccionario interno de usuarios por DNI.

#### Detalles Técnicos

**Patrón**: Singleton  
**Implementación**: `SingletonMeta` (`biblioteca_digital/patrones/singleton/singleton_meta.py`)  
**Clase afectada**: `UsuarioManager` (`biblioteca_digital/servicios/usuarios/usuario_manager.py`)

**Uso**:
```python
manager1 = UsuarioManager.get_instance()
manager2 = UsuarioManager.get_instance()
assert manager1 is manager2
```

**Trazabilidad**: `main.py` líneas 82-89.

---

### US-TECH-002: Implementar Factory Method para Materiales

**Como** arquitecto de software  
**Quiero** centralizar la creación de materiales  
**Para** desacoplar el cliente de las clases concretas

#### Criterios de Aceptación

- [x] Mantener un mapeo de tipos a clases concretas sin cascadas de `if/elif`.
- [x] Permitir crear Libro, Revista, eBook y Audiolibro.
- [x] Lanzar `ValueError` para tipos desconocidos.
- [x] Retornar instancias de `Material` o derivados configuradas con sus atributos específicos.

#### Detalles Técnicos

**Clase**: `MaterialFactory` (`biblioteca_digital/patrones/factory/material_factory.py`)

**Uso**:
```python
libro = MaterialFactory.crear_material(
    tipo="Libro",
    titulo="El Quijote",
    autor="Miguel de Cervantes",
    isbn="978-84-376-0494-7",
    paginas=863,
)
```

**Trazabilidad**: `main.py` líneas 120-154.

---

### US-TECH-003: Implementar Observer Pattern para Notificaciones

**Como** arquitecto de software  
**Quiero** implementar el patrón Observer con Generics  
**Para** notificar eventos del sistema de forma desacoplada

#### Criterios de Aceptación

- [x] Interfaz `Observer[T]` y clase base `Observable[T]` genéricas.
- [x] Métodos para agregar, remover y notificar observadores.
- [x] `NotificacionService` implementado como observable tipo-seguro.
- [x] Observadores concretos (p. ej. `ConsoleNotifier`) reaccionan a eventos.

#### Detalles Técnicos

**Ubicación**: `biblioteca_digital/patrones/observer/`  
**Servicio**: `NotificacionService` (`biblioteca_digital/notificaciones/notificacion_service.py`)

**Trazabilidad**: `main.py` líneas 29-34 y 150-210.

---

### US-TECH-004: Implementar Strategy Pattern para Cálculo de Multas

**Como** arquitecto de software  
**Quiero** algoritmos intercambiables para el cálculo de multas  
**Para** adaptarlos al tipo de membresía del usuario

#### Criterios de Aceptación

- [x] Definir interfaz `MultaStrategy` con método `calcular_multa`.
- [x] Estrategias concretas: `SinMultaStrategy`, `MultaEstandarStrategy`, `MultaReducidaStrategy`.
- [x] Asociar la estrategia en `Membresia` al crearse el usuario.
- [x] Utilizar valores configurables en `constantes.py`.

#### Detalles Técnicos

**Ubicación**: `biblioteca_digital/patrones/strategy/`  
**Entidad**: `Membresia` (`biblioteca_digital/entidades/usuarios/membresia.py`)

**Trazabilidad**: `main.py` líneas 198-210.

---

### US-TECH-005: Implementar Registry Pattern para Dispatch Polimórfico

**Como** arquitecto de software  
**Quiero** eliminar cascadas de `isinstance()`  
**Para** mejorar mantenibilidad y extensibilidad

#### Criterios de Aceptación

- [x] Registrar servicios por tipo de material utilizando un Singleton.
- [x] Centralizar cálculo de días de préstamo.
- [x] Delegar la generación de descripciones específicas por material.
- [x] Lanzar error si no existe servicio registrado para un tipo.

#### Detalles Técnicos

**Clase**: `MaterialServiceRegistry` (`biblioteca_digital/servicios/materiales/material_service_registry.py`)

**Uso**:
```python
registry = MaterialServiceRegistry.get_instance()
dias_libro = registry.obtener_dias_prestamo(libro)
descripcion_ebook = registry.obtener_descripcion(ebook)
```

**Trazabilidad**: `main.py` líneas 156-168.

---

## Resumen de Cobertura Funcional

### Historias de Usuario

| ID | Historia | Completada | Prioridad |
|----|----------|------------|-----------|
| US-001 | Registrar Usuario | ✅ | Alta |
| US-002 | Prestar Material | ✅ | Alta |
| US-003 | Devolver y Calcular Multas | ✅ | Alta |
| US-004 | Reservar Material | ✅ | Media |
| US-005 | Recibir Notificaciones | ✅ | Media |

### Historias Técnicas (Patrones)

| ID | Patrón | Completada | Componente |
|----|--------|------------|------------|
| US-TECH-001 | Singleton | ✅ | UsuarioManager |
| US-TECH-002 | Factory Method | ✅ | MaterialFactory |
| US-TECH-003 | Observer | ✅ | NotificacionService |
| US-TECH-004 | Strategy | ✅ | MultaStrategy |
| US-TECH-005 | Registry | ✅ | MaterialServiceRegistry |

### Totales

- **Historias de Usuario**: 5/5 (100%)
- **Historias Técnicas**: 5/5 (100%)
- **Patrones Implementados**: 5/5 (100%)
- **Cobertura Total**: 100%

---

**Última actualización**: Noviembre 2025  
**Estado**: COMPLETO  
**Cobertura funcional**: 100%

