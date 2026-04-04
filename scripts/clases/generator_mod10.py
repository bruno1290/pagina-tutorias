def generate_html():
    css = """
    @import url('https://fonts.googleapis.com/css2?family=Nunito:wght@600;800;900&display=swap');
    :root {--base: #1C4A82; --bg: #f5f6f8; --tx: #333;}
    * {margin:0; padding:0; box-sizing:border-box;}
    body {font-family: 'Nunito', sans-serif; background: var(--bg); overflow: hidden; height: 100vh; width: 100vw; display: flex; flex-direction: column; align-items: center;}
    .dk {position: relative; width: 100%; height: 100%; max-width: 1000px; display: flex;}
    
    .sl {position: absolute; inset: 0; display: flex; flex-direction: column; align-items: center; justify-content: flex-start; padding: 40px; opacity: 0; transform: scale(.96); transition: opacity .4s, transform .4s; pointer-events: none; z-index: 1;}
    .sl.on {opacity: 1; transform: scale(1); pointer-events: auto; z-index: 10;}
    .sl.pv {opacity: 0; transform: translateX(-50px) scale(.95);}
    .sl.nx {opacity: 0; transform: translateX(50px) scale(.95);}
    
    .head-title {background: var(--base); color: white; padding: 10px 40px; font-size: 32px; font-weight: 900; margin-bottom: 40px; display: inline-block; border-radius: 12px;}
    .sub-text {font-size: 24px; font-weight: 600; margin-bottom: 30px; text-align: center; color: var(--tx);}
    .frac-box {border: 3px dashed var(--base); border-radius: 20px; display: inline-flex; flex-direction: column; align-items: center; justify-content: center; padding: 15px 30px; font-size: 60px; font-weight: 900; line-height: 1; margin: 0 20px; background: white;}
    .frac-box div.line {height: 4px; width: 100%; background: #333; margin: 5px 0; border-radius: 2px;}
    
    /* Navigation */
    .pb {position: fixed; top: 0; left: 0; height: 6px; background: var(--base); transition: width .4s; z-index: 100;}
    .nv {position: fixed; bottom: 0; left: 0; right: 0; height: 60px; background: white; border-top: 1px solid #ddd; display: flex; align-items: center; justify-content: space-between; padding: 0 40px; z-index: 100;}
    .nb {background: #eee; color: var(--base); border: none; padding: 10px 20px; border-radius: 8px; font-family: 'Nunito', sans-serif; font-size: 16px; font-weight: 900; cursor: pointer; transition: all .2s;}
    .nb:hover {background: #ddd;}
    .nb:disabled {opacity: 0.3; cursor: not-allowed;}
    .sc {color: #888; font-size: 16px; font-weight: 900;}
    
    /* Steps Engine */
    .stp {opacity: 0; transform: translateY(20px); transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1); pointer-events: none; position: relative;}
    .stp.shwn {opacity: 1; transform: translateY(0); pointer-events: auto;}
    
    /* Components */
    .pnl {background: #fff; padding: 30px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); border: 2px solid #eaeaea; width: 100%; margin-bottom: 20px;}
    .pnl-border {background: #fff; padding: 30px; border-radius: 20px; border: 4px solid var(--base); width: 100%; margin-bottom: 20px;}
    .hl {color: var(--base); font-weight: 900;}
    
    .btn {background: var(--base); color: white; border: none; padding: 14px 28px; border-radius: 12px; font-size: 20px; font-weight: 900; cursor: pointer; transition: transform .2s;}
    .btn:hover {transform: translateY(-2px); box-shadow: 0 4px 12px rgba(28,74,130,0.3);}
    """
    
    js = """
    const S=document.querySelectorAll('.sl'); let c=0; const T=S.length;
    function ui() {
        S.forEach((s,i)=>{
            s.classList.remove('on','pv','nx');
            if(i===c) s.classList.add('on');
            else if(i<c) s.classList.add('pv');
            else s.classList.add('nx');
        });
        document.getElementById('pb').style.width=((c+1)/T*100)+'%';
        document.getElementById('sc').textContent=`${c+1} / ${T}`;
        document.getElementById('pv').disabled=c===0;
        document.getElementById('nx').disabled=c===T-1;
    }
    function go(d) {
        if(d>0) {
            const hid = S[c].querySelectorAll('.stp:not(.shwn)');
            if(hid.length > 0) { hid[0].classList.add('shwn'); return; }
        } else {
            const shw = S[c].querySelectorAll('.stp.shwn');
            if(shw.length > 0) { shw[shw.length-1].classList.remove('shwn'); return; }
        }
        const n=c+d; if(n>=0 && n<T) { c=n; ui(); }
    }
    document.addEventListener('keydown', e => {
        if(e.key==='ArrowRight' || e.key===' ') go(1);
        if(e.key==='ArrowLeft') go(-1);
    });
    ui();
    """
    
    slides = []
    def slide(html): slides.append(f'<div class="sl">{html}</div>')

    def draw_painted(typ, col, painted_cnt, max_w=240, max_h=240):
        s = f'<svg width="{max_w}" height="{max_h}" viewBox="0 0 {max_w} {max_h}">'
        w, h = max_w, max_h
        if typ == "grid2x4":
            cw, ch = w/4, h/2
            for i in range(2):
                for j in range(4):
                    idx = i*4 + j
                    s += f'<rect x="{j*cw}" y="{i*ch}" width="{cw}" height="{ch}" fill="{col if idx<painted_cnt else "#fff"}" stroke="#555" stroke-width="3"/>'
        s += '</svg>'
        return s

    def custom_rect_frac(den, num, col, mw=180, mh=60):
        w = mw / den
        s = f'<svg width="{mw+4}" height="{mh+4}" viewBox="-2 -2 {mw+4} {mh+4}">'
        for i in range(den):
            fill = col if i < num else "#fff"
            s += f'<rect x="{i*w}" y="0" width="{w}" height="{mh}" fill="{fill}" stroke="#555" stroke-width="3"/>'
        s += '</svg>'
        return s

    # 1. INTRO
    slide(f"""
        <div style="flex:1; display:flex; flex-direction:column; justify-content:center; align-items:center;">
            <h1 style="font-size: 70px; color: var(--base); margin-bottom: 20px; text-align:center;">Módulo 10:<br>Comparaciones y Equivalencias</h1>
            <p class="sub-text">Comencemos midiendo y ordenando pedazos.</p>
            <p style="font-size:90px; margin-top:30px;">⚖️</p>
        </div>
    """)

    # 2. COMPARAR (MISMO DENOMINADOR)
    svg_3_8 = draw_painted("grid2x4", "#E1BEE7", 3)
    svg_5_8 = draw_painted("grid2x4", "#9DDEFF", 5)
    slide(f"""
        <div class="head-title">Denominador Igual: ¿Quién gana?</div>
        <div class="pnl-border" style="flex-direction:column;">
            <div style="flex:1; width:100%;">
                <p style="font-size:28px; font-weight:800; margin-bottom:10px; color:var(--base);">Comparamos <b>3/8</b> y <b>5/8</b></p>
                <div class="stp" style="font-size:22px;">Comparten denominador (8). Esto significa que <b>los cortes de todas las figuras son del mismo tamaño.</b></div>
                
                <div class="stp" style="display:flex; align-items:center; gap:40px; justify-content:center; margin:30px 0;">
                    <div style="text-align:center;">{svg_3_8}<br><b style="font-size:40px;">3/8</b></div>
                    <div style="font-size:60px; font-weight:900; color:#888;">VS</div>
                    <div style="text-align:center;">{svg_5_8}<br><b style="font-size:40px;">5/8</b></div>
                </div>

                <div class="stp" style="background:#eaf1f8; padding:20px; border-radius:15px; border-left:8px solid var(--base); font-size:22px; font-weight:800; text-align:center;">
                    Regla: Gana el que tiene más partes pintadas (mayor numerador).<br>
                    <span style="font-size:46px; color:var(--base);">5/8 > 3/8</span>
                </div>
            </div>
        </div>
    """)

    # Practica MISMO DENOMINADOR (4 slides)
    comps = [
        ("Abre tu cuaderno: Comparemos", 4, 7, 2, 7, "#9DE3BD", "4/7 > 2/7", True),
        ("Abre tu cuaderno: ¿Quién es menor?", 6, 12, 8, 12, "#FF9D9D", "6/12 < 8/12", True),
        ("Dibuja y ordena en tu cuaderno", 5, 9, 4, 9, "#FFE082", "5/9 > 4/9", True),
        ("Abre tu Cuaderno: Ordena visualmente", 2, 5, 4, 5, "#9DDEFF", "2/5 < 4/5", False)
    ]
    for tit, n1, d1, n2, d2, col, ans, left_wins in comps:
        svg1 = custom_rect_frac(d1, n1, col if left_wins else "#ccc", 240, 80)
        svg2 = custom_rect_frac(d2, n2, col if not left_wins else "#ccc", 240, 80)
        slide(f"""
        <div class="head-title">Practicando Formas</div>
        <div style="font-size:28px; font-weight:800; margin-bottom:20px; text-align:center; color:var(--base);">{tit}</div>
        
        <div style="display:flex; justify-content:center; gap:60px; margin-top:20px; width:100%;">
            <div style="display:flex; flex-direction:column; align-items:center; gap:20px;">
                <div class="frac-box"><div>{n1}</div><div class="line"></div><div>{d1}</div></div>
                <div class="stp">{svg1}</div>
            </div>
            
            <div class="stp" style="font-size:100px; font-weight:900; align-self:center; color:#ccc;">?</div>

            <div style="display:flex; flex-direction:column; align-items:center; gap:20px;">
                <div class="frac-box"><div>{n2}</div><div class="line"></div><div>{d2}</div></div>
                <div class="stp">{svg2}</div>
            </div>
        </div>
        
        <div class="stp" style="margin-top:40px; font-size:40px; font-weight:900; text-align:center; color:var(--base); background:#eaf1f8; padding:20px; border-radius:20px;">
            Respuesta correcta:<br>{ans}
        </div>
        """)

    # Problemas Verbales Denominador Igual (2 slides)
    verb_igual = [
        ("El cumpleaños 🎂", "En el cumpleaños de Ana, sobraron pedazos de torta. En la mesa roja hay <b>3/8</b> de torta, y en la azul quedan <b>5/8</b>. ¿En qué mesa hay más torta?", "Como están cortadas en octavos (igual denominador), comparamos las porciones.<br>Mesa Azul tiene 5 trozos, por tanto <span style='font-size:36px; color:var(--base); font-weight:900;'>5/8 > 3/8</span>."),
        ("El camino largo 🏃‍♀️", "Carlos caminó <b>4/5</b> del camino, mientras que María caminó <b>2/5</b>. ¿Quién caminó una distancia mayor?", "Están trabajando con quintos (igual denominador).<br>Carlos tiene un numerador mayor (4).<br><span style='font-size:36px; color:var(--base); font-weight:900;'>4/5 > 2/5</span>.")
    ]
    for tit, prob, ans in verb_igual:
        slide(f"""
        <div class="head-title">Problemas Situacionales 💡</div>
        <div class="pnl-border" style="text-align:center; padding:50px;">
            <p style="font-size:32px; font-weight:800; margin-bottom:20px; color:var(--base);">{tit}</p>
            <p style="font-size:26px; line-height:1.6; margin-bottom:30px;">{prob}</p>
            
            <div class="stp" style="background:#eaf1f8; border-radius: 15px; padding:25px; text-align:left; border-left: 8px solid var(--base);">
                <p style="font-size:22px; color:#555; font-weight:800; margin-bottom:10px;">Respuesta guiada:</p>
                <div style="font-size:24px;">{ans}</div>
            </div>
        </div>
        """)

    # 3. COMPARAR (MISMO NUMERADOR)
    bar_1_3 = custom_rect_frac(3, 1, "#FFB74D", 400, 60)
    bar_1_5 = custom_rect_frac(5, 1, "#9DE3BD", 400, 60)
    slide(f"""
        <div class="head-title">Numerador Igual: El tamaño de los trozos</div>
        <div class="pnl-border" style="flex-direction:column;">
            <p style="font-size:28px; font-weight:800; margin-bottom:10px; color:var(--base);">Comparamos <b>1/3</b> y <b>1/5</b></p>
            <div class="stp" style="font-size:22px; text-align:center;">El numerador es igual (sólo tomamos 1 trozo en ambos). ¡Pero observemos el TAMAÑO de cada trozo!</div>
            
            <div class="stp" style="display:flex; flex-direction:column; gap:30px; align-items:center; width:100%; margin:30px 0;">
                <div style="display:flex; align-items:center; gap:20px; background:#fff; padding:15px; border-radius:15px; border:2px dashed #ccc;">
                    <b style="font-size:30px; width:60px;">1/3</b>
                    {bar_1_3}
                </div>
                <div style="display:flex; align-items:center; gap:20px; background:#fff; padding:15px; border-radius:15px; border:2px dashed #ccc;">
                    <b style="font-size:30px; width:60px;">1/5</b>
                    {bar_1_5}
                </div>
            </div>

            <div class="stp" style="background:#eaf1f8; padding:20px; border-radius:15px; border-left:8px solid var(--base); font-size:22px; font-weight:800; width:100%; text-align:center;">
                Regla: MENOS cortes en la barra = TROZOS MÁS GRANDES.<br>Gana la fracción con el DENOMINADOR MENOR.<br>
                <span style="font-size:46px; color:var(--base);">1/3 > 1/5</span>
            </div>
        </div>
    """)

    # Práctica MISMO NUMERADOR (3 slides)
    comps_num = [
        ("Abre tu cuaderno: Dibuja y compara", 2, 4, 2, 8, "#E1BEE7", "2/4 > 2/8", True),
        ("Abre tu cuaderno: ¿Quién gana?", 3, 5, 3, 7, "#9DDEFF", "3/5 > 3/7", True),
        ("Abre tu Cuaderno: Ordena de menor a mayor", 4, 10, 4, 5, "#FF9D9D", "4/10 < 4/5", False)
    ]
    for tit, n1, d1, n2, d2, col, ans, left_wins in comps_num:
        svg1 = custom_rect_frac(d1, n1, col if left_wins else "#ccc", 240, 80)
        svg2 = custom_rect_frac(d2, n2, col if not left_wins else "#ccc", 240, 80)
        slide(f"""
        <div class="head-title">Engaño Visual</div>
        <div style="font-size:28px; font-weight:800; margin-bottom:20px; text-align:center; color:var(--base);">{tit}</div>
        
        <div style="display:flex; justify-content:center; gap:60px; margin-top:20px; width:100%;">
            <div style="display:flex; flex-direction:column; align-items:center; gap:20px;">
                <div class="frac-box"><div>{n1}</div><div class="line"></div><div>{d1}</div></div>
                <div class="stp">{svg1}</div>
            </div>
            
            <div class="stp" style="font-size:100px; font-weight:900; align-self:center; color:#ccc;">?</div>

            <div style="display:flex; flex-direction:column; align-items:center; gap:20px;">
                <div class="frac-box"><div>{n2}</div><div class="line"></div><div>{d2}</div></div>
                <div class="stp">{svg2}</div>
            </div>
        </div>
        
        <div class="stp" style="margin-top:40px; font-size:40px; font-weight:900; text-align:center; color:var(--base); background:#eaf1f8; padding:20px; border-radius:20px;">
            ¡A menor denominador, trozos más grandes!<br>{ans}
        </div>
        """)

    # Problema Verbal Mismo Numerador
    slide(f"""
        <div class="head-title">Problemas Situacionales 💡</div>
        <div class="pnl-border" style="text-align:center; padding:50px;">
            <p style="font-size:32px; font-weight:800; margin-bottom:20px; color:var(--base);">El Reparto de Pizza 🍕</p>
            <p style="font-size:26px; line-height:1.6; margin-bottom:30px;">Diego comió <b>2/4</b> de una pizza. Lucía comió <b>2/8</b> de una pizza igual. ¿Quién comió mayor cantidad de pizza?</p>
            
            <div class="stp" style="background:#eaf1f8; border-radius: 15px; padding:25px; text-align:left; border-left: 8px solid var(--base);">
                <p style="font-size:22px; color:#555; font-weight:800; margin-bottom:10px;">Respuesta guiada:</p>
                <div style="font-size:24px;">Ambos tomaron 2 trozos (igual numerador).<br>Pero la pizza de Diego se cortó en 4 grandes trozos y la de Lucía en 8 pedazos pequeños.<br>Por ende, Diego comió más.<br><span style='font-size:36px; color:var(--base); font-weight:900;'>2/4 > 2/8</span>.</div>
            </div>
        </div>
    """)

    # 4. LÍNEA NUMÉRICA
    def linea_num(den, num, width=600):
        w = width
        s = f'<svg width="{w+80}" height="120" viewBox="-40 -20 {w+80} 140" style="overflow:visible;">'
        s += f'<line x1="0" y1="50" x2="{w}" y2="50" stroke="#333" stroke-width="4"/>'
        s += f'<text x="0" y="90" font-family="Nunito" font-size="24" font-weight="900" text-anchor="middle">0</text>'
        s += f'<text x="{w}" y="90" font-family="Nunito" font-size="24" font-weight="900" text-anchor="middle">1</text>'
        for i in range(den+1):
            px = (w/den)*i
            s += f'<line x1="{px}" y1="40" x2="{px}" y2="60" stroke="#333" stroke-width="3"/>'
        if num > 0:
            jump_w = (w/den)*num
            s += f'<rect x="0" y="47" width="{jump_w}" height="6" fill="#9DE3BD"/>'
            s += f'<circle cx="{jump_w}" cy="50" r="12" fill="#9DE3BD" stroke="#fff" stroke-width="3"/>'
            s += f'<text x="{jump_w}" y="20" font-family="Nunito" font-size="28" font-weight="900" fill="var(--base)" text-anchor="middle">{num}/{den}</text>'
        s += '</svg>'
        return s

    slide(f"""
        <div class="head-title">La Línea Numérica</div>
        <div class="pnl-border" style="width:100%; text-align:center;">
            <p style="font-size:26px; margin-bottom:30px;">Las fracciones viven escondidas entre el número <b>0</b> y el <b>1</b>.</p>
            
            <div class="stp" style="margin-bottom:20px;">
                <p style="font-size:22px; font-weight:800; color:var(--base);">Si dividimos el espacio entre 0 y 1 en 4 partes iguales (cuartos):</p>
                {linea_num(4, 0, 700)}
            </div>
            
            <div class="stp" style="margin-top:20px;">
                <p style="font-size:22px; font-weight:800; color:#047857;">Hacer 3 saltos nos lleva a la fracción <b>3/4</b>:</p>
                {linea_num(4, 3, 700)}
            </div>
        </div>
    """)

    # Práctica Línea Numérica Adivinar con Cuaderno (4 slides)
    lin_ex = [
        ("Abre tu cuaderno: Dibuja la recta 🐸", 3, 2, "La recta está partida en 3 partes. Haz un salto en el 2."),
        ("Abre tu cuaderno: Dibuja la recta 🐸", 5, 4, "Corta tu recta en 5 y ubica la fracción."),
        ("Abre tu cuaderno: Dibuja la recta 🐸", 8, 5, "Línea cortada en 8. Posiciónate en el 5."),
        ("Abre tu cuaderno: Dibuja la recta 🐸", 6, 1, "Corta en sextos. Avanza un solo salto.")
    ]
    for tit, d, n, desc in lin_ex:
        slide(f"""
        <div class="head-title">Ubicación en la Recta</div>
        <p class="sub-text" style="color:var(--base);">{tit}</p>
        <div class="pnl-border" style="text-align:center; margin-top:20px; box-shadow:0 10px 20px rgba(0,0,0,0.05); width:90%;">
            <div style="font-size:40px; font-weight:900; color:var(--base); margin-bottom:30px; display:inline-flex; align-items:center; justify-content:center;">
                <div class="frac-box" style="margin:0;"><div>{n}</div><div class="line"></div><div>{d}</div></div>
            </div>
            <p style="font-size:20px; color:#666; margin-bottom:20px;">{desc}</p>
            <div class="stp" style="margin-top:20px;">
                <p style="font-size:24px; font-weight:800; color:#047857; margin-bottom:20px;">✅ Así debería verse en tu cuaderno:</p>
                {linea_num(d, n, 700)}
            </div>
        </div>
        """)

    # 5. FRACCIONES EQUIVALENTES (Equivalencias Visuales y Amplificar/Simplificar)
    slide(f"""
        <div class="head-title">Fracciones Equivalentes</div>
        <div class="pnl-border" style="text-align:center; width:100%;">
            <p style="font-size:28px; font-weight:800; margin-bottom:30px; color:var(--base);">A veces, números distintos valen exactamente lo mismo.</p>
            
            <div class="stp" style="display:flex; justify-content:center; gap:40px; align-items:center;">
                <div style="display:flex; flex-direction:column; align-items:center;">
                    <div class="frac-box" style="font-size:40px; padding:10px;"><div>1</div><div class="line"></div><div>2</div></div>
                    {custom_rect_frac(2, 1, "#E1BEE7", 200, 80)}
                </div>
                <div class="stp" style="font-size:80px; font-weight:900; color:var(--base);">=</div>
                <div class="stp" style="display:flex; flex-direction:column; align-items:center;">
                    <div class="frac-box" style="font-size:40px; padding:10px;"><div>2</div><div class="line"></div><div>4</div></div>
                    {custom_rect_frac(4, 2, "#E1BEE7", 200, 80)}
                </div>
            </div>
            
            <div class="stp" style="margin-top:40px; font-size:24px; background:#eaf1f8; padding:20px; border-radius:15px; border-left:8px solid var(--base);">
                Fíjate en las barras. Están partidas distinto, ¡Pero el color ocupa el <b>Mismo Espacio</b> total!<br>Ambas son MEDIO entero.
            </div>
        </div>
    """)

    equiv = [
        ("Abre tu cuaderno: Dibuja y compara", "1/3", 3, 1, "2/6", 6, 2, "#9DDEFF"),
        ("Abre tu cuaderno: Dibuja y compara", "1/4", 4, 1, "2/8", 8, 2, "#FFB74D"),
        ("Abre tu cuaderno: Dibuja y compara", "2/5", 5, 2, "4/10", 10, 4, "#9DE3BD"),
    ]
    for tit, f1, d1, n1, f2, d2, n2, col in equiv:
        slide(f"""
        <div class="head-title">Descubre la Equivalencia 🔍</div>
        <p class="sub-text" style="color:var(--base);">{tit}</p>
        <div style="display:flex; justify-content:center; align-items:center; gap:60px; margin-top:30px; width:100%;">
            <div style="display:flex; flex-direction:column; align-items:center;">
                <b style="font-size:40px; color:var(--base); margin-bottom:20px;">{f1}</b>
                <div class="stp">{custom_rect_frac(d1, n1, col, 300, 100)}</div>
            </div>
            
            <div class="stp" style="font-size:60px; font-weight:900; color:#555;">?</div>
            
            <div class="stp" style="display:flex; flex-direction:column; align-items:center;">
                <b style="font-size:40px; color:var(--base); margin-bottom:20px;">{f2}</b>
                <div class="stp">{custom_rect_frac(d2, n2, col, 300, 100)}</div>
            </div>
        </div>
        <div class="stp" style="margin-top:50px; background:#eaf1f8; padding:20px; text-align:center; font-size:26px; border-radius:15px; width:80%; border-left:8px solid var(--base);">
             ¡Ocupan exactamente el mismo tamaño! ¡Son equivalentes!
        </div>
        """)

    # Simplificación y Amplificación
    slide(f"""
        <div class="head-title">¿Cómo crear equivalencias?</div>
        <div style="display:flex; width:100%; gap:40px; margin-top:20px;">
            <div class="pnl-border stp">
                <h3 style="font-size:28px; color:var(--base); margin-bottom:15px;">🌟 Amplificar</h3>
                <p style="font-size:22px;">Multiplicamos arriba y abajo por el <b>Mismo Número</b>.</p>
                <div style="background:#eaf1f8; padding:20px; margin-top:20px; text-align:center; font-size:24px; border-radius:10px;">
                    1/3  &nbsp; <b style="font-size:30px;">➔</b> &nbsp; <span style="color:var(--base);">(x2)</span> &nbsp; <b style="font-size:30px;">➔</b> &nbsp; <b>2/6</b>
                </div>
            </div>
            
            <div class="pnl-border stp">
                <h3 style="font-size:28px; color:var(--base); margin-bottom:15px;">🔪 Simplificar</h3>
                <p style="font-size:22px;">Dividimos arriba y abajo por el <b>Mismo Número</b>.</p>
                <div style="background:#eaf1f8; padding:20px; margin-top:20px; text-align:center; font-size:24px; border-radius:10px;">
                    4/8  &nbsp; <b style="font-size:30px;">➔</b> &nbsp; <span style="color:var(--base);">(÷4)</span> &nbsp; <b style="font-size:30px;">➔</b> &nbsp; <b>1/2</b>
                </div>
            </div>
        </div>
    """)

    # Ejercicios de Amplificar y simplificar (4 slides)
    ampl_ex = [
        ("Amplifica cruzando la calle", "Amplifica <b>2/5</b> multiplicando por 2.", "2/5", "2", "multiplicar", "4/10"),
        ("Abre tu cuaderno: Amplificando", "Amplifica <b>3/4</b> multiplicando por 3.", "3/4", "3", "multiplicar", "9/12"),
        ("Abre tu cuaderno: Simplificando", "Simplifica <b>5/10</b> dividiendo por 5.", "5/10", "5", "dividir", "1/2"),
        ("El misterio equivalente", "Encuentra una equivalencia simplificando <b>6/8</b> dividiendo por 2.", "6/8", "2", "dividir", "3/4")
    ]
    for tit, prob, f1, num, op, ans in ampl_ex:
        op_sign = "x" if op == "multiplicar" else "÷"
        slide(f"""
        <div class="head-title">Equivalencias Matemáticas ✨</div>
        <p class="sub-text" style="color:var(--base); font-weight:900;">{tit}</p>
        <div class="pnl-border" style="text-align:center; padding:40px;">
            <p style="font-size:28px; margin-bottom:30px;">{prob}</p>
            
            <div style="display:inline-flex; align-items:center; gap:30px; margin-top:20px;">
                <div style="font-size:46px; font-weight:900; color:#555;">{f1}</div>
                <div class="stp" style="font-size:36px; font-weight:900; color:var(--base);">{op_sign}{num}</div>
                <div class="stp" style="font-size:50px; font-weight:900;">➔</div>
                <div class="stp" style="font-size:60px; font-weight:900; color:var(--base); background:#eaf1f8; padding:15px 30px; border-radius:15px;">{ans}</div>
            </div>
        </div>
        """)

    # Problema verbal Equivalencia (1 slide)
    slide(f"""
        <div class="head-title">Problemas Situacionales 🧑‍🍳</div>
        <div class="pnl-border" style="text-align:center; padding:50px;">
            <p style="font-size:32px; font-weight:800; margin-bottom:20px; color:var(--base);">El Chef Equivalente</p>
            <p style="font-size:26px; line-height:1.6; margin-bottom:30px;">Un cocinero necesita <b>1/2</b> litro de leche, pero su medidor solo marca en cuartos (partes de 4). ¿Cuántos cuartos necesita para llenar exactamente el medio litro?</p>
            
            <div class="stp" style="background:#eaf1f8; border-radius: 15px; padding:25px; text-align:left; border-left: 8px solid var(--base);">
                <p style="font-size:22px; color:#555; font-weight:800; margin-bottom:10px;">Respuesta guiada:</p>
                <div style="font-size:24px;">Tenemos que transformar el denominador 2 a 4.<br>Amplificamos 1/2 multiplicando por 2.<br>1x2 = 2 y 2x2= 4.<br>La respuesta es <span style='font-size:36px; color:var(--base); font-weight:900;'>2/4</span>. Necesita 2 botellitas marcadas con cuartos.</div>
            </div>
        </div>
    """)

    # Resumen Módulo 10
    slide(f"""
        <div class="head-title">📋 Qué aprendimos hoy</div>
        <div style="display:flex; flex-direction:column; gap:25px; width:100%;">
            <div class="stp pnl-border" style="padding:15px; font-size:22px;">🥇 <b>Denominador Igual:</b> ¡Sólo nos fijamos en quién pintó más! (Gana numerador mayor)</div>
            <div class="stp pnl-border" style="padding:15px; font-size:22px;">⚖️ <b>Numerador Igual:</b> El que tiene el denominador MÁS CHICO cortó trozos más gordos, así que gana.</div>
            <div class="stp pnl-border" style="padding:15px; font-size:22px;">🐸 <b>Recta Numérica:</b> Las fracciones son divisiones de la distancia entre el cero y el uno.</div>
            <div class="stp pnl-border" style="padding:15px; font-size:22px;">👯‍♀️ <b>Fracciones Equivalentes:</b> 1/2 y 2/4 se ven distintos pero valen lo mismo. Las identificamos amplificando o simplificando.</div>
        </div>
    """)
    
    slide(f"""
        <div class="head-title" style="background: #047857;">🏆 ¡Módulo Completado!</div>
        <div style="font-size:32px; font-weight:800; text-align:center; margin-top:20px;">
            ¡Ya eres un experto midiendo y descubriendo equivalencias!<br>En el último nivel vas a descubrir cómo operarlas formalmente.
        </div>
        <div style="font-size:80px; margin-top:40px; animation: bounce 2s infinite;">🎆</div>
        <style>@keyframes bounce {{ 0%, 100%{{transform:translateY(0);}} 50%{{transform:translateY(-20px);}} }}</style>
    """)

    # Output Gen
    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
    <title>Fracciones II - Comparaciones y Equivalencias</title>
    <style>{css}</style>
</head>
<body>
    <div class="pb" id="pb"></div>
    <div class="dk">
        {"".join(slides)}
    </div>
    <div class="nv">
        <button class="nb" id="pv" onclick="go(-1)">⬅ Anterior</button>
        <div class="sc" id="sc">1 / {len(slides)}</div>
        <button class="nb" id="nx" onclick="go(1)">Siguiente ➡</button>
    </div>
    <script>{js}</script>
</body>
</html>
"""
    with open('/Users/brunonattino/Desktop/PAGINA TUTORIAS/SLIDES/fracciones HTMLS/10-fracciones-2.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Módulo 10 Colors Corregido. Slides:", len(slides))

if __name__ == '__main__':
    generate_html()
