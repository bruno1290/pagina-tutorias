import re

with open("division-1.html", "r", encoding="utf-8") as f:
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

# 2. Add "Abre tu cuaderno" 1
notebook_1 = """
    <!-- SLIDE: Abre tu cuaderno 1 -->
    <div class="sl">
        <div class="head-title">Abre tu cuaderno</div>
        <p class="sub-text">Copia este ejercicio de reparto y resuélvelo.</p>
        <div class="math-eq" style="font-size:36px; padding:20px;">
            Dibuja 12 galletas y repártelas en 3 platos equitativamente.<br>
            <span style="font-size:24px; color:#555;">(Haz una pausa y dibuja)</span>
        </div>
        <div class="stp" style="margin-top:20px;">
            <div class="pnl-border" style="text-align:center; background:#FFF8E1; border-color:#FFB300;">
                <div style="font-size:24px; font-weight:900; color:#F57C00;">¡Revisemos!</div>
                <div style="font-size:20px; font-weight:800; color:#555; margin-top:10px;">
                    Debiste dibujar 4 galletas en cada plato.<br>
                    <b style="font-size:32px; color:var(--base);">12 : 3 = 4</b>
                </div>
            </div>
        </div>
    </div>
"""
# 3. Add "Abre tu cuaderno" 2
notebook_2 = """
    <!-- SLIDE: Abre tu cuaderno 2 -->
    <div class="sl">
        <div class="head-title">Abre tu cuaderno</div>
        <p class="sub-text">Copia este ejercicio de agrupación y resuélvelo.</p>
        <div class="math-eq" style="font-size:36px; padding:20px;">
            Tienes 15 flores. Haz ramos de a 5 flores.<br>
            <span style="font-size:24px; color:#555;">(Haz una pausa y dibuja)</span>
        </div>
        <div class="stp" style="margin-top:20px;">
            <div class="pnl-border" style="text-align:center; background:#E0F7FA; border-color:#00ACC1;">
                <div style="font-size:24px; font-weight:900; color:#00838F;">¡Revisemos!</div>
                <div style="font-size:20px; font-weight:800; color:#555; margin-top:10px;">
                    Debiste formar 3 ramos en total.<br>
                    <b style="font-size:32px; color:var(--base);">15 : 5 = 3</b>
                </div>
            </div>
        </div>
    </div>
"""

# Insert notebook slides before specific slides
html = html.replace('<!-- SLIDE: Agrupación - Introducción -->', notebook_1 + '\n    <!-- SLIDE: Agrupación - Introducción -->')
html = html.replace('<!-- SLIDE: Encontrar el error -->', notebook_2 + '\n    <!-- SLIDE: Encontrar el error -->')

# 4. Add "Respuestas" slide after "Ejercicios Propuestos"
respuestas = """
    <!-- SLIDE: Respuestas -->
    <div class="sl">
        <div class="head-title">Respuestas</div>
        <p class="sub-text">Compara tus resultados del cuaderno.</p>
        <div class="stp" style="display:grid; grid-template-columns: 1fr 1fr; gap:20px; width:100%;">
            <div class="pnl-border" style="padding:16px; background:#D1FAE5; border-color:#059669;">
                <div style="font-size:20px; font-weight:900; color:#059669;">1. 24 : 6 = <b>4</b></div>
            </div>
            <div class="pnl-border" style="padding:16px; background:#D1FAE5; border-color:#059669;">
                <div style="font-size:20px; font-weight:900; color:#059669;">2. 18 : 2 = <b>9</b></div>
            </div>
            <div class="pnl-border" style="padding:16px; background:#D1FAE5; border-color:#059669;">
                <div style="font-size:20px; font-weight:900; color:#059669;">3. 30 en 6 grupos &rarr; <b>5</b> por grupo</div>
            </div>
            <div class="pnl-border" style="padding:16px; background:#D1FAE5; border-color:#059669;">
                <div style="font-size:20px; font-weight:900; color:#059669;">4. 35 en grupos de 5 &rarr; <b>7</b> grupos</div>
            </div>
            <div class="pnl-border" style="padding:16px; background:#D1FAE5; border-color:#059669;">
                <div style="font-size:20px; font-weight:900; color:#059669;">5. 42 bolitas a 6 amigos &rarr; <b>7</b> a cada uno</div>
            </div>
            <div class="pnl-border" style="padding:16px; background:#D1FAE5; border-color:#059669;">
                <div style="font-size:20px; font-weight:900; color:#059669;">6. 20 cuadernos a 5 mesas &rarr; <b>4</b> a cada mesa</div>
            </div>
        </div>
    </div>
"""
html = html.replace('<!-- SLIDE: Desafío Supremo - ObraCraft -->', respuestas + '\n    <!-- SLIDE: Problema Situacional 1 -->\n')

# 5. Add 3 Problemas Situacionales
probs = """
    <!-- SLIDE: Problema Situacional 1 -->
    <div class="sl">
        <div class="head-title" style="background:#8E24AA;">Problema en la Pizzería 🍕</div>
        <p class="sub-text">Contexto de la vida real</p>
        <div class="pnl-border" style="border-color:#8E24AA; padding:30px;">
            <div style="font-size:28px; font-weight:800; color:#333; line-height:1.5;">
                En una pizzería prepararon 32 porciones de pizza para una fiesta. <br>
                Si cada niño se come 4 porciones, ¿para cuántos niños alcanza?
            </div>
            <div class="stp" style="margin-top:20px; background:#F3E5F5; padding:20px; border-radius:12px; border-left:6px solid #8E24AA;">
                <div style="font-size:24px; font-weight:900; color:#8E24AA;">Solución:</div>
                <div style="font-size:22px; color:#555; margin-top:10px;">
                    Tenemos el total (32) y sabemos cuántas van por niño (4).<br>
                    Es un problema de agrupación.<br>
                    <b style="font-size:32px; color:var(--base);">32 : 4 = 8</b><br>
                    ¡Alcanza para 8 niños!
                </div>
            </div>
        </div>
    </div>

    <!-- SLIDE: Problema Situacional 2 -->
    <div class="sl">
        <div class="head-title" style="background:#F4511E;">Problema en la Granja 🚜</div>
        <p class="sub-text">Contexto de la vida real</p>
        <div class="pnl-border" style="border-color:#F4511E; padding:30px;">
            <div style="font-size:28px; font-weight:800; color:#333; line-height:1.5;">
                El granjero recolectó 45 huevos esta mañana. <br>
                Tiene bandejas donde caben 5 huevos cada una. ¿Cuántas bandejas necesita?
            </div>
            <div class="stp" style="margin-top:20px; background:#FBE9E7; padding:20px; border-radius:12px; border-left:6px solid #F4511E;">
                <div style="font-size:24px; font-weight:900; color:#F4511E;">Solución:</div>
                <div style="font-size:22px; color:#555; margin-top:10px;">
                    Sabemos el total (45) y la cantidad por grupo (5).<br>
                    <b style="font-size:32px; color:var(--base);">45 : 5 = 9</b><br>
                    ¡Necesita 9 bandejas completas!
                </div>
            </div>
        </div>
    </div>

    <!-- SLIDE: Problema Situacional 3 -->
    <div class="sl">
        <div class="head-title" style="background:#00897B;">Problema de Organización 📚</div>
        <p class="sub-text">Contexto de la vida real</p>
        <div class="pnl-border" style="border-color:#00897B; padding:30px;">
            <div style="font-size:28px; font-weight:800; color:#333; line-height:1.5;">
                La biblioteca tiene 60 libros nuevos y 6 estantes vacíos. <br>
                Si ponen la misma cantidad en cada estante, ¿cuántos libros van en cada uno?
            </div>
            <div class="stp" style="margin-top:20px; background:#E0F2F1; padding:20px; border-radius:12px; border-left:6px solid #00897B;">
                <div style="font-size:24px; font-weight:900; color:#00897B;">Solución:</div>
                <div style="font-size:22px; color:#555; margin-top:10px;">
                    Repartimos el total (60) en partes iguales (6 estantes).<br>
                    <b style="font-size:32px; color:var(--base);">60 : 6 = 10</b><br>
                    ¡Pondrán 10 libros en cada estante!
                </div>
            </div>
        </div>
    </div>

    <!-- SLIDE: Desafío Supremo - ObraCraft -->
"""
html = html.replace('<!-- SLIDE: Problema Situacional 1 -->\n', probs)

with open("division-1.html", "w", encoding="utf-8") as f:
    f.write(html)
