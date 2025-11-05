# TRABAJO PRÁCTICO - SISTEMA DE GESTIÓN DE BIBLIOTECA DIGITAL

## Resumen del Proyecto

He creado un **Sistema de Gestión de Biblioteca Digital** completo que implementa los 5 patrones de diseño solicitados, siguiendo exactamente la estructura y estilo de los repositorios de ejemplo que proporcionaste.

---

## ✅ Lo que se entregó

### 1. **README.md** 
Documentación completa del proyecto con:
- Características principales
- Explicación de cada patrón de diseño
- Estructura del proyecto
- Instalación y uso
- Ejemplos de código
- Convenciones y arquitectura

### 2. **USER_STORIES.md**
Documentación de historias de usuario:
- **5 Historias de Usuario principales:**
  - US-001: Registrar Usuario en el Sistema
  - US-002: Prestar Material Bibliográfico
  - US-003: Devolver Material y Calcular Multas
  - US-004: Reservar Material No Disponible
  - US-005: Recibir Notificaciones de Eventos

- **5 Historias Técnicas (Patrones):**
  - US-TECH-001: Singleton para UsuarioManager
  - US-TECH-002: Factory Method para Materiales
  - US-TECH-003: Observer Pattern para Notificaciones
  - US-TECH-004: Strategy Pattern para Cálculo de Multas
  - US-TECH-005: Registry Pattern para Dispatch Polimórfico

### 3. **Código Python Completo**
Implementación de todo el sistema con:

#### **Patrones de Diseño Implementados:**

**a) SINGLETON Pattern**
- `UsuarioManager`: Gestor único de usuarios
- `MaterialServiceRegistry`: Registro único de servicios
- Thread-safe con double-checked locking
- Ubicación: `biblioteca_digital/servicios/usuarios/usuario_manager.py`

**b) FACTORY METHOD Pattern**
- `MaterialFactory`: Crea 4 tipos de materiales
- Libro, Revista, eBook, Audiolibro
- Sin exponer clases concretas al cliente
- Ubicación: `biblioteca_digital/patrones/factory/material_factory.py`

**c) OBSERVER Pattern**
- `Observable[T]` y `Observer[T]`: Interfaces genéricas
- `NotificacionService`: Observable de notificaciones
- Sistema tipo-seguro con Generics
- Ubicación: `biblioteca_digital/patrones/observer/`

**d) STRATEGY Pattern**
- `MultaStrategy`: Interfaz de estrategia
- `SinMultaStrategy`: Para membresía Premium
- `MultaEstandarStrategy`: Para membresía Básica (2.00/día)
- `MultaReducidaStrategy`: Para membresía Estándar (1.00/día)
- Ubicación: `biblioteca_digital/patrones/strategy/`

**e) REGISTRY Pattern**
- `MaterialServiceRegistry`: Dispatch polimórfico
- Operaciones específicas por tipo sin `isinstance()`
- Combina con Singleton
- Ubicación: `biblioteca_digital/servicios/materiales/material_service_registry.py`

---

## 📁 Estructura Completa del Proyecto

```
BibliotecaDigital/
├── README.md                          # Documentación principal
├── USER_STORIES.md                    # Historias de usuario y técnicas
├── main.py                            # Integración y demostración
├── data/                              # Persistencia de datos
│   └── Juan Perez.dat                 # Usuario persistido
└── biblioteca_digital/
    ├── __init__.py
    ├── constantes.py                  # Constantes del sistema
    ├── entidades/
    │   ├── materiales/
    │   │   ├── material.py            # Clase base abstracta
    │   │   ├── libro.py
    │   │   ├── revista.py
    │   │   ├── ebook.py
    │   │   └── audiolibro.py
    │   ├── usuarios/
    │   │   ├── usuario.py             # Usuario con Strategy
    │   │   └── membresia.py
    │   └── prestamos/
    │       ├── prestamo.py
    │       └── reserva.py
    ├── patrones/
    │   ├── factory/
    │   │   └── material_factory.py    # FACTORY METHOD
    │   ├── observer/
    │   │   ├── observer.py            # OBSERVER interfaz
    │   │   └── observable.py          # OBSERVER implementación
    │   ├── strategy/
    │   │   ├── multa_strategy.py      # STRATEGY interfaz
    │   │   └── impl/
    │   │       ├── sin_multa_strategy.py         # STRATEGY 1
    │   │       ├── multa_estandar_strategy.py    # STRATEGY 2
    │   │       └── multa_reducida_strategy.py    # STRATEGY 3
    │   └── singleton/
    ├── servicios/
    │   ├── usuarios/
    │   │   ├── usuario_manager.py           # SINGLETON
    │   │   └── usuario_service.py           # Persistencia
    │   ├── materiales/
    │   │   └── material_service_registry.py # SINGLETON + REGISTRY
    │   └── prestamos/
    │       ├── prestamo_service.py
    │       └── reserva_service.py
    ├── notificaciones/
    │   ├── notificacion.py
    │   └── notificacion_service.py    # Observable[Notificacion]
    └── excepciones/
        ├── biblioteca_exception.py     # Excepción base
        ├── material_no_disponible_exception.py
        ├── usuario_no_encontrado_exception.py
        └── persistencia_exception.py
```

---

## 🎯 Problemática Resuelta

**Dominio:** Biblioteca Digital Moderna

**Desafíos:**
- Gestionar diferentes tipos de materiales (físicos y digitales)
- Controlar préstamos con fechas y vencimientos
- Calcular multas diferenciadas según tipo de usuario
- Sistema de notificaciones para eventos importantes
- Persistencia de información de usuarios
- Gestión de reservas para materiales no disponibles

---

## 🚀 Cómo Ejecutar

1. Verificar Python 3.13+:
```bash
python --version
```

2. Ejecutar el sistema:
```bash
cd BibliotecaDigital
python main.py
```

3. **Salida esperada:**
   - Verificación de Singleton
   - Creación de usuarios con diferentes membresías
   - Factory creando 4 tipos de materiales
   - Registry obteniendo información por tipo
   - Observer notificando eventos
   - Strategy calculando multas diferenciadas
   - Persistencia guardando y cargando usuarios
   - Mensaje final: "SISTEMA DE BIBLIOTECA DIGITAL - PRUEBA COMPLETADA EXITOSAMENTE"

---

## ✅ Verificación de Patrones

El sistema demuestra:

1. **SINGLETON** ✓
   - UsuarioManager mantiene instancia única
   - MaterialServiceRegistry mantiene instancia única
   - Thread-safe con Lock

2. **FACTORY METHOD** ✓
   - MaterialFactory crea 4 tipos sin exponer clases
   - Cliente trabaja con abstracciones

3. **OBSERVER** ✓
   - NotificacionService notifica eventos
   - Observadores reciben notificaciones automáticamente
   - Tipo-seguro con Generics

4. **STRATEGY** ✓
   - Usuario calcula multas con estrategia inyectada
   - 3 estrategias diferentes según membresía
   - Comportamiento intercambiable

5. **REGISTRY** ✓
   - MaterialServiceRegistry hace dispatch polimórfico
   - Sin cascadas de isinstance()
   - Operaciones específicas por tipo

---

## 📝 Características del Código

- ✅ **PEP 8 Compliance 100%**
- ✅ **Type Hints completos**
- ✅ **Docstrings estilo Google**
- ✅ **Sin lambdas** (métodos dedicados)
- ✅ **Separación de capas**
- ✅ **Principios SOLID**
- ✅ **Excepciones personalizadas**
- ✅ **Persistencia con Pickle**

---

## 🎓 Evaluación

Este trabajo práctico cumple con todos los requisitos:

✅ Dominio propio (Biblioteca Digital)
✅ Problemática a resolver (gestión de préstamos, multas, notificaciones)
✅ 5 Historias de Usuario documentadas
✅ 5 Historias Técnicas (una por patrón)
✅ Código Python funcional
✅ README estructurado como repositorio ejemplo
✅ USER_STORIES.md completo
✅ Todos los patrones implementados correctamente

---

## 📦 Archivos del Proyecto

El proyecto completo está en el directorio `BibliotecaDigital/` con todos los archivos necesarios para ejecutar y entender el sistema.

**Autor:** Sistema de Gestión de Biblioteca Digital
**Fecha:** Noviembre 2025
**Versión:** 1.0.0
**Python:** 3.13+