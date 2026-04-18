"""
Genera el contenido del MÓDULO 3 (suma/resta 3) — 30 slides.
Enfoque: Resta de 2, 3 y 4 dígitos con desagrupación en cadena,
el 'monstruo de los ceros', problemas situacionales con miles.
"""
from __future__ import annotations
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import generator_suma_resta as G

CUBE_CSS = """
.cube {
    width:58px;height:58px;border-radius:10px;
    background:linear-gradient(135deg,rgba(255,255,255,.55) 0%,rgba(255,255,255,0) 100%),var(--fill,#FF9D9D);
    border:2px solid rgba(0,0,0,.18);
    box-shadow:inset 3px 3px 6px rgba(255,255,255,.4),inset -3px -3px 6px rgba(0,0,0,.08);
}
"""

def alg4(rows, title, notes):
    cells_html = []
    for row in rows:
        label, *cells = row
        cells_html.append(f'<div class="alg-label">{label}</div>')
        for cell in cells:
            cls = ["alg-digit"]; txt = cell
            if cell.startswith("r:"):  cls.append("reserve"); txt = cell[2:]
            elif cell == "_":          cls.append("dim");    txt = ""
            cells_html.append(f'<div class="{" ".join(cls)}">{G.esc(txt)}</div>')
    notes_html = "".join(f'<p class="stp" style="margin-bottom:12px;">{n}</p>' for n in notes)
    return f"""
    <div class="column-wrap">
        <div class="alg-board">
            <div class="alg-grid" style="grid-template-columns:80px repeat(4,64px);">
                {"".join(cells_html)}
                <div class="alg-line" style="grid-column:2/span 4;"></div>
            </div>
        </div>
        <div class="side-panel"><h3>{G.esc(title)}</h3>{notes_html}</div>
    </div>"""


def module_three() -> str:
    s: list[str] = []

    # 1
    s.append(G.intro_slide("¡Suma y resta 3!",
        "Restas de 1, 2 y 3 dígitos con desagrupación. ¡Y nos enfrentamos a los 4 dígitos!", "➖"))

    # 2
    s.append(G.picture_operation_slide(
        "Resta de 1 dígito",
        "Cuando restamos números pequeños, vemos cuántos bloques quitamos.",
        "Tengo 9 cubitos", G.unit_blocks(9, "#FFE082"),
        "Quito 5",         G.unit_blocks(5, "#FF9D9D"),
        "−", "9 − 5 = 4",
        "Quitamos cinco y observamos cuántos quedan.",
        "#FFE082", "#FF9D9D", "#9DE3BD"))

    # 3 — elementos de la resta
    s.append(G.slide("""
        <div class="head-title">Elementos de la resta</div>
        <div class="pnl-border" style="background:#f8fbff;">
            <div class="formula-row" style="margin-bottom:16px;">
                <div class="label-pill stp">Minuendo</div>
                <div class="label-pill stp">Sustraendo</div>
                <div class="label-pill stp">Diferencia</div>
            </div>
            <div class="math-eq" style="font-size:62px;">15 − 6 = 9</div>
            <div class="stp chip-row">
                <div class="mini-chip">15 es el <b>minuendo</b>: la cantidad inicial.</div>
                <div class="mini-chip">6 es el <b>sustraendo</b>: lo que quito.</div>
                <div class="mini-chip">9 es la <b>diferencia</b>: lo que queda.</div>
            </div>
        </div>"""))

    # 4 — ideas importantes
    s.append(G.fact_boxes_slide("Ideas importantes de la resta",
        "Estas reglas ayudan a entender mejor lo que hacemos al restar.",
        [("0 no cambia",    "Si resto <b>0</b>, el número queda igual.", "#FFE082"),
         ("El orden importa","<b>9 − 4</b> no es lo mismo que <b>4 − 9</b>.", "#FFB74D"),
         ("Comprobación",   "Si sumo <b>diferencia + sustraendo</b>, vuelvo al minuendo.", "#E1BEE7")]))

    # 5 — resta en columna sin desagrupar
    s.append(G.slide("""
        <div class="head-title">Primera resta en columna (sin desagrupar)</div>
        <p class="sub-text">Si las unidades alcanzan, restamos primero ahí y luego seguimos con las decenas.</p>
        <div class="two-col">
            <div class="pnl-border">
                <div class="math-eq">58 − 3</div>
                <div class="stp step-box">Unidades: 8 − 3 = 5.</div>
                <div class="stp step-box">Decenas: 5 − 0 = 5.</div>
                <div class="stp math-eq">55</div>
            </div>
            <div class="warn-card stp">El sustraendo tiene 0 decenas. Por eso solo quitamos unidades.</div>
        </div>"""))

    # 6
    s.append(G.notebook_slide(
        'Resuelve: <b class="hl">89 − 5</b>.',
        ["Unidades: 9 − 5 = 4", "Decenas: 8 − 0 = 8", "Resultado: 84"]))

    # 7
    s.append(G.exercise_cards_slide("Restas simples para practicar",
        "Aquí todavía no necesitamos desagrupar.",
        [("🍪", "67 − 5", "= 62", "#FFE082"),
         ("🧸", "74 − 2", "= 72", "#9DE3BD"),
         ("⚽", "93 − 4", "= 89", "#E1BEE7")]))

    # 8 — cuando no alcanza
    s.append(G.slide("""
        <div class="head-title">Cuando no alcanza en unidades</div>
        <p class="sub-text">Si no puedo restar en las unidades, <b class="hl">desagrupo</b> una decena.</p>
        <div class="decomp-flow">
            <div class="decomp-box">42 − 19</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">4D 2U</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">3D 12U</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">23</div>
        </div>
        <div class="stp warn-card" style="margin-top:18px;">Una decena vale <b>10 unidades</b>. Por eso 42 puede transformarse en <b>3 decenas y 12 unidades</b>.</div>"""))

    # 9 — algoritmo desagrupación 2d
    s.append(G.slide("""
        <div class="head-title">Resta en columna con desagrupación</div>
        <p class="sub-text">Primero resolvemos las unidades, luego las decenas.</p>"""
        + G.alg_board(
            [["",     "_",  "3",  "12"],
             ["D U",  "4",  "2",  "_"],
             ["−",    "1",  "9",  "_"],
             ["",     "2",  "3",  "_"]],
            "Paso a paso",
            ["Como <b>2 − 9</b> no se puede, desagrupo una decena. Ahora tengo <b>12 unidades</b> y <b>3 decenas</b>.",
             "Unidades: <b>12 − 9 = 3</b>.",
             "Decenas: <b>3 − 1 = 2</b>. Resultado: <b>23</b>."],
            long=True)
        + ""))

    # 10 — otro caso
    s.append(G.slide("""
        <div class="head-title">Otro caso: una decena completa</div>
        <p class="sub-text">Si el número termina en 0, la decena se convierte en 10 unidades.</p>
        <div class="decomp-flow">
            <div class="decomp-box">50 − 23</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">4D 10U</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">10 − 3 = 7</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">4 − 2 = 2</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">27</div>
        </div>"""))

    # 11 — abre cuaderno 2d
    s.append(G.notebook_slide(
        'Resuelve en tu cuaderno: <b class="hl">81 − 37</b>.',
        ["No alcanza en unidades: 1 − 7",
         "Desagrupo: 8D 1U = 7D 11U",
         "11 − 7 = 4", "7 − 3 = 4", "Resultado: 44"]))

    # 12 — quiz 2d
    s.append(G.quiz_slide("Desafío rápido",
        '¿Cuál es el resultado de <b>42 − 19</b>?',
        ["21", "23", "33"], 1,
        "Después de desagrupar una decena, queda 23."))

    # 13
    s.append(G.exercise_cards_slide("Práctica con desagrupación",
        "Ahora sí necesitamos pedir prestada una decena.",
        [("🌟", "72 − 38", "= 34", "#FFB74D"),
         ("🚲", "61 − 27", "= 34", "#9DE3BD"),
         ("🪁", "90 − 46", "= 44", "#E1BEE7")]))

    # 14 — resta 3d sin desagrupar
    s.append(G.picture_operation_slide(
        "Resta de 3 dígitos sin desagrupar",
        "No siempre hace falta pedir prestado: a veces cada columna alcanza.",
        "864", G.flats(8, "#FFE082") + G.rods(6, "#9DE3BD") + G.unit_blocks(4, "#E1BEE7"),
        "321", G.flats(3, "#FFB74D") + G.rods(2, "#9DE3BD") + G.unit_blocks(1, "#FF9D9D"),
        "−", "864 − 321 = 543",
        "Como 4−1, 6−2 y 8−3 sí se pueden, no necesitamos desagrupar.",
        "#FFE082", "#FFB74D", "#9DE3BD"))

    # 15 — resta 3d con desagrupación (paso a paso)
    s.append(G.slide("""
        <div class="head-title">Resta de 3 dígitos con desagrupación</div>
        <p class="sub-text">En 3 dígitos seguimos el mismo orden: <b class="hl">unidades, decenas y centenas</b>.</p>
        <div class="two-col">
            <div class="pnl-border">
                <div class="math-eq">521 − 143</div>
                <div class="stp step-box">Unidades: 1 − 3 no alcanza. Desagrupo 1 decena → quedan 11 − 3 = 8.</div>
                <div class="stp step-box">Decenas: ahora quedó 1 − 4. Desagrupo 1 centena → quedan 11 − 4 = 7.</div>
                <div class="stp step-box">Centenas: 4 − 1 = 3.</div>
                <div class="stp math-eq">378</div>
            </div>
            <div class="warn-card stp">¡A veces hay que desagrupar <b>dos veces</b>: primero una decena y luego una centena!</div>
        </div>"""))

    # 16 — algoritmo 3d
    s.append(G.slide("""
        <div class="head-title">En columna (3 dígitos con desagrupación)</div>"""
        + G.alg_board(
            [["",      "4",  "11", "11"],
             ["C D U", "5",  "2",  "1"],
             ["−",     "1",  "4",  "3"],
             ["",      "3",  "7",  "8"]],
            "Qué ocurrió",
            ["Primero: 1 unidad no alcanza para quitar 3. Desagrupo → <b>11 unidades</b>.",
             "Luego: 1 decena no alcanza para quitar 4. Desagrupo una centena → <b>11 decenas</b>.",
             "Finalmente obtengo <b>378</b>."])
        + ""))

    # 17 — desagrupación desde centenas
    s.append(G.slide("""
        <div class="head-title">Desagrupación desde centenas</div>
        <p class="sub-text">Si las decenas son 0, primero desagrupo una centena y después una decena.</p>
        <div class="decomp-flow">
            <div class="decomp-box">400 − 175</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">3C 10D 0U</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">3C 9D 10U</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">225</div>
        </div>
        <div class="stp warn-card" style="margin-top:18px;">Primero una centena se transforma en 10 decenas. Luego una de esas decenas se transforma en 10 unidades.</div>"""))

    # 18 — abre cuaderno 3d
    s.append(G.notebook_slide(
        'Ahora intenta: <b class="hl">600 − 248</b>.',
        ["6C 0D 0U", "5C 10D 0U", "5C 9D 10U",
         "10 − 8 = 2", "9 − 4 = 5", "5 − 2 = 3", "Resultado: 352"]))

    # 19
    s.append(G.exercise_cards_slide("Restas de 3 dígitos",
        "Practica con desagrupación en distintos lugares.",
        [("🎯", "521 − 143", "= 378", "#FFE082"),
         ("📘", "731 − 208", "= 523", "#9DE3BD"),
         ("🧩", "642 − 327", "= 315", "#E1BEE7")]))

    # 20 — quiz 3d
    s.append(G.quiz_slide("¿Cuál es correcto?",
        '¿Cuál es el resultado de <b>521 − 143</b>?',
        ["368", "378", "388"], 1,
        "La resta correcta es 378. Hubo dos desagrupaciones."))

    # ── 4 DÍGITOS ─────────────────────────────────────────────────────────────

    # 21 — concepto resta 4d
    s.append(G.slide(f"""
        <style>{CUBE_CSS}</style>
        <div class="head-title">¡Llegamos a los Miles! Resta de 4 dígitos</div>
        <p class="sub-text">La lógica es la misma de siempre, pero ahora tenemos una columna más: las <b class="hl">Unidades de Mil</b>.</p>
        <div class="fact-grid">
            <div class="fact-box" style="border-color:#9DDEFF;">
                <h4>Mismo orden</h4>
                <p>Siempre de derecha a izquierda: U → D → C → UM.</p>
            </div>
            <div class="fact-box stp" style="border-color:#9DE3BD;">
                <h4>Misma regla</h4>
                <p>Si no alcanza, pido prestado de la columna de la izquierda.</p>
            </div>
            <div class="fact-box stp" style="border-color:#FF9D9D;">
                <h4>Hasta 4 veces</h4>
                <p>¡La cadena puede ser U → D → C → UM! Hay que tener paciencia.</p>
            </div>
        </div>"""))

    # 22 — resta 4d sin desagrupar concepto
    s.append(G.slide(f"""
        <style>{CUBE_CSS}</style>
        <div class="head-title">Resta de 4 dígitos (sin desagrupar)</div>
        <p class="sub-text">Cuando cada columna alcanza, es directo.</p>
        <div class="decomp-flow">
            <div class="decomp-box">7 894 − 3 251</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">U: 4 − 1 = 3</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">D: 9 − 5 = 4</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">C: 8 − 2 = 6</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">UM: 7 − 3 = 4</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">4 643</div>
        </div>"""))

    # 23 — algoritmo 4d sin desagrupar
    s.append(G.slide(f"""
        <style>{CUBE_CSS}</style>
        <div class="head-title">En columna (4 dígitos, sin desagrupar)</div>"""
        + alg4(
            [["",          "_",  "_",  "_",  "_"],
             ["UM C D U",  "7",  "8",  "9",  "4"],
             ["−",         "3",  "2",  "5",  "1"],
             ["",          "4",  "6",  "4",  "3"]],
            "Columna por columna",
            ["U: 4 − 1 = 3.",
             "D: 9 − 5 = 4.",
             "C: 8 − 2 = 6.",
             "UM: 7 − 3 = 4.",
             "Resultado: <b>4 643</b>."])
        + ""))

    # 24 — el monstruo de los ceros
    s.append(G.slide(f"""
        <style>{CUBE_CSS}</style>
        <div class="head-title">El Monstruo de los Ceros 😱</div>
        <p class="sub-text">¿Qué pasa cuando hay muchos ceros? ¡Hay que desagrupar en cadena!</p>
        <div class="decomp-flow">
            <div class="decomp-box">5 000 − 2 438</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">4UM 10C 0D 0U</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">4UM 9C 10D 0U</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">4UM 9C 9D 10U</div>
        </div>
        <div class="stp warn-card" style="margin-top:18px;">El 5000 se convierte en <b>4 mil, 9 centenas, 9 decenas y 10 unidades</b> antes de poder restar. ¡La cadena completa!</div>"""))

    # 25 — algoritmo 4d con desagrupación múltiple
    s.append(G.slide(f"""
        <style>{CUBE_CSS}</style>
        <div class="head-title">En columna (4 dígitos, desagrupación en cadena)</div>"""
        + alg4(
            [["",          "4",  "9",  "9",  "10"],
             ["UM C D U",  "5",  "0",  "0",  "0"],
             ["−",         "2",  "4",  "3",  "8"],
             ["",          "2",  "5",  "6",  "2"]],
            "La cadena completa",
            ["U: 0 no alcanza. Pido a D pero D es 0, pido a C pero C es 0, pido a UM → quedan <b>4 UM, 9 C, 9 D, 10 U</b>.",
             "U: 10 − 8 = 2.",
             "D: 9 − 3 = 6.",
             "C: 9 − 4 = 5.",
             "UM: 4 − 2 = 2. Resultado: <b>2 562</b>."])
        + ""))

    # 26 — ejercicios 4d
    s.append(G.exercise_cards_slide("Restas de 4 dígitos",
        "Decide si necesitas desagrupar y en qué columna.",
        [("🔥", "8 752 − 3 410", "= 5 342", "#FFB74D"),
         ("⚡", "6 000 − 2 347", "= 3 653", "#9DDEFF"),
         ("🚀", "9 020 − 4 685", "= 4 335", "#E1BEE7")]))

    # 27 — abre cuaderno 4d
    s.append(G.notebook_slide(
        'Resuelve con paciencia en tu cuaderno: <b class="hl">8 000 − 3 456</b>.',
        ["8000 = 7UM 10C 0D 0U",
         "→ 7UM 9C 10D 0U",
         "→ 7UM 9C 9D 10U",
         "10 − 6 = 4", "9 − 5 = 4", "9 − 4 = 5", "7 − 3 = 4",
         "Resultado: 4 544"]))

    # 28
    s.append(G.problem_slide("Álbum de láminas", "🎴",
        "Martina tenía <b>521 láminas</b> y regaló <b>143</b>. ¿Con cuántas se quedó?",
        "521 − 143 = 378<br><span style='color:var(--base);'>Se quedó con 378 láminas.</span>",
        "#FCE4EC", "#C2185B"))

    # 29
    s.append(G.problem_slide("Viaje en avión", "✈️",
        "Un avión tiene capacidad para <b>8 500 pasajeros</b> por mes. Si ya viajaron <b>3 785</b>, ¿cuántos asientos quedan?",
        "8 500 − 3 785 = 4 715<br><span style='color:var(--base);'>Quedan 4 715 asientos disponibles.</span>",
        "#E8F5E9", "#2E7D32"))

    # 30
    s.append(G.summary_slide([
        "<b>Si las unidades alcanzan:</b> Resto normal de derecha a izquierda.",
        "<b>Si no alcanzan:</b> Desagrupo: 1 decena = 10 unidades (o 1 centena = 10 decenas).",
        "<b>Ceros en cadena:</b> El número 5000 se convierte en 4UM 9C 9D 10U antes de restar.",
        "<b>En 4 dígitos:</b> El mismo proceso, pero con una columna más de Unidades de Mil.",
    ]))

    assert len(s) == 30, f"Module 3 tiene {len(s)} slides"
    return G.html_doc("Suma y resta 3", s)


if __name__ == "__main__":
    out = pathlib.Path("/Users/brunonattino/Desktop/PAGINA TUTORIAS/clases/suma-resta/suma-resta-3.html")
    out.write_text(module_three(), encoding="utf-8")
    print(f"Generado: {out}")
