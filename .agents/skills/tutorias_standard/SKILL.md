---
name: Estándar Global Clases La Obra UC v3.0
description: Guía de diseño pedagógico y técnico universal para TODAS las clases de la plataforma (Suma, Resta, Multiplicación, Fracciones, Geometría, Ecuaciones, etc.). Esta es la versión definitiva — ignorar cualquier versión anterior.
---

> [!IMPORTANT]
> **REGLA CRÍTICA PARA LA IA:** Cuando el usuario pide analizar o editar una clase, siempre leer el **archivo HTML que `index.html` referencia** en el campo `htmlSlide` (ej: `clases/multiplicacion/multiplicaciones_1.html`). NUNCA analizar los scripts Python generadores como fuente de verdad de lo que el usuario ve. Los HTML en `clases/` son los archivos reales en producción.

# 🎓 Estándar Global "La Obra Premium" v3.0

**Aplica a:** Todas las presentaciones de todas las áreas de la plataforma.
**No aplica solo a Suma y Resta.** Fracciones, Multiplicación, Geometría, etc. deben seguir exactamente este mismo flujo y estilo.

---

## 1. Filosofía Pedagógica

Cada clase debe lograr tres cosas:
1. **Entender** el concepto visualmente (nunca solo abstracto).
2. **Practicar** de forma progresiva: del mecánico → al aplicado → al creativo.
3. **Sorprender** con al menos un ejercicio que no parezca matemática (ObraCraft, acertijo, rompecabezas).

---

## 2. Estructura Obligatoria de Cada Presentación

```
[1] Portada
[2-12] Explicación visual + ejemplos resueltos paso a paso
[13-14] Ejercicios propuestos (cuaderno) + respuestas
[15-17] 2-3 Problemas situacionales (vida real)
[18-19] Desafío Supremo (incluye al menos 1 ObraCraft)
[20-21] Resumen + Cierre
```

**Máximo 25-30 slides.** No hay que llegar a 30 si el contenido no lo requiere.

---

## 3. Detalle de Cada Bloque

### 🟢 Bloque 1: Portada (1 slide)
- Título claro del tema (ej: "Suma hasta 3 dígitos", "Fracciones equivalentes").
- Subtítulo motivador corto.
- Un emoji representativo.

### 🟢 Bloque 2: Explicación Visual (8-12 slides)
- Ir de lo concreto a lo abstracto. Ej: dibujar el concepto → representarlo con bloques/figuras → escribir la fórmula.
- Cada slide debe tener **1 idea central**, no 3.
- Usar ejemplos **completamente resueltos** paso a paso (nunca dejar a medias).
- Cuando hay un algoritmo (ej: suma en columna, división larga), mostrarlo con la línea horizontal debajo del último número antes del resultado.
- Para Matemáticas de Números: usar siempre los colores posicionales:
  - 🟡 Unidades → `#FFE082`
  - 🔵 Decenas → `#9DDEFF`
  - 🟢 Centenas → `#9DE3BD`
  - 🟣 Unidades de Mil → `#E1BEE7`
- Intercalar 1-2 slides de **"Abre tu cuaderno"** (ejercicio resuelto con respuesta oculta `.stp`).
- Incluir al menos 1 slide **interactivo con botones** (tipo quiz de opción múltiple) para verificar comprensión.

### 🟢 Bloque 3: Ejercicios Propuestos (2 slides)
- **Slide 1:** Cuadrícula 2×3 con **6 ejercicios** variados. Incluir:
  - 2 ejercicios mecánicos (para fijar el procedimiento).
  - 2 ejercicios aplicados (contexto o dato extra).
  - 2 ejercicios con un giro creativo o de análisis.
- **Slide 2:** Respuestas. Formato checklist, solo el resultado (sin desarrollo). El alumno compara con su cuaderno.

### 🟢 Bloque 4: Problemas Situacionales (2-3 slides)
- Situaciones de la vida real: almacén, viajes, deportes, comida, dinero, etc.
- Cada slide = 1 problema. Debe tener:
  - Enunciado con contexto.
  - Respuesta completa oculta (`.stp`) que se revela al avanzar.
- Usar emojis como "ancla visual" del contexto.

### 🟢 Bloque 5: Desafío Supremo (2 slides)
- Son los más difíciles y creativos de la clase. Se ven **al final**.
- Título fijo: **"Desafío Supremo"** (fondo degradado morado → rosa fucsia).
- Tipos de desafío permitidos (ser variado entre presentaciones):
  - 🔐 Acertijo con pistas (El Cofre Secreto, El Ticket Roto).
  - ⛏️ **ObraCraft** (mundo virtual tipo Minecraft). Mínimo 1 por presentación.
  - 🔢 Número oculto / dígito faltante.
  - ⏳ Encadenado / "viaje en el tiempo" (resolver por partes).
  - 🎯 Juego del Blanco (llegar a un número exacto con operaciones dadas).
- **ObraCraft:** Es un ejercicio puntual ambientado en un mundo virtual mágico (portales, dragones, minerales, pociones, etc.). No es el hilo narrativo de toda la clase, sino un "nivel secreto" al llegar al final.

### 🟢 Bloque 6: Cierre (2 slides)
- **Resumen:** 3-4 ideas clave con viñetas.
- **Felicitación final:** Mensaje de cierre + emoji grande + animación.

---

## 4. Ticket de Salida (en `index.html`)

- **5 preguntas de opción múltiple** por módulo.
- Las preguntas deben ser **nuevas** (no repetir los ejemplos de la clase).
- Nivel: intermedio/aplicado. Nunca trivial (ej: "¿cuánto es 1+1?").
- Al menos 1 pregunta debe evaluar comprensión conceptual, no solo cálculo.
- Al menos 1 pregunta debe ser una aplicación de la vida real.
- Cada pregunta tiene 4 opciones y una explicación de la respuesta correcta.

---

## 5. Reglas de Diseño UI (Todas las Clases)

| Elemento | Especificación |
|---|---|
| Tipografía | Nunito (Google Fonts) |
| Fondo general | `#f5f6f8` (gris muy claro) |
| Color principal | `#1C4A82` (azul marino) |
| Bordes | Redondeados, 16-20px |
| Máximo slides | 30 (ideal: 22-26) |
| Anti-spoilers | Clase `.stp` en todo elemento revelable |
| Navegación | Barra deslizadora `<input type="range">` + flechas |
| Portadas desafío | Degradado `#9333EA → #db2777` |

---

## 6. Reglas de Contenido (Calidad)

- ❌ No repetir el mismo tipo de ejercicio más de 2 veces seguidas.
- ❌ No usar "flash cards" de opción múltiple como relleno.
- ✅ Cada ejercicio debe enseñar algo distinto o aplicar de forma distinta.
- ✅ Variar los contextos: no todos de "la tienda" ni todos de "el almacén".
- ✅ Los nombres en los problemas deben ser chilenos/cercanos (Lucas, Sofía, Valentina, etc.).
- ✅ ObraCraft puede incluir: minar minerales, fabricar pociones, construir fortalezas, cruzar portales, derrotar enemigos.

---

## 7. Archivos de Referencia Técnica

| Archivo | Propósito |
|---|---|
| `scripts/clases/generator_suma_resta.py` | Generador modelo más completo (CSS+JS+Componentes) |
| `scripts/clases/build_4B_mod1_suma.py` | Ejemplo maestro de clase bien estructurada |
| `scripts/clases/template_obracraft.py` | Plantilla base para nuevas clases |

Al crear un generador para un nuevo tema (ej: `generator_fracciones.py`), **heredar el CSS y JS** del generador de Suma y Resta como base.
