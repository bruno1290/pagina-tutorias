# 📦 Manual de Migración: Tutorías La Obra UC

Para que otra IA (como Cursor, VS Code Copilot o ChatGPT) logre los mismos resultados de alta fidelidad, debe seguir este **Sistemas de Instrucciones**. Todo lo que hemos logrado se basa en la combinación de un **Motor de Pasos (STP)** y un **Diseño Visual Sobrio**.

---

## 1. El "Master Prompt" para tu nueva IA
*Copia y pega esto como instrucciones de sistema o contexto inicial en VS Code:*

> Eres un experto en desarrollo Web Educativo y Pedagogía. Tu misión es generar módulos interactivos HTML5 para niños de 4to básico.
> 
> **Reglas de Oro:**
> 1. **Tecnología:** Usa un script de Python que genere un único archivo HTML autocontenido (CSS y JS embebidos).
> 2. **Motor Anti-Spoiler (STP):** Todos los elementos revelables deben tener la clase `class="stp"`. El botón "Siguiente" debe revelar el primer `.stp` oculto antes de pasar a la siguiente slide.
> 3. **Estilo Visual:** Usa la fuente 'Nunito'. Colores base `#1C4A82` (navy) y fondo `#f5f6f8`. Usa bordes redondeados (20px) y paleta de rellenos color pastel.
> 4. **Pedagogía de Bloques:** No enseñes a contar con los dedos. Usa SVGs que representen Bloques Base 10 (Cubos = 1, Barras = 10, Placas = 100).
> 5. **Orden Matemático:** Todo cálculo vertical se revela de DERECHA a IZQUIERDA (Unidad -> Decena -> Centena).
> 6. **Secciones Obligatorias:** Portada Animada -> Concepto -> Abre tu cuaderno (retos) -> Problema de la vida real -> Ticket de Salida.

---

## 2. Template Base del Generador (Python)
*Usa este archivo como base para los nuevos módulos de Suma y Resta:*

```python
import os

def generate_module(filename, title, slides_content):
    css = """
    :root { --base: #1C4A82; --bg: #f5f6f8; --tx: #333; }
    body { font-family: 'Nunito', sans-serif; background: var(--bg); color: var(--tx); overflow: hidden; height: 100vh; }
    .dk { position: relative; width: 100%; height: 100%; max-width: 1000px; margin: 0 auto; }
    .sl { position: absolute; inset: 0; display: flex; flex-direction: column; align-items: center; padding: 40px; opacity: 0; transform: scale(.96); transition: all .4s; pointer-events: none; }
    .sl.on { opacity: 1; transform: scale(1); pointer-events: auto; z-index: 10; }
    .head-title { background: var(--base); color: white; padding: 10px 40px; font-size: 32px; font-weight: 900; border-radius: 12px; margin-bottom: 25px; }
    .stp { opacity: 0; transform: translateY(20px); transition: 0.4s; }
    .stp.shwn { opacity: 1; transform: translateY(0); }
    /* ... añadir más CSS del generator_mult_1.py ... */
    """
    
    js = """
    let c = 0; const S = document.querySelectorAll('.sl');
    function go(d) {
        const h = S[c].querySelectorAll('.stp:not(.shwn)');
        if(d>0 && h.length > 0) { h[0].classList.add('shwn'); return; }
        c = Math.min(Math.max(0, c + d), S.length - 1);
        updateUI();
    }
    /* ... añadir lógica de navegación de generator_mult_1.py ... */
    """
    
    # Renderizar slides y guardar archivo HTML
    # ...
```

---

## 3. Hoja de Ruta para Suma y Resta
Para los 3 módulos que faltan, sigue este guión técnico:

### 🍎 Suma y Resta 1: Fundamentos
- **Visual:** Usa muchos `<svg>` de barras azules y cubos rojos.
- **Key Step:** Slide de "Propiedad Conmutativa" (3+5 = 5+3).
- **Desafío:** Sumar descomponiendo (14 + 5 -> 10 + 4 + 5).

### 🏛️ Suma y Resta 2: Algoritmo y Centenas
- **Visual:** Introduce la "Placa" de 100 (cuadrado grande verde).
- **Key Step:** Suma vertical con rejilla (CSS Grid). Revelar el resultado de la columna unidades, luego la reserva (si hay), luego decenas.
- **Teoría:** Partes de la resta (Minuendo - Sustraendo = Diferencia).

### ⚔️ Suma y Resta 3: El Canje (Desagrupación)
- **Visual:** Animación de "quitar" unidades. Si no alcanza, mostrar cómo una barra de 10 se convierte en 10 cubitos.
- **Key Step:** Resta paso a paso tachando el número de la decena (ej: el 4 pasa a ser 3 y la unidad recibe +10).

---

## 4. Integración en `index.html`
Una vez que generes los HTMLs (ej: `suma1.html`), agrégalos al objeto `MODULES` en tu `index.html` principal:

```javascript
{
    id: 7, 
    cat: 'num', 
    title: 'Suma y Resta 1', 
    dur: '45 min',
    htmlSlide: 'clases/suma_resta/suma_resta_1.html',
    ticket: { ... }
}
```

> [!TIP]
> **Conserva siempre el `generator_mult_1.py`**. Es tu "piedra rosetta". Cualquier IA que lea ese código entenderá inmediatamente cómo replicar la estética y la lógica de navegación.

¡Mucha suerte, Bruno! Ha sido un placer construir esta plataforma contigo. 🚀✨
