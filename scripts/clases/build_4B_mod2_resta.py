"""
Módulo 2: Resta completa (hasta 3 dígitos)
"""
from __future__ import annotations
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import generator_suma_resta as G

OUT = pathlib.Path("/Users/brunonattino/Desktop/PAGINA TUTORIAS/clases/suma-resta")

def module() -> str:
    s: list[str] = []

    s.append(G.intro_slide("Presentación 2: Resta", "Módulo de resta hasta 3 dígitos.", "➖"))

    s.append(G.picture_operation_slide(
        "¿Qué es restar?",
        "Restar es <b class=\"hl\">quitar</b> o saber la diferencia entre dos cantidades.",
        "Tengo 7", G.emoji_pack("🟨", 7, 54),
        "Quito 3", G.emoji_pack("⬜", 3, 54),
        "−", "7 − 3 = 4",
        "Observamos lo que teníamos y quitamos la cantidad indicada.",
        "#FFE082", "#FF9D9D", "#9DE3BD"
    ))

    s.append(G.slide("""
        <div class="head-title">Elementos de la Resta</div>
        <div class="pnl-border" style="background:#f8fbff;">
            <div class="math-eq" style="font-size:62px;">25 − 14 = 11</div>
            <div class="stp chip-row">
                <div class="mini-chip">25 es el <b>minuendo</b> (lo que tengo).</div>
                <div class="mini-chip">14 es el <b>sustraendo</b> (lo que quito).</div>
                <div class="mini-chip">11 es la <b>diferencia</b> (lo que queda).</div>
            </div>
        </div>
    """))

    s.append(G.picture_operation_slide(
        "Resta sin pedir prestado",
        "Cuando el minuendo es mayor en todas las posiciones, restamos directo.",
        "345", G.flats(3) + G.rods(4) + G.unit_blocks(5),
        "123", G.flats(1) + G.rods(2) + G.unit_blocks(3),
        "−", "345 − 123 = 222",
        "Unidades: 5−3=2. Decenas: 4−2=2. Centenas: 3−1=2.",
        "#9DE3BD", "#FF9D9D", "#FFE082"
    ))

    s.append(G.slide("""
        <div class="head-title">En columna (sin desagrupar)</div>
        <p class="sub-text">Alineamos los números y restamos de derecha a izquierda: U → D → C.</p>
        """ + G.alg_board(
            [["", "_", "_", "_"],
             ["C D U", "5", "8", "6"],
             ["−", "2", "3", "4"],
             ["", "3", "5", "2"]],
            "Paso a paso",
            ["U: 6 − 4 = 2", "D: 8 − 3 = 5", "C: 5 − 2 = 3"]
        )
    ))

    s.append(G.slide("""
        <div class="head-title">¿Qué pasa si no alcanza?</div>
        <p class="sub-text">Si las unidades de arriba son menores que las de abajo, <b class="hl">desagrupamos</b>.</p>
        <div class="decomp-flow">
            <div class="decomp-box" style="border-color:#9DDEFF; color:#1C4A82;">1 Decena</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp" style="border-color:#FFE082; color:#b08d1e;">10 Unidades sueltas</div>
        </div>
        <div class="stp warn-card" style="margin-top:18px;">
            El número total no cambia, solo rompemos una barra para tener suficientes cubitos.
        </div>
    """))

    s.append(G.slide("""
        <div class="head-title">Desagrupar una Decena</div>
        """ + G.alg_board(
            [["", "_", "r:3", "r:12"],
             ["C D U", "2", "4", "2"],
             ["−", "1", "1", "5"],
             ["", "1", "2", "7"]],
            "Paso a paso",
            ["U: 2 no alcanza para quitar 5. Desagrupo 1 decena (quedan 3) y obtengo 12 unidades.",
             "U: 12 − 5 = 7.",
             "D: 3 − 1 = 2.",
             "C: 2 − 1 = 1."]
        )
    ))

    s.append(G.slide("""
        <div class="head-title">Desagrupar una Centena</div>
        """ + G.alg_board(
            [["", "r:2", "r:13", "_"],
             ["C D U", "3", "3", "6"],
             ["−", "1", "8", "4"],
             ["", "1", "5", "2"]],
            "Paso a paso",
            ["U: 6 − 4 = 2.",
             "D: 3 no alcanza para quitar 8. Desagrupo 1 centena (quedan 2) y obtengo 13 decenas.",
             "D: 13 − 8 = 5.",
             "C: 2 − 1 = 1."]
        )
    ))

    s.append(G.slide("""
        <div class="head-title">El caso del Cero</div>
        <p class="sub-text">Cuando las decenas son 0, tenemos que pedir a las centenas primero.</p>
        """ + G.alg_board(
            [["", "r:4", "r:9", "r:10"],
             ["C D U", "5", "0", "0"],
             ["−", "2", "3", "4"],
             ["", "2", "6", "6"]],
            "Cadena de desagrupación",
            ["U: 0 no alcanza. D es 0, no puede prestar. Pido a C.",
             "C: 5 pasa a 4. D pasa a 10.",
             "Ahora D presta a U: D pasa de 10 a 9. U pasa a 10.",
             "Restamos: 10−4=6, 9−3=6, 4−2=2."]
        )
    ))

    s.append(G.notebook_slide(
        "Resuelve: <b class=\"hl\">600 − 148</b>",
        ["6C 0D 0U → 5C 9D 10U", "U: 10 − 8 = 2", "D: 9 − 4 = 5", "C: 5 − 1 = 4", "Resultado: 452"]
    ))

    s.append(G.slide("""
        <div class="head-title">Comprobar con la suma</div>
        <p class="sub-text">Si sumas la diferencia con el sustraendo, debes obtener el minuendo original.</p>
        <div class="decomp-flow">
            <div class="decomp-box">345 − 128 = 217</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">Compruebo: 217 + 128</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">= 345 ✅</div>
        </div>
    """))

    s.append(G.quiz_slide(
        "Quiz rápido",
        "¿Cuánto es <b>402 − 157</b>?",
        ["245", "345", "255"],
        0,
        "4C0D2U → 3C9D12U. 12-7=5, 9-5=4, 3-1=2. Total: 245."
    ))

    s.append(G.ejercicios_propuestos(
        "Ejercicios Propuestos",
        "Copia en tu cuaderno y resuelve en columna. Tómate tu tiempo.",
        ["586 − 342", "735 − 289", "500 − 164", "840 − 315", "602 − 258", "911 − 488"]
    ))

    s.append(G.ejercicios_respuestas(
        "Respuestas",
        ["586 − 342 = 244", "735 − 289 = 446", "500 − 164 = 336", "840 − 315 = 525", "602 − 258 = 344", "911 − 488 = 423"]
    ))

    s.append(G.problem_slide("Billetes en la billetera", "💵", "Matías tenía $800 y compró un jugo por $450. ¿Cuánto le sobró?", "800 − 450 = 350.<br><span style='color:var(--base);'>Le sobraron $350.</span>", "#FFF8E1", "#F9A825"))
    s.append(G.problem_slide("Árboles en el parque", "🌳", "El parque tiene espacio para 500 árboles. Ya plantaron 234. ¿Cuántos faltan?", "500 − 234 = 266.<br><span style='color:var(--base);'>Faltan 266 árboles.</span>", "#E8F5E9", "#2E7D32"))
    s.append(G.problem_slide("Páginas del libro", "📖", "El libro tiene 412 páginas y he leído 187. ¿Cuántas me faltan?", "412 − 187 = 225.<br><span style='color:var(--base);'>Me faltan 225 páginas.</span>", "#E3F2FD", "#1565C0"))
    
    s.append(G.summary_slide([
        "<b>Resta en columna:</b> Siempre U con U, D con D, C con C.",
        "<b>Desagrupar:</b> Si el número de arriba es menor, pido prestado 10 al de la izquierda.",
        "<b>Ceros:</b> Si la columna es 0, pido prestado a la que sigue, rompiendo la placa 100 en 10 barras de 10.",
        "<b>Comprobar:</b> diferencia + sustraendo = minuendo."
    ]))
    
    s.append(G.finish_slide("¡Eres un experto restando hasta 3 dígitos!", "🏆"))

    return G.html_doc("Módulo 2: Resta", s)

if __name__ == "__main__":
    out = OUT / "suma-resta-2.html"
    out.write_text(module(), encoding="utf-8")
    print(f"✅ Generado: {out}")
