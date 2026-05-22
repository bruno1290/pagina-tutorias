import re

with open("division-3.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Add .pnl-border to CSS
if ".pnl-border" not in html:
    css_insert = """
.pnl-border {
    background: #fff;
    border: 4px solid var(--base);
    border-radius: 20px;
    padding: 24px;
    width: 100%;
}
"""
    html = html.replace(".btn {", css_insert + ".btn {")

# 2. Add 3 Interactive slides for "Multiplicar o Dividir"
interactivo = """
    <!-- SLIDE: Decisión 2 -->
    <div class="sl">
        <div class="head-title">Decisión de Operación</div>
        <p class="sub-text">¿Multiplicar o Dividir?</p>
        <div class="pnl-border" style="border-color:#1976D2; padding:30px; text-align:center;">
            <div style="font-size:32px; font-weight:900; color:#333;">
                "Tengo 3 estuches. En cada estuche hay 8 lápices de colores."
            </div>
            <div style="font-size:24px; color:#555; margin-top:20px;">
                ¿Qué operación necesito para saber cuántos lápices tengo en total?
            </div>
            <div style="display:flex; justify-content:center; gap:20px; margin-top:30px;">
                <button class="dec-btn" onclick="checkDec(this, 10, true)">Multiplicación (3 • 8)</button>
                <button class="dec-btn" onclick="checkDec(this, 10, false)">División (8 : 3)</button>
            </div>
            <div id="msg-10" style="margin-top:20px; font-size:24px; font-weight:900; min-height:30px;"></div>
        </div>
    </div>

    <!-- SLIDE: Decisión 3 -->
    <div class="sl">
        <div class="head-title">Decisión de Operación</div>
        <p class="sub-text">¿Multiplicar o Dividir?</p>
        <div class="pnl-border" style="border-color:#1976D2; padding:30px; text-align:center;">
            <div style="font-size:32px; font-weight:900; color:#333;">
                "Tengo 40 dulces y quiero guardarlos en bolsitas poniendo 5 dulces en cada una."
            </div>
            <div style="font-size:24px; color:#555; margin-top:20px;">
                ¿Qué operación necesito para saber cuántas bolsitas necesito?
            </div>
            <div style="display:flex; justify-content:center; gap:20px; margin-top:30px;">
                <button class="dec-btn" onclick="checkDec(this, 11, false)">Multiplicación (40 • 5)</button>
                <button class="dec-btn" onclick="checkDec(this, 11, true)">División (40 : 5)</button>
            </div>
            <div id="msg-11" style="margin-top:20px; font-size:24px; font-weight:900; min-height:30px;"></div>
        </div>
    </div>

    <!-- SLIDE: Decisión 4 -->
    <div class="sl">
        <div class="head-title">Decisión de Operación</div>
        <p class="sub-text">¿Multiplicar o Dividir?</p>
        <div class="pnl-border" style="border-color:#1976D2; padding:30px; text-align:center;">
            <div style="font-size:32px; font-weight:900; color:#333;">
                "Para la fiesta, cada niño debe pagar 4 dólares. Si van 6 niños a la fiesta..."
            </div>
            <div style="font-size:24px; color:#555; margin-top:20px;">
                ¿Qué operación necesito para saber el total de dinero recaudado?
            </div>
            <div style="display:flex; justify-content:center; gap:20px; margin-top:30px;">
                <button class="dec-btn" onclick="checkDec(this, 12, true)">Multiplicación (6 • 4)</button>
                <button class="dec-btn" onclick="checkDec(this, 12, false)">División (6 : 4)</button>
            </div>
            <div id="msg-12" style="margin-top:20px; font-size:24px; font-weight:900; min-height:30px;"></div>
        </div>
    </div>
"""
html = html.replace('<!-- SLIDE: Contexto Problema 1 -->', interactivo + '\n    <!-- SLIDE: Contexto Problema 1 -->')


# 3. Add Abre tu cuaderno guiado
cuaderno = """
    <!-- SLIDE: Abre tu cuaderno -->
    <div class="sl">
        <div class="head-title">Abre tu cuaderno</div>
        <p class="sub-text">Usa el modelo de 4 pasos para resolver este problema.</p>
        <div class="math-eq" style="font-size:28px; padding:20px;">
            En una fábrica se produjeron 48 juguetes en 6 horas. <br>
            Si se fabrica la misma cantidad cada hora, ¿cuántos juguetes se fabrican por hora?<br>
            <span style="font-size:20px; color:#555;">(Copia en tu cuaderno: Comprende, Planifica, Resuelve, Comprueba)</span>
        </div>
        <div class="stp" style="margin-top:20px;">
            <div class="pnl-border" style="text-align:left; background:#FFF8E1; border-color:#FFB300;">
                <div style="font-size:24px; font-weight:900; color:#F57C00; text-align:center;">¡Revisemos!</div>
                <div style="font-size:20px; font-weight:800; color:#555; margin-top:10px;">
                    <b>C:</b> Total=48 juguetes. Horas=6. Busco juguetes por hora.<br>
                    <b>P:</b> Debo repartir el total de juguetes en las 6 horas. Dividir.<br>
                    <b>R:</b> 48 : 6 = 8.<br>
                    <b>C:</b> Compruebo: 8 • 6 = 48. La respuesta es 8 juguetes por hora.
                </div>
            </div>
        </div>
    </div>
"""
html = html.replace('<!-- SLIDE: Ejercicios Propuestos -->', cuaderno + '\n    <!-- SLIDE: Ejercicios Propuestos -->')


# 4. Add Respuestas
respuestas = """
    <!-- SLIDE: Respuestas -->
    <div class="sl">
        <div class="head-title">Respuestas</div>
        <p class="sub-text">Revisa tus respuestas creativas.</p>
        <div class="stp" style="display:grid; grid-template-columns: 1fr; gap:20px; width:100%; max-width:800px;">
            <div class="pnl-border" style="padding:16px; background:#D1FAE5; border-color:#059669;">
                <div style="font-size:20px; font-weight:900; color:#059669;">1. Hay 6 cajas con 5 juguetes... &rarr; <b>Multiplicación</b> (6 • 5)</div>
            </div>
            <div class="pnl-border" style="padding:16px; background:#D1FAE5; border-color:#059669;">
                <div style="font-size:20px; font-weight:900; color:#059669;">2. Tengo 30 galletas para 6 niños... &rarr; <b>División</b> (30 : 6)</div>
            </div>
            <div class="pnl-border" style="padding:16px; background:#D1FAE5; border-color:#059669;">
                <div style="font-size:20px; font-weight:900; color:#059669;">3. 72 : 8 (Reparto) &rarr; <i>Ej: Tengo 72 dulces y los reparto entre 8 niños.</i></div>
            </div>
            <div class="pnl-border" style="padding:16px; background:#D1FAE5; border-color:#059669;">
                <div style="font-size:20px; font-weight:900; color:#059669;">4. 20 : 5 (Agrupación) &rarr; <i>Ej: Tengo 20 libros y los agrupo en torres de 5 libros.</i></div>
            </div>
        </div>
    </div>
"""

# 5. Add 3 Problemas Situacionales
probs = """
    <!-- SLIDE: Problema Situacional 1 -->
    <div class="sl">
        <div class="head-title" style="background:#8E24AA;">Problema en el Zoológico 🦒</div>
        <p class="sub-text">Aplica el modelo de 4 pasos mentalmente</p>
        <div class="pnl-border" style="border-color:#8E24AA; padding:30px;">
            <div style="font-size:28px; font-weight:800; color:#333; line-height:1.5;">
                En el zoológico, le dan 42 kilos de pasto a 7 jirafas. <br>
                Si todas comen la misma cantidad, ¿cuántos kilos come cada jirafa?
            </div>
            <div class="stp" style="margin-top:20px; background:#F3E5F5; padding:20px; border-radius:12px; border-left:6px solid #8E24AA;">
                <div style="font-size:24px; font-weight:900; color:#8E24AA;">Solución:</div>
                <div style="font-size:22px; color:#555; margin-top:10px;">
                    Repartimos el total (42) entre las 7 jirafas.<br>
                    <b style="font-size:32px; color:var(--base);">42 : 7 = 6</b><br>
                    Cada jirafa come 6 kilos.
                </div>
            </div>
        </div>
    </div>

    <!-- SLIDE: Problema Situacional 2 -->
    <div class="sl">
        <div class="head-title" style="background:#F4511E;">Problema de Construcción 🏗️</div>
        <p class="sub-text">Aplica el modelo de 4 pasos mentalmente</p>
        <div class="pnl-border" style="border-color:#F4511E; padding:30px;">
            <div style="font-size:28px; font-weight:800; color:#333; line-height:1.5;">
                Los obreros tienen 64 ladrillos y hacen torres de 8 ladrillos cada una.<br>
                ¿Cuántas torres podrán hacer?
            </div>
            <div class="stp" style="margin-top:20px; background:#FBE9E7; padding:20px; border-radius:12px; border-left:6px solid #F4511E;">
                <div style="font-size:24px; font-weight:900; color:#F4511E;">Solución:</div>
                <div style="font-size:22px; color:#555; margin-top:10px;">
                    Queremos saber cuántos grupos de 8 salen del total de 64.<br>
                    <b style="font-size:32px; color:var(--base);">64 : 8 = 8</b><br>
                    Podrán hacer 8 torres.
                </div>
            </div>
        </div>
    </div>

    <!-- SLIDE: Problema Situacional 3 -->
    <div class="sl">
        <div class="head-title" style="background:#00897B;">Problema de Ahorro 💰</div>
        <p class="sub-text">Aplica el modelo de 4 pasos mentalmente</p>
        <div class="pnl-border" style="border-color:#00897B; padding:30px;">
            <div style="font-size:28px; font-weight:800; color:#333; line-height:1.5;">
                Martín ahorró 45 monedas. Quiere repartirlas en 5 alcancías <br>
                poniendo exactamente lo mismo en cada una. ¿Cuántas monedas van en cada alcancía?
            </div>
            <div class="stp" style="margin-top:20px; background:#E0F2F1; padding:20px; border-radius:12px; border-left:6px solid #00897B;">
                <div style="font-size:24px; font-weight:900; color:#00897B;">Solución:</div>
                <div style="font-size:22px; color:#555; margin-top:10px;">
                    Repartimos las 45 monedas equitativamente en 5 grupos.<br>
                    <b style="font-size:32px; color:var(--base);">45 : 5 = 9</b><br>
                    Van 9 monedas en cada alcancía.
                </div>
            </div>
        </div>
    </div>
"""
html = html.replace('<!-- SLIDE: Desafío Supremo - ObraCraft -->', respuestas + '\n' + probs + '\n    <!-- SLIDE: Desafío Supremo - ObraCraft -->')

with open("division-3.html", "w", encoding="utf-8") as f:
    f.write(html)
