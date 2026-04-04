from __future__ import annotations

from pathlib import Path
import sys

ROOT_DIR = Path(__file__).resolve().parents[2]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from scripts.clases.generator_suma_resta import (
    CSS,
    JS,
    ROOT,
    alg_board,
    emoji_pack,
    esc,
    exercise_cards_slide,
    fact_boxes_slide,
    finish_slide,
    html_doc,
    intro_slide,
    notebook_slide,
    picture_operation_slide,
    problem_slide,
    quiz_slide,
    slide,
    summary_slide,
)


OUTPUT_DIR = ROOT / "clases" / "division"


def share_visual(total: int, groups: int, emoji: str, color: str = "#FFE082") -> str:
    per_group = total // groups
    boxes = []
    for idx in range(groups):
        boxes.append(
            f"""
            <div class="count-card stp" style="border-color:{color}; max-width:220px;">
                <h3>Grupo {idx + 1}</h3>
                <div class="emoji-pack">{emoji_pack(emoji, per_group, 48)}</div>
                <div class="mini-chip">{per_group} en cada grupo</div>
            </div>
            """
        )
    return f'<div class="count-board">{"".join(boxes)}</div>'


def remainder_visual(dividend: int, divisor: int, emoji: str, color: str = "#FFB74D", leftover_color: str = "#E1BEE7") -> str:
    q, r = divmod(dividend, divisor)
    boxes = []
    for idx in range(q):
        boxes.append(
            f"""
            <div class="count-card stp" style="border-color:{color}; max-width:210px;">
                <h3>Grupo {idx + 1}</h3>
                <div class="emoji-pack">{emoji_pack(emoji, divisor, 46)}</div>
            </div>
            """
        )
    left = ""
    if r:
        left = f"""
        <div class="count-card stp" style="border-color:{leftover_color}; max-width:240px; background:linear-gradient(180deg,#faf4ff 0%,#ffffff 100%);">
            <h3>Sobran</h3>
            <div class="emoji-pack">{emoji_pack(emoji, r, 46)}</div>
            <div class="mini-chip">Resto = {r}</div>
        </div>
        """
    return f'<div class="count-board">{"".join(boxes)}{left}</div>'


def division_parts_slide() -> str:
    return slide(
        """
        <div class="head-title">Partes de la división</div>
        <div class="pnl-border" style="background:#f8fbff;">
            <div class="formula-row" style="margin-bottom:16px;">
                <div class="label-pill stp">Dividendo</div>
                <div class="label-pill stp">Divisor</div>
                <div class="label-pill stp">Cociente</div>
                <div class="label-pill stp">Resto</div>
            </div>
            <div class="math-eq" style="font-size:58px;">17 ÷ 5 = 3 y sobra 2</div>
            <div class="stp fact-grid">
                <div class="fact-box" style="border-color:#FFE082;"><h4>17</h4><p>Es el <b>dividendo</b>: lo que vamos a repartir.</p></div>
                <div class="fact-box" style="border-color:#9DE3BD;"><h4>5</h4><p>Es el <b>divisor</b>: cuántos grupos o cuánto va en cada grupo.</p></div>
                <div class="fact-box" style="border-color:#FFB74D;"><h4>3</h4><p>Es el <b>cociente</b>: lo que alcanzó para cada grupo.</p></div>
                <div class="fact-box" style="border-color:#E1BEE7;"><h4>2</h4><p>Es el <b>resto</b>: lo que no alcanzó a repartirse.</p></div>
            </div>
        </div>
        """
    )


def long_division_slide(title: str, subtitle: str, dividend: int, divisor: int, quotient: int, side_notes: list[str]) -> str:
    digits = list(str(dividend))
    q_digits = list(str(quotient))
    top = ["_"] * max(0, len(digits) - len(q_digits)) + q_digits
    rows = [
        ["", *top[-3:]] if len(top) >= 3 else ["", *(['_'] * (3 - len(top)) + top)],
        ["÷", *digits[-3:]] if len(digits) >= 3 else ["÷", *(['_'] * (3 - len(digits)) + digits)],
        [str(divisor), "_", "_", "_"],
    ]
    return slide(
        f"""
        <div class="head-title">{esc(title)}</div>
        <p class="sub-text">{subtitle}</p>
        """ + alg_board(
            rows,
            "Cómo pensar",
            side_notes,
            long=True,
        )
    )


def module_one() -> str:
    slides: list[str] = []
    slides.append(intro_slide("¡División 1!", "Repartir en partes iguales, conectar multiplicación con división y entender dividendo, divisor, cociente y resto.", "🍊"))
    slides.append(
        picture_operation_slide(
            "¿Qué significa dividir?",
            "Dividir es <b class=\"hl\">repartir en partes iguales</b>.",
            "Tengo 12 naranjas",
            emoji_pack("🍊", 12, 46),
            "Las repartiré en 3 grupos",
            emoji_pack("🧺", 3, 56),
            "÷",
            "12 ÷ 3 = 4",
            "Si el reparto es justo, todos reciben la misma cantidad.",
            "#FFB74D",
            "#9DE3BD",
            "#FFE082",
        )
    )
    slides.append(
        slide(
            """
            <div class="head-title">Repartimos 12 en 3 grupos</div>
            <p class="sub-text">Cada grupo debe quedar con la <b class="hl">misma cantidad</b>.</p>
            """ + share_visual(12, 3, "🍊", "#FFE082") + """
            <div class="stp math-eq">12 ÷ 3 = 4</div>
            """
        )
    )
    slides.append(
        picture_operation_slide(
            "Otra situación de reparto",
            "Si tengo 15 caramelos y hago 5 bolsas iguales, ¿cuántos van en cada bolsa?",
            "15 caramelos",
            emoji_pack("🍬", 15, 44),
            "5 bolsas",
            emoji_pack("🛍️", 5, 54),
            "÷",
            "15 ÷ 5 = 3",
            "Cada bolsa recibe 3 caramelos.",
            "#E1BEE7",
            "#9DE3BD",
            "#FFB74D",
        )
    )
    slides.append(
        fact_boxes_slide(
            "Reglas del reparto justo",
            "En una división, estas ideas siempre importan.",
            [
                ("1. Igualdad", "Todos los grupos deben quedar con <b>la misma cantidad</b>.", "#FFE082"),
                ("2. Orden", "Primero miro cuánto tengo y cuántos grupos haré.", "#9DE3BD"),
                ("3. Revisión", "Al final compruebo si el reparto fue exacto.", "#E1BEE7"),
            ],
        )
    )
    slides.append(
        exercise_cards_slide(
            "Repartos exactos",
            "Observa y resuelve estos casos de reparto igualitario.",
            [
                ("🧁", "8 ÷ 2", "= 4", "#FFE082"),
                ("🍪", "18 ÷ 3", "= 6", "#9DE3BD"),
                ("⚽", "20 ÷ 5", "= 4", "#E1BEE7"),
            ],
        )
    )
    slides.append(
        picture_operation_slide(
            "Multiplicación y división son familia",
            "Si sé una multiplicación, puedo pensar la división relacionada.",
            "3 × 4",
            emoji_pack("⭐", 12, 42),
            "Repartido en 3 grupos",
            emoji_pack("🧺", 3, 54),
            "↔",
            "3 × 4 = 12 y 12 ÷ 3 = 4",
            "La división nos pregunta cuánto toca en cada grupo o cuántos grupos puedo formar.",
            "#FFE082",
            "#9DE3BD",
            "#FFB74D",
        )
    )
    slides.append(
        slide(
            """
            <div class="head-title">La familia de operaciones</div>
            <div class="pnl-border" style="background:linear-gradient(135deg,#fff7e8 0%,#f4fff8 50%,#faf4ff 100%);">
                <div class="math-eq" style="font-size:54px;">4 × 5 = 20</div>
                <div class="stp math-eq" style="font-size:46px;">20 ÷ 5 = 4</div>
                <div class="stp math-eq" style="font-size:46px;">20 ÷ 4 = 5</div>
                <div class="stp mini-chip">La multiplicación arma el total y la división lo reparte.</div>
            </div>
            """
        )
    )
    slides.append(
        exercise_cards_slide(
            "Pasa de multiplicación a división",
            "Usa la multiplicación conocida para encontrar la división.",
            [
                ("🌈", "5 × 2 = 10 → 10 ÷ 5", "= 2", "#FFB74D"),
                ("🧩", "4 × 3 = 12 → 12 ÷ 4", "= 3", "#9DE3BD"),
                ("🎈", "6 × 2 = 12 → 12 ÷ 2", "= 6", "#E1BEE7"),
            ],
        )
    )
    slides.append(division_parts_slide())
    slides.append(
        slide(
            """
            <div class="head-title">División exacta e inexacta</div>
            <div class="fact-grid">
                <div class="fact-box" style="border-color:#9DE3BD;">
                    <h4>Exacta</h4>
                    <p><b>12 ÷ 3 = 4</b><br>No sobra nada.</p>
                </div>
                <div class="fact-box" style="border-color:#E1BEE7;">
                    <h4>Inexacta</h4>
                    <p><b>14 ÷ 3 = 4 y sobra 2</b><br>Queda resto.</p>
                </div>
                <div class="fact-box" style="border-color:#FFE082;">
                    <h4>Idea clave</h4>
                    <p>El resto siempre debe ser <b>menor que el divisor</b>.</p>
                </div>
            </div>
            """
        )
    )
    slides.append(
        picture_operation_slide(
            "Dividir en 1",
            "Si divido en un solo grupo, todo queda junto en ese grupo.",
            "9 lápices",
            emoji_pack("✏️", 9, 48),
            "1 estuche",
            emoji_pack("🎒", 1, 62),
            "÷",
            "9 ÷ 1 = 9",
            "Dividir entre 1 deja la cantidad igual.",
            "#FFE082",
            "#9DE3BD",
            "#FFB74D",
        )
    )
    slides.append(
        fact_boxes_slide(
            "Reglas básicas de la división",
            "Estas reglas ayudan a empezar con seguridad.",
            [
                ("Dividir en 1", "Todo número dividido en <b>1</b> queda igual.", "#FFE082"),
                ("Dividirse a sí mismo", "Si no es 0, un número dividido por sí mismo da <b>1</b>.", "#9DE3BD"),
                ("Resto", "Si sobra, el resto debe ser <b>más pequeño</b> que el divisor.", "#E1BEE7"),
            ],
        )
    )
    slides.append(
        exercise_cards_slide(
            "Reglas en acción",
            "Practiquemos estas primeras reglas.",
            [
                ("🧮", "7 ÷ 1", "= 7", "#FFE082"),
                ("📦", "9 ÷ 9", "= 1", "#9DE3BD"),
                ("🍎", "16 ÷ 4", "= 4", "#E1BEE7"),
            ],
        )
    )
    slides.append(
        notebook_slide(
            "Abre tu cuaderno y resuelve: <b class=\"hl\">24 ÷ 6</b>.",
            ["Pienso: 6 × 4 = 24", "Entonces 24 ÷ 6 = 4"],
        )
    )
    slides.append(
        slide(
            """
            <div class="head-title">¿Cuántos grupos puedo formar?</div>
            <p class="sub-text">La división también puede preguntar por la <b class="hl">cantidad de grupos</b>.</p>
            <div class="count-board">
                <div class="count-card" style="border-color:#FFE082; max-width:260px;">
                    <h3>12 galletas</h3>
                    <div class="emoji-pack">""" + emoji_pack("🍪", 12, 44) + """</div>
                </div>
                <div class="count-card stp" style="border-color:#9DE3BD; max-width:260px;">
                    <h3>Grupos de 3</h3>
                    <div class="emoji-pack">""" + emoji_pack("🍪", 3, 44) + """</div>
                    <div class="mini-chip">Se forman 4 grupos</div>
                </div>
            </div>
            <div class="stp math-eq">12 ÷ 3 = 4 grupos</div>
            """
        )
    )
    slides.append(
        exercise_cards_slide(
            "Divisiones exactas para dominar",
            "Más práctica antes de avanzar.",
            [
                ("🍓", "21 ÷ 3", "= 7", "#FFB74D"),
                ("🚗", "24 ÷ 4", "= 6", "#9DE3BD"),
                ("🧸", "30 ÷ 5", "= 6", "#E1BEE7"),
            ],
        )
    )
    slides.append(
        exercise_cards_slide(
            "Otro set de práctica",
            "Sigue relacionando división y multiplicación.",
            [
                ("⭐", "32 ÷ 8", "= 4", "#FFE082"),
                ("🌟", "27 ÷ 9", "= 3", "#9DE3BD"),
                ("🎨", "18 ÷ 6", "= 3", "#E1BEE7"),
            ],
        )
    )
    slides.append(
        picture_operation_slide(
            "Otra división exacta visual",
            "Observa cómo se reparte el total en grupos iguales.",
            "24 estrellas",
            emoji_pack("⭐", 12, 42) + emoji_pack("⭐", 12, 42),
            "6 grupos",
            emoji_pack("🪣", 6, 50),
            "÷",
            "24 ÷ 6 = 4",
            "Cada grupo recibe 4 estrellas.",
            "#FFE082",
            "#9DE3BD",
            "#FFB74D",
        )
    )
    slides.append(
        exercise_cards_slide(
            "Más práctica exacta",
            "Un último grupo de ejercicios para consolidar.",
            [
                ("🧃", "28 ÷ 7", "= 4", "#FFB74D"),
                ("🍊", "36 ÷ 6", "= 6", "#9DE3BD"),
                ("📚", "45 ÷ 9", "= 5", "#E1BEE7"),
            ],
        )
    )
    slides.append(
        notebook_slide(
            "Abre tu cuaderno: <b class=\"hl\">32 ÷ 4</b>.",
            ["Pienso: 4 × 8 = 32", "Entonces 32 ÷ 4 = 8"],
        )
    )
    slides.append(
        quiz_slide(
            "Desafío rápido",
            "Si <b>5 × 4 = 20</b>, entonces <b>20 ÷ 5</b> es...",
            ["3", "4", "5"],
            1,
            "20 dividido en 5 grupos iguales da 4.",
        )
    )
    slides.append(
        notebook_slide(
            "Resuelve usando la familia de operaciones: <b class=\"hl\">18 ÷ 2</b>.",
            ["Pienso: 2 × 9 = 18", "Entonces 18 ÷ 2 = 9"],
        )
    )
    slides.append(
        problem_slide(
            "Jugo para el paseo",
            "🧃",
            "Hay <b>12 jugos</b> para repartir en <b>3 grupos</b> iguales. ¿Cuántos jugos recibe cada grupo?",
            "12 ÷ 3 = 4<br><span style='color:var(--base);'>Cada grupo recibe 4 jugos.</span>",
            "#FFF3E0",
            "#EF6C00",
        )
    )
    slides.append(
        problem_slide(
            "Lápices por mesa",
            "✏️",
            "Hay <b>20 lápices</b> y se reparten en <b>5 mesas</b> iguales. ¿Cuántos lápices van en cada mesa?",
            "20 ÷ 5 = 4<br><span style='color:var(--base);'>Van 4 lápices por mesa.</span>",
            "#E3F2FD",
            "#1565C0",
        )
    )
    slides.append(
        problem_slide(
            "Canastos de fruta",
            "🍐",
            "Se quieren armar canastos con <b>4 peras</b> cada uno. Si hay <b>16 peras</b>, ¿cuántos canastos se pueden formar?",
            "16 ÷ 4 = 4<br><span style='color:var(--base);'>Se pueden formar 4 canastos.</span>",
            "#E8F5E9",
            "#2E7D32",
        )
    )
    slides.append(
        problem_slide(
            "Piedras de colección",
            "🪨",
            "Tomás reparte <b>9 piedras</b> en <b>1 caja</b>. ¿Cuántas piedras quedan en la caja?",
            "9 ÷ 1 = 9<br><span style='color:var(--base);'>La caja tiene 9 piedras.</span>",
            "#F3E5F5",
            "#8E44AD",
        )
    )
    slides.append(
        problem_slide(
            "Galletas del recreo",
            "🍪",
            "Hay <b>24 galletas</b> y se reparten en <b>6 platos</b> iguales. ¿Cuántas galletas recibe cada plato?",
            "24 ÷ 6 = 4<br><span style='color:var(--base);'>Cada plato recibe 4 galletas.</span>",
            "#FFF8E1",
            "#F9A825",
        )
    )
    slides.append(
        summary_slide(
            [
                "<b>Dividir</b> es repartir en partes iguales.",
                "<b>Multiplicación y división</b> son operaciones relacionadas.",
                "<b>Dividendo, divisor, cociente y resto</b> son las partes de la división.",
                "<b>Dividir entre 1</b> deja la cantidad igual.",
            ]
        )
    )
    slides.append(finish_slide("Ya puedes repartir en partes iguales y leer una división con seguridad.", "🏆"))
    assert len(slides) == 30, len(slides)
    return html_doc("División 1", slides)


def module_two() -> str:
    slides: list[str] = []
    slides.append(intro_slide("¡División 2!", "División exacta e inexacta, resto y primeros cuocientes de dos dígitos.", "🧺"))
    slides.append(
        slide(
            """
            <div class="head-title">Recordemos la división exacta</div>
            <p class="sub-text">Una división es exacta cuando <b class="hl">no sobra nada</b>.</p>
            """ + share_visual(24, 6, "🍪", "#FFE082") + """
            <div class="stp math-eq">24 ÷ 6 = 4</div>
            """
        )
    )
    slides.append(
        slide(
            """
            <div class="head-title">¿Qué pasa si sobran objetos?</div>
            <p class="sub-text">Cuando no todo se puede repartir, aparece el <b class="hl">resto</b>.</p>
            """ + remainder_visual(14, 3, "🍎", "#9DE3BD", "#E1BEE7") + """
            <div class="stp math-eq">14 ÷ 3 = 4 y sobra 2</div>
            """
        )
    )
    slides.append(
        fact_boxes_slide(
            "Reglas del resto",
            "Para que la división tenga sentido, estas reglas deben cumplirse.",
            [
                ("Resto menor", "El resto siempre debe ser <b>menor</b> que el divisor.", "#FFE082"),
                ("Reparto máximo", "El cociente muestra cuánto sí alcanzó a repartirse.", "#9DE3BD"),
                ("Comprobación", "Divisor × cociente + resto = dividendo.", "#E1BEE7"),
            ],
        )
    )
    slides.append(
        slide(
            """
            <div class="head-title">Comprobamos una división con resto</div>
            <div class="pnl-border">
                <div class="math-eq">17 ÷ 5 = 3 y sobra 2</div>
                <div class="stp decomp-flow">
                    <div class="decomp-box">5 × 3 = 15</div>
                    <div class="arrow">→</div>
                    <div class="decomp-box">15 + 2 = 17</div>
                </div>
                <div class="stp mini-chip">Si la cuenta vuelve al dividendo, la división está bien revisada.</div>
            </div>
            """
        )
    )
    slides.append(
        exercise_cards_slide(
            "Divisiones con resto",
            "Lee el reparto y reconoce el resto.",
            [
                ("🍊", "14 ÷ 3", "= 4 r 2", "#FFB74D"),
                ("🍬", "17 ÷ 5", "= 3 r 2", "#9DE3BD"),
                ("🧁", "22 ÷ 4", "= 5 r 2", "#E1BEE7"),
            ],
        )
    )
    slides.append(
        slide(
            """
            <div class="head-title">Cuocientes de 2 dígitos</div>
            <p class="sub-text">A veces la respuesta de la división tiene <b class="hl">dos cifras</b>.</p>
            <div class="pnl-border">
                <div class="math-eq">48 ÷ 3 = 16</div>
                <div class="stp fact-grid">
                    <div class="fact-box" style="border-color:#FFE082;"><h4>3 × 10</h4><p>Sabemos que 3 × 10 = 30.</p></div>
                    <div class="fact-box" style="border-color:#9DE3BD;"><h4>Faltan 18</h4><p>Para llegar a 48 faltan 18.</p></div>
                    <div class="fact-box" style="border-color:#E1BEE7;"><h4>3 × 6</h4><p>3 × 6 = 18, entonces 10 + 6 = 16.</p></div>
                </div>
            </div>
            """
        )
    )
    slides.append(
        long_division_slide(
            "Primera división con cuociente de 2 dígitos",
            "Pensamos cuántas veces cabe el divisor en el dividendo.",
            48,
            3,
            16,
            [
                "3 cabe en 4 decenas al menos <b>1 decena</b> de veces.",
                "Después reviso cuánto falta para llegar a 48.",
                "Como 3 × 16 = 48, el cociente es <b>16</b>.",
            ],
        )
    )
    slides.append(
        exercise_cards_slide(
            "Cuocientes de 2 dígitos sin resto",
            "Primero practiquemos casos exactos.",
            [
                ("🚗", "48 ÷ 3", "= 16", "#FFE082"),
                ("📚", "72 ÷ 4", "= 18", "#9DE3BD"),
                ("⚽", "84 ÷ 6", "= 14", "#E1BEE7"),
            ],
        )
    )
    slides.append(
        notebook_slide(
            "Resuelve: <b class=\"hl\">96 ÷ 8</b>.",
            ["Pienso: 8 × 10 = 80", "Faltan 16", "8 × 2 = 16", "Resultado: 12"],
        )
    )
    slides.append(
        slide(
            """
            <div class="head-title">Otra división exacta</div>
            <p class="sub-text">Mira cómo aparece un cuociente de dos dígitos en una división exacta.</p>
            <div class="pnl-border">
                <div class="math-eq">75 ÷ 5 = 15</div>
                <div class="stp decomp-flow">
                    <div class="decomp-box">5 × 10 = 50</div>
                    <div class="arrow">→</div>
                    <div class="decomp-box">Faltan 25</div>
                    <div class="arrow">→</div>
                    <div class="decomp-box">5 × 5 = 25</div>
                    <div class="arrow">→</div>
                    <div class="decomp-box">10 + 5 = 15</div>
                </div>
            </div>
            """
        )
    )
    slides.append(
        exercise_cards_slide(
            "Más exactas con dos cifras",
            "Sigue practicando divisiones exactas.",
            [
                ("🧩", "75 ÷ 5", "= 15", "#FFB74D"),
                ("🎨", "63 ÷ 3", "= 21", "#9DE3BD"),
                ("🌈", "88 ÷ 4", "= 22", "#E1BEE7"),
            ],
        )
    )
    slides.append(
        quiz_slide(
            "Desafío exacto",
            "¿Cuál es el resultado de <b>72 ÷ 4</b>?",
            ["16", "18", "19"],
            1,
            "Porque 4 × 18 = 72.",
        )
    )
    slides.append(
        slide(
            """
            <div class="head-title">Cuocientes de 2 dígitos con resto</div>
            <p class="sub-text">Ahora la división no termina exacta y aparece un resto.</p>
            <div class="pnl-border">
                <div class="math-eq">58 ÷ 4 = 14 y sobra 2</div>
                <div class="stp decomp-flow">
                    <div class="decomp-box">4 × 10 = 40</div>
                    <div class="arrow">→</div>
                    <div class="decomp-box">Faltan 18</div>
                    <div class="arrow">→</div>
                    <div class="decomp-box">4 × 4 = 16</div>
                    <div class="arrow">→</div>
                    <div class="decomp-box">Sobran 2</div>
                </div>
            </div>
            """
        )
    )
    slides.append(
        slide(
            """
            <div class="head-title">Comprobamos otra vez</div>
            <div class="pnl-border">
                <div class="math-eq">58 ÷ 4 = 14 r 2</div>
                <div class="stp math-eq" style="font-size:46px;">4 × 14 + 2 = 58</div>
                <div class="stp mini-chip">Multiplico el divisor por el cociente y luego sumo el resto.</div>
            </div>
            """
        )
    )
    slides.append(
        exercise_cards_slide(
            "Divisiones con cuociente de 2 dígitos y resto",
            "Ahora ya aparecen dos cifras y sobra algo.",
            [
                ("🍪", "58 ÷ 4", "= 14 r 2", "#FFE082"),
                ("📦", "67 ÷ 5", "= 13 r 2", "#9DE3BD"),
                ("🚲", "95 ÷ 6", "= 15 r 5", "#E1BEE7"),
            ],
        )
    )
    slides.append(
        notebook_slide(
            "Abre tu cuaderno: <b class=\"hl\">73 ÷ 6</b>.",
            ["6 × 10 = 60", "Faltan 13", "6 × 2 = 12", "Resultado: 12 y sobra 1"],
        )
    )
    visual_73_6 = remainder_visual(73, 6, "🟣")
    slides.append(
        slide(
            f"""
            <div class="head-title">Visualizamos 73 ÷ 6</div>
            <p class="sub-text">Se forman grupos completos y luego miramos qué sobra.</p>
            {visual_73_6}
            <div class="stp math-eq">73 ÷ 6 = 12 y sobra 1</div>
            """
        )
    )
    slides.append(
        exercise_cards_slide(
            "Práctica mezclada",
            "Decide si la división es exacta o inexacta.",
            [
                ("⭐", "64 ÷ 8", "= 8", "#FFB74D"),
                ("🍎", "70 ÷ 6", "= 11 r 4", "#9DE3BD"),
                ("🎈", "81 ÷ 7", "= 11 r 4", "#E1BEE7"),
            ],
        )
    )
    slides.append(
        fact_boxes_slide(
            "Cómo leer una división inexacta",
            "No solo decimos el cociente: también nombramos el resto.",
            [
                ("Ejemplo", "67 ÷ 5 = <b>13 y sobra 2</b>.", "#FFE082"),
                ("No sirve decir solo 13", "Porque todavía quedaron <b>2</b> sin repartir.", "#9DE3BD"),
                ("Comprobación", "5 × 13 + 2 = 67.", "#E1BEE7"),
            ],
        )
    )
    slides.append(
        exercise_cards_slide(
            "Más cuocientes de 2 dígitos",
            "Sigue practicando divisiones exactas e inexactas.",
            [
                ("🧁", "84 ÷ 4", "= 21", "#FFE082"),
                ("🎒", "66 ÷ 5", "= 13 r 1", "#9DE3BD"),
                ("🚀", "91 ÷ 7", "= 13", "#E1BEE7"),
            ],
        )
    )
    slides.append(
        notebook_slide(
            "Abre tu cuaderno: <b class=\"hl\">84 ÷ 4</b>.",
            ["4 × 20 = 80", "Faltan 4", "4 × 1 = 4", "Resultado: 21"],
        )
    )
    slides.append(
        quiz_slide(
            "Desafío con resto",
            "En <b>58 ÷ 4 = 14 r 2</b>, el resto es...",
            ["2", "4", "14"],
            0,
            "El resto es 2.",
        )
    )
    slides.append(
        problem_slide(
            "Equipos de fútbol",
            "⚽",
            "Hay <b>48 niños</b> y se forman <b>3 equipos iguales</b>. ¿Cuántos niños van en cada equipo?",
            "48 ÷ 3 = 16<br><span style='color:var(--base);'>Van 16 niños por equipo.</span>",
            "#E3F2FD",
            "#1565C0",
        )
    )
    slides.append(
        problem_slide(
            "Bolsitas de dulces",
            "🍬",
            "Hay <b>58 dulces</b> y se reparten en <b>4 bolsitas</b> iguales. ¿Cuántos van en cada bolsita y cuántos sobran?",
            "58 ÷ 4 = 14 y sobran 2<br><span style='color:var(--base);'>Cada bolsita tiene 14 y sobran 2.</span>",
            "#FFF3E0",
            "#EF6C00",
        )
    )
    slides.append(
        problem_slide(
            "Cajas de cuadernos",
            "📘",
            "Una librería reparte <b>75 cuadernos</b> en <b>5 cajas</b> iguales. ¿Cuántos cuadernos van en cada caja?",
            "75 ÷ 5 = 15<br><span style='color:var(--base);'>Van 15 cuadernos por caja.</span>",
            "#E8F5E9",
            "#2E7D32",
        )
    )
    slides.append(
        problem_slide(
            "Pulseras con cuentas",
            "🟣",
            "Hay <b>66 cuentas</b> y se hacen pulseras de <b>5 cuentas</b>. ¿Cuántas pulseras completas salen y cuántas cuentas sobran?",
            "66 ÷ 5 = 13 y sobra 1<br><span style='color:var(--base);'>Salen 13 pulseras y sobra 1 cuenta.</span>",
            "#F3E5F5",
            "#8E44AD",
        )
    )
    slides.append(
        problem_slide(
            "Asientos del bus",
            "🚌",
            "Hay <b>73 pasajeros</b> y se sientan en filas de <b>6</b>. ¿Cuántas filas completas se llenan y cuántas personas quedan sin fila completa?",
            "73 ÷ 6 = 12 y sobra 1<br><span style='color:var(--base);'>Se llenan 12 filas y sobra 1 pasajero.</span>",
            "#F3E5F5",
            "#8E44AD",
        )
    )
    slides.append(
        summary_slide(
            [
                "<b>División exacta</b>: no sobra nada.",
                "<b>División inexacta</b>: aparece un resto.",
                "<b>Cuocientes de 2 dígitos</b>: la respuesta puede tener dos cifras.",
                "<b>Comprobación</b>: divisor × cociente + resto = dividendo.",
            ]
        )
    )
    slides.append(finish_slide("Ya puedes reconocer restos y resolver divisiones con cuocientes de dos dígitos.", "🚀"))
    assert len(slides) == 30, len(slides)
    return html_doc("División 2", slides)


def module_three() -> str:
    slides: list[str] = []
    slides.append(intro_slide("¡División 3!", "Dividir por descomposición y estimar cuocientes para resolver ejercicios con más estrategia.", "🧠"))
    slides.append(
        slide(
            """
            <div class="head-title">¿Qué es dividir por descomposición?</div>
            <p class="sub-text">Separamos el dividendo en partes más fáciles de dividir.</p>
            <div class="decomp-flow">
                <div class="decomp-box">84 ÷ 4</div>
                <div class="arrow stp">→</div>
                <div class="decomp-box stp">(80 ÷ 4) + (4 ÷ 4)</div>
                <div class="arrow stp">→</div>
                <div class="decomp-box stp">20 + 1</div>
                <div class="arrow stp">→</div>
                <div class="decomp-box stp">21</div>
            </div>
            """
        )
    )
    slides.append(
        picture_operation_slide(
            "Descomposición visual",
            "El 84 se puede mirar como 80 y 4.",
            "80",
            emoji_pack("🟨", 8, 50),
            "4",
            emoji_pack("🟣", 4, 50),
            "÷",
            "84 ÷ 4 = 21",
            "80 ÷ 4 = 20 y 4 ÷ 4 = 1.",
            "#FFE082",
            "#E1BEE7",
            "#9DE3BD",
        )
    )
    slides.append(
        exercise_cards_slide(
            "Descomponiendo divisiones exactas",
            "Resuelve separando el dividendo en partes fáciles.",
            [
                ("🎯", "84 ÷ 4", "= 21", "#FFE082"),
                ("📦", "96 ÷ 3", "= 32", "#9DE3BD"),
                ("🚗", "72 ÷ 6", "= 12", "#E1BEE7"),
            ],
        )
    )
    slides.append(
        slide(
            """
            <div class="head-title">Otro ejemplo de descomposición</div>
            <div class="pnl-border">
                <div class="math-eq">96 ÷ 3</div>
                <div class="stp decomp-flow">
                    <div class="decomp-box">90 ÷ 3 = 30</div>
                    <div class="arrow">+</div>
                    <div class="decomp-box">6 ÷ 3 = 2</div>
                    <div class="arrow">→</div>
                    <div class="decomp-box">32</div>
                </div>
                <div class="stp mini-chip">Descompongo el 96 en 90 y 6 porque ambos se pueden dividir fácil por 3.</div>
            </div>
            """
        )
    )
    slides.append(
        notebook_slide(
            "Abre tu cuaderno: <b class=\"hl\">63 ÷ 3</b>.",
            ["60 ÷ 3 = 20", "3 ÷ 3 = 1", "20 + 1 = 21"],
        )
    )
    slides.append(
        slide(
            """
            <div class="head-title">Cuando no es exacta</div>
            <p class="sub-text">También puedo descomponer y luego mirar qué sobra.</p>
            <div class="decomp-flow">
                <div class="decomp-box">95 ÷ 6</div>
                <div class="arrow stp">→</div>
                <div class="decomp-box stp">60 ÷ 6 = 10</div>
                <div class="arrow stp">+</div>
                <div class="decomp-box stp">30 ÷ 6 = 5</div>
                <div class="arrow stp">→</div>
                <div class="decomp-box stp">Quedan 5</div>
            </div>
            <div class="stp math-eq">95 ÷ 6 = 15 y sobra 5</div>
            """
        )
    )
    slides.append(
        exercise_cards_slide(
            "Descomposición con resto",
            "Resuelve por partes y después revisa el resto.",
            [
                ("🍎", "95 ÷ 6", "= 15 r 5", "#FFB74D"),
                ("⚽", "67 ÷ 4", "= 16 r 3", "#9DE3BD"),
                ("🧁", "52 ÷ 5", "= 10 r 2", "#E1BEE7"),
            ],
        )
    )
    slides.append(
        fact_boxes_slide(
            "Elegimos una buena descomposición",
            "La idea es partir el dividendo en números que sí se dejen dividir.",
            [
                ("84 ÷ 4", "Conviene usar <b>80 y 4</b>.", "#FFE082"),
                ("96 ÷ 3", "Conviene usar <b>90 y 6</b>.", "#9DE3BD"),
                ("95 ÷ 6", "Conviene usar <b>60 y 30</b>, y luego mirar lo que sobra.", "#E1BEE7"),
            ],
        )
    )
    slides.append(
        quiz_slide(
            "Desafío por descomposición",
            "Si <b>84 ÷ 4</b> se separa como <b>80 ÷ 4</b> y <b>4 ÷ 4</b>, el resultado es...",
            ["20", "21", "24"],
            1,
            "20 + 1 = 21.",
        )
    )
    slides.append(
        slide(
            """
            <div class="head-title">¿Qué es estimar un cuociente?</div>
            <p class="sub-text">Estimamos para saber <b class="hl">más o menos</b> cuántas veces cabe el divisor.</p>
            <div class="decomp-flow">
                <div class="decomp-box">92 ÷ 4</div>
                <div class="arrow stp">→</div>
                <div class="decomp-box stp">92 está cerca de 80 o 100</div>
                <div class="arrow stp">→</div>
                <div class="decomp-box stp">4 × 20 = 80</div>
                <div class="arrow stp">→</div>
                <div class="decomp-box stp">El cuociente estará cerca de 20</div>
            </div>
            """
        )
    )
    slides.append(
        slide(
            """
            <div class="head-title">Estimamos y luego ajustamos</div>
            <div class="pnl-border">
                <div class="math-eq">92 ÷ 4</div>
                <div class="stp step-box">Estimación: 4 × 20 = 80. Entonces el cuociente será un poco mayor que 20.</div>
                <div class="stp step-box">Ajuste: 4 × 23 = 92.</div>
                <div class="stp math-eq">92 ÷ 4 = 23</div>
            </div>
            """
        )
    )
    slides.append(
        exercise_cards_slide(
            "Estimamos cuocientes exactos",
            "Primero adivina cerca de cuánto será y luego confirma.",
            [
                ("🎈", "92 ÷ 4", "= 23", "#FFE082"),
                ("📚", "88 ÷ 4", "= 22", "#9DE3BD"),
                ("🌈", "96 ÷ 8", "= 12", "#E1BEE7"),
            ],
        )
    )
    slides.append(
        slide(
            """
            <div class="head-title">Estimación con resto</div>
            <div class="pnl-border">
                <div class="math-eq">77 ÷ 6</div>
                <div class="stp step-box">Estimación: 6 × 10 = 60. El cuociente será un poco mayor que 10.</div>
                <div class="stp step-box">Pruebo: 6 × 12 = 72. Sobran 5.</div>
                <div class="stp math-eq">77 ÷ 6 = 12 y sobra 5</div>
            </div>
            """
        )
    )
    slides.append(
        notebook_slide(
            "Abre tu cuaderno: <b class=\"hl\">77 ÷ 6</b>.",
            ["6 × 10 = 60", "Quedan 17", "6 × 2 = 12", "Resultado: 12 y sobra 5"],
        )
    )
    slides.append(
        exercise_cards_slide(
            "Estimaciones con resto",
            "Adivina primero y corrige después.",
            [
                ("🧩", "77 ÷ 6", "= 12 r 5", "#FFB74D"),
                ("🚲", "85 ÷ 7", "= 12 r 1", "#9DE3BD"),
                ("🍪", "94 ÷ 8", "= 11 r 6", "#E1BEE7"),
            ],
        )
    )
    slides.append(
        long_division_slide(
            "Unimos estimación y división",
            "La estimación da una pista para el cociente.",
            92,
            4,
            23,
            [
                "Primero pienso: 4 × 20 = 80. El resultado será cercano a <b>20</b>.",
                "Luego pruebo un poco más: 4 × 23 = 92.",
                "Así sé que el cuociente exacto es <b>23</b>.",
            ],
        )
    )
    slides.append(
        fact_boxes_slide(
            "Pistas para estimar bien",
            "Estas ideas ayudan a no probar números al azar.",
            [
                ("Redondea", "Busca un múltiplo cercano del divisor.", "#FFE082"),
                ("Compara", "Si 4 × 20 = 80, entonces 92 ÷ 4 será mayor que 20.", "#9DE3BD"),
                ("Ajusta", "Sube o baja hasta encontrar el cuociente que sí sirve.", "#E1BEE7"),
            ],
        )
    )
    slides.append(
        exercise_cards_slide(
            "Descomposición más estimación",
            "Ahora mezcla ambas estrategias.",
            [
                ("📦", "84 ÷ 4", "= 21", "#FFE082"),
                ("🎯", "92 ÷ 4", "= 23", "#9DE3BD"),
                ("🟣", "77 ÷ 6", "= 12 r 5", "#E1BEE7"),
            ],
        )
    )
    slides.append(
        notebook_slide(
            "Resuelve estimando y ajustando: <b class=\"hl\">92 ÷ 4</b>.",
            ["4 × 20 = 80", "4 × 23 = 92", "Resultado: 23"],
        )
    )
    slides.append(
        slide(
            """
            <div class="head-title">Ejemplo completo</div>
            <div class="pnl-border">
                <div class="math-eq">67 ÷ 4</div>
                <div class="stp step-box">Estimación: 4 × 10 = 40, así que el cuociente será mayor que 10.</div>
                <div class="stp step-box">Descomposición: 40 ÷ 4 = 10 y 24 ÷ 4 = 6.</div>
                <div class="stp step-box">Llevamos 16 y quedan 3.</div>
                <div class="stp math-eq">67 ÷ 4 = 16 y sobra 3</div>
            </div>
            """
        )
    )
    slides.append(
        quiz_slide(
            "Desafío de estrategia",
            "En <b>92 ÷ 4</b>, una buena estimación inicial para el cuociente es...",
            ["20", "4", "40"],
            0,
            "Porque 4 × 20 = 80 y 92 está cerca de 80.",
        )
    )
    slides.append(
        notebook_slide(
            "Resuelve estimando y ajustando: <b class=\"hl\">85 ÷ 7</b>.",
            ["7 × 10 = 70", "7 × 12 = 84", "Resultado: 12 y sobra 1"],
        )
    )
    slides.append(
        exercise_cards_slide(
            "Ejercicios finales de estrategia",
            "Ya puedes combinar descomposición y estimación.",
            [
                ("🚌", "85 ÷ 7", "= 12 r 1", "#FFE082"),
                ("🍓", "99 ÷ 9", "= 11", "#9DE3BD"),
                ("🎨", "94 ÷ 8", "= 11 r 6", "#E1BEE7"),
            ],
        )
    )
    slides.append(
        problem_slide(
            "Asientos del cine",
            "🎬",
            "Hay <b>92 personas</b> y se sientan en filas de <b>4</b>. ¿Cuántas filas completas se llenan?",
            "92 ÷ 4 = 23<br><span style='color:var(--base);'>Se llenan 23 filas completas.</span>",
            "#E3F2FD",
            "#1565C0",
        )
    )
    slides.append(
        problem_slide(
            "Bolsas de papas",
            "🥔",
            "Hay <b>77 papas</b> para poner en bolsas de <b>6</b>. ¿Cuántas bolsas completas se llenan y cuántas papas sobran?",
            "77 ÷ 6 = 12 y sobra 5<br><span style='color:var(--base);'>Se llenan 12 bolsas y sobran 5 papas.</span>",
            "#FFF3E0",
            "#EF6C00",
        )
    )
    slides.append(
        problem_slide(
            "Láminas del álbum",
            "🎴",
            "Un niño tiene <b>84 láminas</b> y las guarda en páginas de <b>4</b>. ¿Cuántas páginas completas ocupa?",
            "84 ÷ 4 = 21<br><span style='color:var(--base);'>Ocupa 21 páginas completas.</span>",
            "#E8F5E9",
            "#2E7D32",
        )
    )
    slides.append(
        problem_slide(
            "Pulseras de colores",
            "🟣",
            "Hay <b>67 cuentas</b> y se hacen pulseras de <b>4</b> cuentas cada una. ¿Cuántas pulseras completas salen y cuántas cuentas sobran?",
            "67 ÷ 4 = 16 y sobra 3<br><span style='color:var(--base);'>Salen 16 pulseras y sobran 3 cuentas.</span>",
            "#F3E5F5",
            "#8E44AD",
        )
    )
    slides.append(
        summary_slide(
            [
                "<b>Descomponer</b> ayuda a dividir números grandes en partes fáciles.",
                "<b>Estimar cuocientes</b> da una pista para empezar mejor.",
                "<b>Ajustar</b> significa probar un poco más o un poco menos hasta llegar al resultado.",
                "<b>Con resto</b>, seguimos comprobando con divisor × cociente + resto.",
            ]
        )
    )
    slides.append(finish_slide("Ya puedes resolver divisiones pensando, estimando y descomponiendo con más estrategia.", "🌟"))
    assert len(slides) == 30, len(slides)
    return html_doc("División 3", slides)


def generate_all() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    files = {
        "division-1.html": module_one(),
        "division-2.html": module_two(),
        "division-3.html": module_three(),
    }
    for name, content in files.items():
        (OUTPUT_DIR / name).write_text(content, encoding="utf-8")
        print(f"Generado: {OUTPUT_DIR / name}")


if __name__ == "__main__":
    generate_all()
