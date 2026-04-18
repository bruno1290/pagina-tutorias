"""
Genera el contenido del MÓDULO 2 (suma/resta 2) — 30 slides.
Enfoque: Suma de 3 y 4 dígitos (Unidades de Mil), reservas múltiples,
problemas situacionales con miles.
"""
from __future__ import annotations
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import generator_suma_resta as G

# ── helpers adicionales ────────────────────────────────────────────────────────

CUBE_CSS = """
.cube {
    width: 58px; height: 58px; border-radius: 10px;
    background: linear-gradient(135deg,rgba(255,255,255,.55) 0%,rgba(255,255,255,0) 100%),
                var(--fill, #FF9D9D);
    border: 2px solid rgba(0,0,0,.18);
    box-shadow: inset 3px 3px 6px rgba(255,255,255,.4),inset -3px -3px 6px rgba(0,0,0,.08);
}
.alg-grid.four {
    grid-template-columns: 80px repeat(4, 68px) !important;
}
.alg-grid.four .alg-line {
    grid-column: 2 / span 4 !important;
}
"""

def cubes(n: int, color: str = "#FF9D9D") -> str:
    return "".join(f'<span class="cube" style="--fill:{color};"></span>' for _ in range(n))

def base_ten_card_4(number: int, title: str) -> str:
    th = number // 1000
    hu = (number % 1000) // 100
    te = (number % 100) // 10
    un = number % 10
    return f"""
    <div class="base-card" style="flex:1 1 400px;">
        <h3>{G.esc(title)}</h3>
        <div class="place-grid" style="grid-template-columns:repeat(4,1fr);">
            <div class="place-box">
                <div class="place-title">U. de Mil</div>
                <div class="block-stack">{cubes(th)}</div>
                <div class="number-tag">{th}</div>
            </div>
            <div class="place-box">
                <div class="place-title">Centenas</div>
                <div class="block-stack">{G.flats(hu, "#FFE082")}</div>
                <div class="number-tag">{hu}</div>
            </div>
            <div class="place-box">
                <div class="place-title">Decenas</div>
                <div class="block-stack">{G.rods(te, "#9DE3BD")}</div>
                <div class="number-tag">{te}</div>
            </div>
            <div class="place-box">
                <div class="place-title">Unidades</div>
                <div class="block-stack">{G.unit_blocks(un, "#9DDEFF")}</div>
                <div class="number-tag">{un}</div>
            </div>
        </div>
        <div class="math-eq" style="font-size:34px;">{number:,}</div>
    </div>"""

def alg4(rows, title, notes):
    """alg_board para 4 dígitos + signo = 5 columnas."""
    cells_html = []
    for row in rows:
        label, *cells = row
        cells_html.append(f'<div class="alg-label">{label}</div>')
        for cell in cells:
            cls = ["alg-digit"]
            txt = cell
            if cell.startswith("r:"):
                cls.append("reserve"); txt = cell[2:]
            elif cell == "_":
                cls.append("dim"); txt = ""
            cells_html.append(f'<div class="{" ".join(cls)}">{G.esc(txt)}</div>')
    notes_html = "".join(f'<p class="stp" style="margin-bottom:12px;">{n}</p>' for n in notes)
    return f"""
    <div class="column-wrap">
        <div class="alg-board">
            <div class="alg-grid four" style="grid-template-columns:80px repeat(4,64px);">
                {"".join(cells_html)}
                <div class="alg-line" style="grid-column:2/span 4;"></div>
            </div>
        </div>
        <div class="side-panel">
            <h3>{G.esc(title)}</h3>
            {notes_html}
        </div>
    </div>"""

# Extra CSS se inyecta vía slide raw — usamos un slide invisible al principio
def inject_css_slide() -> str:
    return f'<div class="sl" style="display:none;"><style>{CUBE_CSS}</style></div>'

# ── módulo ─────────────────────────────────────────────────────────────────────

def module_two() -> str:
    s: list[str] = []

    # 1 — Intro
    s.append(G.intro_slide("¡Suma y resta 2!",
        "Centenas, sumas de 3 dígitos, ¡y entramos al mundo de los miles!", "🏗️"))

    # 2
    s.append(G.slide("""
        <div class="head-title">Centenas, decenas y unidades</div>
        <p class="sub-text">Con bloques grandes podemos representar números de <b class="hl">3 dígitos</b>.</p>
        <div class="base-row">""" + G.base_ten_card(248, "248 = 2 centenas, 4 decenas y 8 unidades") + """</div>
        <div class="stp mini-chip">Una centena vale 100. Una decena vale 10. Una unidad vale 1.</div>"""))

    # 3
    s.append(G.slide("""
        <div class="head-title">Otro ejemplo visual</div>
        <p class="sub-text">Miremos cómo se ve un número grande cuando lo separamos por valor posicional.</p>
        <div class="base-row">""" + G.base_ten_card(356, "356 = 3 centenas, 5 decenas y 6 unidades",
            ("#FFB74D", "#9DE3BD", "#9DDEFF")) + """</div>
        <div class="stp mini-chip">356 = 300 + 50 + 6.</div>"""))

    # 4
    s.append(G.slide("""
        <div class="head-title">Sumar 3 dígitos con bloques</div>
        <p class="sub-text">Primero juntamos unidades, después decenas y finalmente centenas.</p>
        <div class="base-row">"""
        + G.base_ten_card(125, "Primer número", ("#FFE082", "#9DE3BD", "#9DDEFF"))
        + G.base_ten_card(243, "Segundo número", ("#FFB74D", "#B39DDB", "#FF9D9D"))
        + """</div>
        <div class="stp decomp-flow" style="margin-top:18px;">
            <div class="decomp-box">125 + 243</div>
            <div class="arrow">→</div>
            <div class="decomp-box">300 + 60 + 8</div>
            <div class="arrow">→</div>
            <div class="decomp-box">368</div>
        </div>"""))

    # 5 — reserva concepto
    s.append(G.slide("""
        <div class="head-title">Cuando hay reserva</div>
        <p class="sub-text">Si junto 10 unidades, las cambio por 1 decena. Si junto 10 decenas, las cambio por 1 centena.</p>
        <div class="two-col">
            <div class="pnl-border">
                <div class="math-eq">138 + 274</div>
                <div class="stp step-box">Unidades: 8 + 4 = 12. Escribo 2 y <b>reservo 1 decena</b>.</div>
                <div class="stp step-box">Decenas: 3 + 7 + 1 = 11. Escribo 1 y <b>reservo 1 centena</b>.</div>
                <div class="stp step-box">Centenas: 1 + 2 + 1 = 4.</div>
                <div class="stp math-eq">412</div>
            </div>
            <div class="warn-card stp">La reserva aparece porque estamos cambiando <b>10 unidades por 1 decena</b> o <b>10 decenas por 1 centena</b>.</div>
        </div>"""))

    # 6 — algoritmo en columna
    s.append(G.slide("""
        <div class="head-title">Suma en columna (3 dígitos)</div>
        <p class="sub-text">Seguimos el orden correcto: <b class="hl">unidades, decenas y centenas</b>.</p>"""
        + G.alg_board(
            [["",       "r:1", "r:1", "_"],
             ["C D U",  "1",   "3",   "8"],
             ["+",      "2",   "7",   "4"],
             ["",       "4",   "1",   "2"]],
            "Paso a paso",
            ["Unidades: 8 + 4 = 12. El <b>2</b> queda abajo y la <b>1 decena</b> sube.",
             "Decenas: 3 + 7 + 1 = 11. El <b>1</b> queda abajo y la <b>1 centena</b> sube.",
             "Centenas: 1 + 2 + 1 = 4. Resultado final: <b>412</b>."])
        + ""))

    # 7 — abre cuaderno 1
    s.append(G.notebook_slide(
        'Resuelve en columna: <b class="hl">326 + 157</b>.',
        ["Unidades: 6 + 7 = 13", "Decenas: 2 + 5 + 1 = 8", "Centenas: 3 + 1 = 4", "Resultado: 483"]))

    # 8 — tres números
    s.append(G.slide("""
        <div class="head-title">Sumar 3 números en columna</div>
        <p class="sub-text">El orden sigue siendo el mismo, pero ahora juntamos <b class="hl">tres números</b> en cada columna.</p>"""
        + G.alg_board(
            [["",      "_",   "r:2", "_"],
             ["C D U", "1",   "0",   "8"],
             ["+",     "5",   "4",   "9"],
             ["+",     "1",   "3",   "7"],
             ["",      "7",   "9",   "4"]],
            "Cómo pensar",
            ["Unidades: 8 + 9 + 7 = 24. Escribo 4 y reservo 2 decenas.",
             "Decenas: 0 + 4 + 3 + 2 = 9. Escribo 9.",
             "Centenas: 1 + 5 + 1 = 7. Resultado: <b>794</b>."])
        + ""))

    # 9
    s.append(G.notebook_slide(
        'Suma estos tres números: <b class="hl">370 + 48 + 64</b>.',
        ["Unidades: 0 + 8 + 4 = 12", "Decenas: 7 + 4 + 6 + 1 = 18", "Centenas: 3 + 1 = 4", "Resultado: 482"]))

    # 10
    s.append(G.exercise_cards_slide("Sumas de 3 dígitos sin reserva",
        "Primero practica casos donde no necesitamos cambiar unidades por decenas.",
        [("📦", "241 + 126", "= 367", "#FFE082"),
         ("🚲", "352 + 214", "= 566", "#9DE3BD"),
         ("🌈", "430 + 125", "= 555", "#E1BEE7")]))

    # 11
    s.append(G.exercise_cards_slide("Sumas de 3 dígitos con reserva",
        "Ahora sí aparece la reserva en unidades o decenas.",
        [("🎯", "138 + 274", "= 412", "#FFB74D"),
         ("🧩", "247 + 168", "= 415", "#9DE3BD"),
         ("🪁", "359 + 186", "= 545", "#E1BEE7")]))

    # 12
    s.append(G.notebook_slide(
        'Resuelve en columna: <b class="hl">451 + 239</b>.',
        ["Unidades: 1 + 9 = 10", "Decenas: 5 + 3 + 1 = 9", "Centenas: 4 + 2 = 6", "Resultado: 690"]))

    # 13
    s.append(G.fact_boxes_slide("Cómo ordenar los números en columna",
        "En columna, cada cifra va con su lugar correcto.",
        [("🟡 Unidades", "Las unidades van <b>debajo de unidades</b>.", "#FFE082"),
         ("🟢 Decenas",  "Las decenas van <b>debajo de decenas</b>.", "#9DE3BD"),
         ("🟣 Centenas", "Las centenas van <b>debajo de centenas</b>.", "#E1BEE7")]))

    # 14 — quiz 3d
    s.append(G.quiz_slide("Desafío rápido",
        '¿Cuál es el resultado de <b>138 + 274</b>?',
        ["302", "412", "422"], 1, "La suma correcta es 412."))

    # ── MILES ──────────────────────────────────────────────────────────────────

    # 15 — concepto miles (inyectamos CSS aquí con un style tag inline)
    s.append(G.slide(f"""
        <style>{CUBE_CSS}</style>
        <div class="head-title">¡Las Unidades de Mil!</div>
        <p class="sub-text">Después de las centenas viene un lugar todavía más grande: las <b class="hl">Unidades de Mil (UM)</b>.</p>
        <div class="fact-grid">
            <div class="fact-box" style="border-color:#9DDEFF;">
                <h4>Una unidad</h4>
                <p>Vale <b>1</b>. Es un cuadradito.</p>
            </div>
            <div class="fact-box stp" style="border-color:#9DE3BD;">
                <h4>Una decena</h4>
                <p>Vale <b>10</b>. Es una barrita.</p>
            </div>
            <div class="fact-box stp" style="border-color:#FFE082;">
                <h4>Una centena</h4>
                <p>Vale <b>100</b>. Es un cuadrado plano.</p>
            </div>
            <div class="fact-box stp" style="border-color:#FF9D9D;">
                <h4>Una U. de Mil</h4>
                <p>Vale <b>1000</b>. ¡Es un cubo grande!</p>
            </div>
        </div>"""))

    # 16 — visualizando 4 dígitos
    s.append(G.slide(f"""
        <style>{CUBE_CSS}</style>
        <div class="head-title">Visualizando un número de 4 dígitos</div>
        <p class="sub-text">Cada dígito ocupa su propio lugar.</p>
        <div class="base-row">
            {base_ten_card_4(2345, "2 345 = 2 UM · 3 C · 4 D · 5 U")}
        </div>
        <div class="stp mini-chip">2345 = 2000 + 300 + 40 + 5</div>"""))

    # 17 — otro ejemplo
    s.append(G.slide(f"""
        <style>{CUBE_CSS}</style>
        <div class="head-title">Otro ejemplo de 4 dígitos</div>
        <div class="base-row">
            {base_ten_card_4(5080, "5 080 = 5 UM · 0 C · 8 D · 0 U")}
        </div>
        <div class="stp mini-chip">Cuando un lugar vale 0, escribimos cero. ¡El 0 es un guardador de posición!</div>"""))

    # 18 — suma 4d sin reserva concepto
    s.append(G.slide(f"""
        <style>{CUBE_CSS}</style>
        <div class="head-title">Suma de 4 dígitos (sin reserva)</div>
        <p class="sub-text">La lógica es la misma: sumamos de derecha a izquierda, ahora con cuatro columnas.</p>
        <div class="decomp-flow">
            <div class="decomp-box">3412 + 5264</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">U: 2 + 4 = 6</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">D: 1 + 6 = 7</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">C: 4 + 2 = 6</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">UM: 3 + 5 = 8</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">8 676</div>
        </div>"""))

    # 19 — algoritmo 4d sin reserva
    s.append(G.slide(f"""
        <style>{CUBE_CSS}</style>
        <div class="head-title">En columna (4 dígitos, sin reserva)</div>"""
        + alg4(
            [["",          "_",  "_",  "_",  "_"],
             ["UM C D U",  "3",  "4",  "1",  "2"],
             ["+",         "5",  "2",  "6",  "4"],
             ["",          "8",  "6",  "7",  "6"]],
            "Columna por columna",
            ["U: 2 + 4 = 6.",
             "D: 1 + 6 = 7.",
             "C: 4 + 2 = 6.",
             "UM: 3 + 5 = 8.",
             "Resultado: <b>8676</b>."])
        + ""))

    # 20 — suma 4d con reserva concepto
    s.append(G.slide(f"""
        <style>{CUBE_CSS}</style>
        <div class="head-title">Suma de 4 dígitos (con reserva)</div>
        <p class="sub-text">Las reservas se encadenan: pueden pasar de unidades a decenas, ¡y hasta a miles!</p>
        <div class="two-col">
            <div class="pnl-border">
                <div class="math-eq" style="font-size:36px;">2 684 + 1 537</div>
                <div class="stp step-box">U: 4 + 7 = 11. Escribo 1, <b>reservo 1 D</b>.</div>
                <div class="stp step-box">D: 8 + 3 + 1 = 12. Escribo 2, <b>reservo 1 C</b>.</div>
                <div class="stp step-box">C: 6 + 5 + 1 = 12. Escribo 2, <b>reservo 1 UM</b>.</div>
                <div class="stp step-box">UM: 2 + 1 + 1 = 4.</div>
                <div class="stp math-eq">4 221</div>
            </div>
            <div class="warn-card stp">¡La reserva puede viajar hasta los miles! Por eso es tan importante el orden.</div>
        </div>"""))

    # 21 — algoritmo 4d con reserva doble
    s.append(G.slide(f"""
        <style>{CUBE_CSS}</style>
        <div class="head-title">En columna (4 dígitos, con reserva)</div>"""
        + alg4(
            [["",         "r:1", "r:1", "r:1",  "_"],
             ["UM C D U", "2",   "6",   "8",   "4"],
             ["+",        "1",   "5",   "3",   "7"],
             ["",         "4",   "2",   "2",   "1"]],
            "Cascada de reservas",
            ["U: 4 + 7 = 11 → reservo 1D.",
             "D: 8 + 3 + 1 = 12 → reservo 1C.",
             "C: 6 + 5 + 1 = 12 → reservo 1UM.",
             "UM: 2 + 1 + 1 = 4.",
             "Resultado: <b>4221</b>."])
        + ""))

    # 22 — ejercicios 4d sin reserva
    s.append(G.exercise_cards_slide("Sumas de 4 dígitos sin reserva",
        "Ubica bien cada dígito en su columna y suma.",
        [("🏔️", "3 201 + 4 567", "= 7 768", "#FFE082"),
         ("🌊", "6 310 + 2 415", "= 8 725", "#9DDEFF"),
         ("🧁", "4 020 + 3 170", "= 7 190", "#E1BEE7")]))

    # 23 — ejercicios 4d con reserva
    s.append(G.exercise_cards_slide("Sumas de 4 dígitos con reserva",
        "Ahora cuida las reservas que pasan de columna en columna.",
        [("🏗️", "2 684 + 1 537", "= 4 221", "#FFB74D"),
         ("🪐", "4 859 + 3 462", "= 8 321", "#9DE3BD"),
         ("🎯", "5 678 + 2 934", "= 8 612", "#E1BEE7")]))

    # 24 — abre cuaderno 4d
    s.append(G.notebook_slide(
        'Resuelve con mucho cuidado: <b class="hl">4 859 + 3 462</b>.',
        ["U: 9 + 2 = 11 → reservo 1D",
         "D: 5 + 6 + 1 = 12 → reservo 1C",
         "C: 8 + 4 + 1 = 13 → reservo 1UM",
         "UM: 4 + 3 + 1 = 8",
         "Resultado: 8 321"]))

    # 25 — quiz 4d
    s.append(G.quiz_slide("Desafío con miles",
        'Al resolver <b>2 684 + 1 537</b>, ¿qué obtienes al sumar las decenas?',
        ["8 + 3 = 11, escribo 1 y reservo 1 decena.",
         "8 + 3 + 1 = 12, escribo 2 y reservo 1 centena.",
         "8 + 3 + 1 = 12, escribo 12 sin reservar."],
        1, "¡Correcto! 8 + 3 más la reserva de unidades = 12. El 2 queda y la 1 sube a centenas."))

    # 26
    s.append(G.problem_slide("Cajas en la bodega", "📦",
        "En una bodega había <b>138 cajas</b> y llegaron <b>274 cajas</b> más. ¿Cuántas cajas hay en total?",
        "138 + 274 = 412<br><span style='color:var(--base);'>Ahora hay 412 cajas.</span>",
        "#E8F5E9", "#2E7D32"))

    # 27
    s.append(G.problem_slide("Puntos del campeonato", "🏅",
        "Un equipo logró <b>108 puntos</b> en la mañana, <b>549</b> en la tarde y <b>137</b> al final. ¿Cuántos puntos juntó?",
        "108 + 549 + 137 = 794<br><span style='color:var(--base);'>Juntó 794 puntos.</span>",
        "#E3F2FD", "#1565C0"))

    # 28 — problema con 4 dígitos
    s.append(G.problem_slide("Pasajes vendidos", "🎡",
        "En octubre se vendieron <b>2 684 pasajes</b> para el parque. En noviembre se vendieron <b>1 537 pasajes</b> más. ¿Cuántos pasajes se vendieron en total?",
        "2 684 + 1 537 = 4 221<br><span style='color:var(--base);'>Se vendieron 4221 pasajes en los dos meses.</span>",
        "#FFF3E0", "#EF6C00"))

    # 29
    s.append(G.summary_slide([
        "<b>Suma de 3 dígitos:</b> Centenas, decenas y unidades. Siempre de derecha a izquierda.",
        "<b>Reserva:</b> Al llegar a 10 o más en una columna, pasamos 1 al lugar siguiente.",
        "<b>Unidades de Mil (UM):</b> El cuarto lugar, que vale 1 000. Se usa para números de 4 dígitos.",
        "<b>Cascada de reservas:</b> En sumas grandes la reserva puede pasar de unidades → decenas → centenas → miles.",
    ]))

    # 30
    s.append(G.finish_slide(
        "Ya puedes sumar números gigantes en columna. ¡Incluso con reservas que viajan hasta los miles!", "🚀"))

    assert len(s) == 30, f"Module 2 tiene {len(s)} slides"
    return G.html_doc("Suma y resta 2", s)


if __name__ == "__main__":
    out = pathlib.Path("/Users/brunonattino/Desktop/PAGINA TUTORIAS/clases/suma-resta/suma-resta-2.html")
    out.write_text(module_two(), encoding="utf-8")
    print(f"Generado: {out}")
