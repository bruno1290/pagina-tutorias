"""
Genera el MÓDULO 3B-3: "Resta: Casos Difíciles" — 30 slides
Curso: 3° Básico | OA9 (semana 3 del calendario — casos con 0, doble desagrupación, operaciones combinadas)
Enfoque: Casos difíciles de resta → Operaciones combinadas (+/−) → Estrategias de cálculo mental
"""
from __future__ import annotations
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import generator_suma_resta as G

OUT = pathlib.Path("/Users/brunonattino/Desktop/PAGINA TUTORIAS/clases/tercero")

def alg3(rows, title, notes):
    cells_html = []
    ncols = max(len(r) - 1 for r in rows)
    for row in rows:
        label, *cells = row
        cells_html.append(f'<div class="alg-label">{label}</div>')
        for cell in cells:
            cls = ["alg-digit"]; txt = cell
            if cell.startswith("r:"): cls.append("reserve"); txt = cell[2:]
            elif cell == "_":         cls.append("dim");    txt = ""
            cells_html.append(f'<div class="{" ".join(cls)}">{G.esc(txt)}</div>')
    notes_html = "".join(f'<p class="stp" style="margin-bottom:12px;">{n}</p>' for n in notes)
    return f"""
    <div class="column-wrap">
        <div class="alg-board">
            <div class="alg-grid" style="grid-template-columns:80px repeat({ncols},64px);">
                {"".join(cells_html)}
                <div class="alg-line" style="grid-column:2/span {ncols};"></div>
            </div>
        </div>
        <div class="side-panel"><h3>{G.esc(title)}</h3>{notes_html}</div>
    </div>"""


def module() -> str:
    s: list[str] = []

    # 1 — Intro
    s.append(G.intro_slide(
        "Resta: ¡Los casos difíciles! 💪",
        "Dominamos la doble desagrupación, los ceros en cadena y las operaciones combinadas.",
        "🧠"))

    # 2 — Repaso rápido
    s.append(G.slide("""
        <div class="head-title">Repaso: Regla de oro</div>
        <p class="sub-text">Antes de empezar, recordemos la regla más importante de la resta.</p>
        <div class="fact-grid">
            <div class="fact-box" style="border-color:#9DE3BD;">
                <h4>✅ Si U alcanza</h4>
                <p>Resto directo: U − U, luego D − D, luego C − C.</p>
            </div>
            <div class="fact-box stp" style="border-color:#FF9D9D;">
                <h4>⚠️ Si U no alcanza</h4>
                <p>Pido 1 decena prestada → tengo 10 unidades más.</p>
            </div>
            <div class="fact-box stp" style="border-color:#FFB74D;">
                <h4>🔥 Si D tampoco alcanza</h4>
                <p>Pido 1 centena prestada → tengo 10 decenas más.</p>
            </div>
        </div>"""))

    # 3 — Doble desagrupación: concepto
    s.append(G.slide("""
        <div class="head-title">Doble desagrupación</div>
        <p class="sub-text">A veces hay que pedir prestado <b class="hl">dos veces</b>: a las decenas Y a las centenas.</p>
        <div class="decomp-flow">
            <div class="decomp-box">423 − 185</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">U: 3 − 5 no alcanza → pido a D</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">→ 3D 13U → 13 − 5 = 8</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">D: 1 − 8 no alcanza → pido a C</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">→ 3C 11D → 11 − 8 = 3. C: 3 − 1 = 2</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">Resultado: 238</div>
        </div>"""))

    # 4 — Algoritmo doble desagrupación
    s.append(G.slide("""
        <div class="head-title">En columna (doble desagrupación)</div>"""
        + alg3(
            [["",      "r:3", "r:11", "r:13"],
             ["C D U", "4",   "2",    "3"],
             ["−",     "1",   "8",    "5"],
             ["",      "2",   "3",    "8"]],
            "Dos pedidos prestados",
            ["U: 3−5 no alcanza. Pido a D. Ahora <b>3D 13U</b>. 13−5=8.",
             "D: 1−8 no alcanza. Pido a C. Ahora <b>3C 11D</b>. 11−8=3.",
             "C: <b>3−1=2</b>. Resultado: <b>238</b> ✅"])
        + ""))

    # 5 — Abre cuaderno 1
    s.append(G.notebook_slide(
        'Resuelve: <b class="hl">534 − 276</b>',
        ["U: 4−6 no alcanza → 2D 14U → 14−6=8",
         "D: 2−7 no alcanza → 4C 12D → 12−7=5... espera, 12D",
         "C: 4−2=2. Resultado: 258"]))

    # 6 — Ceros: el caso más difícil
    s.append(G.slide("""
        <div class="head-title">🧨 El caso más difícil: el 0 doble</div>
        <p class="sub-text">Cuando hay <b class="hl">ceros</b> en decenas y unidades, pedimos prestado en cadena.</p>
        <div class="decomp-flow">
            <div class="decomp-box">400 − 163</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">4C 0D 0U</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">3C 10D 0U</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">3C 9D 10U</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">10−3=7, 9−6=3, 3−1=2</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">= 237 ✅</div>
        </div>"""))

    # 7 — Algoritmo con doble cero
    s.append(G.slide("""
        <div class="head-title">En columna (con ceros en cadena)</div>"""
        + alg3(
            [["",      "r:3", "r:9", "r:10"],
             ["C D U", "4",   "0",   "0"],
             ["−",     "1",   "6",   "3"],
             ["",      "2",   "3",   "7"]],
            "La cadena completa",
            ["U: 0−3 no alcanza. Voy a D, pero D=0.",
             "Primero pido a C: 3C 10D 0U.",
             "Luego pido a D: 3C 9D 10U.",
             "10−3=7. 9−6=3. 3−1=2. Resultado: <b>237</b> ✅"])
        + ""))

    # 8 — Ejercicios casos difíciles
    s.append(G.exercise_cards_slide(
        "Los casos más difíciles — ¡tú puedes!",
        "Doble desagrupación y ceros en cadena.",
        [("💪", "300 − 147", "= 153", "#FFB74D"),
         ("🔥", "600 − 283", "= 317", "#9DDEFF"),
         ("⚡", "504 − 267", "= 237", "#E1BEE7")]))

    # 9 — Quiz 1
    s.append(G.quiz_slide(
        "Desafío difícil",
        '¿Cuánto es <b>700 − 348</b>?',
        ["352", "362", "452"], 0,
        "7C 0D 0U → 6C 10D 0U → 6C 9D 10U. Luego: 10−8=2, 9−4=5, 6−3=3. Resultado: 352."))

    # 10 — Verificar con suma
    s.append(G.slide("""
        <div class="head-title">Estrategia Pro: Verificar siempre</div>
        <p class="sub-text">Después de restar, <b class="hl">suma la diferencia + el sustraendo</b> para verificar.</p>
        <div class="two-col">
            <div class="pnl-border">
                <div class="math-eq">423 − 185 = 238</div>
                <div class="stp step-box">Verifico: 238 + 185 = ?</div>
                <div class="stp step-box">238 + 185 = 423 ✅</div>
                <div class="stp warn-card">¡Perfecto! La resta es correcta.</div>
            </div>
            <div class="pnl-border stp">
                <div class="math-eq">700 − 348 = 352</div>
                <div class="stp step-box">Verifico: 352 + 348 = ?</div>
                <div class="stp math-eq">= 700 ✅</div>
            </div>
        </div>"""))

    # 11 — Operaciones combinadas: introducción
    s.append(G.slide("""
        <div class="head-title">Operaciones combinadas (+  y  −)</div>
        <p class="sub-text">A veces un problema tiene <b class="hl">suma Y resta</b> juntas. ¿En qué orden las resolvemos?</p>
        <div class="fact-grid">
            <div class="fact-box" style="border-color:#9DDEFF;">
                <h4>Sin paréntesis</h4>
                <p>Resolvemos <b>de izquierda a derecha</b>.</p>
                <p class="stp"><b>20 + 5 − 8 = 25 − 8 = 17</b></p>
            </div>
            <div class="fact-box stp" style="border-color:#FFE082;">
                <h4>Con paréntesis</h4>
                <p>Primero lo que está <b>dentro del paréntesis</b>.</p>
                <p class="stp"><b>20 + (5 − 8)</b> ← primero el paréntesis</p>
            </div>
        </div>"""))

    # 12 — Ejemplo operación combinada
    s.append(G.slide("""
        <div class="head-title">Ejemplo: operación combinada</div>
        <p class="sub-text">Resolvemos paso a paso, de izquierda a derecha.</p>
        <div class="decomp-flow">
            <div class="decomp-box">35 + 48 − 27</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">Primero: 35 + 48 = 83</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">Luego: 83 − 27 = 56</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">Resultado: 56</div>
        </div>"""))

    # 13 — Abre cuaderno: operación combinada
    s.append(G.notebook_slide(
        'Resuelve: <b class="hl">250 + 130 − 75</b>',
        ["Primero: 250 + 130 = 380",
         "Luego: 380 − 75 = 305",
         "Resultado: 305"]))

    # 14 — Ejercicios operaciones combinadas
    s.append(G.exercise_cards_slide(
        "Operaciones combinadas",
        "Recuerda: de izquierda a derecha.",
        [("🌟", "64 + 28 − 35", "= 57", "#FFE082"),
         ("⚽", "200 − 83 + 47", "= 164", "#9DE3BD"),
         ("📚", "150 + 75 − 98", "= 127", "#E1BEE7")]))

    # 15 — Cálculo mental: compensación
    s.append(G.slide("""
        <div class="head-title">Estrategia mental: Compensación</div>
        <p class="sub-text">Para restar números cercanos a 10, 100, etc., podemos <b class="hl">redondear y ajustar</b>.</p>
        <div class="decomp-flow">
            <div class="decomp-box">83 − 29</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">29 ≈ 30</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">83 − 30 = 53</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">+ 1 (porque restamos 1 de más)</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">53 + 1 = 54 ✅</div>
        </div>"""))

    # 16 — Cálculo mental: diferencia con recta
    s.append(G.slide("""
        <div class="head-title">Estrategia: Contar hacia arriba</div>
        <p class="sub-text">Para restar, a veces es más fácil <b class="hl">contar cuánto le falta</b> al número pequeño para llegar al grande.</p>
        <div class="decomp-flow">
            <div class="decomp-box">72 − 45</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">45 + 5 = 50</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">50 + 22 = 72</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">5 + 22 = 27 ✅</div>
        </div>
        <div class="stp warn-card" style="margin-top:16px;">Esta técnica se llama "complemento". En vez de restar, sumamos hacia arriba.</div>"""))

    # 17 — Abre cuaderno: estrategias
    s.append(G.notebook_slide(
        'Usa la estrategia que prefieras: <b class="hl">93 − 48</b>',
        ["Opción 1 — Columna: 3−8 no alcanza, pido: 13−8=5, 8−4=4 → 45",
         "Opción 2 — Complemento: 48+2=50, 50+43=93 → 2+43=45",
         "Opción 3 — Compensar: 93−50=43, +2=45",
         "Resultado: 45 ✅"]))

    # 18 — Problema real 1
    s.append(G.problem_slide(
        "La maratón escolar", "🏃",
        "Los estudiantes de 3° deben correr <b>500 metros</b>. Ya corrieron <b>237 metros</b>. ¿Cuántos metros les faltan?",
        "500 − 237 = 263<br><span style='color:var(--base);'>Les faltan 263 metros.</span>",
        "#FFF8E1", "#F57F17"))

    # 19 — Problema real 2
    s.append(G.problem_slide(
        "La juguetería de Valeria", "🎮",
        "Valeria tenía <b>$650</b>, gastó <b>$283</b> en un juego y luego su mamá le dio <b>$100</b> más. ¿Cuánto tiene ahora?",
        "650 − 283 = 367. Luego 367 + 100 = 467.<br><span style='color:var(--base);'>Valeria tiene $467.</span>",
        "#E8F5E9", "#2E7D32"))

    # 20 — Problema real 3
    s.append(G.problem_slide(
        "Los cuadernos del colegio", "📓",
        "La bodega tiene <b>800 cuadernos</b>. Repartieron <b>345</b> en 3° básico y <b>228</b> en 4° básico. ¿Cuántos cuadernos quedan?",
        "345 + 228 = 573 (cuadernos entregados).<br>800 − 573 = 227.<br><span style='color:var(--base);'>Quedan 227 cuadernos en bodega.</span>",
        "#E3F2FD", "#1565C0"))

    # 21 — Quiz 2
    s.append(G.quiz_slide(
        "Operación combinada",
        '¿Cuál es el resultado de <b>400 − 158 + 75</b>?',
        ["317", "327", "307"], 0,
        "Primero: 400 − 158 = 242. Luego: 242 + 75 = 317."))

    # 22 — Ejercicio mixto difícil
    s.append(G.exercise_cards_slide(
        "Desafío combinado",
        "Mezcla de suma, resta y casos difíciles.",
        [("🧩", "600 − 247 + 83", "= 436", "#FFB74D"),
         ("🏆", "450 + 275 − 368", "= 357", "#9DDEFF"),
         ("🎯", "800 − 463 − 125", "= 212", "#E1BEE7")]))

    # 23 — Errores frecuentes revisión
    s.append(G.slide("""
        <div class="head-title">¿Cuál tiene error? — Corrígelo</div>
        <p class="sub-text">Detecta el error y explica qué falló.</p>
        <div class="two-col">
            <div class="pnl-border" style="border-color:#FF9D9D;">
                <div style="font-size:20px; font-weight:800; color:#e53935;">¿Correcto o incorrecto?</div>
                <div class="math-eq">302 − 145 = 257</div>
                <div class="stp" style="font-size:20px; margin-top:10px; color:#e53935;">❌ Incorrecto: 302−145=157</div>
            </div>
            <div class="pnl-border stp" style="border-color:#9DE3BD;">
                <div style="font-size:20px; font-weight:800; color:#2e7d32;">¿Correcto o incorrecto?</div>
                <div class="math-eq">500 − 237 = 263</div>
                <div class="stp" style="font-size:20px; margin-top:10px; color:#2e7d32;">✅ Correcto</div>
            </div>
        </div>"""))

    # 24 — Abre cuaderno: problema difícil
    s.append(G.notebook_slide(
        'Crea un problema que se resuelva con: <b class="hl">700 − 245 + 68</b>',
        ["Ejemplo: El estadio tiene 700 asientos.",
         "Se vendieron 245 entradas.",
         "Luego se vendieron 68 más.",
         "700 − 245 + 68 = 523 asientos vendidos total."]))

    # 25 — Estrategia: estimar para verificar
    s.append(G.slide("""
        <div class="head-title">Estimación para verificar</div>
        <p class="sub-text">Antes de calcular, <b class="hl">redondea</b> para saber si tu resultado "tiene sentido".</p>
        <div class="decomp-flow">
            <div class="decomp-box">487 − 263</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">≈ 500 − 260 = 240</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">Resultado real: 224</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">224 ≈ 240 ✅ ¡Tiene sentido!</div>
        </div>
        <div class="stp warn-card" style="margin-top:16px;">Si hubiera dado 724, sabríamos que algo salió mal.</div>"""))

    # 26 — Ejercicios finales intensivos
    s.append(G.exercise_cards_slide(
        "Ejercicios finales — ¡Sin rendirse!",
        "Los casos más difíciles para dominar.",
        [("🔥", "1000 − 348", "= 652", "#FFB74D"),
         ("⚡", "703 − 456", "= 247", "#9DDEFF"),
         ("🚀", "900 − 528 + 143", "= 515", "#E1BEE7")]))

    # 27 — Quiz 3
    s.append(G.quiz_slide(
        "Quiz avanzado",
        'Una tienda tenía <b>500 lápices</b>, vendió <b>237</b> en la mañana y <b>148</b> en la tarde. ¿Cuántos le quedan?',
        ["115", "125", "215"], 0,
        "237 + 148 = 385 lápices vendidos. 500 − 385 = 115 lápices quedan."))

    # 28 — Problema de 3 pasos
    s.append(G.problem_slide(
        "El huerto del colegio", "🌱",
        "El huerto tenía <b>350 plantas</b>. Se secaron <b>87</b> en julio. En agosto sembraron <b>124 nuevas</b>. ¿Cuántas plantas hay ahora?",
        "350 − 87 = 263. Luego 263 + 124 = 387.<br><span style='color:var(--base);'>El huerto tiene 387 plantas.</span>",
        "#FCE4EC", "#C2185B"))

    # 29 — Problema integrador
    s.append(G.problem_slide(
        "El campeonato de lectura", "📖",
        "La meta del curso es leer <b>1000 páginas</b>. En abril leyeron <b>287</b>, en mayo <b>334</b> y en junio <b>256</b>. ¿Cuántas páginas les faltan para la meta?",
        "287 + 334 + 256 = 877 páginas leídas.<br>1000 − 877 = 123.<br><span style='color:var(--base);'>Les faltan 123 páginas para la meta.</span>",
        "#E8F5E9", "#2E7D32"))

    # 30 — Resumen
    s.append(G.summary_slide([
        "<b>Doble desagrupación:</b> Pido a D, luego a C si también falta.",
        "<b>Ceros en cadena:</b> Paso por las columnas hasta encontrar dónde pedir prestado.",
        "<b>Operaciones combinadas:</b> Sin paréntesis → de izquierda a derecha.",
        "<b>Comprobación:</b> diferencia + sustraendo = minuendo siempre.",
        "<b>Estrategias mentales:</b> complemento (contar hacia arriba) y compensación (redondear y ajustar).",
    ]))

    assert len(s) == 30, f"Módulo 3B-3 tiene {len(s)} slides (necesita 30)"
    return G.html_doc("Resta: Casos Difíciles — 3° Básico", s)


if __name__ == "__main__":
    out = OUT / "3B-clase3-resta-dificil.html"
    out.write_text(module(), encoding="utf-8")
    print(f"✅ Generado: {out}")
