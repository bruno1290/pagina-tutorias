"""
Módulo 3: Suma y Resta Avanzada (hasta 4 dígitos + Combinadas)
"""
from __future__ import annotations
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import generator_suma_resta as G

OUT = pathlib.Path("/Users/brunonattino/Desktop/PAGINA TUTORIAS/clases/suma-resta")

def module() -> str:
    s: list[str] = []

    s.append(G.intro_slide("Presentación 3: Suma y Resta", "Módulo avanzado con miles y problemas combinados.", "🌟"))

    s.append(G.slide("""
        <div class="head-title">Conoce la Unidad de Mil</div>
        <p class="sub-text">Si juntamos 10 centenas, formamos un bloque gigante: <b class="hl">1 Unidad de Mil</b>.</p>
        <div class="fact-grid">
            <div class="fact-box" style="border-color:#388E3C;">
                <h4 style="color:#388E3C;">10 Centenas (C)</h4>
                <div class="block-stack">""" + G.flats(10, "#9DE3BD") + """</div>
            </div>
            <div class="fact-box stp" style="border-color:#7B1FA2;">
                <h4 style="color:#7B1FA2;">1 Unidad de Mil (UM)</h4>
                <div class="block-stack" style="margin-top:20px;">""" + G.cube_3d(1, "#E1BEE7") + """</div>
                <p>Equivale a 1.000 unidades.</p>
            </div>
        </div>
    """))

    s.append(G.slide("""
        <div class="head-title">Números de 4 dígitos</div>
        <p class="sub-text">Así se ve un número grande con todos nuestros bloques posicionales.</p>
        <div class="base-row">
            """ + G.base_ten_card(1245, "1.245 = 1 UM, 2 C, 4 D, 5 U", ("#E1BEE7", "#9DE3BD", "#9DDEFF", "#FFE082")) + """
        </div>
    """))

    s.append(G.slide("""
        <div class="head-title">Suma de miles</div>
        <p class="sub-text">Funciona exactamente igual, solo agregamos una columna más para los miles.</p>
        """ + G.alg_board(
            [["", "_", "_", "_", "_"],
             ["UM C D U", "1", "2", "3", "4"],
             ["+", "2", "1", "4", "5"],
             ["", "3", "3", "7", "9"]],
            "Paso a paso",
            ["U: 4+5=9", "D: 3+4=7", "C: 2+1=3", "UM: 1+2=3"]
        )
    ))

    s.append(G.slide("""
        <div class="head-title">Reserva hacia los miles</div>
        <p class="sub-text">Si juntamos 10 centenas, agrupamos y pasamos 1 Unidad de Mil a la siguiente columna.</p>
        """ + G.alg_board(
            [["", "r:1", "_", "_", "_"],
             ["UM C D U", "3", "8", "4", "2"],
             ["+", "1", "5", "1", "6"],
             ["", "5", "3", "5", "8"]],
            "Explicación",
            ["U: 2+6=8. D: 4+1=5.",
             "C: 8+5=13. Escribo 3 centenas y reservo 1 Unidad de Mil.",
             "UM: 3+1+1 (reserva) = 5."]
        )
    ))

    s.append(G.notebook_slide(
        "Suma en columna: <b class=\"hl\">4.560 + 2.830</b>",
        ["U: 0+0=0", "D: 6+3=9", "C: 5+8=13 (reservo 1)", "UM: 4+2+1=7", "Resultado: 7.390"]
    ))

    s.append(G.slide("""
        <div class="head-title">Resta de miles con desagrupación</div>
        <p class="sub-text">Si nos faltan centenas, podemos pedir prestado a la Unidad de Mil.</p>
        """ + G.alg_board(
            [["", "r:2", "r:14", "_", "_"],
             ["UM C D U", "3", "4", "5", "8"],
             ["−", "1", "6", "2", "4"],
             ["", "1", "8", "3", "4"]],
            "Desagrupación",
            ["U: 8-4=4. D: 5-2=3.",
             "C: 4 no alcanza para quitar 6. Pido 1 UM. Quedan 2 UM y me dan 10 centenas.",
             "C: 14-6=8.",
             "UM: 2-1=1. Total: 1.834"]
        )
    ))

    s.append(G.slide("""
        <div class="head-title">Resta con ceros en miles</div>
        <p class="sub-text">La cadena de ceros puede llegar hasta la Unidad de Mil.</p>
        """ + G.alg_board(
            [["", "r:4", "r:9", "r:9", "r:10"],
             ["UM C D U", "5", "0", "0", "0"],
             ["−", "1", "2", "3", "4"],
             ["", "3", "7", "6", "6"]],
            "Paso a paso",
            ["Pido prestado en cadena desde la Unidad de Mil hasta las Unidades.",
             "U: 10-4=6. D: 9-3=6. C: 9-2=7. UM: 4-1=3.",
             "Total: 3.766"]
        )
    ))

    s.append(G.notebook_slide(
        "Resta en columna: <b class=\"hl\">3.000 − 1.450</b>",
        ["U: 0-0=0", "La cadena empieza para las D y C", "D: 10-5=5", "C: 9-4=5", "UM: 2-1=1", "Resultado: 1.550"]
    ))

    s.append(G.slide("""
        <div class="head-title">Operaciones Combinadas (+ y -)</div>
        <p class="sub-text">¿Qué hacemos si hay suma y resta en el mismo ejercicio?</p>
        <div class="decomp-flow">
            <div class="decomp-box">500 + 300 − 200</div>
        </div>
        <div class="stp warn-card" style="margin-top:18px;">
            <b>Regla de Oro:</b> Resolvemos siempre de <b>izquierda a derecha</b>, un paso a la vez.
        </div>
    """))

    s.append(G.slide("""
        <div class="head-title">Combinada: Paso a paso</div>
        <div class="decomp-flow">
            <div class="decomp-box">450 + 200 − 150</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">Paso 1: 450 + 200 = 650</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">Paso 2: 650 − 150</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">= 500</div>
        </div>
    """))

    s.append(G.slide("""
        <div class="head-title">Con más dificultad (3 dígitos)</div>
        <p class="sub-text">Puedes hacer la operación en columna en una hoja de borrador para cada paso.</p>
        <div class="decomp-flow">
            <div class="decomp-box">342 − 185 + 230</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">Paso 1: 342 − 185 = 157</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">Paso 2: 157 + 230</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">= 387</div>
        </div>
    """))

    s.append(G.notebook_slide(
        "Resuelve: <b class=\"hl\">560 − 240 + 120</b>",
        ["Paso 1: 560 − 240 = 320", "Paso 2: 320 + 120 = 440", "Resultado final: 440"]
    ))

    s.append(G.slide("""
        <div class="head-title">Combinadas de 4 dígitos</div>
        <p class="sub-text">La regla de izquierda a derecha aplica siempre, sin importar qué tan grande sea el número.</p>
        <div class="decomp-flow">
            <div class="decomp-box">2.500 + 1.200 − 800</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">2.500 + 1.200 = 3.700</div>
            <div class="arrow stp">→</div>
            <div class="decomp-box stp">3.700 − 800 = 2.900</div>
        </div>
    """))

    s.append(G.quiz_slide(
        "Quiz de jerarquía",
        "¿Qué resuelvo primero en <b>1.000 − 300 + 500</b>?",
        ["1.000 − 300", "300 + 500", "Puedo empezar por cualquiera"],
        0,
        "Siempre de izquierda a derecha. Primero 1.000 − 300 = 700."
    ))

    s.append(G.ejercicios_propuestos(
        "Ejercicios Propuestos",
        "Copia en tu cuaderno y resuelve paso a paso de izquierda a derecha.",
        ["2.000 + 1.500", "4.000 − 1.250", "850 − 200 + 150", "3.400 + 1.200", "5.000 − 2.800", "1.200 − 400 + 300"]
    ))

    s.append(G.ejercicios_respuestas(
        "Respuestas",
        ["2.000 + 1.500 = 3.500", "4.000 − 1.250 = 2.750", "850 − 200 + 150 = 800", "3.400 + 1.200 = 4.600", "5.000 − 2.800 = 2.200", "1.200 − 400 + 300 = 1.100"]
    ))

    s.append(G.problem_slide("La tienda de ropa", "👕", "Una tienda vendió $2.500 y luego tuvo que devolver $400. Más tarde vendió $1.200. ¿Cuánto ganó en total?", "2.500 - 400 = 2.100.<br>2.100 + 1.200 = 3.300.<br><span style='color:var(--base);'>Ganó $3.300 en total.</span>", "#FFF8E1", "#F9A825"))
    s.append(G.problem_slide("Pasajeros del tren", "🚂", "El tren llevaba 1.250 pasajeros. Bajaron 300 en la primera estación y subieron 150. ¿Cuántos pasajeros hay ahora?", "1.250 - 300 = 950.<br>950 + 150 = 1.100.<br><span style='color:var(--base);'>Hay 1.100 pasajeros.</span>", "#E8F5E9", "#2E7D32"))
    s.append(G.problem_slide("Cosecha de manzanas", "🍎", "Recolectamos 3.500 manzanas, pero 250 estaban malas. Luego recolectamos 1.000 más. ¿Cuántas buenas tenemos?", "3.500 - 250 = 3.250.<br>3.250 + 1.000 = 4.250.<br><span style='color:var(--base);'>Tenemos 4.250 manzanas buenas.</span>", "#E3F2FD", "#1565C0"))
    
    s.append(G.summary_slide([
        "<b>Unidades de Mil:</b> Equivalen a 10 centenas. Forman números de 4 dígitos.",
        "<b>Sumar y restar miles:</b> Agregamos una columna, pero las reglas de reserva y desagrupación son las mismas.",
        "<b>Operaciones Combinadas:</b> Si no hay paréntesis, resolvemos siempre de izquierda a derecha."
    ]))
    
    s.append(G.finish_slide("¡Felicidades! Completaste el módulo avanzado de suma y resta.", "🎉"))

    return G.html_doc("Módulo 3: Suma y Resta Avanzada", s)

if __name__ == "__main__":
    out = OUT / "suma-resta-3.html"
    out.write_text(module(), encoding="utf-8")
    print(f"✅ Generado: {out}")
