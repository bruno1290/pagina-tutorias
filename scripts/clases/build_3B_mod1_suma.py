"""
Genera el MÓDULO 3B-1: "Suma hasta 100" — 30 slides
Curso: 3° Básico | OA6 (Adición y sustracción)
Enfoque: Suma sin reserva → con reserva (una vez) → con doble reserva
         Números hasta 100, algoritmo en columna C/D/U
"""
from __future__ import annotations
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import generator_suma_resta as G

OUT = pathlib.Path("/Users/brunonattino/Desktop/PAGINA TUTORIAS/clases/tercero")

def alg3(rows, title, notes):
    """Algoritmo en columna 3 columnas (C D U)."""
    cells_html = []
    for row in rows:
        label, *cells = row
        cells_html.append(f'<div class="alg-label">{label}</div>')
        for cell in cells:
            cls = ["alg-digit"]; txt = cell
            if cell.startswith("r:"): cls.append("reserve"); txt = cell[2:]
            elif cell == "_":        cls.append("dim");    txt = ""
            cells_html.append(f'<div class="{" ".join(cls)}">{G.esc(txt)}</div>')
    notes_html = "".join(f'<p class="stp" style="margin-bottom:12px;">{n}</p>' for n in notes)
    return f"""
    <div class="column-wrap">
        <div class="alg-board">
            <div class="alg-grid" style="grid-template-columns:80px repeat(3,64px);">
                {"".join(cells_html)}
                <div class="alg-line" style="grid-column:2/span 3;"></div>
            </div>
        </div>
        <div class="side-panel"><h3>{G.esc(title)}</h3>{notes_html}</div>
    </div>"""


def module() -> str:
    s: list[str] = []

    # 1 — Intro
    s.append(G.intro_slide(
        "¡Suma hasta 100! ➕",
        "Aprendemos a sumar con bloques, con la tabla posicional y con el algoritmo en columna.",
        "🔢"))

    # 2 — Repaso: ¿qué es sumar?
    s.append(G.slide("""
        <div class="head-title">¿Qué es sumar?</div>
        <p class="sub-text">Sumar es <b class="hl">juntar dos grupos</b> y contar el total.</p>
        <div class="two-col">
            <div class="pnl-border" style="text-align:center;">
                <div style="font-size:52px;">🍎🍎🍎</div>
                <div class="stp" style="font-size:28px; margin-top:8px;">3 manzanas</div>
            </div>
            <div class="pnl-border" style="text-align:center;">
                <div style="font-size:52px;">🍎🍎</div>
                <div class="stp" style="font-size:28px; margin-top:8px;">2 manzanas</div>
            </div>
        </div>
        <div class="stp math-eq" style="margin-top:16px;">3 + 2 = 5 manzanas en total</div>"""))

    # 3 — Valor posicional: decenas y unidades
    s.append(G.slide("""
        <div class="head-title">Decenas y Unidades</div>
        <p class="sub-text">Antes de sumar, reconocemos el <b class="hl">valor de cada dígito</b>.</p>
        <div class="fact-grid">
            <div class="fact-box" style="border-color:#9DDEFF;">
                <h4>📏 Decena (D)</h4>
                <p>Un grupo de <b>10 unidades</b>.<br>Está en la posición de la izquierda.</p>
            </div>
            <div class="fact-box stp" style="border-color:#FFE082;">
                <h4>🟡 Unidad (U)</h4>
                <p>Un objeto solo.<br>Está en la posición de la derecha.</p>
            </div>
        </div>
        <div class="stp warn-card" style="margin-top:16px;">
            En el número <b>47</b>: el <b>4</b> son 4 decenas (= 40) y el <b>7</b> son 7 unidades.
        </div>"""))

    # 4 — Suma sin reserva: concepto visual
    s.append(G.picture_operation_slide(
        "Suma sin reserva",
        "Si las unidades suman menos de 10, no necesitamos reservar nada.",
        "23", G.rods(2, "#9DDEFF") + G.unit_blocks(3, "#FFE082"),
        "14", G.rods(1, "#9DDEFF") + G.unit_blocks(4, "#FFE082"),
        "+", "23 + 14 = 37",
        "Sumamos las unidades: 3 + 4 = 7. Luego las decenas: 2 + 1 = 3. ¡Total: 37!",
        "#9DDEFF", "#FFE082", "#9DE3BD"))

    # 5 — Algoritmo sin reserva
    s.append(G.slide("""
        <div class="head-title">En columna (sin reserva)</div>
        <p class="sub-text">Sumamos <b class="hl">primero las unidades</b>, luego las decenas.</p>"""
        + alg3(
            [["",    "_", "_"],
             ["D U", "2", "3"],
             ["+",   "1", "4"],
             ["",    "3", "7"]],
            "Paso a paso",
            ["Unidades: <b>3 + 4 = 7</b>. Lo escribimos abajo.",
             "Decenas: <b>2 + 1 = 3</b>. Lo escribimos abajo.",
             "Resultado: <b>37</b> ✅"])
        + ""))

    # 6 — Abre cuaderno: suma sin reserva
    s.append(G.notebook_slide(
        'Resuelve en tu cuaderno: <b class="hl">34 + 25</b>',
        ["Unidades: 4 + 5 = 9",
         "Decenas: 3 + 2 = 5",
         "Resultado: 59"]))

    # 7 — Ejercicios sin reserva
    s.append(G.exercise_cards_slide(
        "Sumas sin reserva — ¡a practicar!",
        "En estos ejemplos no hay que reservar nada.",
        [("🍬", "41 + 35", "= 76", "#FFE082"),
         ("⚽", "62 + 17", "= 79", "#9DE3BD"),
         ("📚", "53 + 24", "= 77", "#E1BEE7")]))

    # 8 — Suma con reserva: introducción
    s.append(G.slide("""
        <div class="head-title">¿Qué pasa si las unidades suman 10 o más?</div>
        <p class="sub-text">Cuando las unidades dan <b class="hl">10 o más</b>, necesitamos <b class="hl">reservar</b> una decena.</p>
        <div class="decomp-flow">
            <div class="decomp-box">28 + 15</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">U: 8 + 5 = 13</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">13 = 1 decena + 3 unidades</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">Llevo la decena a D</div>
        </div>
        <div class="stp warn-card" style="margin-top:16px;">La "reserva" o "llevo" es el <b>1</b> pequeño que escribimos arriba de las decenas.</div>"""))

    # 9 — Algoritmo con reserva
    s.append(G.slide("""
        <div class="head-title">En columna (con reserva)</div>
        <p class="sub-text">El pequeño <b class="hl">1</b> de arriba es lo que "llevamos" a las decenas.</p>"""
        + alg3(
            [["",    "r:1", "_"],
             ["D U", "2",   "8"],
             ["+",   "1",   "5"],
             ["",    "4",   "3"]],
            "¿Qué ocurrió?",
            ["Unidades: <b>8 + 5 = 13</b>. Escribo el 3 y llevo 1.",
             "Decenas: <b>2 + 1 + 1 (llevado) = 4</b>.",
             "Resultado: <b>43</b> ✅"])
        + ""))

    # 10 — Abre cuaderno: con reserva
    s.append(G.notebook_slide(
        'Resuelve en tu cuaderno: <b class="hl">47 + 36</b>',
        ["Unidades: 7 + 6 = 13 → escribo 3, llevo 1",
         "Decenas: 4 + 3 + 1 (llevado) = 8",
         "Resultado: 83"]))

    # 11 — Ejercicios con reserva
    s.append(G.exercise_cards_slide(
        "Sumas con reserva",
        "Aquí sí necesitamos llevar una decena.",
        [("🌟", "38 + 47", "= 85", "#FFB74D"),
         ("🎯", "56 + 27", "= 83", "#9DDEFF"),
         ("🚲", "69 + 14", "= 83", "#E1BEE7")]))

    # 12 — Quiz 1
    s.append(G.quiz_slide(
        "Desafío rápido",
        '¿Cuánto es <b>45 + 38</b>?',
        ["73", "83", "93"], 1,
        "5 + 8 = 13 → escribo 3 y llevo 1. Luego 4 + 3 + 1 = 8. Resultado: 83."))

    # 13 — Suma de 3 dígitos sin reserva
    s.append(G.slide("""
        <div class="head-title">Suma de 3 dígitos (sin reserva)</div>
        <p class="sub-text">Ahora agregamos las <b class="hl">centenas (C)</b>. ¡El proceso es el mismo!</p>
        <div class="two-col">
            <div class="pnl-border">
                <div class="math-eq">234 + 152</div>
                <div class="stp step-box">Unidades: 4 + 2 = 6</div>
                <div class="stp step-box">Decenas: 3 + 5 = 8</div>
                <div class="stp step-box">Centenas: 2 + 1 = 3</div>
                <div class="stp math-eq">386</div>
            </div>
            <div class="warn-card stp">¡El orden siempre es el mismo:<br><b>U → D → C</b><br>De derecha a izquierda!</div>
        </div>"""))

    # 14 — Algoritmo 3 dígitos con reserva en unidades
    s.append(G.slide("""
        <div class="head-title">Suma de 3 dígitos con reserva</div>
        <p class="sub-text">Cuando las unidades superan 9, reservamos y llevamos a las decenas.</p>"""
        + alg3(
            [["",      "r:1", "_"],
             ["C D U", "3",   "4",  "8"],
             ["+",     "2",   "3",  "5"],
             ["",      "5",   "8",  "3"]],
            "Paso a paso",
            ["Unidades: <b>8 + 5 = 13</b> → escribo 3, llevo 1.",
             "Decenas: <b>4 + 3 + 1 = 8</b>.",
             "Centenas: <b>3 + 2 = 5</b>. Resultado: <b>583</b> ✅"])
        + ""))

    # 15 — Suma con reserva en decenas
    s.append(G.slide("""
        <div class="head-title">Reserva en las decenas</div>
        <p class="sub-text">A veces la reserva ocurre en las <b class="hl">decenas</b>, no en las unidades.</p>"""
        + alg3(
            [["",      "_", "r:1", "_"],
             ["C D U", "1", "7",   "2"],
             ["+",     "2", "5",   "4"],
             ["",      "4", "2",   "6"]],
            "¿Qué ocurrió?",
            ["Unidades: <b>2 + 4 = 6</b>. Sin reserva.",
             "Decenas: <b>7 + 5 = 12</b> → escribo 2, llevo 1.",
             "Centenas: <b>1 + 2 + 1 = 4</b>. Resultado: <b>426</b> ✅"])
        + ""))

    # 16 — Abre cuaderno: 3 dígitos
    s.append(G.notebook_slide(
        'Resuelve en tu cuaderno: <b class="hl">365 + 248</b>',
        ["Unidades: 5 + 8 = 13 → 3 y llevo 1",
         "Decenas: 6 + 4 + 1 = 11 → 1 y llevo 1",
         "Centenas: 3 + 2 + 1 = 6",
         "Resultado: 613"]))

    # 17 — Ejercicios mixtos 3 dígitos
    s.append(G.exercise_cards_slide(
        "¡Suma de 3 dígitos!",
        "Algunos tienen reserva, otros no. ¡Tú decides!",
        [("🏆", "415 + 237", "= 652", "#FFE082"),
         ("🎵", "568 + 175", "= 743", "#9DDEFF"),
         ("🌈", "329 + 436", "= 765", "#E1BEE7")]))

    # 18 — Propiedades de la suma
    s.append(G.fact_boxes_slide(
        "Propiedades de la suma",
        "Estas reglas nos ayudan a calcular más rápido.",
        [("El orden no importa", "5 + 3 es igual a 3 + 5. ¡Da lo mismo quién va primero!", "#9DDEFF"),
         ("Suma con 0", "Cualquier número más 0 sigue siendo el mismo número.", "#FFE082"),
         ("Agrupación", "(2 + 3) + 4 = 2 + (3 + 4). Podemos agrupar como queramos.", "#9DE3BD")]))

    # 19 — Cálculo mental
    s.append(G.slide("""
        <div class="head-title">Estrategia: Sumar desde las decenas</div>
        <p class="sub-text">Una forma rápida de sumar: primero las decenas, luego las unidades.</p>
        <div class="decomp-flow">
            <div class="decomp-box">36 + 47</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">30 + 40 = 70</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">6 + 7 = 13</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">70 + 13 = 83</div>
        </div>
        <div class="stp warn-card" style="margin-top:16px;">Esta estrategia se llama <b>"descomposición"</b>. ¡Separamos el número en decenas y unidades!</div>"""))

    # 20 — Quiz 2
    s.append(G.quiz_slide(
        "¿Cuánto es?",
        '¿Cuál es el resultado de <b>256 + 387</b>?',
        ["533", "633", "643"], 1,
        "6+7=13 (3, llevo 1). 5+8+1=14 (4, llevo 1). 2+3+1=6. Resultado: 643."))

    # 21 — Problema real 1
    s.append(G.problem_slide(
        "La colección de figuritas", "🃏",
        "Tomás tiene <b>47 figuritas</b> y su hermana le regala <b>36 más</b>. ¿Cuántas tiene ahora?",
        "47 + 36 = 83<br><span style='color:var(--base);'>Tomás tiene ahora 83 figuritas.</span>",
        "#FFF8E1", "#F57F17"))

    # 22 — Problema real 2
    s.append(G.problem_slide(
        "Los libros de la biblioteca", "📖",
        "La biblioteca tiene <b>234 libros de cuentos</b> y <b>148 libros de ciencias</b>. ¿Cuántos libros hay en total?",
        "234 + 148 = 382<br><span style='color:var(--base);'>Hay 382 libros en total.</span>",
        "#E8F5E9", "#2E7D32"))

    # 23 — Problema real 3
    s.append(G.problem_slide(
        "Los pasajeros del bus", "🚌",
        "En la primera parada suben <b>35 personas</b> y en la segunda suben <b>48 más</b>. ¿Cuántas personas hay en el bus?",
        "35 + 48 = 83<br><span style='color:var(--base);'>Hay 83 personas en el bus.",
        "#E3F2FD", "#1565C0"))

    # 24 — Estrategia: redondear para estimar
    s.append(G.slide("""
        <div class="head-title">Estimación: ¿El resultado tiene sentido?</div>
        <p class="sub-text">Antes de calcular exacto, podemos <b class="hl">estimar</b> redondeando.</p>
        <div class="decomp-flow">
            <div class="decomp-box">48 + 33</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">≈ 50 + 30</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">≈ 80</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">Resultado real: 81 ✅</div>
        </div>
        <div class="stp warn-card" style="margin-top:16px;">Si redondeamos y obtenemos ~80, y nuestro resultado es 81, ¡está cerca! Si nos da 180, algo salió mal.</div>"""))

    # 25 — Abre cuaderno final
    s.append(G.notebook_slide(
        'Resuelve: <b class="hl">458 + 374</b> y estima primero.',
        ["Estimo: 460 + 370 ≈ 830",
         "Unidades: 8 + 4 = 12 → 2, llevo 1",
         "Decenas: 5 + 7 + 1 = 13 → 3, llevo 1",
         "Centenas: 4 + 3 + 1 = 8",
         "Resultado: 832 ✅ (¡cerca de 830!)"]))

    # 26 — Ejercicio combo
    s.append(G.exercise_cards_slide(
        "Suma de todo tipo — ¡desafío!",
        "Mezcla de 2 y 3 dígitos, con y sin reserva.",
        [("🔥", "87 + 56", "= 143", "#FFB74D"),
         ("⚡", "209 + 384", "= 593", "#9DDEFF"),
         ("🚀", "477 + 368", "= 845", "#E1BEE7")]))

    # 27 — Suma de más de 2 números
    s.append(G.slide("""
        <div class="head-title">¿Y si sumamos 3 números?</div>
        <p class="sub-text">Sumamos <b class="hl">de a dos</b>, paso a paso.</p>
        <div class="two-col">
            <div class="pnl-border">
                <div class="math-eq">24 + 31 + 15</div>
                <div class="stp step-box">Primero: 24 + 31 = 55</div>
                <div class="stp step-box">Luego: 55 + 15 = 70</div>
                <div class="stp math-eq">= 70</div>
            </div>
            <div class="warn-card stp">También podemos buscar pares que sumen 10 primero:<br><b>4 + 6 + 3 = 13</b> (busco 4+6=10 primero)</div>
        </div>"""))

    # 28 — Quiz final
    s.append(G.quiz_slide(
        "Quiz final — Suma",
        'Camila leyó <b>125 páginas</b> el lunes y <b>237 páginas</b> el martes. ¿Cuántas páginas leyó en total?',
        ["352", "362", "362"], 1,
        "125 + 237: unidades 5+7=12 (2, llevo 1), decenas 2+3+1=6, centenas 1+2=3. Total: 362 páginas."))

    # 29 — Problema integrador
    s.append(G.problem_slide(
        "El kiosco del colegio", "🛒",
        "El lunes el kiosco vendió <b>156 jugos</b>, el martes <b>234 jugos</b> y el miércoles <b>98 jugos</b>. ¿Cuántos jugos vendió en total esos tres días?",
        "156 + 234 = 390. Luego 390 + 98 = 488.<br><span style='color:var(--base);'>El kiosco vendió 488 jugos en total.</span>",
        "#FCE4EC", "#C2185B"))

    # 30 — Resumen
    s.append(G.summary_slide([
        "<b>Sin reserva:</b> Cuando U + U < 10. Sumamos columna por columna: U → D → C.",
        "<b>Con reserva:</b> Cuando U + U ≥ 10, escribimos la unidad y 'llevamos' 1 a las decenas.",
        "<b>Puede pasar también en D:</b> Si D + D ≥ 10, llevamos 1 a las centenas.",
        "<b>Propiedad:</b> El orden de los sumandos no cambia el resultado.",
        "<b>Comprueba:</b> Usa estimación para verificar que tu respuesta tiene sentido.",
    ]))

    assert len(s) == 30, f"Módulo 3B-1 tiene {len(s)} slides (necesita 30)"
    return G.html_doc("Suma hasta 100 — 3° Básico", s)


if __name__ == "__main__":
    out = OUT / "3B-clase1-suma.html"
    out.write_text(module(), encoding="utf-8")
    print(f"✅ Generado: {out}")
