import re

with open("division-2.html", "r", encoding="utf-8") as f:
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

# 2. Add 2 explanation slides (triangles)
triangulos = """
    <!-- SLIDE: Triángulo Explicación Extra 1 -->
    <div class="sl">
        <div class="head-title">Más Familias: Familia del 4</div>
        <p class="sub-text">Observa cómo estos 3 números siempre van juntos.</p>
        <div class="tri-wrap">
            <div class="tri-num tn-top">36</div>
            <div class="tri-num tn-bl">4</div>
            <div class="tri-num tn-br">9</div>
            <div class="tri-op to-mul">✖</div>
            <div class="tri-op to-dl">➗</div>
            <div class="tri-op to-dr">➗</div>
        </div>
        <div class="stp" style="display:flex; gap:30px; margin-top:20px;">
            <div class="pnl-border" style="padding:16px; border-color:#9C27B0;">
                <b style="color:#9C27B0;">Multiplicamos:</b><br>
                4 • 9 = 36<br>
                9 • 4 = 36
            </div>
            <div class="pnl-border" style="padding:16px; border-color:#009688;">
                <b style="color:#009688;">Dividimos:</b><br>
                36 : 4 = 9<br>
                36 : 9 = 4
            </div>
        </div>
    </div>

    <!-- SLIDE: Triángulo Explicación Extra 2 -->
    <div class="sl">
        <div class="head-title">Familia del 8</div>
        <p class="sub-text">Intenta encontrar las 4 operaciones antes de presionar siguiente.</p>
        <div class="tri-wrap">
            <div class="tri-num tn-top">56</div>
            <div class="tri-num tn-bl">8</div>
            <div class="tri-num tn-br">7</div>
            <div class="tri-op to-mul">✖</div>
            <div class="tri-op to-dl">➗</div>
            <div class="tri-op to-dr">➗</div>
        </div>
        <div class="stp" style="display:flex; gap:30px; margin-top:20px;">
            <div class="pnl-border" style="padding:16px; border-color:#9C27B0;">
                <b style="color:#9C27B0;">Multiplicamos:</b><br>
                8 • 7 = 56<br>
                7 • 8 = 56
            </div>
            <div class="pnl-border" style="padding:16px; border-color:#009688;">
                <b style="color:#009688;">Dividimos:</b><br>
                56 : 8 = 7<br>
                56 : 7 = 8
            </div>
        </div>
    </div>
"""
html = html.replace('<!-- SLIDE: Aplica el truco 1 -->', triangulos + '\n    <!-- SLIDE: Aplica el truco 1 -->')

# 3. Add Abre tu cuaderno
cuaderno = """
    <!-- SLIDE: Abre tu cuaderno -->
    <div class="sl">
        <div class="head-title">Abre tu cuaderno</div>
        <p class="sub-text">Crea tú mismo el triángulo y las 4 operaciones.</p>
        <div class="math-eq" style="font-size:36px; padding:20px;">
            Dibuja la familia del <b>5</b>, el <b>6</b> y el <b>30</b>.<br>
            <span style="font-size:24px; color:#555;">(Haz una pausa y escribe)</span>
        </div>
        <div class="stp" style="margin-top:20px;">
            <div class="pnl-border" style="text-align:center; background:#FFF8E1; border-color:#FFB300;">
                <div style="font-size:24px; font-weight:900; color:#F57C00;">¡Revisemos!</div>
                <div style="font-size:20px; font-weight:800; color:#555; margin-top:10px;">
                    5 • 6 = 30  |  6 • 5 = 30 <br>
                    30 : 5 = 6  |  30 : 6 = 5
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
        <p class="sub-text">Revisa tus respuestas del puente multiplicativo.</p>
        <div class="stp" style="display:grid; grid-template-columns: 1fr 1fr; gap:20px; width:100%;">
            <div class="pnl-border" style="padding:16px; background:#D1FAE5; border-color:#059669;">
                <div style="font-size:20px; font-weight:900; color:#059669;">1. 56 : 7 = <b>8</b> (porque 8 • 7 = 56)</div>
            </div>
            <div class="pnl-border" style="padding:16px; background:#D1FAE5; border-color:#059669;">
                <div style="font-size:20px; font-weight:900; color:#059669;">2. 36 : 9 = <b>4</b> (porque 4 • 9 = 36)</div>
            </div>
            <div class="pnl-border" style="padding:16px; background:#D1FAE5; border-color:#059669;">
                <div style="font-size:20px; font-weight:900; color:#059669;">3. <b>8•5=40 | 5•8=40 | 40:8=5 | 40:5=8</b></div>
            </div>
            <div class="pnl-border" style="padding:16px; background:#D1FAE5; border-color:#059669;">
                <div style="font-size:20px; font-weight:900; color:#059669;">4. <b>9 • 5 = 45</b></div>
            </div>
            <div class="pnl-border" style="padding:16px; background:#D1FAE5; border-color:#059669;">
                <div style="font-size:20px; font-weight:900; color:#059669;">5. <b>7 • 7 = 49</b> (Sí, es correcto)</div>
            </div>
            <div class="pnl-border" style="padding:16px; background:#D1FAE5; border-color:#059669;">
                <div style="font-size:20px; font-weight:900; color:#059669;">6. <b>45 : 5 = 9</b></div>
            </div>
        </div>
    </div>
"""

# 5. Add 3 Problemas Situacionales
probs = """
    <!-- SLIDE: Problema Situacional 1 -->
    <div class="sl">
        <div class="head-title" style="background:#8E24AA;">Problema en la Florería 🌻</div>
        <p class="sub-text">Contexto de la vida real</p>
        <div class="pnl-border" style="border-color:#8E24AA; padding:30px;">
            <div style="font-size:28px; font-weight:800; color:#333; line-height:1.5;">
                Ana tiene 54 girasoles y quiere hacer ramos de 6 girasoles cada uno.<br>
                Usa el puente multiplicativo para saber cuántos ramos hará.
            </div>
            <div class="stp" style="margin-top:20px; background:#F3E5F5; padding:20px; border-radius:12px; border-left:6px solid #8E24AA;">
                <div style="font-size:24px; font-weight:900; color:#8E24AA;">Solución:</div>
                <div style="font-size:22px; color:#555; margin-top:10px;">
                    ¿Qué número • 6 da 54?<br>
                    ¡La tabla del 9! &rarr; 9 • 6 = 54.<br>
                    Por lo tanto, <b style="font-size:32px; color:var(--base);">54 : 6 = 9</b><br>
                    Hará 9 ramos.
                </div>
            </div>
        </div>
    </div>

    <!-- SLIDE: Problema Situacional 2 -->
    <div class="sl">
        <div class="head-title" style="background:#F4511E;">Problema en la Cancha 🏀</div>
        <p class="sub-text">Contexto de la vida real</p>
        <div class="pnl-border" style="border-color:#F4511E; padding:30px;">
            <div style="font-size:28px; font-weight:800; color:#333; line-height:1.5;">
                Hay 40 niños en el gimnasio. El profe quiere formar 5 equipos iguales.<br>
                Usa el puente multiplicativo para saber cuántos irán en cada equipo.
            </div>
            <div class="stp" style="margin-top:20px; background:#FBE9E7; padding:20px; border-radius:12px; border-left:6px solid #F4511E;">
                <div style="font-size:24px; font-weight:900; color:#F4511E;">Solución:</div>
                <div style="font-size:22px; color:#555; margin-top:10px;">
                    ¿Qué número • 5 da 40?<br>
                    ¡La tabla del 8! &rarr; 8 • 5 = 40.<br>
                    Por lo tanto, <b style="font-size:32px; color:var(--base);">40 : 5 = 8</b><br>
                    Irán 8 niños en cada equipo.
                </div>
            </div>
        </div>
    </div>

    <!-- SLIDE: Problema Situacional 3 -->
    <div class="sl">
        <div class="head-title" style="background:#00897B;">Problema de Galletas 🍪</div>
        <p class="sub-text">Contexto de la vida real</p>
        <div class="pnl-border" style="border-color:#00897B; padding:30px;">
            <div style="font-size:28px; font-weight:800; color:#333; line-height:1.5;">
                Tienes 24 galletas y se las das a 3 amigos. <br>
                Si lo compruebas multiplicando, ¿cómo quedaría la comprobación?
            </div>
            <div class="stp" style="margin-top:20px; background:#E0F2F1; padding:20px; border-radius:12px; border-left:6px solid #00897B;">
                <div style="font-size:24px; font-weight:900; color:#00897B;">Solución:</div>
                <div style="font-size:22px; color:#555; margin-top:10px;">
                    Primero divides: 24 : 3 = 8 galletas por amigo.<br>
                    Comprobación: <b style="font-size:32px; color:var(--base);">8 • 3 = 24</b><br>
                    Como da 24, el resultado está correcto.
                </div>
            </div>
        </div>
    </div>
"""
html = html.replace('<!-- SLIDE: Desafío Supremo - El Cofre -->', respuestas + '\n' + probs + '\n    <!-- SLIDE: Desafío Supremo - El Cofre -->')

with open("division-2.html", "w", encoding="utf-8") as f:
    f.write(html)
