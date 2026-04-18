"""
Genera el contenido del MÓDULO 1 (suma/resta 1) — 30 slides.
Enfoque: Introducción, suma de 1 y 2 dígitos, descomposición, cruzar decenas.
"""
from __future__ import annotations
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import generator_suma_resta as G

def module_one() -> str:
    s: list[str] = []

    # 1
    s.append(G.intro_slide("¡Suma y resta 1!",
        "Bloques, descomposición y las primeras estrategias para sumar con inteligencia.", "🧩"))

    # 2
    s.append(G.picture_operation_slide(
        "¿Qué es sumar?",
        'Sumar es <b class="hl">juntar</b> dos cantidades para obtener una cantidad mayor.',
        "Primero tengo 6", G.emoji_pack("🟨", 6, 54),
        "Luego agrego 3", G.emoji_pack("🟩", 3, 54),
        "+", "6 + 3 = 9",
        "Siempre parto de lo que ya tengo y después agrego lo nuevo.",
        "#FFE082", "#9DE3BD", "#E1BEE7"))

    # 3
    s.append(G.slide("""
        <div class="head-title">Elementos de la suma</div>
        <div class="pnl-border" style="background:#f8fbff;">
            <div class="formula-row" style="margin-bottom:16px;">
                <div class="label-pill stp">Sumando</div>
                <div class="label-pill stp">Sumando</div>
                <div class="label-pill stp">Suma total</div>
            </div>
            <div class="math-eq" style="font-size:64px;">7 + 2 = 9</div>
            <div class="stp chip-row">
                <div class="mini-chip">7 es un <b>sumando</b>.</div>
                <div class="mini-chip">2 es otro <b>sumando</b>.</div>
                <div class="mini-chip">9 es la <b>suma</b>.</div>
            </div>
        </div>"""))

    # 4
    s.append(G.fact_boxes_slide("Miramos bloques, no dedos",
        'Queremos <b class="hl">ver las cantidades</b>, no solo contarlas de memoria.',
        [("🟨 Unidades", "Cada cubito vale <b>1</b>. Muestran la cantidad exacta.", "#FFE082"),
         ("🟩 Decenas",  "Una barra vale <b>10</b>. Así vemos más rápido.", "#9DE3BD"),
         ("🟪 Idea clave","Los bloques ayudan a pensar sin depender de los dedos.", "#E1BEE7")]))

    # 5
    s.append(G.slide("""
        <div class="head-title">Bloques grandes y claros</div>
        <p class="sub-text">Con bloques grandes distinguimos mejor <b class="hl">cuánto tenemos</b> y <b class="hl">qué agregamos</b>.</p>
        <div class="card-row">
            <div class="idea-card" style="border-color:#9DDEFF;">
                <h3>7</h3>
                <div class="block-stack">""" + G.unit_blocks(7) + """</div>
                <p style="margin-top:12px;">Siete unidades son siete cubitos.</p>
            </div>
            <div class="idea-card stp" style="border-color:#9DE3BD;">
                <h3>12</h3>
                <div class="block-stack">""" + G.rods(1) + G.unit_blocks(2) + """</div>
                <p style="margin-top:12px;">12 es <b>1 decena y 2 unidades</b>.</p>
            </div>
            <div class="idea-card stp" style="border-color:#FFB74D;">
                <h3>15</h3>
                <div class="block-stack">""" + G.rods(1, "#FFB74D") + G.unit_blocks(5, "#E1BEE7") + """</div>
                <p style="margin-top:12px;">Ver los bloques hace más fácil sumar.</p>
            </div>
        </div>"""))

    # 6
    s.append(G.slide("""
        <div class="head-title">Propiedad conmutativa</div>
        <p class="sub-text">Si cambiamos el orden de los sumandos, la suma <b class="hl">no cambia</b>.</p>
        <div class="formula-row">
            <div class="math-eq stp" style="background:#fff7e8; border-color:#FFB74D;">4 + 2 = 6</div>
            <div class="math-eq stp" style="background:#f2fff5; border-color:#9DE3BD;">2 + 4 = 6</div>
        </div>
        <div class="stp pnl-border" style="background:linear-gradient(135deg,#fff7e8 0%,#f4fff8 50%,#f8f2ff 100%); text-align:center;">
            <div style="font-size:30px; font-weight:900;">El total sigue siendo <span class="hl">6</span>.</div>
            <p style="font-size:22px; margin-top:10px;">Mover los sumandos no cambia la cantidad final.</p>
        </div>"""))

    # 7
    s.append(G.slide("""
        <div class="head-title">Elemento neutro</div>
        <div class="pnl-border">
            <div class="math-eq">8 + 0 = 8</div>
            <div class="stp warn-card">
                Si sumo <b>0</b>, no agrego ningún bloque nuevo. Por eso el número queda igual.
            </div>
            <div class="stp formula-row">
                <div class="pnl" style="max-width:300px; text-align:center;">""" + G.unit_blocks(8, "#FFE082") + """</div>
                <div class="math-eq" style="font-size:54px;">+</div>
                <div class="pnl" style="max-width:220px; text-align:center; font-size:34px; font-weight:900;">0 bloques</div>
            </div>
        </div>"""))

    # 8
    s.append(G.picture_operation_slide(
        "Suma de 1 dígito con 1 dígito",
        "Primero miramos el número grande y después agregamos el otro sumando.",
        "Tengo 5 globos", G.emoji_pack("🎈", 5, 56),
        "Agrego 3 más",   G.emoji_pack("🟣", 3, 54),
        "+", "5 + 3 = 8",
        "Parto en 5 y agrego 1, 2, 3.",
        "#FFB74D", "#E1BEE7", "#9DDEFF"))

    # 9
    s.append(G.exercise_cards_slide("Practiquemos con sumas pequeñas",
        "Resuelve estas sumas mirando las cantidades.",
        [("🍎", "4 + 3", "= 7",  "#FFE082"),
         ("⚽", "6 + 2", "= 8",  "#9DE3BD"),
         ("🟣", "5 + 4", "= 9",  "#E1BEE7")]))

    # 10
    s.append(G.notebook_slide(
        'Escribe la suma y resuélvela con bloques: <b class="hl">7 + 2</b>.',
        ["7 + 2", "7, 8, 9", "Resultado: 9"],
        '<div class="pnl" style="max-width:760px; text-align:center;"><div class="block-stack">'
        + G.unit_blocks(7, "#FFE082") + '<span class="math-eq" style="font-size:46px;">+</span>'
        + G.unit_blocks(2, "#9DE3BD") + "</div></div>"))

    # 11
    s.append(G.slide("""
        <div class="head-title">Cruzar la decena</div>
        <p class="sub-text">Cuando estamos cerca del 10, conviene <b class="hl">descomponer</b> para llegar primero a una decena completa.</p>
        <div class="decomp-flow" style="margin-bottom:18px;">
            <div class="decomp-box">8 + 5</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">8 + 2 + 3</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">10 + 3</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">13</div>
        </div>
        <div class="stp warn-card">Partimos el <b>5</b> en <b>2 y 3</b> porque a 8 le faltan 2 para llegar a 10.</div>"""))

    # 12
    s.append(G.picture_operation_slide(
        "Llegar a 10 primero",
        "Esta estrategia hace la suma más rápida y más ordenada.",
        "Tengo 9 estrellas", G.emoji_pack("⭐", 9, 52),
        "Agrego 4",          G.emoji_pack("🟢", 4, 50),
        "+", "9 + 4 = 13",
        "Primero hago 9 + 1 = 10 y después sumo 3.",
        "#FFE082", "#9DE3BD", "#FFB74D"))

    # 13
    s.append(G.exercise_cards_slide("Cruzando la decena",
        "Descompón el segundo sumando para llegar a 10.",
        [("🌟", "9 + 4", "= 13", "#FFB74D"),
         ("🍊", "8 + 5", "= 13", "#9DE3BD"),
         ("🧩", "7 + 6", "= 13", "#E1BEE7")]))

    # 14
    s.append(G.slide("""
        <div class="head-title">Números de 2 dígitos</div>
        <p class="sub-text">Un número de 2 dígitos se puede pensar como <b class="hl">decenas y unidades</b>.</p>
        <div class="base-row">""" + G.base_ten_card(23, "23 = 2 decenas y 3 unidades", ("#FFE082", "#9DE3BD", "#E1BEE7")) + """</div>
        <div class="stp mini-chip">23 es lo mismo que 20 + 3.</div>"""))

    # 15
    s.append(G.slide("""
        <div class="head-title">Descomponer para sumar</div>
        <p class="sub-text">Si sumamos un número de 2 dígitos con uno de 1 dígito, miramos primero sus unidades.</p>
        <div class="decomp-flow">
            <div class="decomp-box">23 + 5</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">(20 + 3) + 5</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">20 + 8</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">28</div>
        </div>
        <div class="stp base-row" style="margin-top:20px;">"""
        + G.base_ten_card(23, "Partimos de 23", ("#FFE082", "#9DE3BD", "#E1BEE7"))
        + G.base_ten_card(28, "Agregamos 5 unidades", ("#FFB74D", "#9DE3BD", "#9DDEFF"))
        + """</div>"""))

    # 16
    s.append(G.slide("""
        <div class="head-title">Otro ejemplo con descomposición</div>
        <p class="sub-text">A veces conviene partir el sumando pequeño para llegar a 10 y seguir.</p>
        <div class="decomp-flow">
            <div class="decomp-box">18 + 6</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">18 + 2 + 4</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">20 + 4</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">24</div>
        </div>
        <div class="stp warn-card" style="margin-top:18px;">Al 18 le faltan <b>2</b> para llegar a 20. Por eso partimos el 6 en <b>2 y 4</b>.</div>"""))

    # 17
    s.append(G.slide("""
        <div class="head-title">Un ejemplo más</div>
        <p class="sub-text">Mira cómo se ve esta suma cuando pensamos en llegar a la siguiente decena.</p>
        <div class="decomp-flow">
            <div class="decomp-box">27 + 4</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">27 + 3 + 1</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">30 + 1</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">31</div>
        </div>
        <div class="stp mini-chip">A 27 le faltan 3 para llegar a 30.</div>"""))

    # 18
    s.append(G.exercise_cards_slide("Práctica con 2 dígitos",
        "Ahora resuelve sumas de 2 dígitos con 1 dígito.",
        [("🚗", "24 + 3", "= 27", "#FFE082"),
         ("🐠", "36 + 2", "= 38", "#9DE3BD"),
         ("🟣", "41 + 5", "= 46", "#E1BEE7")]))

    # 19
    s.append(G.notebook_slide(
        'Resuelve descomponiendo: <b class="hl">29 + 4</b>.',
        ["29 + 4", "29 + 1 + 3", "30 + 3", "Resultado: 33"]))

    # 20
    s.append(G.picture_operation_slide(
        "Suma visual con decenas",
        "Las barras y los cubitos también nos ayudan a sumar números más grandes.",
        "26", G.rods(2, "#9DE3BD") + G.unit_blocks(6, "#FFE082"),
        "7 unidades más", G.unit_blocks(7, "#FFB74D"),
        "+", "26 + 7 = 33",
        "Primero 26 + 4 = 30 y luego + 3.",
        "#9DE3BD", "#FFB74D", "#E1BEE7"))

    # 21
    s.append(G.exercise_cards_slide("Ejercicios relámpago",
        "Tres sumas más para practicar sin usar los dedos.",
        [("🎨", "34 + 5", "= 39", "#FFB74D"),
         ("🌈", "18 + 7", "= 25", "#9DE3BD"),
         ("🧸", "45 + 4", "= 49", "#E1BEE7")]))

    # 22  — 2d + 2d concepto
    s.append(G.slide("""
        <div class="head-title">Suma de 2 dígitos + 2 dígitos</div>
        <p class="sub-text">Ahora juntamos dos números de 2 dígitos. La clave: <b class="hl">sumar decenas con decenas y unidades con unidades</b>.</p>
        <div class="decomp-flow">
            <div class="decomp-box">34 + 23</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">30 + 20 = 50</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">4 + 3 = 7</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">50 + 7 = 57</div>
        </div>
        <div class="stp warn-card" style="margin-top:16px;">Separo las <b>decenas</b> y las <b>unidades</b>, las sumo por separado y las uno al final.</div>"""))

    # 23 — algoritmo columna sin reserva
    s.append(G.slide("""
        <div class="head-title">En columna (sin reserva)</div>
        <p class="sub-text">Escribimos uno encima del otro y sumamos de <b class="hl">derecha a izquierda</b>.</p>"""
        + G.alg_board(
            [["", "_", "_"],
             ["D U", "3", "4"],
             ["+",  "2", "3"],
             ["",   "5", "7"]],
            "Paso a paso",
            ["Unidades: 4 + 3 = 7.",
             "Decenas: 3 + 2 = 5.",
             "Resultado: <b>57</b>."])
        + ""))

    # 24 — suma con reserva concepto
    s.append(G.slide("""
        <div class="head-title">Cuando hay reserva</div>
        <p class="sub-text">Si las unidades suman <b class="hl">10 o más</b>, guardamos una decena y la pasamos a la columna de decenas.</p>
        <div class="two-col">
            <div class="pnl-border">
                <div class="math-eq">46 + 37</div>
                <div class="stp step-box">Unidades: 6 + 7 = 13. Escribo 3 y <b>reservo 1 decena</b>.</div>
                <div class="stp step-box">Decenas: 4 + 3 + 1 = 8.</div>
                <div class="stp math-eq">83</div>
            </div>
            <div class="warn-card stp">La reserva es el <b>intercambio de 10 unidades por 1 decena</b>.</div>
        </div>"""))

    # 25 — algoritmo columna con reserva
    s.append(G.slide("""
        <div class="head-title">En columna (con reserva)</div>
        <p class="sub-text">Observa cómo aparece el pequeño número de reserva <b class="hl">arriba</b>.</p>"""
        + G.alg_board(
            [["",  "_", "r:1", "_"],
             ["D U", "4", "6", "_"],
             ["+",  "3", "7", "_"],
             ["",   "8", "3", "_"]],
            "Qué ocurrió",
            ["Unidades: 6 + 7 = 13. El 3 queda abajo y la <b>1 decena</b> sube.",
             "Decenas: 4 + 3 + 1 = 8.",
             "Resultado final: <b>83</b>."])
        + ""))

    # 26 — quiz
    s.append(G.quiz_slide("Desafío rápido",
        '¿Cuál descomposición ayuda mejor a resolver <b>8 + 5</b>?',
        ["8 + 4 + 1", "8 + 2 + 3", "8 + 5 + 5"],
        1, "8 necesita 2 para llegar a 10. Luego quedan 3."))

    # 27
    s.append(G.quiz_slide("¡Otro desafío!",
        'Si sumas <b>46 + 37</b>, ¿cuánto reservas para las decenas?',
        ["Nada, se suma normal.", "1 decena, porque 6 + 7 = 13.", "2 decenas, porque los dos son grandes."],
        1, "¡Correcto! 6 + 7 = 13, así que guardas 1 decena."))

    # 28
    s.append(G.problem_slide("Lápices de colores", "✏️",
        "Sofía tenía <b>23 lápices</b> y su tía le regaló <b>37 más</b>. ¿Cuántos lápices tiene ahora?",
        "23 + 37 = 60<br><span style='color:var(--base);'>Sofía tiene 60 lápices.</span>",
        "#E3F2FD", "#1976D2"))

    # 29
    s.append(G.problem_slide("Globos en la fiesta", "🎈",
        "Había <b>48 globos</b> rojos y <b>35 globos</b> azules. ¿Cuántos globos hay en total?",
        "48 + 35 = 83<br><span style='color:var(--base);'>Hay 83 globos en total.</span>",
        "#FFF8E1", "#F9A825"))

    # 30
    s.append(G.summary_slide([
        "<b>Sumando + sumando = suma.</b> Los números que juntamos se llaman sumandos.",
        "<b>Propiedad conmutativa:</b> 4 + 2 y 2 + 4 dan el mismo resultado.",
        "<b>Cruzar la decena:</b> Descomponemos para llegar a 10 primero (ej. 8 + 5 = 8 + 2 + 3 = 13).",
        "<b>Reserva:</b> Cuando las unidades suman 10 o más, pasamos 1 decena a la columna izquierda.",
    ]))

    assert len(s) == 30, f"Module 1 tiene {len(s)} slides"
    return G.html_doc("Suma y resta 1", s)

if __name__ == "__main__":
    out = pathlib.Path("/Users/brunonattino/Desktop/PAGINA TUTORIAS/clases/suma-resta/suma-resta-1.html")
    out.write_text(module_one(), encoding="utf-8")
    print(f"Generado: {out}")
