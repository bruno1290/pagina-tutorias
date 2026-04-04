# Implementación de Módulos: Suma y Resta 1, 2 y 3

El objetivo es crear tres módulos interactivos HTML5 de alta fidelidad para la enseñanza de la Suma y la Resta, siguiendo estrictamente el estándar pedagógico y visual (SKILL) de Tutorías La Obra UC. Para ello, nos basaremos en los conceptos presentados en las presentaciones de la carpeta "Conectado aprendo" y utilizaremos una arquitectura basada en generadores Python (`generator_suma_1.py`, `generator_suma_2.py`, `generator_suma_3.py`) para orquestar los pasos y el HTML final.

## User Review Required

> [!IMPORTANT]
> Revisa la estructura propuesta para los 3 módulos. Confirma si la progresión pedagógica y la distribución de contenidos corresponde a lo que buscas. Si estás de acuerdo, procederé con la creación paso a paso (primero generador 1, luego generador 2, luego generador 3) en la carpeta `clases/suma_resta/`.

## Proposed Changes

La estrategia de estructuración se dividirá en tres módulos de aproximadamente 30 slides o "pasos" cada uno, garantizando el uso de la lógica "cero spoilers" (botón `Siguiente` que revela progresivamente) y enfocándose en interactividad visual (bloques base 10) en vez de conteo con los dedos.

---

### Módulo 1: Fundamentos de la Suma y Bloques
**Directorio Destino:** `clases/suma_resta/suma_resta_1.html`
**Enfoque:** Conceptos básicos, propiedades, bloques y sumas iniciales.
- **Portada:** Título llamativo, subtítulo motivador, animación de "bounce".
- **Concepto (Elementos y Propiedades):** Qué es un sumando, qué es el total. Propiedad conmutativa (ej: cambiar el orden de los sumandos no altera el total).
- **Herramienta Visual (Bloques):** Introducir los números como bloques (ej. 1 cubo = unidad, 1 barra = decena). Explicación repetida: "¡No usemos los dedos, usemos bloques y nuestra mente!".
- **Suma 1 dígito + 1 dígito:** Ejercicios visuales con bloques en la pantalla, paso a paso utilizando `.stp`.
- **Suma 1 dígito + 2 dígitos:** Representar el de 2 dígitos como barras (decenas) y cubos (unidades), añadir las unidades extra, recalcular, mostrar total.
- **Descomposición:** Romper números grandes para sumar fácil. Ejemplo: 15 + 4 -> (10 + 5) + 4 -> 10 + 9 = 19.
- **"Abre tu cuaderno":** 4 dilemas interactivos de suma simple basados en problemas reales.
- **Cierre/Ticket:** Slide de felicitación.

---

### Módulo 2: Suma de 3 Dígitos y Fundamentos de Resta
**Directorio Destino:** `clases/suma_resta/suma_resta_2.html`
**Enfoque:** Transición hacia sumas mayores (algoritmos verticales) e introducción a la resta.
- **Recordatorio:** Breve recapitulación de bloques. Introducción del bloque "Placa" (Centena = 100).
- **Suma de 3 dígitos (Bloques y Columna):** Unir representación de placas, barras y cubos con el cálculo vertical de la suma. Enfatizar la suma por columnas de Derecha a Izquierda. Explicación dinámica de "Acarreo" o "Reserva".
- **Concepto (Introducción a la Resta):** Qué es la resta, diferencias entre quitar y comparar.
- **Elementos de la Resta:** Minuendo, Sustraendo, Diferencia o Resto.
- **Propiedades de la Resta:** Aclarar que la resta NO es conmutativa.
- **"Abre tu cuaderno":** Sumas verticales de 3 dígitos con y sin reserva, y preguntas conceptuales de resta.
- **Cierre/Ticket:** Slide de felicitación y preparativos para el súper jefe de la resta.

---

### Módulo 3: Dominando la Resta (Desagrupación)
**Directorio Destino:** `clases/suma_resta/suma_resta_3.html`
**Enfoque:** Restas con reserva (Canje o Desagrupación) de 2 y 3 dígitos.
- **Resta 1 y 2 dígitos:** Ejercicios simples de quitar decenas y unidades.
- **El desafío del Canje (Desagrupación en unidades):** ¿Qué pasa si las unidades del minuendo son menores que las del sustraendo? Explicar con animación visual el "romper" una barra de decena en 10 unidades sueltas.
- **Práctica Guiada (Resta vertical de 2 dígitos):** Resolver paso a paso (de derecha a izquierda) restas como 42 - 18, marcando el canje en rojo y tachando el número.
- **Resta de 3 dígitos (Desagrupación doble):** Aplicar la misma lógica a las centenas. (Ej. romper una placa de 100 en 10 barras de 10).
- **"Abre tu cuaderno":** Problemas situacionales con restas pesadas.
- **Cierre/Ticket:** Certificación de "Maestro de las Operaciones".

## Open Questions

- ¿Debería omitir por completo menciones de "Llevar la reserva" prefiriendo palabras más modernas como "Reagrupar" o "Desagrupar" (para restas)?
- ¿Mantengo la estructura de crear los HTML mediante los scripts de Python locales (ej. `generator_suma_1.py`) y dejarlos en la carpeta `SLIDES` para que luego generen el HTML en `clases/suma_resta/` al ejecutarlos localmente?

## Verification Plan

- Ejecutaré el script Python de cada módulo.
- Revisaré visualmente cada HTML generado comprobando el funcionamiento de los botones "Continuar" (`.stp`), confirmando que las cuadrículas de sumas/restas verticales no se desconfiguren (CSS Grid).
- Al finalizar, actualizaré las referencias en el documento `walkthrough.md` para confirmarlo con el usuario.
