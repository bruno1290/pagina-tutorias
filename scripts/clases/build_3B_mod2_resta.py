"""
Genera el MÓDULO 3B-2: "Resta hasta 100" — 30 slides
Curso: 3° Básico | OA9 (Sustracción — el más crítico: 35% logro)
Enfoque: Resta sin desagrupar → con desagrupación (1 decena) →
         Casos con 0 → Resta de 3 dígitos con desagrupación
"""
from __future__ import annotations
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import generator_suma_resta as G

OUT = pathlib.Path("/Users/brunonattino/Desktop/PAGINA TUTORIAS/clases/tercero")

def alg3(rows, title, notes, long=False):
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
    grid_cols = f"80px repeat({ncols},64px)"
    return f"""
    <div class="column-wrap">
        <div class="alg-board">
            <div class="alg-grid" style="grid-template-columns:{grid_cols};">
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
        "¡Resta hasta 100! ➖",
        "Aprendemos a restar: desde lo más simple hasta los casos difíciles con desagrupación.",
        "🔢"))

    # 2 — ¿Qué es restar?
    s.append(G.slide("""
        <div class="head-title">¿Qué es restar?</div>
        <p class="sub-text">Restar es <b class="hl">quitar una cantidad</b> de otra y ver cuánto queda.</p>
        <div class="two-col">
            <div class="pnl-border" style="text-align:center;">
                <div style="font-size:48px;">🍓🍓🍓🍓🍓🍓🍓</div>
                <div class="stp" style="font-size:26px; margin-top:8px;">7 frutillas</div>
            </div>
            <div class="pnl-border" style="text-align:center;">
                <div style="font-size:48px; opacity:.3;">🍓🍓🍓</div>
                <div class="stp" style="font-size:26px; margin-top:8px; color:#e53935;">Quito 3</div>
            </div>
        </div>
        <div class="stp math-eq" style="margin-top:16px;">7 − 3 = 4 frutillas quedan</div>"""))

    # 3 — Elementos de la resta
    s.append(G.slide("""
        <div class="head-title">Las partes de una resta</div>
        <div class="pnl-border" style="background:#f8fbff; text-align:center;">
            <div class="math-eq" style="margin-bottom:20px;">58 − 23 = 35</div>
            <div class="chip-row">
                <div class="mini-chip stp">
                    <b>58</b> es el <b>minuendo</b>:<br>la cantidad de la que resto.
                </div>
                <div class="mini-chip stp">
                    <b>23</b> es el <b>sustraendo</b>:<br>lo que quito.
                </div>
                <div class="mini-chip stp">
                    <b>35</b> es la <b>diferencia</b>:<br>lo que queda.
                </div>
            </div>
        </div>
        <div class="stp warn-card" style="margin-top:14px;">🔍 Comprobación: diferencia + sustraendo = minuendo → <b>35 + 23 = 58 ✅</b></div>"""))

    # 4 — Resta sin desagrupar visual
    s.append(G.picture_operation_slide(
        "Resta sin desagrupar",
        "Cuando las unidades del minuendo son mayores, podemos restar directo.",
        "75", G.rods(7, "#9DDEFF") + G.unit_blocks(5, "#FFE082"),
        "32", G.rods(3, "#FF9D9D") + G.unit_blocks(2, "#FF9D9D"),
        "−", "75 − 32 = 43",
        "Unidades: 5 − 2 = 3. Decenas: 7 − 3 = 4. ¡Sin problema!",
        "#9DDEFF", "#FF9D9D", "#9DE3BD"))

    # 5 — Algoritmo sin desagrupar
    s.append(G.slide("""
        <div class="head-title">En columna (sin desagrupar)</div>
        <p class="sub-text">Restamos <b class="hl">primero las unidades</b>, luego las decenas.</p>"""
        + alg3(
            [["",    "_", "_"],
             ["D U", "7", "5"],
             ["−",   "3", "2"],
             ["",    "4", "3"]],
            "Columna a columna",
            ["Unidades: <b>5 − 2 = 3</b> ✅",
             "Decenas: <b>7 − 3 = 4</b> ✅",
             "Resultado: <b>43</b>"])
        + ""))

    # 6 — Abre cuaderno 1
    s.append(G.notebook_slide(
        'Resuelve: <b class="hl">89 − 56</b>',
        ["Unidades: 9 − 6 = 3",
         "Decenas: 8 − 5 = 3",
         "Resultado: 33"]))

    # 7 — Ejercicios sin desagrupar
    s.append(G.exercise_cards_slide(
        "Restas sin desagrupar — ¡a practicar!",
        "En estos ejemplos las unidades siempre alcanzan.",
        [("🎈", "96 − 43", "= 53", "#FFE082"),
         ("🦋", "78 − 25", "= 53", "#9DE3BD"),
         ("🎸", "85 − 31", "= 54", "#E1BEE7")]))

    # 8 — El problema: cuando no alcanza
    s.append(G.slide("""
        <div class="head-title">⚠️ ¿Qué pasa si las unidades no alcanzan?</div>
        <p class="sub-text">Si el dígito de abajo en unidades es <b class="hl">mayor</b> que el de arriba, necesitamos <b class="hl">pedir prestado</b>.</p>
        <div class="decomp-flow">
            <div class="decomp-box">43 − 17</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">¿3 − 7? ❌ No alcanza</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">Pido 1 decena → 13 − 7 = 6</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">Decenas: 3 − 1 = 2</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">Resultado: 26</div>
        </div>"""))

    # 9 — Concepto de desagrupación
    s.append(G.slide("""
        <div class="head-title">La desagrupación — "Pido prestada" una decena</div>
        <p class="sub-text">Cuando las unidades no alcanzan, transformo <b class="hl">1 decena en 10 unidades</b>.</p>
        <div class="fact-grid">
            <div class="fact-box" style="border-color:#9DDEFF;">
                <h4>Antes</h4>
                <p>43 = <b>4 decenas</b> y <b>3 unidades</b></p>
            </div>
            <div class="fact-box stp" style="border-color:#9DE3BD;">
                <h4>Después de pedir prestada</h4>
                <p>43 = <b>3 decenas</b> y <b>13 unidades</b></p>
            </div>
        </div>
        <div class="stp warn-card" style="margin-top:16px;">
            ¡El número total <b>no cambió</b>! 3D 13U = 30 + 13 = 43. Solo lo reorganizamos.
        </div>"""))

    # 10 — Algoritmo con desagrupación
    s.append(G.slide("""
        <div class="head-title">En columna (con desagrupación)</div>
        <p class="sub-text">El pequeño número tachado arriba muestra que "pedimos prestado".</p>"""
        + alg3(
            [["",    "r:3", "r:13"],
             ["D U", "4",   "3"],
             ["−",   "1",   "7"],
             ["",    "2",   "6"]],
            "¿Qué hicimos?",
            ["Unidades: <b>3 − 7</b> no alcanza. Pedimos 1 decena.",
             "Ahora tenemos <b>13 unidades</b> y <b>3 decenas</b>.",
             "Unidades: <b>13 − 7 = 6</b> ✅",
             "Decenas: <b>3 − 1 = 2</b> ✅. Resultado: <b>26</b>"])
        + ""))

    # 11 — Abre cuaderno: con desagrupación
    s.append(G.notebook_slide(
        'Resuelve: <b class="hl">62 − 38</b>',
        ["Unidades: 2 − 8 no alcanza",
         "Pido prestada 1 decena: ahora 12 unidades y 5 decenas",
         "Unidades: 12 − 8 = 4",
         "Decenas: 5 − 3 = 2",
         "Resultado: 24"]))

    # 12 — Ejercicios con desagrupación
    s.append(G.exercise_cards_slide(
        "¡Ahora sí necesitamos pedir prestado!",
        "En estos ejercicios hay desagrupación.",
        [("⚡", "71 − 48", "= 23", "#FFB74D"),
         ("🌟", "84 − 56", "= 28", "#9DDEFF"),
         ("🏆", "93 − 67", "= 26", "#E1BEE7")]))

    # 13 — Quiz 1
    s.append(G.quiz_slide(
        "Desafío rápido",
        '¿Cuánto es <b>52 − 37</b>?',
        ["25", "15", "35"], 1,
        "2 − 7 no alcanza. Pido prestada: 12 − 7 = 5. Decenas: 4 − 3 = 1. Resultado: 15."))

    # 14 — Caso especial: termina en 0
    s.append(G.slide("""
        <div class="head-title">Caso especial: cuando hay un 0 en las unidades</div>
        <p class="sub-text">Si el minuendo termina en <b class="hl">0</b>, ese cero se convierte en <b class="hl">10 unidades</b>.</p>
        <div class="decomp-flow">
            <div class="decomp-box">50 − 23</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">5D 0U</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">4D 10U</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">10 − 3 = 7</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">4 − 2 = 2</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">= 27</div>
        </div>"""))

    # 15 — Algoritmo caso con 0
    s.append(G.slide("""
        <div class="head-title">En columna (minuendo con 0 en unidades)</div>"""
        + alg3(
            [["",    "r:4", "r:10"],
             ["D U", "5",   "0"],
             ["−",   "2",   "3"],
             ["",    "2",   "7"]],
            "El 0 se convierte en 10",
            ["Las unidades son 0. No puedo restar 3.",
             "Pido prestada 1 decena: <b>4 decenas y 10 unidades</b>.",
             "Unidades: <b>10 − 3 = 7</b> ✅",
             "Decenas: <b>4 − 2 = 2</b> ✅. Resultado: <b>27</b>"])
        + ""))

    # 16 — Abre cuaderno: caso 0
    s.append(G.notebook_slide(
        'Resuelve: <b class="hl">80 − 47</b>',
        ["8D 0U → 7D 10U",
         "Unidades: 10 − 7 = 3",
         "Decenas: 7 − 4 = 3",
         "Resultado: 33"]))

    # 17 — Resta de 3 dígitos sin desagrupar
    s.append(G.slide("""
        <div class="head-title">Resta de 3 dígitos (sin desagrupar)</div>
        <p class="sub-text">Ahora sumamos las <b class="hl">centenas (C)</b>. ¡El proceso es igual!</p>
        <div class="two-col">
            <div class="pnl-border">
                <div class="math-eq">865 − 432</div>
                <div class="stp step-box">Unidades: 5 − 2 = 3 ✅</div>
                <div class="stp step-box">Decenas: 6 − 3 = 3 ✅</div>
                <div class="stp step-box">Centenas: 8 − 4 = 4 ✅</div>
                <div class="stp math-eq">= 433</div>
            </div>
            <div class="warn-card stp">Siempre: U → D → C<br>¡De derecha a izquierda!</div>
        </div>"""))

    # 18 — Resta 3 dígitos CON desagrupación
    s.append(G.slide("""
        <div class="head-title">Resta de 3 dígitos con desagrupación</div>
        <p class="sub-text">Cuando las unidades no alcanzan, pedimos a las decenas. Si las decenas tampoco, pedimos a las centenas.</p>"""
        + alg3(
            [["",      "r:4", "r:11", "_"],
             ["C D U", "5",   "2",    "1"],
             ["−",     "1",   "4",    "3"],
             ["",      "3",   "7",    "8"]],
            "Dos desagrupaciones",
            ["Unidades: <b>1 − 3</b> no alcanza → 5D2U → 4D 11U → <b>11 − 3 = 8</b>",
             "Decenas: <b>4 − 4</b> no alcanza → 4C4D → 3C 14D → <b>14 − 4 = 7... espera</b>",
             "Centenas: <b>4 − 1 = 3</b>. Resultado: <b>378</b> ✅"])
        + ""))

    # 19 — Ejercicios 3 dígitos
    s.append(G.exercise_cards_slide(
        "Restas de 3 dígitos",
        "Algunos necesitan desagrupación, otros no.",
        [("🎯", "742 − 315", "= 427", "#FFE082"),
         ("📘", "600 − 247", "= 353", "#9DDEFF"),
         ("🧩", "531 − 248", "= 283", "#E1BEE7")]))

    # 20 — Quiz 2
    s.append(G.quiz_slide(
        "¿Cuál es el resultado?",
        '¿Cuánto es <b>500 − 163</b>?',
        ["337", "347", "237"], 0,
        "5C 0D 0U → 4C 10D 0U → 4C 9D 10U. Luego: 10−3=7, 9−6=3, 4−1=3. Resultado: 337."))

    # 21 — Problema real 1
    s.append(G.problem_slide(
        "El ahorro de Lucas", "💰",
        "Lucas tiene <b>85 pesos</b> y gasta <b>47 pesos</b> en una fruta. ¿Cuánto le queda?",
        "85 − 47 = 38<br><span style='color:var(--base);'>A Lucas le quedan 38 pesos.</span>",
        "#FFF8E1", "#F57F17"))

    # 22 — Problema real 2
    s.append(G.problem_slide(
        "Los lápices del curso", "✏️",
        "Había <b>240 lápices</b> en la sala. Se usaron <b>137</b>. ¿Cuántos lápices quedan?",
        "240 − 137 = 103<br><span style='color:var(--base);'>Quedan 103 lápices.</span>",
        "#E8F5E9", "#2E7D32"))

    # 23 — Problema real 3
    s.append(G.problem_slide(
        "Las entradas al zoológico", "🦒",
        "El zoológico tiene capacidad para <b>500 personas</b>. Ya entraron <b>328</b>. ¿Cuántas personas más pueden entrar?",
        "500 − 328 = 172<br><span style='color:var(--base);'>Pueden entrar 172 personas más.</span>",
        "#E3F2FD", "#1565C0"))

    # 24 — Estrategia: comprobación con suma
    s.append(G.slide("""
        <div class="head-title">¿Cómo compruebo mi resta?</div>
        <p class="sub-text">Si la resta es correcta, <b class="hl">diferencia + sustraendo = minuendo</b>.</p>
        <div class="decomp-flow">
            <div class="decomp-box">85 − 47 = 38</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">Compruebo: 38 + 47</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">= 85 ✅ ¡Correcto!</div>
        </div>
        <div class="stp warn-card" style="margin-top:16px;">Esta comprobación funciona siempre. Si no da el minuendo original, hay un error en la resta.</div>"""))

    # 25 — Abre cuaderno final
    s.append(G.notebook_slide(
        'Resuelve y comprueba: <b class="hl">723 − 458</b>',
        ["Unidades: 3 − 8 no alcanza → pido prestada: 13 − 8 = 5",
         "Decenas: 1 − 5 no alcanza → pido prestada: 11 − 5 = 6... espera...",
         "Centenas: 6 − 4 = 2. Resultado: 265",
         "Compruebo: 265 + 458 = 723 ✅"]))

    # 26 — Ejercicios variados
    s.append(G.exercise_cards_slide(
        "¡Mezcla de desafíos!",
        "Decide cuándo desagrupar y en qué columna.",
        [("🔥", "90 − 63", "= 27", "#FFB74D"),
         ("⚡", "405 − 238", "= 167", "#9DDEFF"),
         ("🚀", "800 − 347", "= 453", "#E1BEE7")]))

    # 27 — Error frecuente
    s.append(G.slide("""
        <div class="head-title">🚨 Error común — ¡Cuidado!</div>
        <p class="sub-text">El error más frecuente: <b class="hl">restar al revés</b> cuando no alcanza.</p>
        <div class="two-col">
            <div class="pnl-border" style="border-color:#FF9D9D;">
                <div style="font-size:22px; font-weight:800; color:#e53935; margin-bottom:12px;">❌ INCORRECTO</div>
                <div class="math-eq">43 − 17</div>
                <div style="font-size:20px; margin-top:10px;">"7 − 3 = 4" → resultado: 34</div>
                <div class="stp" style="font-size:18px; color:#e53935; margin-top:8px;">¡Restaron al revés!</div>
            </div>
            <div class="pnl-border" style="border-color:#9DE3BD;">
                <div style="font-size:22px; font-weight:800; color:#2e7d32; margin-bottom:12px;">✅ CORRECTO</div>
                <div class="math-eq">43 − 17</div>
                <div class="stp" style="font-size:20px; margin-top:10px;">Pido prestada: 13 − 7 = 6</div>
                <div class="stp" style="font-size:20px;">Decenas: 3 − 1 = 2 → 26</div>
            </div>
        </div>"""))

    # 28 — Quiz 3
    s.append(G.quiz_slide(
        "Quiz final — Resta",
        'Una panadería tenía <b>300 marraquetas</b> y vendió <b>147</b>. ¿Cuántas quedan?',
        ["153", "143", "253"], 0,
        "300 − 147: 3C 0D 0U → 2C 9D 10U. Luego: 10−7=3, 9−4=5, 2−1=1. Resultado: 153 marraquetas."))

    # 29 — Problema integrador difícil
    s.append(G.problem_slide(
        "El campeonato de puntos", "🏅",
        "El equipo Rojo empezó con <b>500 puntos</b>. Perdió <b>127 puntos</b> en la primera ronda y <b>85 puntos</b> en la segunda. ¿Cuántos puntos tiene ahora?",
        "500 − 127 = 373. Luego 373 − 85 = 288.<br><span style='color:var(--base);'>El equipo Rojo tiene 288 puntos.</span>",
        "#FCE4EC", "#C2185B"))

    # 30 — Resumen
    s.append(G.summary_slide([
        "<b>Sin desagrupar:</b> Si U del minuendo ≥ U del sustraendo, restamos directo: U → D → C.",
        "<b>Con desagrupación:</b> Si U no alcanza, 1 decena se convierte en 10 unidades.",
        "<b>El 0 especial:</b> Si hay 0 en las unidades, ése 0 se convierte en 10 al pedir prestado.",
        "<b>En 3 dígitos:</b> La misma lógica, pero puede haber 2 desagrupaciones seguidas.",
        "<b>Comprobación:</b> Diferencia + sustraendo = minuendo. ¡Siempre puedes verificar!",
    ]))

    assert len(s) == 30, f"Módulo 3B-2 tiene {len(s)} slides (necesita 30)"
    return G.html_doc("Resta hasta 100 — 3° Básico", s)


if __name__ == "__main__":
    out = OUT / "3B-clase2-resta.html"
    out.write_text(module(), encoding="utf-8")
    print(f"✅ Generado: {out}")
