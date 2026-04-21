"""
Genera el MÓDULO 3B-4: "Multiplicación: Grupos Iguales y Tablas" — 30 slides
Curso: 3° Básico | OA8 (Multiplicación — 37% logro, CRÍTICO)
Enfoque: Suma repetida → multiplicación → tablas 2, 5, 10 → tablas 3, 4
         Propiedad conmutativa → Problemas situacionales chilenos
"""
from __future__ import annotations
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import generator_suma_resta as G

OUT = pathlib.Path("/Users/brunonattino/Desktop/PAGINA TUTORIAS/clases/tercero")


def module() -> str:
    s: list[str] = []

    # 1 — Intro
    s.append(G.intro_slide(
        "¡Multiplicación! ✖️",
        "Descubrimos que multiplicar es sumar grupos iguales de forma rápida.",
        "🔢"))

    # 2 — ¿Qué es multiplicar?
    s.append(G.slide("""
        <div class="head-title">¿Qué es multiplicar?</div>
        <p class="sub-text">Multiplicar es <b class="hl">sumar el mismo número varias veces</b>.</p>
        <div class="two-col">
            <div class="pnl-border" style="text-align:center;">
                <div style="font-size:40px;">🍎🍎🍎 🍎🍎🍎 🍎🍎🍎</div>
                <div class="stp" style="font-size:22px; margin-top:10px;">3 grupos de 3 manzanas</div>
                <div class="stp" style="font-size:22px;">3 + 3 + 3 = 9</div>
                <div class="stp math-eq">3 × 3 = 9</div>
            </div>
            <div class="warn-card stp">
                <b>¡Es más rápido!</b><br>En vez de sumar 3 + 3 + 3,<br>escribimos directamente <b>3 × 3 = 9</b>.
            </div>
        </div>"""))

    # 3 — Suma repetida → multiplicación
    s.append(G.slide("""
        <div class="head-title">De la suma a la multiplicación</div>
        <p class="sub-text">Observa el patrón: cuando sumamos el <b class="hl">mismo número</b> varias veces, ¡es multiplicación!</p>
        <div class="fact-grid">
            <div class="fact-box" style="border-color:#9DE3BD;">
                <h4>✏️ Suma larga</h4>
                <p>5 + 5 + 5 + 5 = 20</p>
                <p class="stp"><b>4 veces el 5</b></p>
            </div>
            <div class="fact-box stp" style="border-color:#9DDEFF;">
                <h4>⚡ Multiplicación</h4>
                <p class="stp"><b>4 × 5 = 20</b></p>
                <p class="stp">¡Mucho más rápido!</p>
            </div>
        </div>
        <div class="stp warn-card" style="margin-top:16px;">
            <b>4 × 5</b> se lee: "4 <b>veces</b> 5" o "4 <b>grupos</b> de 5".
        </div>"""))

    # 4 — Partes de la multiplicación
    s.append(G.slide("""
        <div class="head-title">Las partes de una multiplicación</div>
        <div class="pnl-border" style="text-align:center;">
            <div class="math-eq" style="margin-bottom:20px;">4 × 5 = 20</div>
            <div class="chip-row">
                <div class="mini-chip stp"><b>4</b> es el primer <b>factor</b>:<br>la cantidad de grupos.</div>
                <div class="mini-chip stp"><b>5</b> es el segundo <b>factor</b>:<br>la cantidad en cada grupo.</div>
                <div class="mini-chip stp"><b>20</b> es el <b>producto</b>:<br>el resultado total.</div>
            </div>
        </div>"""))

    # 5 — Tabla del 2
    s.append(G.slide("""
        <div class="head-title">Tabla del 2 🦘</div>
        <p class="sub-text">El 2 salta de en 2 en 2. ¡Observa el patrón!</p>
        <div class="two-col">
            <div class="pnl-border">
                <div class="stp step-box">1 × 2 = 2</div>
                <div class="stp step-box">2 × 2 = 4</div>
                <div class="stp step-box">3 × 2 = 6</div>
                <div class="stp step-box">4 × 2 = 8</div>
                <div class="stp step-box">5 × 2 = 10</div>
            </div>
            <div class="pnl-border">
                <div class="stp step-box">6 × 2 = 12</div>
                <div class="stp step-box">7 × 2 = 14</div>
                <div class="stp step-box">8 × 2 = 16</div>
                <div class="stp step-box">9 × 2 = 18</div>
                <div class="stp step-box">10 × 2 = 20</div>
            </div>
        </div>
        <div class="stp warn-card" style="margin-top:12px;">Los resultados de la tabla del 2 siempre terminan en <b>0, 2, 4, 6 u 8</b> (números pares).</div>"""))

    # 6 — Tabla del 5
    s.append(G.slide("""
        <div class="head-title">Tabla del 5 🖐️</div>
        <p class="sub-text">El 5 salta de 5 en 5. Los resultados siempre terminan en <b class="hl">0 o 5</b>.</p>
        <div class="two-col">
            <div class="pnl-border">
                <div class="stp step-box">1 × 5 = 5</div>
                <div class="stp step-box">2 × 5 = 10</div>
                <div class="stp step-box">3 × 5 = 15</div>
                <div class="stp step-box">4 × 5 = 20</div>
                <div class="stp step-box">5 × 5 = 25</div>
            </div>
            <div class="pnl-border">
                <div class="stp step-box">6 × 5 = 30</div>
                <div class="stp step-box">7 × 5 = 35</div>
                <div class="stp step-box">8 × 5 = 40</div>
                <div class="stp step-box">9 × 5 = 45</div>
                <div class="stp step-box">10 × 5 = 50</div>
            </div>
        </div>"""))

    # 7 — Tabla del 10
    s.append(G.slide("""
        <div class="head-title">Tabla del 10 🔟</div>
        <p class="sub-text">¡La más fácil! Multiplica por 10 y solo agrega un <b class="hl">0</b> al final.</p>
        <div class="two-col">
            <div class="pnl-border">
                <div class="stp step-box">1 × 10 = 10</div>
                <div class="stp step-box">2 × 10 = 20</div>
                <div class="stp step-box">3 × 10 = 30</div>
                <div class="stp step-box">4 × 10 = 40</div>
                <div class="stp step-box">5 × 10 = 50</div>
            </div>
            <div class="pnl-border">
                <div class="stp step-box">6 × 10 = 60</div>
                <div class="stp step-box">7 × 10 = 70</div>
                <div class="stp step-box">8 × 10 = 80</div>
                <div class="stp step-box">9 × 10 = 90</div>
                <div class="stp step-box">10 × 10 = 100</div>
            </div>
        </div>"""))

    # 8 — Abre cuaderno 1
    s.append(G.notebook_slide(
        'Completa usando las tablas del 2, 5 y 10: <b class="hl">6 × 2 = ?  |  7 × 5 = ?  |  4 × 10 = ?</b>',
        ["6 × 2 = 12",
         "7 × 5 = 35",
         "4 × 10 = 40"]))

    # 9 — Propiedad conmutativa
    s.append(G.slide("""
        <div class="head-title">El orden no cambia el resultado ↔️</div>
        <p class="sub-text">En la multiplicación, <b class="hl">4 × 3 = 3 × 4</b>. ¡Da lo mismo el orden!</p>
        <div class="two-col">
            <div class="pnl-border" style="text-align:center;">
                <div style="font-size:36px;">⭐⭐⭐⭐<br>⭐⭐⭐⭐<br>⭐⭐⭐⭐</div>
                <div class="stp" style="font-size:22px; margin-top:8px;"><b>3 filas × 4 columnas = 12</b></div>
            </div>
            <div class="pnl-border stp" style="text-align:center;">
                <div style="font-size:36px;">⭐⭐⭐<br>⭐⭐⭐<br>⭐⭐⭐<br>⭐⭐⭐</div>
                <div class="stp" style="font-size:22px; margin-top:8px;"><b>4 filas × 3 columnas = 12</b></div>
            </div>
        </div>
        <div class="stp warn-card" style="margin-top:12px;">Esta propiedad se llama <b>conmutativa</b>. ¡Es muy útil para aprender las tablas!</div>"""))

    # 10 — Tabla del 3
    s.append(G.slide("""
        <div class="head-title">Tabla del 3 🌱</div>
        <p class="sub-text">El 3 salta de 3 en 3. La suma de sus dígitos siempre da un múltiplo de 3.</p>
        <div class="two-col">
            <div class="pnl-border">
                <div class="stp step-box">1 × 3 = 3</div>
                <div class="stp step-box">2 × 3 = 6</div>
                <div class="stp step-box">3 × 3 = 9</div>
                <div class="stp step-box">4 × 3 = 12</div>
                <div class="stp step-box">5 × 3 = 15</div>
            </div>
            <div class="pnl-border">
                <div class="stp step-box">6 × 3 = 18</div>
                <div class="stp step-box">7 × 3 = 21</div>
                <div class="stp step-box">8 × 3 = 24</div>
                <div class="stp step-box">9 × 3 = 27</div>
                <div class="stp step-box">10 × 3 = 30</div>
            </div>
        </div>"""))

    # 11 — Tabla del 4
    s.append(G.slide("""
        <div class="head-title">Tabla del 4 🚀</div>
        <p class="sub-text">El 4 es el doble del 2. Si sé la tabla del 2, ¡duplico los resultados!</p>
        <div class="two-col">
            <div class="pnl-border">
                <div class="stp step-box">1 × 4 = 4</div>
                <div class="stp step-box">2 × 4 = 8</div>
                <div class="stp step-box">3 × 4 = 12</div>
                <div class="stp step-box">4 × 4 = 16</div>
                <div class="stp step-box">5 × 4 = 20</div>
            </div>
            <div class="pnl-border">
                <div class="stp step-box">6 × 4 = 24</div>
                <div class="stp step-box">7 × 4 = 28</div>
                <div class="stp step-box">8 × 4 = 32</div>
                <div class="stp step-box">9 × 4 = 36</div>
                <div class="stp step-box">10 × 4 = 40</div>
            </div>
        </div>
        <div class="stp warn-card" style="margin-top:12px;">Truco: 4 × 7 = (2 × 7) × 2 = 14 × 2 = 28 ✅</div>"""))

    # 12 — Abre cuaderno 2
    s.append(G.notebook_slide(
        'Completa: <b class="hl">7 × 3 = ?  |  8 × 4 = ?  |  9 × 3 = ?</b>',
        ["7 × 3 = 21",
         "8 × 4 = 32",
         "9 × 3 = 27"]))

    # 13 — Quiz 1
    s.append(G.quiz_slide(
        "Desafío de tablas",
        '¿Cuánto es <b>6 × 4</b>?',
        ["20", "24", "28"], 1,
        "6 × 4 = 24. Si tienes dudas: 4+4+4+4+4+4 = 24."))

    # 14 — Matrices de puntos (arrays)
    s.append(G.slide("""
        <div class="head-title">La matriz de puntos 🔲</div>
        <p class="sub-text">Podemos representar la multiplicación como <b class="hl">filas y columnas</b>.</p>
        <div class="two-col">
            <div class="pnl-border" style="text-align:center;">
                <div style="font-size:28px; line-height:1.8; letter-spacing:8px;">
                    🔵🔵🔵🔵🔵<br>
                    🔵🔵🔵🔵🔵<br>
                    🔵🔵🔵🔵🔵
                </div>
                <div class="stp" style="font-size:22px; margin-top:10px;"><b>3 filas × 5 columnas = 15</b></div>
            </div>
            <div class="warn-card stp">
                <b>¿Para qué sirve?</b><br>Para organizar objetos en grupos iguales: asientos de teatro, cajas en una bodega, etc.
            </div>
        </div>"""))

    # 15 — Multiplicar con descomposición
    s.append(G.slide("""
        <div class="head-title">Estrategia: Descomponer para multiplicar</div>
        <p class="sub-text">Para multiplicar números más grandes, <b class="hl">descomponemos</b> en decenas y unidades.</p>
        <div class="decomp-flow">
            <div class="decomp-box">12 × 3</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">10 × 3 = 30</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">2 × 3 = 6</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">30 + 6 = 36</div>
        </div>
        <div class="stp warn-card" style="margin-top:16px;">Descomponemos 12 en <b>10 + 2</b>. Multiplicamos cada parte y sumamos al final.</div>"""))

    # 16 — Ejercicios tablas mixtas
    s.append(G.exercise_cards_slide(
        "¡Tablas mixtas!",
        "Mezcla de tablas del 2, 3, 4, 5 y 10.",
        [("🏆", "8 × 3", "= 24", "#FFE082"),
         ("🎯", "7 × 4", "= 28", "#9DDEFF"),
         ("🚲", "6 × 5", "= 30", "#E1BEE7")]))

    # 17 — Problema real 1
    s.append(G.problem_slide(
        "Las cajas de jugos", "🧃",
        "En el kiosco hay <b>5 cajas</b> con <b>8 jugos</b> cada una. ¿Cuántos jugos hay en total?",
        "5 × 8 = 40<br><span style='color:var(--base);'>Hay 40 jugos en total.</span>",
        "#FFF8E1", "#F57F17"))

    # 18 — Problema real 2
    s.append(G.problem_slide(
        "Las sillas del teatro", "🎭",
        "El teatro tiene <b>9 filas</b> con <b>7 sillas</b> en cada fila. ¿Cuántas sillas hay?",
        "9 × 7 = 63<br><span style='color:var(--base);'>Hay 63 sillas en el teatro.</span>",
        "#E8F5E9", "#2E7D32"))

    # 19 — Problema real 3
    s.append(G.problem_slide(
        "Las semanas de vacaciones", "🌞",
        "Las vacaciones de verano duran <b>3 semanas</b>. ¿Cuántos días son en total?",
        "3 × 7 = 21<br><span style='color:var(--base);'>Las vacaciones son 21 días.</span>",
        "#E3F2FD", "#1565C0"))

    # 20 — Quiz 2
    s.append(G.quiz_slide(
        "Problema con tablas",
        'Hay <b>4 bandejas</b> con <b>9 galletas</b> cada una. ¿Cuántas galletas hay en total?',
        ["32", "36", "40"], 1,
        "4 × 9 = 36 galletas."))

    # 21 — Abre cuaderno 3: con descomposición
    s.append(G.notebook_slide(
        'Resuelve usando descomposición: <b class="hl">13 × 4</b>',
        ["Descompongo: 13 = 10 + 3",
         "10 × 4 = 40",
         "3 × 4 = 12",
         "40 + 12 = 52"]))

    # 22 — Relación multiplicación y suma
    s.append(G.slide("""
        <div class="head-title">Conexión: multiplicación y suma</div>
        <p class="sub-text">Siempre puedes verificar una multiplicación <b class="hl">sumando los grupos</b>.</p>
        <div class="decomp-flow">
            <div class="decomp-box">6 × 4 = ?</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">4 + 4 + 4 + 4 + 4 + 4</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">= 24 ✅</div>
        </div>
        <div class="stp warn-card" style="margin-top:16px;">
            Si no recuerdas la tabla, ¡suma el número esa cantidad de veces!<br>Es más lento pero siempre funciona.
        </div>"""))

    # 23 — Ejercicios variados
    s.append(G.exercise_cards_slide(
        "Desafíos con tablas",
        "¡Mezcla de todas las tablas aprendidas!",
        [("🔥", "9 × 5", "= 45", "#FFB74D"),
         ("⚡", "7 × 3", "= 21", "#9DDEFF"),
         ("🚀", "8 × 4", "= 32", "#E1BEE7")]))

    # 24 — Completar tablas
    s.append(G.slide("""
        <div class="head-title">Completar la tabla de multiplicación</div>
        <p class="sub-text">¿Puedes completar estas celdas usando lo que aprendiste?</p>
        <div class="pnl-border">
            <table style="width:100%; text-align:center; font-size:24px; border-collapse:collapse;">
                <tr style="background:var(--base); color:white;">
                    <td style="padding:10px; border-radius:8px;">×</td>
                    <td style="padding:10px;">2</td><td style="padding:10px;">3</td>
                    <td style="padding:10px;">4</td><td style="padding:10px;">5</td>
                </tr>
                <tr><td style="font-weight:900; color:var(--base);">3</td>
                    <td class="stp" style="background:#FFE082; border-radius:6px;">6</td>
                    <td class="stp" style="background:#9DE3BD; border-radius:6px;">9</td>
                    <td class="stp" style="background:#9DDEFF; border-radius:6px;">12</td>
                    <td class="stp" style="background:#FFB74D; border-radius:6px;">15</td></tr>
                <tr><td style="font-weight:900; color:var(--base);">4</td>
                    <td class="stp" style="background:#FFE082; border-radius:6px;">8</td>
                    <td class="stp" style="background:#9DE3BD; border-radius:6px;">12</td>
                    <td class="stp" style="background:#9DDEFF; border-radius:6px;">16</td>
                    <td class="stp" style="background:#FFB74D; border-radius:6px;">20</td></tr>
            </table>
        </div>"""))

    # 25 — Problema combinado (mult + suma)
    s.append(G.problem_slide(
        "El almuerzo del comedor", "🍱",
        "El comedor preparó <b>6 fuentes</b> con <b>8 porciones</b> cada una, y además <b>7 porciones extra</b>. ¿Cuántas porciones hay en total?",
        "6 × 8 = 48 porciones. Luego 48 + 7 = 55.<br><span style='color:var(--base);'>Hay 55 porciones en total.</span>",
        "#FCE4EC", "#C2185B"))

    # 26 — Quiz 3
    s.append(G.quiz_slide(
        "Quiz final",
        '¿Cuánto es <b>7 × 5 + 3</b>?',
        ["38", "40", "38"], 0,
        "Primero la multiplicación: 7 × 5 = 35. Luego la suma: 35 + 3 = 38."))

    # 27 — Abre cuaderno final
    s.append(G.notebook_slide(
        'Inventa un problema que se resuelva con <b class="hl">4 × 6</b>.',
        ["Ejemplo: En el huerto hay 4 hileras de plantas.",
         "En cada hilera hay 6 plantas.",
         "4 × 6 = 24 plantas en total."]))

    # 28 — Error frecuente
    s.append(G.slide("""
        <div class="head-title">🚨 Error común en multiplicación</div>
        <p class="sub-text">Confundir la tabla: creer que <b class="hl">6 × 3 = 21</b>.</p>
        <div class="two-col">
            <div class="pnl-border" style="border-color:#FF9D9D;">
                <div style="font-size:22px; font-weight:800; color:#e53935; margin-bottom:12px;">❌ Error</div>
                <div class="math-eq">6 × 3 = 21</div>
                <div class="stp" style="font-size:18px; color:#e53935; margin-top:8px;">¡Confundió con 7 × 3!</div>
            </div>
            <div class="pnl-border stp" style="border-color:#9DE3BD;">
                <div style="font-size:22px; font-weight:800; color:#2e7d32; margin-bottom:12px;">✅ Correcto</div>
                <div class="math-eq">6 × 3 = 18</div>
                <div class="stp" style="font-size:18px;">3+3+3+3+3+3=18<br>O: 6D = 6 × 3 = 18</div>
            </div>
        </div>"""))

    # 29 — Problema difícil
    s.append(G.problem_slide(
        "La feria de ciencias", "🔬",
        "Hay <b>5 mesas</b> en la feria. Cada mesa tiene <b>4 proyectos</b> con <b>3 estudiantes</b> en cada proyecto. ¿Cuántos estudiantes participan en total?",
        "4 × 3 = 12 estudiantes por mesa.<br>5 × 12 = 60 estudiantes en total.<br><span style='color:var(--base);'>Participan 60 estudiantes.</span>",
        "#E8F5E9", "#2E7D32"))

    # 30 — Resumen
    s.append(G.summary_slide([
        "<b>Multiplicar = grupos iguales:</b> 4 × 3 significa 4 grupos de 3 = 3+3+3+3 = 12.",
        "<b>Tabla del 2:</b> Números pares (2, 4, 6, 8...). Tabla del 5: Termina en 0 o 5. Tabla del 10: Agrega un 0.",
        "<b>Propiedad conmutativa:</b> 4 × 3 = 3 × 4. ¡El orden no cambia el resultado!",
        "<b>Descomposición:</b> 12 × 4 = (10 × 4) + (2 × 4) = 40 + 8 = 48.",
        "<b>Comprueba:</b> Puedes verificar sumando el número tantas veces como indica el factor.",
    ]))

    assert len(s) == 30, f"Módulo 3B-4 tiene {len(s)} slides (necesita 30)"
    return G.html_doc("Multiplicación — 3° Básico", s)


if __name__ == "__main__":
    out = OUT / "3B-clase4-multiplicacion.html"
    out.write_text(module(), encoding="utf-8")
    print(f"✅ Generado: {out}")
