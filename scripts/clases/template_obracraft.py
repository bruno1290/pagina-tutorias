"""
╔══════════════════════════════════════════════════════════════════╗
║  🎓 PLANTILLA OFICIAL — La Obra UC v3.0                          ║
║  Para crear un nuevo módulo de clase copiar este archivo,        ║
║  renombrar a build_CURSO_TEMA.py y adaptar el contenido.         ║
╚══════════════════════════════════════════════════════════════════╝

INSTRUCCIONES:
  1. Copiar este archivo.
  2. Cambiar OUT para apuntar a la carpeta correcta.
  3. Completar cada bloque con el contenido del tema nuevo.
  4. Ejecutar: python3 build_CURSO_TEMA.py

REFERENCIA DEL FLUJO OBLIGATORIO:
  [PORTADA] → [EXPLICACIÓN VISUAL (8-12 slides)] →
  [EJERCICIOS PROPUESTOS + RESPUESTAS] →
  [PROBLEMAS SITUACIONALES (2-3)] →
  [DESAFÍO SUPREMO (2 slides, ≥1 ObraCraft)] →
  [RESUMEN] → [CIERRE]
"""

from __future__ import annotations
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))

# Importar el generador. Si el tema nuevo lo requiere,
# crear generator_TEMA.py heredando el CSS/JS del base.
import generator_suma_resta as G

# ── CONFIGURACIÓN ──────────────────────────────────────────────────
TITULO_MODULO  = "Nombre del Módulo"    # Ej: "Fracciones equivalentes"
EMOJI_PORTADA  = "➕"                   # Emoji del tema
SUBTITULO      = "Aprendemos paso a paso"
OUT = pathlib.Path("/Users/brunonattino/Desktop/PAGINA TUTORIAS/clases/TEMA")
ARCHIVO_SALIDA = "nombre-archivo.html"


def module() -> str:
    s: list[str] = []

    # ──────────────────────────────────────────────────────────────
    # [1] PORTADA
    # ──────────────────────────────────────────────────────────────
    s.append(G.intro_slide(TITULO_MODULO, SUBTITULO, EMOJI_PORTADA))


    # ──────────────────────────────────────────────────────────────
    # [2-12] EXPLICACIÓN VISUAL
    # Reglas:
    #  - 1 idea por slide. Ir de lo concreto a lo abstracto.
    #  - Ejemplos completamente resueltos (no dejar a medias).
    #  - Para números: usar colores posicionales:
    #      Unidades #FFE082 | Decenas #9DDEFF | Centenas #9DE3BD | UM #E1BEE7
    #  - Incluir 1-2 slides "Abre tu cuaderno" con solución oculta.
    #  - Incluir 1 slide interactivo (quiz_slide) para verificar comprensión.
    # ──────────────────────────────────────────────────────────────

    # Slide conceptual básico
    s.append(G.slide("""
        <div class="head-title">¿Qué es [CONCEPTO]?</div>
        <p class="sub-text">Descripción visual y sencilla del concepto.</p>
        <div class="fact-grid">
            <div class="fact-box" style="border-color:#9DE3BD;">
                <h4 style="color:#388E3C;">🟢 Idea 1</h4>
                <p>Descripción breve.</p>
            </div>
            <div class="fact-box stp" style="border-color:#9DDEFF;">
                <h4 style="color:#1976D2;">🔵 Idea 2</h4>
                <p>Descripción breve.</p>
            </div>
            <div class="fact-box stp" style="border-color:#FFE082;">
                <h4 style="color:#F57F17;">🟡 Idea 3</h4>
                <p>Descripción breve.</p>
            </div>
        </div>
    """))

    # Slide con ejemplo resuelto (algoritmo en columna cuando aplique)
    # s.append(G.alg_board(...))  # Para suma/resta/multiplicación en columna

    # Slide "Abre tu cuaderno" — solución oculta
    s.append(G.notebook_slide(
        "Resuelve en tu cuaderno: <b class=\"hl\">[EJERCICIO]</b>.",
        ["Paso 1: ...", "Paso 2: ...", "Resultado: ..."]
    ))

    # Quiz interactivo para verificar comprensión
    s.append(G.quiz_slide(
        "¿Lo entendiste?",
        "Pregunta directa sobre el concepto recién visto.",
        ["Opción incorrecta", "Opción correcta ✓", "Opción incorrecta", "Opción incorrecta"],
        ok=1,
        exp="Explicación de por qué la opción 2 es correcta."
    ))


    # ──────────────────────────────────────────────────────────────
    # [13-14] EJERCICIOS PROPUESTOS + RESPUESTAS
    # Reglas:
    #  - 6 ejercicios en cuadrícula 2×3.
    #  - Variar: 2 mecánicos, 2 aplicados, 2 con análisis/giro creativo.
    #  - NO repetir el mismo tipo de operación o contexto 3 veces.
    # ──────────────────────────────────────────────────────────────
    s.append(G.ejercicios_propuestos(
        "Ejercicios para tu cuaderno",
        "Copia y resuelve. Revisa bien tu procedimiento antes de pasar.",
        [
            "Ejercicio mecánico 1",      # Directo, fijar procedimiento
            "Ejercicio mecánico 2",      # Directo, fijar procedimiento
            "Ejercicio aplicado 1",      # Con un dato de contexto
            "Ejercicio aplicado 2",      # Con un dato de contexto
            "Ejercicio análisis 1",      # Requiere pensar un poco más
            "Ejercicio análisis 2",      # Requiere pensar un poco más
        ]
    ))
    s.append(G.ejercicios_respuestas(
        "Revisa tus respuestas",
        [
            "Ej 1 = Resultado",
            "Ej 2 = Resultado",
            "Ej 3 = Resultado",
            "Ej 4 = Resultado",
            "Ej 5 = Resultado",
            "Ej 6 = Resultado",
        ]
    ))


    # ──────────────────────────────────────────────────────────────
    # [15-17] PROBLEMAS SITUACIONALES
    # Reglas:
    #  - 2 a 3 problemas máximo.
    #  - Contextos distintos entre sí (no todos del almacén).
    #  - Nombres chilenos: Lucas, Sofía, Valentina, Matías, etc.
    #  - La respuesta completa es oculta (.stp).
    # ──────────────────────────────────────────────────────────────
    s.append(G.problem_slide(
        "Título del Problema 1", "🛒",
        "Enunciado del problema con contexto real.",
        "Operación = Resultado.<br><span style='color:var(--base);'>Respuesta completa.</span>",
        "#FFF8E1", "#F9A825"
    ))
    s.append(G.problem_slide(
        "Título del Problema 2", "⚽",
        "Enunciado del problema con contexto real diferente.",
        "Operación = Resultado.<br><span style='color:var(--base);'>Respuesta completa.</span>",
        "#E8F5E9", "#2E7D32"
    ))


    # ──────────────────────────────────────────────────────────────
    # [18-19] DESAFÍO SUPREMO
    # Reglas:
    #  - Exactamente 2 slides de desafío supremo por presentación.
    #  - Mínimo 1 DEBE ser un ejercicio de ObraCraft.
    #  - ObraCraft = ambientado en un mundo virtual mágico tipo Minecraft.
    #    (minar minerales, cruzar portales, derrotar dragones, fabricar pociones).
    #    Es un EJERCICIO PUNTUAL, no el hilo narrativo de toda la clase.
    #  - El otro puede ser: acertijo, número oculto, encadenado, juego del blanco, etc.
    #  - Usar challenge_slide con fondo diferente para cada uno.
    # ──────────────────────────────────────────────────────────────

    # Desafío 1: ObraCraft (⛏️ OBLIGATORIO)
    s.append(G.challenge_slide(
        "Misión ObraCraft: [NOMBRE]", "⛏️",
        "Eres un explorador en ObraCraft. [Plantear el problema matemático "
        "usando elementos del mundo virtual: minerales, dragones, portales, "
        "fortalezas, pociones, etc.]",
        "Paso 1: ... = ...<br>Paso 2: ... = ...<br>"
        "<span style='color:#16a34a;'>Resultado final.</span>",
        "#DCFCE7", "#16A34A"
    ))

    # Desafío 2: Otro tipo creativo (acertijo, juego, encadenado, etc.)
    s.append(G.challenge_slide(
        "El [NOMBRE DEL ACERTIJO]", "🔐",
        "Enunciado del desafío creativo (no ObraCraft). "
        "Puede ser: acertijo con pistas, número oculto, "
        "ticket roto, juego del blanco, etc.",
        "Solución paso a paso.<br><span style='color:#db2777;'>Respuesta final.</span>",
        "#FDF2F8", "#DB2777"
    ))


    # ──────────────────────────────────────────────────────────────
    # [20-21] RESUMEN + CIERRE
    # ──────────────────────────────────────────────────────────────
    s.append(G.summary_slide([
        "<b>Idea clave 1:</b> Descripción corta.",
        "<b>Idea clave 2:</b> Descripción corta.",
        "<b>Idea clave 3:</b> Descripción corta.",
    ]))
    s.append(G.finish_slide("¡Lo lograste! Eres un experto en [TEMA].", "🏆"))

    return G.html_doc(TITULO_MODULO, s)


# ── EJECUCIÓN ──────────────────────────────────────────────────────
if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    out_path = OUT / ARCHIVO_SALIDA
    out_path.write_text(module(), encoding="utf-8")
    print(f"✅ Generado: {out_path}")
