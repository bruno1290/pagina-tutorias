---
name: Estándar Clases Tutorías
description: Guía técnica y pedagógica para generar módulos interactivos HTML5 de alta fidelidad, basados en Python generador, estilo visual sobrio azul/pastel y motor de pasos (anti-spoilers).
---

# Estándar Clases Tutorías (v1.0) 🎓

Este Skill define el "blueprint" para transformar presentaciones estáticas (PPT) en experiencias interactivas modernas y pedagógicas. Sigue estas instrucciones para cada nueva materia.

## 1. Análisis de Contenido (PPT Protocol)
- **Modularización:** Si un PPT es denso (>40 slides), divídelo en temas lógicos. Ejemplo: Fracciones -> Anatomía, Comparación, Operaciones.
- **Simplificación:** Extrae el concepto medular. Elimina texto excesivo. Prefiere una imagen/SVG grande con poco texto.
- **Tono:** Mantener un vínculo cálido. Evitar tecnicismos innecesarios ("aritmética") o matices negativos ("trampa").

## 2. Diseño Visual (Visual System)
- **Base CSS:**
    ```css
    :root {
        --base: #1C4A82;   /* Azul Marino Principal */
        --bg: #f5f6f8;     /* Fondo sutil */
        --tx: #333;        /* Texto */
    }
    ```
- **Paleta de Rellenos (SVGs/Pastels):**
    - `#FF9D9D` (Rosa), `#9DDEFF` (Celeste), `#9DE3BD` (Verde), `#FFE082` (Amarillo), `#FFB74D` (Naranja), `#E1BEE7` (Morado).
- **Componentes:**
    - `.pnl-border`: Contenedor blanco con borde de 4px color `--base`, radio de 20px.
    - `.head-title`: Pastilla/Tira de 10px 40px con fondo `--base`, texto blanco, peso 900.
    - **Tipografía:** Nunito (Google Fonts).

## 3. Dinámica del Módulo (Pedagogical Flow)
- **Secuencia:** Intro -> Concepto -> "Abre tu cuaderno" -> Práctica Interactiva -> Problemas Situacionales -> Resumen -> Cierre.
- **Cero Spoilers (Lógica STP):**
    - Todo elemento revelable debe llevar la clase `.stp`.
    - El script JS debe detectar si hay elementos `.stp:not(.shwn)` antes de cambiar de slide.
    - **Abre tu cuaderno:** Presentar el dilema, indicar resolución en papel, y revelar la respuesta con un click.

## 4. Motor de Generación (Python Master)
- **Template:** Usar una función `generate_html()` que encapsule el CSS y JS.
- **Modularidad:** Utilizar una lista de slides `slides.append(f'<div class="sl">{content}</div>')`.
- **SVGs y Animaciones:** Crear funciones auxiliares en Python que generen el código `<svg>` dinámicamente.
- **UX de Algoritmos Complejos:** Cuando se enseñen cálculos matemáticos en vertical o paso a paso exhaustivo:
    - Usar **CSS Grid** (`display: grid`) manipulando el DOM order en HTML o `grid-column`/`grid-row` para asegurar exactitud matemática.
    - Evitar el uso de `position: absolute` encima de los números, crea solapamiento. Utilizar un **Panel Lateral de Explicación** que cambie secuencialmente sincronizado con el motor `.stp`.
    - Orden matemático estricto: Todo cálculo vertical DEBE ser presentado vía motor de pasos estrictamente de Derecha a Izquierda (ej, calcular Unidad, mostrar Reserva de Unidad, calcular Decena).

## 5. Checklist de Verificación
- [ ] ¿Hay al menos 3 problemas de la vida real con emojis?
- [ ] ¿Todos los colores de relleno son pasteles claros?
- [ ] ¿Los títulos de las slides están en el formato `.head-title`?
- [ ] ¿El motor de pasos evita ver el resultado de "Abre tu cuaderno" de inmediato?
- [ ] ¿Se eliminaron frases "infantiles" o complejas?
