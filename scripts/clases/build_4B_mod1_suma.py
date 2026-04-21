"""
Módulo 1: Suma completa (hasta 3 dígitos)
"""
from __future__ import annotations
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import generator_suma_resta as G

OUT = pathlib.Path("/Users/brunonattino/Desktop/PAGINA TUTORIAS/clases/suma-resta")

def module() -> str:
    s: list[str] = []

    s.append(G.intro_slide("Presentación 1: Suma", "Módulo de suma hasta 3 dígitos.", "➕"))

    s.append(G.picture_operation_slide(
        "¿Qué es sumar?",
        "Sumar es <b class=\"hl\">juntar</b> dos cantidades para formar una mayor.",
        "Tengo 6", G.emoji_pack("🟨", 6, 54),
        "Agrego 3", G.emoji_pack("🟩", 3, 54),
        "+", "6 + 3 = 9",
        "Siempre partimos de una base y agregamos algo nuevo.",
        "#FFE082", "#9DE3BD", "#E1BEE7"
    ))

    s.append(G.slide("""
        <div class="head-title">Unidades, Decenas y Centenas</div>
        <p class="sub-text">Para sumar números más grandes, usamos los valores posicionales y sus colores.</p>
        <div class="fact-grid">
            <div class="fact-box" style="border-color:#9DE3BD;">
                <h4 style="color:#388E3C;">🟢 Centenas (C)</h4>
                <p>Placas de 100 cubitos.</p>
            </div>
            <div class="fact-box stp" style="border-color:#9DDEFF;">
                <h4 style="color:#1976D2;">🔵 Decenas (D)</h4>
                <p>Barras de 10 cubitos.</p>
            </div>
            <div class="fact-box stp" style="border-color:#FFE082;">
                <h4 style="color:#F57F17;">🟡 Unidades (U)</h4>
                <p>Cubitos sueltos de 1.</p>
            </div>
        </div>
    """))

    s.append(G.slide("""
        <div class="head-title">Viendo los números grandes</div>
        <p class="sub-text">Así se ve un número de 3 dígitos con nuestros bloques a escala.</p>
        <div class="base-row">
            """ + G.base_ten_card(345, "345 = 3 centenas, 4 decenas y 5 unidades", ("#E1BEE7", "#9DE3BD", "#9DDEFF", "#FFE082")) + """
        </div>
    """))

    s.append(G.slide("""
        <div class="head-title">En columna (sin reserva)</div>
        <p class="sub-text">Alineamos los números y sumamos de derecha a izquierda: U → D → C.</p>
        """ + G.alg_board(
            [["", "_", "_", "_"],
             ["C D U", "1", "2", "3"],
             ["+", "2", "1", "4"],
             ["", "3", "3", "7"]],
            "Paso a paso",
            ["U: 3 + 4 = 7", "D: 2 + 1 = 3", "C: 1 + 2 = 3"]
        )
    ))

    s.append(G.notebook_slide(
        "Resuelve en columna: <b class=\"hl\">452 + 316</b>.",
        ["Unidades: 2 + 6 = 8", "Decenas: 5 + 1 = 6", "Centenas: 4 + 3 = 7", "Resultado: 768"]
    ))

    s.append(G.slide("""
        <div class="head-title">¿Qué es la reserva?</div>
        <p class="sub-text">Si al sumar juntamos 10 o más en una columna, <b class="hl">agrupamos 10</b> y los pasamos a la izquierda.</p>
        <div class="decomp-flow">
            <div class="decomp-box" style="border-color:#FFE082; color:#b08d1e;">13 Unidades</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp" style="border-color:#9DDEFF; color:#1C4A82;">1 Decena y <span style="color:#b08d1e;">3 Unidades</span></div>
        </div>
        <div class="stp warn-card" style="margin-top:18px;">
            ¡Ese es el <b>1</b> chiquitito que anotamos arriba de la siguiente columna!
        </div>
    """))

    s.append(G.slide("""
        <div class="head-title">Suma con reserva en las unidades</div>
        """ + G.alg_board(
            [["", "_", "r:1", "_"],
             ["C D U", "2", "4", "8"],
             ["+", "1", "3", "6"],
             ["", "3", "8", "4"]],
            "Explicación",
            ["U: 8 + 6 = 14. Escribo 4 unidades y reservo 1 decena.",
             "D: 4 + 3 + 1 (reserva) = 8.",
             "C: 2 + 1 = 3."]
        )
    ))

    s.append(G.slide("""
        <div class="head-title">Suma con doble reserva</div>
        <p class="sub-text">A veces se nos junta reserva en las unidades Y en las decenas.</p>
        """ + G.alg_board(
            [["", "r:1", "r:1", "_"],
             ["C D U", "3", "8", "7"],
             ["+", "2", "4", "5"],
             ["", "6", "3", "2"]],
            "Paso a paso",
            ["U: 7 + 5 = 12. Pongo 2 y reservo 1.",
             "D: 8 + 4 + 1 = 13. Pongo 3 y reservo 1.",
             "C: 3 + 2 + 1 = 6."]
        )
    ))

    s.append(G.notebook_slide(
        "Resuelve: <b class=\"hl\">456 + 289</b>",
        ["U: 6 + 9 = 15 (5 y reservo 1)", "D: 5 + 8 + 1 = 14 (4 y reservo 1)", "C: 4 + 2 + 1 = 7", "Resultado: 745"]
    ))

    s.append(G.slide("""
        <div class="head-title">¿Y si son 3 números?</div>
        <p class="sub-text">Sumamos todo en la misma columna. La reserva puede ser 2 en vez de 1.</p>
        """ + G.alg_board(
            [["", "r:1", "r:2", "_"],
             ["C D U", "1", "4", "8"],
             ["+", "2", "0", "5"],
             ["+", "3", "1", "9"],
             ["", "6", "7", "2"]],
            "Sumando tres",
            ["U: 8 + 5 + 9 = 22. Pongo 2 y reservo 2 decenas.",
             "D: 4 + 0 + 1 + 2 = 7.",
             "C: 1 + 2 + 3 = 6."]
        )
    ))

    s.append(G.quiz_slide(
        "Quiz de rapidez mental",
        "¿Cuánto es <b>647 + 285</b>?",
        ["832", "932", "922"],
        1,
        "7+5=12, reservo 1. 4+8+1=13, reservo 1. 6+2+1=9. Total: 932."
    ))

    s.append(G.ejercicios_propuestos(
        "Ejercicios Propuestos",
        "Copia en tu cuaderno y resuelve en columna. Tómate tu tiempo.",
        ["124 + 352", "408 + 291", "675 + 186", "532 + 254", "380 + 195", "416 + 288"]
    ))

    s.append(G.ejercicios_respuestas(
        "Respuestas",
        ["124 + 352 = 476", "408 + 291 = 699", "675 + 186 = 861", "532 + 254 = 786", "380 + 195 = 575", "416 + 288 = 704"]
    ))

    s.append(G.problem_slide("Los libros de la biblioteca", "📚", "El primer piso tiene 358 libros y el segundo tiene 479. ¿Cuántos hay en total?", "358 + 479 = 837.<br><span style='color:var(--base);'>Hay 837 libros en total.</span>", "#FFF8E1", "#F9A825"))
    s.append(G.problem_slide("Los puntos del juego", "🎮", "Lucas hizo 589 puntos en la primera ronda y 274 en la segunda. ¿Cuál es su puntaje total?", "589 + 274 = 863.<br><span style='color:var(--base);'>El puntaje total es 863.</span>", "#E8F5E9", "#2E7D32"))
    s.append(G.problem_slide("Ahorros de la familia", "💰", "Papá ahorró $450, mamá $320 y el hijo $185. ¿Cuánto ahorraron en total?", "450 + 320 + 185 = 955.<br><span style='color:var(--base);'>Ahorraron $955 en total.</span>", "#E3F2FD", "#1565C0"))
    
    s.append(G.summary_slide([
        "<b>Suma en columna:</b> Alineamos U con U, D con D, C con C.",
        "<b>Reserva:</b> Si sumo 10 o más, agrupo y paso la decena/centena a la columna de la izquierda.",
        "<b>Bloques a escala:</b> Visualmente, 10 unidades forman 1 decena y 10 decenas forman 1 centena."
    ]))
    
    s.append(G.finish_slide("¡Eres un experto sumando hasta 3 dígitos!", "🏆"))

    return G.html_doc("Módulo 1: Suma", s)

if __name__ == "__main__":
    out = OUT / "suma-resta-1.html"
    out.write_text(module(), encoding="utf-8")
    print(f"✅ Generado: {out}")
