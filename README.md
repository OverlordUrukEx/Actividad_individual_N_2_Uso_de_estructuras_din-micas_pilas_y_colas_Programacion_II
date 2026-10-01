# Actividad Individual N° 2: Pilas y Colas - Programación II

**Institución:** Universidad de Manizales
**Programa:** Ingeniería de Sistemas
**Estudiante:** Johan Marcelo Rojas Cruz

---

## 📋 Descripción del Proyecto

Sistema de consola en Python que emula un **consultorio odontológico** con dos estructuras dinámicas:

1. **Pila de urgencias:** clientes con cita de **Extracción** y prioridad **Urgente**, ordenados por fecha (la más cercana primero). Genera el informe para llamarlos prioritariamente.
2. **Cola de atención diaria:** agenda del día atendida en estricto orden FIFO (orden de registro).

## ⚙️ Estructura (Arquitectura Modular)

- `main.py` — punto de entrada.
- `models/cita.py` — entidad `Cita` (`@dataclass`) y constantes de dominio.
- `core/pila.py` — `Pila` LIFO con nodos.
- `core/cola.py` — `Cola` FIFO con nodos.
- `core/engine.py` — filtros de negocio, construcción de pila/cola e informe (`listar_urgentes`).
- `core/validators.py` — validación centralizada de todas las entradas del usuario.
- `views/ui.py` — menús de consola.

## ✅ Principios aplicados

- **DRY:** una única capa de validadores y captura reutilizada.
- **KISS:** solo biblioteca estándar, menús simples.
- **SOLID:** responsabilidad única por módulo (S), clases pequeñas (I), interfaces consistentes (L), extensión sin modificar (O), `Engine` desacoplado de la UI (D).
- **Clean Code:** nombres descriptivos, funciones pequeñas, comentarios de regla de negocio, sin conversiones innecesarias.

## 🛡️ Validaciones implementadas

- Nombre: mínimo 3 letras, sin números ni símbolos.
- **Cédula: solo dígitos, 7 a 10 caracteres** (no se permiten letras).
- Tipo de atención y prioridad: valores del dominio (tolerantes a tildes y mayúsculas).
- Fecha: formato DD/MM/AAAA.
- Cantidad: entero 1–32, **forzada a 1 en Limpieza y Diagnóstico**.
- Opciones de menú dentro de rango; respuestas `s/n`.
- No duplicar cédula en la misma fecha; control de pila/cola vacías.

## 🚀 Ejecución

```bash
python3 main.py
```

Requisito: Python 3.8+.
