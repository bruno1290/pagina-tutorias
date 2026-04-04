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
    .sub-text {font-size: 24px; font-weight: 600; margin-bottom: 30px; text-align: center;}
    .frac-box {border: 3px dashed var(--base); border-radius: 20px; display: inline-flex; flex-direction: column; align-items: center; justify-content: center; padding: 15px 30px; font-size: 60px; font-weight: 900; line-height: 1; margin: 0 20px;}
    .frac-box div.line {height: 4px; width: 100%; background: #333; margin: 5px 0; border-radius: 2px;}
    .read-as {font-size: 24px; font-weight: 800;}
    
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
    .hl {color: var(--base); font-weight: 900;}
    
    .btn {background: var(--base); color: white; border: none; padding: 14px 28px; border-radius: 12px; font-size: 20px; font-weight: 900; cursor: pointer; transition: transform .2s;}
    .btn:hover {transform: translateY(-2px); box-shadow: 0 4px 12px rgba(28,74,130,0.3);}
    .svg-pt {cursor: pointer; transition: opacity .2s;}
    .svg-pt:hover {opacity: 0.8;}
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
    function ptSVG(el, colon, coloff) {
        let isOn = el.getAttribute('data-on') === '1';
        el.setAttribute('fill', isOn ? coloff : colon);
        el.setAttribute('data-on', isOn ? '0' : '1');
    }
    """
    
    slides = []
    def slide(html): slides.append(f'<div class="sl">{html}</div>')

    # Intro
    slide(f"""
        <div style="flex:1; display:flex; flex-direction:column; justify-content:center; align-items:center;">
            <h1 style="font-size: 70px; color: var(--base); margin-bottom: 20px;">¡Fracciones I!</h1>
            <p class="sub-text">Paso a paso, a tu ritmo.</p>
            <p style="font-size:90px; margin-top:30px;">🏫</p>
        </div>
    """)
    
    # 1. ¿Qué es una fracción? (PPT 1)
    slide(f"""
        <div class="head-title">Recordemos lo que es una fracción</div>
        <div style="display:flex; align-items: center; justify-content: center; gap: 40px; margin-top: 40px; width:100%;">
            <svg width="300" height="200" viewBox="0 0 300 200" style="border:3px solid #555; background: #fff;">
                <rect x="0" y="0" width="100" height="100" fill="#6be3db" stroke="#555" stroke-width="3"/>
                <rect x="100" y="0" width="100" height="100" fill="#6be3db" stroke="#555" stroke-width="3"/>
                <rect x="200" y="0" width="100" height="100" fill="#fff" stroke="#555" stroke-width="3"/>
                <rect x="0" y="100" width="100" height="100" fill="#6be3db" stroke="#555" stroke-width="3"/>
                <rect x="100" y="100" width="100" height="100" fill="#fff" stroke="#555" stroke-width="3"/>
                <rect x="200" y="100" width="100" height="100" fill="#fff" stroke="#555" stroke-width="3"/>
            </svg>
            <div class="frac-box" style="position:relative;">
                <div>3</div><div class="line"></div><div>6</div>
                <div class="stp" style="position:absolute; top:25px; left:100%; width:220px; font-size:18px; margin-left:30px; border-left: 4px solid var(--base); padding-left: 15px;">
                    <b class="hl">NUMERADOR:</b><br>Cantidad de partes pintadas.
                </div>
                <div class="stp" style="position:absolute; bottom:15px; left:100%; width:220px; font-size:18px; margin-left:30px; border-left: 4px solid var(--base); padding-left: 15px;">
                    <b class="hl">DENOMINADOR:</b><br>Cantidad de partes totales de la figura.
                </div>
            </div>
        </div>
    """)

    # PPT 1: Partes iguales
    slide(f"""
        <div class="head-title">¡Deben ser partes IGUALES!</div>
        <p class="sub-text">Para que sea una fracción, cada pedacito debe ser <b>exactamente del mismo tamaño</b>.</p>
        <div style="display:flex; width:100%; justify-content:center; gap: 40px; margin-top:20px;">
            <div class="pnl stp" style="display:flex; flex-direction:column; align-items:center; width: 45%;">
                <div style="font-size:24px; font-weight:800; margin-bottom: 20px;">¿Esto es 1/4?</div>
                <svg width="150" height="150" viewBox="0 0 150 150">
                    <circle cx="75" cy="75" r="70" fill="#fff" stroke="#555" stroke-width="3"/>
                    <path d="M75 75 L75 5 A70 70 0 0 1 145 75 Z" fill="#FF6B9D" stroke="#555" stroke-width="3"/>
                    <path d="M75 75 L145 75 A70 70 0 0 1 75 145 Z" fill="#fff" stroke="#555" stroke-width="3"/>
                    <path d="M75 75 L75 145 A70 70 0 0 1 5 75 Z" fill="#fff" stroke="#555" stroke-width="3"/>
                    <path d="M75 75 L5 75 A70 70 0 0 1 75 5 Z" fill="#fff" stroke="#555" stroke-width="3"/>
                </svg>
                <div class="stp" style="margin-top:20px; font-size:20px; font-weight:800; color:#047857;">✅ ¡Sí! Están todos iguales.</div>
            </div>
            
            <div class="pnl stp" style="display:flex; flex-direction:column; align-items:center; width: 45%;">
                <div style="font-size:24px; font-weight:800; margin-bottom: 20px;">¿Y esto es 1/4?</div>
                <svg width="150" height="150" viewBox="0 0 150 150">
                    <rect x="5" y="5" width="140" height="140" fill="#fff" stroke="#555" stroke-width="3"/>
                    <rect x="5" y="5" width="40" height="140" fill="#FFD166" stroke="#555" stroke-width="3"/>
                    <line x1="100" y1="5" x2="100" y2="145" stroke="#555" stroke-width="3"/>
                    <line x1="120" y1="5" x2="120" y2="145" stroke="#555" stroke-width="3"/>
                </svg>
                <div class="stp" style="margin-top:20px; font-size:20px; font-weight:800; color:#b91c1c;">❌ ¡No! Tienen distinto tamaño.</div>
            </div>
        </div>
    """)

    # PPT 2: ¿Qué fracción representa? (Abre tu cuaderno logic)
    slide(f"""
        <div class="head-title">Abre tu cuaderno</div>
        <p class="sub-text">Observa y anota: ¿Qué fracción representa cada figura?</p>
        <div style="display:flex; flex-direction:column; width:100%; gap: 30px; margin-top:10px;">
            <div class="stp" style="display:flex; align-items:center; gap:40px; padding-left: 80px;">
                <svg width="240" height="80" viewBox="0 0 240 80">
                    <rect x="0" y="0" width="240" height="80" fill="#fff" stroke="#555" stroke-width="2"/>
                    <rect x="0" y="0" width="60" height="80" fill="#9de3bd" stroke="#555" stroke-width="2"/>
                    <rect x="60" y="0" width="60" height="80" fill="#9de3bd" stroke="#555" stroke-width="2"/>
                    <rect x="120" y="0" width="60" height="80" fill="#9de3bd" stroke="#555" stroke-width="2"/>
                    <line x1="180" y1="0" x2="180" y2="80" stroke="#555" stroke-width="2"/>
                </svg>
                <b style="font-size:40px;">➔</b>
                <div class="stp">
                    <div class="frac-box" style="padding:10px 20px; font-size:40px; margin:0;"><div>3</div><div class="line"></div><div>4</div></div>
                </div>
            </div>

            <div class="stp" style="display:flex; align-items:center; gap:40px; padding-left: 80px;">
                <svg width="240" height="80" viewBox="0 0 240 80">
                    <rect x="0" y="0" width="240" height="80" fill="#fff" stroke="#555" stroke-width="2"/>
                    <rect x="0" y="0" width="40" height="80" fill="#f194b4" stroke="#555" stroke-width="2"/>
                    <rect x="40" y="0" width="40" height="80" fill="#f194b4" stroke="#555" stroke-width="2"/>
                    <line x1="80" y1="0" x2="80" y2="80" stroke="#555" stroke-width="2"/>
                    <line x1="120" y1="0" x2="120" y2="80" stroke="#555" stroke-width="2"/>
                    <line x1="160" y1="0" x2="160" y2="80" stroke="#555" stroke-width="2"/>
                    <line x1="200" y1="0" x2="200" y2="80" stroke="#555" stroke-width="2"/>
                </svg>
                <b style="font-size:40px;">➔</b>
                <div class="stp">
                    <div class="frac-box" style="padding:10px 20px; font-size:40px; margin:0;"><div>2</div><div class="line"></div><div>6</div></div>
                </div>
            </div>
            
            <div class="stp" style="display:flex; justify-content:center; margin-top:20px;">
                <p style="font-size:24px; color:var(--base); font-weight:800;">¡Recuerda contar el total de cuadritos para el denominador!</p>
            </div>
        </div>
    """)

    # PPT 3: Diferentes formas
    def rep_slide(n, d, text, svgs):
        return f"""
        <div class="head-title">Representaciones (PPT 3)</div>
        <p class="sub-text">La fracción puede representarse en distintas figuras.</p>
        <div style="display:flex; width:100%; justify-content:center; gap: 60px; margin-top:40px;">
            <div style="display:flex; align-items:center; gap:20px;">
                <div class="frac-box"><div>{n}</div><div class="line"></div><div>{d}</div></div>
                <div class="read-as" style="font-size:28px;">{text}</div>
            </div>
            <div class="stp" style="display:flex; flex-direction:column; align-items:center;">
                <div style="font-size:28px; font-weight:800; margin-bottom:30px;">Se representa:</div>
                <div style="display:flex; gap:30px; align-items:flex-end;">
                    {svgs}
                </div>
            </div>
        </div>
        """

    # 1/2
    slide(rep_slide("1", "2", "Un<br>medio", """
        <svg width="140" height="140" viewBox="0 0 120 120"><rect x="0" y="0" width="60" height="120" fill="#f194b4" stroke="#555" stroke-width="3"/><rect x="60" y="0" width="60" height="120" fill="#fff" stroke="#555" stroke-width="3"/></svg>
        <svg width="160" height="140" viewBox="0 0 140 120"><polygon points="70,0 0,120 70,120" fill="#fff" stroke="#555" stroke-width="3"/><polygon points="70,0 140,120 70,120" fill="#6be3db" stroke="#555" stroke-width="3"/></svg>
        <svg width="200" height="80" viewBox="0 0 160 60"><polygon points="0,15 120,15 120,0 160,30 120,60 120,45 0,45" fill="#f5f6f8" stroke="#555" stroke-width="3"/><polygon points="0,15 120,15 120,0 160,30 110,30 0,30" fill="#f3a033" stroke-width="0"/><polygon points="0,15 120,15 120,0 160,30 120,60 120,45 0,45" fill="none" stroke="#555" stroke-width="3"/></svg>
    """))

    # 1/3
    slide(rep_slide("1", "3", "Un<br>tercio", """
        <svg width="140" height="140" viewBox="0 0 120 120"><rect x="0" y="0" width="40" height="120" fill="#b993d6" stroke="#555" stroke-width="3"/><rect x="40" y="0" width="40" height="120" fill="#fff" stroke="#555" stroke-width="3"/><rect x="80" y="0" width="40" height="120" fill="#fff" stroke="#555" stroke-width="3"/></svg>
        <svg width="140" height="140" viewBox="0 0 120 120"><circle cx="60" cy="60" r="58" fill="#fff" stroke="#555" stroke-width="3"/><path d="M60 60 L60 2 A58 58 0 0 1 110 90 Z" fill="#fff" stroke="#555" stroke-width="3"/><path d="M60 60 L110 90 A58 58 0 0 1 10 90 Z" fill="#a4cbfc" stroke="#555" stroke-width="3"/><path d="M60 60 L10 90 A58 58 0 0 1 60 2 Z" fill="#fff" stroke="#555" stroke-width="3"/></svg>
    """))

    # 1/4
    slide(rep_slide("1", "4", "Un<br>cuarto", """
        <svg width="160" height="140" viewBox="0 0 140 120"><polygon points="70,0 0,120 140,120" fill="#fff" stroke="#555" stroke-width="3"/><polygon points="70,0 35,60 105,60" fill="#fff" stroke="#555" stroke-width="2"/><polygon points="35,60 0,120 70,120" fill="#fff" stroke="#555" stroke-width="2"/><polygon points="105,60 70,120 140,120" fill="#f194b4" stroke="#555" stroke-width="2"/><polygon points="35,60 105,60 70,120" fill="#fff" stroke="#555" stroke-width="2"/></svg>
        <svg width="140" height="140" viewBox="0 0 120 120"><circle cx="60" cy="60" r="58" fill="#fff" stroke="#555" stroke-width="3"/><path d="M60 60 L60 2 A58 58 0 0 1 118 60 Z" fill="#b993d6" stroke="#555" stroke-width="3"/><path d="M60 60 L118 60 A58 58 0 0 1 60 118 Z" fill="#fff" stroke="#555" stroke-width="3"/><path d="M60 60 L60 118 A58 58 0 0 1 2 60 Z" fill="#fff" stroke="#555" stroke-width="3"/><path d="M60 60 L2 60 A58 58 0 0 1 60 2 Z" fill="#fff" stroke="#555" stroke-width="3"/></svg>
    """))

    # PPT 4: COMPARACIÓN Mismo Denominador
    slide(f"""
        <div class="head-title">Comparar Mismo Denominador (PPT 4)</div>
        <div class="pnl">
            <p style="font-size:24px; text-align:center; font-weight:800; margin-bottom:20px;">Comparamos <b>3/8</b> y <b>5/8</b></p>
            <div style="display:flex; justify-content:center; gap:20px; align-items:center;">
                <div style="text-align:center;">
                    <div class="frac-box" style="font-size:40px; padding: 10px 20px;"><div>3</div><div class="line"></div><div>8</div></div>
                </div>
                <div style="font-size:40px; font-weight:900;">vs</div>
                <div style="text-align:center;">
                    <div class="frac-box" style="font-size:40px; padding: 10px 20px;"><div>5</div><div class="line"></div><div>8</div></div>
                </div>
            </div>
        </div>
        <div class="stp" style="width: 100%;">
            <p class="sub-text" style="color:var(--base); margin-bottom:10px;">¡Tienen el mismo denominador!</p>
            <p class="sub-text" style="font-size:20px;">Significa que los pedazos de la torta son del mismo tamaño.</p>
        </div>
        <div class="stp" style="width: 100%;">
            <div class="pnl" style="background:#eaf1f8; text-align:center; border: 3px dashed var(--base);">
                <p style="font-size:26px; font-weight:900;">Regla: Si hay la misma cantidad de pedazos en la torta (denominador), la fracción mayor es la que tiene... ¡Más pedazos pintados (NUMERADOR MAYOR)!</p>
                <div class="stp" style="margin-top:20px; font-size:36px; font-weight:900; color:var(--base);">5/8 > 3/8</div>
            </div>
        </div>
    """)

    # PPT 4: COMPARACIÓN Mismo Numerador
    slide(f"""
        <div class="head-title">Comparar Mismo Numerador (PPT 4)</div>
        <div class="pnl">
            <p style="font-size:24px; text-align:center; font-weight:800; margin-bottom:20px;">Comparamos <b>1/3</b> y <b>1/5</b></p>
            <div style="display:flex; justify-content:center; gap:20px; align-items:center;">
                <div style="text-align:center;">
                    <div class="frac-box" style="font-size:40px; padding: 10px 20px;"><div>1</div><div class="line"></div><div>3</div></div>
                </div>
                <div style="font-size:40px; font-weight:900;">vs</div>
                <div style="text-align:center;">
                    <div class="frac-box" style="font-size:40px; padding: 10px 20px;"><div>1</div><div class="line"></div><div>5</div></div>
                </div>
            </div>
        </div>
        <div class="stp" style="width: 100%;">
            <p class="sub-text" style="color:var(--base); margin-bottom:10px;">¡El numerador es igual, tomas solo 1 trozo!</p>
            <p class="sub-text" style="font-size:20px;">Pero... ¿Qué torta tiene pedazos más grandes?</p>
        </div>
        <div class="stp" style="display:flex; gap:40px; justify-content:center; width: 100%;">
            <svg width="100" height="100" viewBox="0 0 120 120"><circle cx="60" cy="60" r="58" fill="#fff" stroke="#555" stroke-width="3"/><path d="M60 60 L60 2 A58 58 0 0 1 110 90 Z" fill="#f194b4" stroke="#555" stroke-width="3"/><path d="M60 60 L110 90 A58 58 0 0 1 10 90 Z" fill="#fff" stroke="#555" stroke-width="3"/><path d="M60 60 L10 90 A58 58 0 0 1 60 2 Z" fill="#fff" stroke="#555" stroke-width="3"/></svg>
            <svg width="100" height="100" viewBox="0 0 120 120"><circle cx="60" cy="60" r="58" fill="#fff" stroke="#555" stroke-width="3"/><path d="M60 60 L60 2 A58 58 0 0 0 5 42 Z" fill="#9de3bd" stroke="#555" stroke-width="3"/><path d="M60 60 L5 42 A58 58 0 0 0 26 107 Z" fill="#fff" stroke="#555" stroke-width="3"/><path d="M60 60 L26 107 A58 58 0 0 0 94 107 Z" fill="#fff" stroke="#555" stroke-width="3"/><path d="M60 60 L94 107 A58 58 0 0 0 115 42 Z" fill="#fff" stroke="#555" stroke-width="3"/><path d="M60 60 L115 42 A58 58 0 0 0 60 2 Z" fill="#fff" stroke="#555" stroke-width="3"/></svg>
        </div>
        <div class="stp" style="width: 100%; margin-top:20px;">
            <div class="pnl" style="background:#fce7f3; text-align:center; border: 3px dashed #db2777;">
                <p style="font-size:26px; font-weight:900;">Regla: Si comparten numerador, es mayor la fracción con el DENOMINADOR MÁS CHICO (¡menos cortes = trozos más grandes!). -> 1/3 > 1/5</p>
            </div>
        </div>
    """)

    # PPT 5: Distinto Denominador
    slide(f"""
        <div class="head-title">Todo Distinto (PPT 5)</div>
        <p class="sub-text">¿Y si queremos comparar <b>2/3</b> y <b>3/4</b>?</p>
        
        <div class="pnl stp" style="padding: 20px 40px; margin-bottom:15px; font-size:24px;">
            <b class="hl">Paso 1:</b> Buscamos el Mínimo Común Múltiplo (MCM) de los denominadores (3 y 4).
            <div class="stp" style="text-align:center; font-weight:800; font-size:32px; margin-top:10px; color:var(--base);">MCM = 12</div>
        </div>

        <div class="pnl stp" style="padding: 20px 40px; margin-bottom:15px; font-size:24px;">
            <b class="hl">Paso 2:</b> Amplificamos ambas fracciones para que su denominador sea 12.
            <div class="stp" style="display:flex; justify-content:space-around; margin-top:15px; font-weight:800; font-size:26px;">
                <div>2/3 x 4 = <span class="hl">8/12</span></div>
                <div>3/4 x 3 = <span class="hl">9/12</span></div>
            </div>
        </div>

        <div class="pnl stp" style="padding: 20px 40px; margin-bottom:15px; font-size:24px;">
            <b class="hl">Paso 3:</b> ¡Ahora comparamos! Ambas tienen denominador 12.
            <div class="stp" style="text-align:center; margin-top:15px; font-weight:900; font-size:36px; color:#047857;">
                9/12 > 8/12 <br><span style="font-size:24px;">Por lo tanto: <b>3/4 es mayor que 2/3</b></span>
            </div>
        </div>
    """)

    # Añadimos Interactividades Visuales (para completar slides hasta ~25)
    ex_list = [
        ("¡Pinta 2/3 en el rectángulo!", "2", "3", "rect", "#b993d6", 3),
        ("¡Pinta 3/4 en el círculo!", "3", "4", "circle4", "#f194b4", 4),
        ("¡Pinta 2/5 en el círculo!", "2", "5", "circle5", "#9de3bd", 5),
        ("¡Pinta 4/6 en el cuadro!", "4", "6", "grid2x3", "#6be3db", 6),
        ("¡Pinta 3/8 en esta grilla!", "3", "8", "grid2x4", "#fc4d51", 8),
    ]

    def get_svg(typ, color):
        s = f'<svg width="240" height="240" viewBox="0 0 240 240">'
        if typ == "rect":
            for i in range(3):
                s += f'<rect x="{i*80}" y="20" width="80" height="200" fill="#fff" stroke="#555" stroke-width="3" class="svg-pt" data-on="0" onclick="ptSVG(this,\\"{color}\\",\\"#fff\\")"/>'
        elif typ == "grid2x3":
            for i in range(2):
                for j in range(3):
                    s += f'<rect x="{j*80}" y="{i*120}" width="80" height="120" fill="#fff" stroke="#555" stroke-width="3" class="svg-pt" data-on="0" onclick="ptSVG(this,\\"{color}\\",\\"#fff\\")"/>'
        elif typ == "grid2x4":
            for i in range(2):
                for j in range(4):
                    s += f'<rect x="{j*60}" y="{i*120}" width="60" height="120" fill="#fff" stroke="#555" stroke-width="3" class="svg-pt" data-on="0" onclick="ptSVG(this,\\"{color}\\",\\"#fff\\")"/>'
        elif typ == "circle4":
            s += f'<circle cx="120" cy="120" r="115" fill="none" stroke="#555" stroke-width="3"/>'
            s += f'<path d="M120 120 L120 5 A115 115 0 0 1 235 120 Z" fill="#fff" stroke="#555" stroke-width="2" class="svg-pt" data-on="0" onclick="ptSVG(this,\\"{color}\\",\\"#fff\\")"/>'
            s += f'<path d="M120 120 L235 120 A115 115 0 0 1 120 235 Z" fill="#fff" stroke="#555" stroke-width="2" class="svg-pt" data-on="0" onclick="ptSVG(this,\\"{color}\\",\\"#fff\\")"/>'
            s += f'<path d="M120 120 L120 235 A115 115 0 0 1 5 120 Z" fill="#fff" stroke="#555" stroke-width="2" class="svg-pt" data-on="0" onclick="ptSVG(this,\\"{color}\\",\\"#fff\\")"/>'
            s += f'<path d="M120 120 L5 120 A115 115 0 0 1 120 5 Z" fill="#fff" stroke="#555" stroke-width="2" class="svg-pt" data-on="0" onclick="ptSVG(this,\\"{color}\\",\\"#fff\\")"/>'
        elif typ == "circle5":
            s += f'<circle cx="120" cy="120" r="115" fill="none" stroke="#555" stroke-width="3"/>'
            s += f'<path d="M120 120 L120 5 A115 115 0 0 0 10 84 Z" fill="#fff" stroke="#555" stroke-width="2" class="svg-pt" data-on="0" onclick="ptSVG(this,\\"{color}\\",\\"#fff\\")"/>'
            s += f'<path d="M120 120 L10 84 A115 115 0 0 0 52 213 Z" fill="#fff" stroke="#555" stroke-width="2" class="svg-pt" data-on="0" onclick="ptSVG(this,\\"{color}\\",\\"#fff\\")"/>'
            s += f'<path d="M120 120 L52 213 A115 115 0 0 0 188 213 Z" fill="#fff" stroke="#555" stroke-width="2" class="svg-pt" data-on="0" onclick="ptSVG(this,\\"{color}\\",\\"#fff\\")"/>'
            s += f'<path d="M120 120 L188 213 A115 115 0 0 0 230 84 Z" fill="#fff" stroke="#555" stroke-width="2" class="svg-pt" data-on="0" onclick="ptSVG(this,\\"{color}\\",\\"#fff\\")"/>'
            s += f'<path d="M120 120 L230 84 A115 115 0 0 0 120 5 Z" fill="#fff" stroke="#555" stroke-width="2" class="svg-pt" data-on="0" onclick="ptSVG(this,\\"{color}\\",\\"#fff\\")"/>'
        s += '</svg>'
        return s

    for ex in ex_list:
        title, n, d, typ, col, tot = ex
        slide(f"""
        <div class="head-title">¡A Practicar!</div>
        <div style="display:flex; align-items:center; gap:30px; margin-top:30px;">
            <div style="display:flex; flex-direction:column; align-items:center;">
                <div style="font-size:28px; font-weight:800; margin-bottom:10px;">{title}</div>
                <div class="frac-box"><div>{n}</div><div class="line"></div><div>{d}</div></div>
            </div>
            {get_svg(typ, col)}
        </div>
        """)
        
    def draw_painted(typ, col, painted_cnt):
        s = f'<svg width="240" height="240" viewBox="0 0 240 240">'
        if typ == "grid2x3":
            for i in range(2):
                for j in range(3):
                    idx = i*3 + j
                    fill = col if idx < painted_cnt else "#fff"
                    s += f'<rect x="{j*80}" y="{i*120}" width="80" height="120" fill="{fill}" stroke="#555" stroke-width="3"/>'
        elif typ == "circle6":
            paths = [
                'M120 120 L120 5 A115 115 0 0 1 220 62 Z',
                'M120 120 L220 62 A115 115 0 0 1 220 178 Z',
                'M120 120 L220 178 A115 115 0 0 1 120 235 Z',
                'M120 120 L120 235 A115 115 0 0 1 20 178 Z',
                'M120 120 L20 178 A115 115 0 0 1 20 62 Z',
                'M120 120 L20 62 A115 115 0 0 1 120 5 Z'
            ]
            for i, p in enumerate(paths):
                fill = col if i < painted_cnt else "#fff"
                s += f'<path d="{p}" fill="{fill}" stroke="#555" stroke-width="2"/>'
        elif typ == "circle4":
            paths = [
                'M120 120 L120 5 A115 115 0 0 1 235 120 Z',
                'M120 120 L235 120 A115 115 0 0 1 120 235 Z',
                'M120 120 L120 235 A115 115 0 0 1 5 120 Z',
                'M120 120 L5 120 A115 115 0 0 1 120 5 Z'
            ]
            for i, p in enumerate(paths):
                fill = col if i < painted_cnt else "#fff"
                s += f'<path d="{p}" fill="{fill}" stroke="#555" stroke-width="2"/>'
        elif typ == "circle5":
            paths = [
                'M120 120 L120 5 A115 115 0 0 0 10 84 Z',
                'M120 120 L10 84 A115 115 0 0 0 52 213 Z',
                'M120 120 L52 213 A115 115 0 0 0 188 213 Z',
                'M120 120 L188 213 A115 115 0 0 0 230 84 Z',
                'M120 120 L230 84 A115 115 0 0 0 120 5 Z'
            ]
            for i, p in enumerate(paths):
                fill = col if i < painted_cnt else "#fff"
                s += f'<path d="{p}" fill="{fill}" stroke="#555" stroke-width="2"/>'
        s += '</svg>'
        return s

    id_list = [
        ("¿Qué fracción está pintada?", "grid2x3", "#6be3db", 3, ["3/6", "4/6", "6/3"]),
        ("Elige la fracción correcta", "circle4", "#f194b4", 1, ["1/4", "3/4", "1/3"]),
        ("¿Cuál es esta fracción?", "circle5", "#9de3bd", 2, ["2/5", "3/5", "5/2"]),
    ]

    for i, ex in enumerate(id_list):
        opts = "".join([f"<button class='btn stp' style='min-width:120px; font-size:24px; margin:5px;' onclick='this.style.background=\"#047857\"'>{o}</button>" for o in ex[4]])
        svg = draw_painted(ex[1], ex[2], ex[3])
        
        slide(f"""
        <div class="head-title">Adivina la Fracción</div>
        <p class="sub-text">{ex[0]}</p>
        <div style="display:flex; align-items:center; gap:40px;">
            {svg}
            <div style="display:flex; flex-direction:column; gap:15px;">
                <p class="stp" style="font-size:20px; font-weight: 800;">Opciones:</p>
                {opts}
            </div>
        </div>
        """)

    # More practice slides
    slide(f"""
        <div class="head-title">¡Reforzando Comparaciones!</div>
        <div class="pnl">
            <p style="font-size:24px; text-align:center;">Abre tu cuaderno y compara: <b>4/7</b> y <b>2/7</b></p>
            <div class="stp" style="margin-top:20px; font-weight:800; font-size:32px; text-align:center;">
                <span class="hl">4/7</span> es mayor que 2/7, ¡porque 4 partes es más que 2 partes del mismo tamaño (séptimos)!
            </div>
        </div>
    """)
    slide(f"""
        <div class="head-title">¡Reforzando Comparaciones!</div>
        <div class="pnl">
            <p style="font-size:24px; text-align:center;">Abre tu cuaderno y compara: <b>1/8</b> y <b>1/2</b></p>
            <div class="stp" style="margin-top:20px; font-weight:800; font-size:32px; text-align:center;">
                <span class="hl">1/2</span> es más grande, ¡porque si cortas en 2, los pedazos son ENORMES comparados a si cortas en 8!
            </div>
        </div>
    """)

    # 4 Verbals Problems with step-by-step resolution
    verbals = [
        ("La Pizza de Ana", "Ana pidió una pizza cortada en <b>4 partes</b>. Se comió <b>3</b>. ¿Qué fracción comió?", "Comió 3 partes de 4 totales = <span class='hl' style='font-size:36px'>3/4</span>"),
        ("El Curso", "En tu clase hay <b>10 alumnos</b>. Hoy faltaron <b>2</b>. ¿Qué fracción del curso faltó?", "Faltaron 2 de 10 totales = <span class='hl' style='font-size:36px'>2/10</span>"),
        ("Dilema de Galletas", "Tienes <b>1/4</b> de galleta y tu amigo tiene <b>1/3</b> de galleta (igual a la tuya). ¿Quién tiene más?", "1/3 es MÁS GRANDE que 1/4. Entonces, ¡tu amigo tiene más!"),
        ("Problema Final", "Comparamos <b>1/2</b> y <b>2/4</b>. Si uso el MCM (4), 1/2 amplificado es 2/4. ¿Cuál es mayor?", "¡Ups! 2/4 = 2/4. ¡Son EXACTAMENTE IGUALES! A esto le llamamos fracciones equivalentes (lo veremos en la próxima clase).")
    ]
    for tit, prob, ans in verbals:
        slide(f"""
        <div class="head-title">Calcula y Escribe: {tit}</div>
        <div class="pnl" style="min-height:200px; display:flex; flex-direction:column; justify-content:center;">
            <p style="font-size:26px; text-align:center;">{prob}</p>
        </div>
        <div class="stp" style="margin-top:20px; width:100%;">
            <div class="pnl" style="background:#e0f2fe; text-align:center; border: 3px dashed var(--base);">
                <p style="font-size:28px; font-weight:800;">Resolución:</p>
                <div class="stp" style="margin-top:10px; font-size:24px;">{ans}</div>
            </div>
        </div>
        """)

    # Resumen
    slide(f"""
        <div class="head-title">📋 Qué aprendimos hoy</div>
        <div style="display:flex; flex-direction:column; gap:20px; width:100%;">
            <div class="stp pnl" style="padding:15px; font-size:20px;"><b style="font-size:30px">🍕</b> <b>Partes Iguales:</b> Toda fracción requiere que la figura se corte en trozos exactos.</div>
            <div class="stp pnl" style="padding:15px; font-size:20px;"><b style="font-size:30px">🔢</b> <b>Num/Denom:</b> Arriba son las que tomas. Abajo el TOTAL en que se dividió.</div>
            <div class="stp pnl" style="padding:15px; font-size:20px;"><b style="font-size:30px">⚖️</b> <b>Comparar Mismo Denom:</b> Mayor numerador gana (más trozos).</div>
            <div class="stp pnl" style="padding:15px; font-size:20px;"><b style="font-size:30px">⚖️</b> <b>Comparar Mismo Numerador:</b> MENOR denominador gana (¡cortes más gordos!).</div>
            <div class="stp pnl" style="padding:15px; font-size:20px;"><b style="font-size:30px">✖️</b> <b>Distinto Todo:</b> Usamos el MCM y amplificamos.</div>
        </div>
    """)
    
    # Cierre
    slide(f"""
        <div class="head-title" style="background: #047857;">🏆 ¡Misión Cumplida!</div>
        <div style="font-size:32px; font-weight:800; text-align:center; margin-top:20px;">
            ¡Gran trabajo hoy!<br>La próxima clase descubriremos cómo hacer magia sumando fracciones juntas.
        </div>
        <div style="font-size:80px; margin-top:40px; animation: pulse 2s infinite;">🎇</div>
        <style>@keyframes pulse {{ 0%{{transform:scale(1);}} 50%{{transform:scale(1.2);}} 100%{{transform:scale(1);}} }}</style>
    """)

    # Output Gen
    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
    <title>Fracciones I - Interactivo</title>
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
    with open('/Users/brunonattino/Desktop/PAGINA TUTORIAS/SLIDES/fracciones HTMLS/09-fracciones-1.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Módulo 09 corregido con éxito! Slides:", len(slides))

if __name__ == '__main__':
    generate_html()
