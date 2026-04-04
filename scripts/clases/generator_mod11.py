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

    def double_painted(typ, max_cnt, col1, col1_val, col2, col2_val):
        s = f'<svg width="240" height="240" viewBox="0 0 240 240">'
        c_1 = col1_val
        c_2 = col1_val + col2_val
        w,h = 240,240
        if typ == "circle6":
            s += f'<circle cx="120" cy="120" r="115" fill="none" stroke="#555" stroke-width="3"/>'
            paths = ['M120 120 L120 5 A115 115 0 0 1 220 62 Z','M120 120 L220 62 A115 115 0 0 1 220 178 Z','M120 120 L220 178 A115 115 0 0 1 120 235 Z','M120 120 L120 235 A115 115 0 0 1 20 178 Z','M120 120 L20 178 A115 115 0 0 1 20 62 Z','M120 120 L20 62 A115 115 0 0 1 120 5 Z']
            for i, p in enumerate(paths):
                if i < c_1: fill = col1
                elif i < c_2: fill = col2
                else: fill = "#fff"
                s += f'<path d="{p}" fill="{fill}" stroke="#555" stroke-width="2"/>'
        elif typ == "grid2x4":
            cw, ch = w/4, h/2
            for i in range(2):
                for j in range(4):
                    idx = i*4 + j
                    if idx < c_1: fill = col1
                    elif idx < c_2: fill = col2
                    else: fill = "#fff"
                    s += f'<rect x="{j*cw}" y="{i*ch}" width="{cw}" height="{ch}" fill="{fill}" stroke="#555" stroke-width="3"/>'
        elif typ == "circle4":
            s += f'<circle cx="120" cy="120" r="115" fill="none" stroke="#555" stroke-width="3"/>'
            paths = ['M120 120 L120 5 A115 115 0 0 1 235 120 Z','M120 120 L235 120 A115 115 0 0 1 120 235 Z','M120 120 L120 235 A115 115 0 0 1 5 120 Z','M120 120 L5 120 A115 115 0 0 1 120 5 Z']
            for i, p in enumerate(paths):
                if i < c_1: fill = col1
                elif i < c_2: fill = col2
                else: fill = "#fff"
                s += f'<path d="{p}" fill="{fill}" stroke="#555" stroke-width="2"/>'
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
            <h1 style="font-size: 70px; color: var(--base); margin-bottom: 20px; text-align:center;">Módulo 11:<br>Suma, Resta y MCM</h1>
            <p class="sub-text">Combinando piezas y descubriendo fracciones de distinto tamaño.</p>
            <p style="font-size:90px; margin-top:30px;">🎩</p>
        </div>
    """)

    # 2. SUMAR MISMO DENOMINADOR (Explicación)
    slide(f"""
        <div class="head-title">Suma de igual Denominador</div>
        <div class="pnl-border" style="flex-direction:column; width:100%;">
            <p style="font-size:28px; font-weight:800; margin-bottom:20px; color:var(--base);">Sumemos: <b>1/4</b> + <b>2/4</b></p>
            
            <div class="stp" style="display:flex; justify-content:center; align-items:center; gap:30px; margin:20px 0;">
                <div style="text-align:center;">
                    <div class="frac-box" style="margin-bottom:10px;"><div>1</div><div class="line"></div><div>4</div></div>
                </div>
                <div style="font-size:60px; font-weight:800; color:#555;">+</div>
                <div style="text-align:center;">
                    <div class="frac-box" style="margin-bottom:10px;"><div>2</div><div class="line"></div><div>4</div></div>
                </div>
                <div style="font-size:60px; font-weight:800; color:#555;">=</div>
                <div class="stp" style="text-align:center;">
                    <div class="frac-box" style="margin-bottom:10px; border-color:#047857; color:#047857;"><div>3</div><div class="line" style="background:#047857;"></div><div>4</div></div>
                </div>
            </div>

            <div class="stp" style="display:flex; align-items:center; gap:40px; margin-top:20px;">
                {double_painted("circle4", 4, "#9DDEFF", 1, "#FF9D9D", 2)}
                <div style="background:#eaf1f8; padding:20px; border-radius:15px; border-left:8px solid #047857; font-size:22px;">
                    ¡Al tener el mismo tamaño de corte abajo (denominador), sólo sumamos los números de arriba y el corte se mantiene igual!
                </div>
            </div>
        </div>
    """)

    # Ejercicios Suma/Resta MISMO DENOMINADOR Simples (8 slides!)
    sums = [
        ("Suma: 2/6 + 3/6", 2, 6, 3, 6, "+", 5, 6),
        ("Suma: 3/8 + 4/8", 3, 8, 4, 8, "+", 7, 8),
        ("Suma: 1/5 + 2/5", 1, 5, 2, 5, "+", 3, 5),
        ("Suma: 2/7 + 4/7", 2, 7, 4, 7, "+", 6, 7),
        ("Resta: 5/6 - 2/6", 5, 6, 2, 6, "-", 3, 6),
        ("Resta: 7/8 - 3/8", 7, 8, 3, 8, "-", 4, 8),
        ("Resta: 4/5 - 1/5", 4, 5, 1, 5, "-", 3, 5),
        ("Resta: 9/10 - 4/10", 9, 10, 4, 10, "-", 5, 10),
    ]
    for tit, n1, d1, n2, d2, op, rn, rd in sums:
        slide(f"""
        <div class="head-title">Practica Sumas y Restas</div>
        <p class="sub-text" style="color:var(--base);">{tit}</p>
        <div class="pnl-border" style="display:flex; justify-content:center; align-items:center; gap:40px; width:100%;">
            <div style="display:flex; flex-direction:column; align-items:center;">
                 <div class="frac-box" style="font-size:40px; margin-bottom:10px;"><div>{n1}</div><div class="line"></div><div>{d1}</div></div>
            </div>
            <div style="font-size:60px; font-weight:900; color:#888;">{op}</div>
            <div style="display:flex; flex-direction:column; align-items:center;">
                 <div class="frac-box" style="font-size:40px; margin-bottom:10px;"><div>{n2}</div><div class="line"></div><div>{d2}</div></div>
            </div>
            <div class="stp" style="font-size:60px; font-weight:900; color:#888;">=</div>
            <div class="stp" style="display:flex; flex-direction:column; align-items:center;">
                <div class="frac-box" style="font-size:60px; border-color:#047857; color:#047857; padding:20px 40px; background:#eaf1f8;">
                    <div>{rn}</div><div class="line" style="background:#047857;"></div><div>{rd}</div>
                </div>
            </div>
        </div>
        """)

    # Problemas Verbales Suma/Resta Igual Deno (2 slides)
    slide(f"""
        <div class="head-title">Analizando Situaciones 🧐</div>
        <div class="pnl-border" style="text-align:center; padding:50px;">
            <p style="font-size:32px; font-weight:800; margin-bottom:20px; color:var(--base);">Racionando el Agua 💧</p>
            <p style="font-size:26px; line-height:1.6; margin-bottom:30px;">Tenías una botella completa de agua que medía <b>5/5</b> de litro. Bebiste <b>2/5</b> en el recreo. ¿Qué fracción de agua queda en tu botella?</p>
            
            <div class="stp" style="background:#eaf1f8; border-radius: 15px; padding:25px; text-align:left; border-left: 8px solid var(--base);">
                <p style="font-size:22px; color:#555; font-weight:800; margin-bottom:10px;">Desarrollo:</p>
                <div style="font-size:24px;">Es una resta con denominador "5". <br> A 5 le quitas 2 = 3.<br><span style='font-size:36px; color:var(--base); font-weight:900;'>3/5 de litro</span> quedan en la botella.</div>
            </div>
        </div>
    """)
    slide(f"""
        <div class="head-title">Analizando Situaciones 🧐</div>
        <div class="pnl-border" style="text-align:center; padding:50px;">
            <p style="font-size:32px; font-weight:800; margin-bottom:20px; color:var(--base);">La huerta compartida 🥕</p>
            <p style="font-size:26px; line-height:1.6; margin-bottom:30px;">Plantaste tomates en <b>3/7</b> del jardín y zanahorias en <b>2/7</b> del jardín. ¿Qué fracción total del jardín usaste?</p>
            
            <div class="stp" style="background:#eaf1f8; border-radius: 15px; padding:25px; text-align:left; border-left: 8px solid var(--base);">
                <p style="font-size:22px; color:#555; font-weight:800; margin-bottom:10px;">Desarrollo:</p>
                <div style="font-size:24px;">Es una suma directa (mismo denominador "7").<br> 3 + 2 = 5.<br>Ocupaste <span style='font-size:36px; color:var(--base); font-weight:900;'>5/7</span> del jardín.</div>
            </div>
        </div>
    """)

    # 3. EL PROBLEMA (MCM Intro)
    slide(f"""
        <div class="head-title" style="background:#F57F17;">¡Problema! ¿Denominadores Distintos?</div>
        <div class="pnl-border" style="border-color: #FBC02D; text-align:center; font-size:26px;">
            <p>¿Qué pasa si queremos <b>Sumar</b>:  <b>2/3</b> y <b>3/4</b>?</p>
            <div class="stp" style="margin-top:20px; font-weight:800; color:#b91c1c;">¡No tienen el mismo denominador! Unos son pedazos de tres, y otros de cuatro.</div>
            <div class="stp" style="margin-top:20px; font-size:80px; animation:shake 1s infinite alternate;">😖</div>
            <div class="stp" style="margin-top:20px; font-weight:800; font-size:24px; color:var(--base);">
                Para poder operarlas, tenemos que hacer que tengan el mismo denominador inferior.<br><br>
                Para lograr eso, buscamos un aliado llamado: <br><span style="font-size:40px; color:#F57C00; font-weight:900;">Mínimo Común Múltiplo (MCM)</span>.
            </div>
        </div>
        <style>@keyframes shake {{ 0%{{transform:translateX(-10px);}} 100%{{transform:translateX(10px);}} }}</style>
    """)

    # EXPLICANDO EL MCM
    slide(f"""
        <div class="head-title">¿Qué es el MCM?</div>
        <div class="pnl-border" style="flex-direction:column; text-align:center;">
            <p style="font-size:24px; margin-top:5px; color:var(--base); font-weight:900;">Es buscar el número <b>más pequeño</b> que aparezca repetido en las tablas de multiplicar de los dos denominadores.</p>
            
            <div class="stp" style="background:#f5f6f8; padding:20px; border-radius:20px; width:100%; margin-top:20px;">
                <b style="font-size:24px; color:#555;">Miremos 2/3 y 3/4. Vamos a las tablas del 3 y del 4.</b>
                <div style="font-size:26px; margin-top:20px; display:inline-block; font-family:monospace; text-align:left;">
                    <b>Tabla del 3:</b> 3 - 6 - 9 - <span class="stp hl" style="background:#FFDEE9; padding:5px; border-radius:8px;">12</span> - 15 - 18...\n
                    <br><br>
                    <b>Tabla del 4:</b> 4 - 8 - <span class="stp hl" style="background:#FFDEE9; padding:5px; border-radius:8px;">12</span> - 16 - 20...
                </div>
            </div>
            
            <div class="stp" style="margin-top:20px; font-size:30px; font-weight:900; color:var(--base);">
                Tienen como primer MÍNIMO REPETIDO el número 12. ¡Ese es su MCM!
            </div>
        </div>
    """)

    # PRÁCTICA DE MCM (7 slides de tablas)
    mcm_ex = [
        ("Encuentra el MCM de 2 y 5", 2, "2, 4, 6, 8, <span class='hl'>10</span>", 5, "5, <span class='hl'>10</span>, 15", 10),
        ("Encuentra el MCM de 4 y 5", 4, "4, 8, 12, 16, <span class='hl'>20</span>", 5, "5, 10, 15, <span class='hl'>20</span>", 20),
        ("Encuentra el MCM de 3 y 6", 3, "3, <span class='hl'>6</span>, 9", 6, "<span class='hl'>6</span>, 12", 6),
        ("Encuentra el MCM de 2 y 3", 2, "2, 4, <span class='hl'>6</span>", 3, "3, <span class='hl'>6</span>", 6),
        ("Encuentra el MCM de 3 y 5", 3, "3, 6, 9, 12, <span class='hl'>15</span>", 5, "5, 10, <span class='hl'>15</span>", 15),
        ("Encuentra el MCM de 2 y 4", 2, "2, <span class='hl'>4</span>, 6", 4, "<span class='hl'>4</span>, 8, 12", 4),
        ("Encuentra el MCM de 6 y 8", 6, "6, 12, 18, <span class='hl'>24</span>", 8, "8, 16, <span class='hl'>24</span>", 24),
    ]
    for tit, d1, t1, d2, t2, mcm in mcm_ex:
        slide(f"""
        <div class="head-title">¡A Practicar MCM!</div>
        <p class="sub-text" style="font-size:28px; color:var(--base);">{tit}</p>
        <div class="pnl-border" style="font-size:26px; text-align:center;">
            Calculemos revisando las tablas de multiplicar del <b>{d1}</b> y <b>{d2}</b>.
            
            <div class="stp" style="margin-top:20px; display:flex; flex-direction:column; gap:15px; font-size:30px;">
                <div style="background:#f8f9fa; padding:15px; border-radius:10px;">
                    <b>Tabla del {d1}:</b> <span class="stp">{t1}...</span>
                </div>
                <div style="background:#f8f9fa; padding:15px; border-radius:10px;">
                    <b>Tabla del {d2}:</b> <span class="stp">{t2}...</span>
                </div>
            </div>
            
            <div class="stp" style="margin-top:40px; font-size:46px; font-weight:900; color:#047857; background:#E8F5E9; padding:20px; border-radius:20px;">
                ¡El MCM es {mcm}! ✅
            </div>
        </div>
        """)

    # 4. APLICANDO MCM PARA COMPARAR Y SUMAR
    slide(f"""
        <div class="head-title">Paso Final: Amplificar con el MCM</div>
        <div class="pnl-border" style="width:100%;">
            <p style="font-size:28px; font-weight:800; text-align:center; margin-bottom:20px; color:var(--base);">Cómo operar: <b>2/3 + 3/4</b></p>
            
            <div class="stp" style="background:#f5f6f8; padding:15px 30px; border-radius:15px; font-size:24px;">
                <b>Paso 1:</b> Sabemos que el MCM de 3 y 4 es <b style="font-size:30px; color:var(--base);">12</b>.
            </div>
            
            <div class="stp" style="margin-top:15px; background:#f5f6f8; padding:15px 30px; border-radius:15px; font-size:24px;">
                <b>Paso 2:</b> Amplificar (multiplicar arriba y abajo) para que el denominador quede en 12:<br><br>
                El 3 para llegar a 12 se multiplica por 4: &nbsp; <b>2/3 <span style="color:var(--base);">(x4)</span> = 8/12</b><br>
                El 4 para llegar a 12 se multiplica por 3: &nbsp; <b>3/4 <span style="color:var(--base);">(x3)</span> = 9/12</b>
            </div>
            
            <div class="stp" style="margin-top:15px; background:#E8F5E9; padding:15px 30px; border-radius:15px; font-size:28px; text-align:center;">
                <b style="color:#2E7D32;">Paso 3: ¡Ya tienen denominadores iguales!</b><br>
                Reemplazamos: <b style="font-size:36px;">8/12 + 9/12 = 17/12</b><br>
                ¡Listo!
            </div>
        </div>
    """)

    # 5. SUMA/RESTA CON MCM Ejemplos y Práctica (4 slides)
    res_list = [
        ("Suma: 1/2 + 1/3", 2, 3, 6, "1/2 (x3) = 3/6<br>1/3 (x2) = 2/6", "3/6 + 2/6 = <b style='color:#047857'>5/6</b>"),
        ("Resta: 3/4 - 1/2", 4, 2, 4, "3/4 se queda en 3/4 (ya es 4).<br>1/2 (x2) = 2/4", "3/4 - 2/4 = <b style='color:#047857'>1/4</b>"),
        ("Suma: 2/5 + 1/2", 5, 2, 10, "2/5 (x2) = 4/10<br>1/2 (x5) = 5/10", "4/10 + 5/10 = <b style='color:#047857'>9/10</b>"),
        ("Resta: 2/3 - 1/6", 3, 6, 6, "2/3 (x2) = 4/6.<br>1/6 se queda igual.", "4/6 - 1/6 = <b style='color:#047857'>3/6</b>")
    ]
    for tit, d1, d2, mcm, paso2, ans in res_list:
        slide(f"""
        <div class="head-title">Suma y Resta Avanzada</div>
        <div class="pnl-border" style="padding:40px; width:100%;">
            <p style="font-size:32px; font-weight:900; text-align:center; margin-bottom:30px; color:var(--base);">{tit}</p>
            
            <div class="stp" style="font-size:26px; border-bottom:2px dashed #ccc; padding-bottom:15px;">
                <b>1.</b> MCM entre {d1} y {d2} = <b>{mcm}</b>
            </div>
            <div class="stp" style="font-size:26px; border-bottom:2px dashed #ccc; padding:15px 0;">
                <b>2.</b> Amplificar:<br>{paso2}
            </div>
            <div class="stp" style="font-size:36px; padding-top:15px; text-align:center;">
                <b>3.</b> ¡Resultado!<br>{ans}
            </div>
        </div>
        """)

    # 6. PROBLEMAS VERBALES MCM (4 slides)
    verbals = [
        ("Muro a medias", "Pintaste <b>1/2</b> del muro y tu hermana pintó <b>1/4</b>. ¿Cuánto muro pintaron en total?", "MCM es 4.<br>Amplificas tu 1/2 multiplicando por 2 = 2/4.<br>2/4 + 1/4 = <span style='font-size:46px; color:var(--base);'>3/4</span>.", "🎨"),
        ("El pastel de zanahoria", "Quedaba <b>3/4</b> del pastel. Un amigo con hambre se comió <b>1/2</b> del pastel completo. ¿Cuánto pastel queda ahora?", "MCM es 4.<br>El medio que se comió equivale a 2/4.<br>3/4 menos 2/4 = <span style='font-size:46px; color:var(--base);'>1/4</span>.", "🍰"),
        ("Ejercicio matutino", "Corriste <b>2/3</b> de kilómetro y luego caminaste <b>1/6</b> de kilómetro más. ¿Cuántos kilómetros avanzaste?", "MCM de 3 y 6 es 6.<br>2/3 por (x2) = 4/6.<br>4/6 + 1/6 = <span style='font-size:46px; color:var(--base);'>5/6</span>.", "🏃🏽‍♂️"),
        ("Colección de rocas", "Tú ocupaste <b>1/5</b> de la caja con rocas y tu primo ocupó <b>1/2</b>. ¿Cuánto de la caja está llena por ambos?", "MCM entre 5 y 2 es 10.<br>Tú tienes 2/10 y tu primo 5/10.<br>En total ocuparon <span style='font-size:46px; color:var(--base);'>7/10</span>.", "🪨")
    ]
    for tit, prob, ans, emoji in verbals:
        slide(f"""
        <div class="head-title">Resolviendo la realidad 💡</div>
        <div class="pnl-border" style="padding:40px; display:flex; gap:40px; align-items:center; width:100%;">
            <div style="font-size:120px;">{emoji}</div>
            <div style="flex:1;">
                <h2 style="font-size:32px; color:var(--base); margin-bottom:15px;">{tit}</h2>
                <p style="font-size:26px;">{prob}</p>
                
                <div class="stp" style="margin-top:20px; background:#f5f6f8; padding:20px; border-radius:20px; border-left: 10px solid var(--base);">
                    <p style="font-size:22px; font-weight:800; color:#555;">La respuesta guiada:</p>
                    <div style="font-size:26px; font-weight:900; margin-top:10px;">{ans}</div>
                </div>
            </div>
        </div>
        """)

    # 7. CIERRE DEFINITIVO (2 slides funcionales)
    slide(f"""
        <div class="head-title">📋 Resumen Definitivo</div>
        <div style="display:flex; flex-direction:column; gap:20px; width:100%;">
            <div class="stp pnl-border" style="padding:15px; font-size:22px;"><b style="font-size:36px">➕</b> <b>Igual Denominador:</b> Para sumar/restar, mantenemos el número inferior y operamos sólo lo de arriba.</div>
            <div class="stp pnl-border" style="padding:15px; font-size:22px;"><b style="font-size:36px">❌</b> <b>Distinto Denominador:</b> No se pueden combinar si están cortadas distinto. Hay que transformar usando tablitas.</div>
            <div class="stp pnl-border" style="padding:15px; font-size:22px;"><b style="font-size:36px">✨</b> <b>El MCM Mágico:</b> Buscamos el mínimo común múltiplo para saber a qué corte debemos igualarlas usando amplificación.</div>
        </div>
    """)
    
    slide(f"""
        <div class="head-title" style="background: #047857;">🏆 CURSO COMPLETADO</div>
        <div style="font-size:32px; font-weight:800; text-align:center; margin-top:20px; line-height:1.5;">
            Has dominado las divisiones de la realidad.<br>Sabes qué son, sabes ordenarlas y ¡sabes sumarlas y restarlas usando MCM!<br>
            <b style="font-size:40px; color:#2E7D32;">¡Felicitaciones gigantes! Eres un genio de las fracciones.</b>
        </div>
        <div style="font-size:100px; margin-top:40px; animation: bounce 2s infinite;">😎🎉🌠</div>
        <style>@keyframes bounce {{ 0%, 100%{{transform:translateY(0);}} 50%{{transform:translateY(-20px);}} }}</style>
    """)

    # Output Gen
    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
    <title>Fracciones III - Suma, Resta y MCM</title>
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
    with open('/Users/brunonattino/Desktop/PAGINA TUTORIAS/SLIDES/fracciones HTMLS/11-ejercicios-fracciones.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Módulo 11 Colors Corregido. Slides:", len(slides))

if __name__ == '__main__':
    generate_html()
