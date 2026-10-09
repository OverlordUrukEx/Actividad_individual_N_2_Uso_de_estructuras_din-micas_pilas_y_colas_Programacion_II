# Actividad Individual N° 2: Uso de estructuras dinámicas (Cola) - Programación II

**Institución:** Universidad de Manizales
**Programa:** Ingeniería de Sistemas
**Estudiante:** Johan Marcelo Rojas Cruz

---

## 📋 Descripción del Proyecto

Sistema de consola en Python que emula un **consultorio odontológico** usando la estructura dinámica **Cola** (`collections.deque`) en dos escenarios:

1. **Cola de urgencias:** clientes con cita de **Extracción** y prioridad **Urgente**, encolados por fecha (la más cercana primero). Genera el informe para llamarlos prioritariamente.
2. **Cola de atención diaria:** agenda del día atendida en estricto orden FIFO (orden de registro).

## ⚙️ Estructura (Arquitectura Modular)

- `main.py` — punto de entrada.
- `models/cita.py` — entidad `Cita` (`@dataclass`) y constantes de dominio.
- `core/cola.py` — `Cola` FIFO sobre `collections.deque` (sin nodos enlazados).
- `core/engine.py` — filtros de negocio, construcción de las colas (urgencias y del día) e informe (`listar_urgentes`).
- `core/validators.py` — validación centralizada de todas las entradas del usuario.
- `views/ui.py` — menús de consola.

## ✅ Principios aplicados

- **Estructura dinámica:** `Cola` implementada con `collections.deque`, evitando nodos enlazados manuales y listas usadas como cola (según la observación del diseño).
- **DRY:** una única capa de validadores y captura reutilizada.
- **KISS:** solo biblioteca estándar, menús simples.
- **SOLID:** responsabilidad única por módulo (S), clases pequeñas (I), interfaces consistentes (L), extensión sin modificar (O), `Engine` desacoplado de la UI (D).
- **Clean Code:** nombres descriptivos, funciones pequeñas, comentarios de regla de negocio, sin conversiones innecesarias.

## 🧠 ¿Cuándo se usa una Cola?

Una **Cola (FIFO)** se usa cuando los elementos deben procesarse **en el mismo orden en que llegaron**: el primero que entra es el primero que sale (`encolar` al final, `desencolar` por el frente). En este programa:

- **Cola de urgencias:** las citas de Extracción + Urgente se encolan de la fecha más cercana a la más lejana, de modo que se llaman y atienden primero las más próximas.
- **Cola de atención diaria:** los clientes del día se encolan según su registro y se atienden en ese estricto orden.

Se implementa con `collections.deque` porque permite insertar y extraer en ambos extremos en tiempo O(1), sin la complejidad de los nodos enlazados manuales. Al atender una cita, se marca como `atendida` y deja de aparecer en la agenda y en el informe.

## 🛡️ Validaciones implementadas

- Nombre: mínimo 3 letras, sin números ni símbolos.
- **Cédula: solo dígitos, 7 a 10 caracteres** (no se permiten letras).
- Tipo de atención y prioridad: valores del dominio (tolerantes a tildes y mayúsculas).
- Fecha: formato DD/MM/AAAA; **nunca anterior a hoy** al registrar una cita y al generar/atender la agenda (solo día actual o futuros; ver fechas anteriores sería un informe histórico no contemplado).
- Cantidad: entero 1–32, **forzada a 1 en Limpieza y Diagnóstico**.
- Opciones de menú dentro de rango; respuestas `s/n`.
- No duplicar cédula en la misma fecha; control de cola vacía y de citas ya atendidas.

## 🚀 Ejecución

```bash
python3 main.py
```

Requisito: Python 3.8+.
