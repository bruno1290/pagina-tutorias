def generate_html():
    from textwrap import dedent
    
    css = """
    @import url('https://fonts.googleapis.com/css2?family=Nunito:wght@600;800;900&display=swap');
    :root {--teal: #0c9c90; --bg: #f5f6f8; --tx: #333;}
    * {margin:0; padding:0; box-sizing:border-box;}
    body {font-family: 'Nunito', sans-serif; background: var(--bg); overflow: hidden; height: 100vh; width: 100vw; display: flex; flex-direction: column; align-items: center;}
    .dk {position: relative; width: 100%; height: 100%; max-width: 1000px; display: flex;}
    .sl {position: absolute; inset: 0; display: flex; flex-direction: column; align-items: center; justify-content: flex-start; padding: 40px; opacity: 0; transform: scale(.96); transition: opacity .4s, transform .4s; pointer-events: none; z-index: 1;}
    .sl.on {opacity: 1; transform: scale(1); pointer-events: auto; z-index: 10;}
    .sl.pv {opacity: 0; transform: translateX(-50px) scale(.95);}
    .sl.nx {opacity: 0; transform: translateX(50px) scale(.95);}
    
    .head-title {background: var(--teal); color: white; padding: 10px 40px; font-size: 32px; font-weight: 900; margin-bottom: 40px; display: inline-block;}
    .sub-text {font-size: 24px; font-weight: 600; margin-bottom: 40px; text-align: center;}
    .frac-box {border: 2px dashed var(--teal); border-radius: 20px; display: inline-flex; flex-direction: column; align-items: center; justify-content: center; padding: 15px 30px; font-size: 60px; font-weight: 900; line-height: 1; margin: 0 20px;}
    .frac-box div.line {height: 2px; width: 100%; background: #333; margin: 5px 0;}
    .read-as {font-size: 24px; font-weight: 800;}
    
    /* Navigation */
    .pb {position: fixed; top: 0; left: 0; height: 5px; background: var(--teal); transition: width .4s; z-index: 100;}
    .nv {position: fixed; bottom: 0; left: 0; right: 0; height: 60px; background: white; border-top: 1px solid #ddd; display: flex; align-items: center; justify-content: space-between; padding: 0 40px; z-index: 100;}
    .nb {background: #eee; border: none; padding: 10px 20px; border-radius: 8px; font-family: 'Nunito', sans-serif; font-size: 16px; font-weight: 800; cursor: pointer;}
    .nb:hover {background: #e0e0e0;}
    .nb:disabled {opacity: 0.3; cursor: not-allowed;}
    .sc {color: #888; font-size: 14px; font-weight: 800;}
    
    /* Interactions */
    .btn {background: var(--teal); color: white; border: none; padding: 12px 24px; border-radius: 12px; font-size: 18px; font-weight: 800; cursor: pointer; margin-top: 20px; transition: transform .2s;}
    .btn:hover {transform: translateY(-2px);}
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
    function go(d) { const n=c+d; if(n>=0 && n<T) { c=n; ui(); } }
    document.addEventListener('keydown', e => {
        if(e.key==='ArrowRight' || e.key===' ') go(1);
        if(e.key==='ArrowLeft') go(-1);
    });
    ui();
    
    function ptSVG(el, colon, coloff, idCounter) {
        let isOn = el.getAttribute('data-on') === '1';
        el.setAttribute('fill', isOn ? coloff : colon);
        el.setAttribute('data-on', isOn ? '0' : '1');
        if(idCounter) {
            let p = el.parentElement;
            let total = p.querySelectorAll('.svg-pt').length;
            let onCount = p.querySelectorAll('.svg-pt[data-on="1"]').length;
            document.getElementById(idCounter).textContent = onCount + '/' + total;
        }
    }
    """
    
    slides = []
    
    def add_slide(content):
        slides.append(f'<div class="sl">{content}</div>')

    # Slide 1: Welcome
    add_slide("""
    <div style="flex:1; display:flex; flex-direction:column; justify-content:center; align-items:center;">
        <h1 style="font-size: 60px; color: var(--teal); margin-bottom: 20px;">¡Fracciones I!</h1>
        <p class="sub-text">Vamos a aprender jugando y observando.</p>
        <p style="font-size:80px; margin-top:20px;">🎒</p>
    </div>
    """)
    
    # Slides 2-3: Intro / Bonding
    for msg in ["¿Cómo estuvo tu semana?", "Si pudieras ser un animal... ¿Cuál serías?"]:
        add_slide(f"""
        <div style="flex:1; display:flex; flex-direction:column; justify-content:center; align-items:center; text-align:center;">
            <div class="head-title">Antes de partir...</div>
            <p class="sub-text" style="font-size:36px;">{msg}</p>
        </div>
        """)
    
    # Slide 4: Recordemos lo que es una fraccion (Replica 1)
    add_slide("""
    <div class="head-title">Recordemos lo que es una fracción</div>
    <div style="display:flex; align-items: center; justify-content: center; gap: 40px; margin-top: 40px; width:100%;">
        <svg width="300" height="200" viewBox="0 0 300 200" style="border:2px solid #555;">
            <rect x="0" y="0" width="100" height="100" fill="#6be3db" stroke="#555" stroke-width="2"/>
            <rect x="100" y="0" width="100" height="100" fill="#6be3db" stroke="#555" stroke-width="2"/>
            <rect x="200" y="0" width="100" height="100" fill="#f5f6f8" stroke="#555" stroke-width="2"/>
            <rect x="0" y="100" width="100" height="100" fill="#6be3db" stroke="#555" stroke-width="2"/>
            <rect x="100" y="100" width="100" height="100" fill="#f5f6f8" stroke="#555" stroke-width="2"/>
            <rect x="200" y="100" width="100" height="100" fill="#f5f6f8" stroke="#555" stroke-width="2"/>
        </svg>
        <div class="frac-box" style="position:relative;">
            <div>3</div><div class="line"></div><div>6</div>
            <div style="position:absolute; top:25px; left:100%; width:180px; text-align:left; font-size:16px; margin-left:20px;">
                <span style="color:var(--teal)">➔</span> <b>NUMERADOR:</b> cantidad de partes pintadas
            </div>
            <div style="position:absolute; bottom:25px; left:100%; width:180px; text-align:left; font-size:16px; margin-left:20px;">
                <span style="color:var(--teal)">➔</span> <b>DENOMINADOR:</b> Cantidad de partes total
            </div>
        </div>
    </div>
    """)
    
    # Template para Replica de Fracciones y Formas
    def replica_slide(frac_num, frac_den, text, svgs):
        return f"""
        <div class="head-title">Fracciones</div>
        <p class="sub-text">La fracción puede representarse en distintas figuras ➔ siempre dividida en partes iguales.</p>
        <div style="display:flex; width:100%; justify-content:center; gap: 40px; margin-top:20px;">
            <div style="display:flex; align-items:center; gap:20px;">
                <div class="frac-box"><div>{frac_num}</div><div class="line"></div><div>{frac_den}</div></div>
                <div class="read-as">Se lee como: <br>{text}</div>
            </div>
            <div style="display:flex; flex-direction:column; align-items:center;">
                <div style="font-size:24px; font-weight:800; margin-bottom:20px;">Se representa:</div>
                <div style="display:flex; gap:30px; align-items:flex-end;">
                    {svgs}
                </div>
            </div>
        </div>
        """

    # Slide 5: Replica 1/2
    add_slide(replica_slide("1", "2", "un medio", """
        <svg width="120" height="120" viewBox="0 0 120 120">
            <rect x="0" y="0" width="60" height="120" fill="#f194b4" stroke="#555"/>
            <rect x="60" y="0" width="60" height="120" fill="#fff" stroke="#555"/>
        </svg>
        <svg width="140" height="120" viewBox="0 0 140 120">
            <polygon points="70,0 0,120 70,120" fill="#fff" stroke="#555"/>
            <polygon points="70,0 140,120 70,120" fill="#6be3db" stroke="#555"/>
        </svg>
        <svg width="160" height="60" viewBox="0 0 160 60">
            <polygon points="0,15 120,15 120,0 160,30 120,60 120,45 0,45" fill="#f5f6f8" stroke="#555"/>
            <polygon points="0,15 120,15 120,0 160,30 110,30 0,30" fill="#f3a033" stroke="#555" stroke-width="0"/>
            <polygon points="0,15 120,15 120,0 160,30 120,60 120,45 0,45" fill="none" stroke="#555"/>
        </svg>
    """))

    # Slide 6: Replica 1/3
    add_slide(replica_slide("1", "3", "un tercio", """
        <svg width="120" height="120" viewBox="0 0 120 120">
            <rect x="0" y="0" width="40" height="120" fill="#b993d6" stroke="#555"/>
            <rect x="40" y="0" width="40" height="120" fill="#fff" stroke="#555"/>
            <rect x="80" y="0" width="40" height="120" fill="#fff" stroke="#555"/>
        </svg>
        <svg width="120" height="120" viewBox="0 0 120 120">
            <circle cx="60" cy="60" r="58" fill="#fff" stroke="#555" stroke-width="2"/>
            <path d="M60 60 L60 2 A58 58 0 0 1 110 90 Z" fill="#fff" stroke="#555" stroke-width="2"/>
            <path d="M60 60 L110 90 A58 58 0 0 1 10 90 Z" fill="#a4cbfc" stroke="#555" stroke-width="2"/>
            <path d="M60 60 L10 90 A58 58 0 0 1 60 2 Z" fill="#fff" stroke="#555" stroke-width="2"/>
        </svg>
    """))

    # Slide 7: Replica 1/4
    add_slide(replica_slide("1", "4", "un cuarto", """
        <svg width="140" height="120" viewBox="0 0 140 120">
            <polygon points="70,0 0,120 140,120" fill="#fff" stroke="#555" stroke-width="2"/>
            <polygon points="70,0 35,60 105,60" fill="#fff" stroke="#555" stroke-width="1"/>
            <polygon points="35,60 0,120 70,120" fill="#fff" stroke="#555" stroke-width="1"/>
            <polygon points="105,60 70,120 140,120" fill="#f194b4" stroke="#555" stroke-width="1"/>
            <polygon points="35,60 105,60 70,120" fill="#fff" stroke="#555" stroke-width="1"/>
        </svg>
        <svg width="120" height="120" viewBox="0 0 120 120">
            <circle cx="60" cy="60" r="58" fill="#fff" stroke="#555" stroke-width="2"/>
            <path d="M60 60 L60 2 A58 58 0 0 1 118 60 Z" fill="#b993d6" stroke="#555" stroke-width="2"/>
            <path d="M60 60 L118 60 A58 58 0 0 1 60 118 Z" fill="#fff" stroke="#555" stroke-width="2"/>
            <path d="M60 60 L60 118 A58 58 0 0 1 2 60 Z" fill="#fff" stroke="#555" stroke-width="2"/>
            <path d="M60 60 L2 60 A58 58 0 0 1 60 2 Z" fill="#fff" stroke="#555" stroke-width="2"/>
        </svg>
        <svg width="180" height="60" viewBox="0 0 180 60">
            <rect x="0" y="0" width="90" height="30" fill="#fc4d51" stroke="#555"/>
            <rect x="90" y="0" width="90" height="30" fill="#fff" stroke="#555"/>
            <rect x="0" y="30" width="90" height="30" fill="#fff" stroke="#555"/>
            <rect x="90" y="30" width="90" height="30" fill="#fff" stroke="#555"/>
        </svg>
    """))

    # Slide 8: Replica 1/5 and 1/6
    add_slide("""
        <div class="head-title">Fracciones</div>
        <p class="sub-text">La fracción puede representarse en distintas figuras ➔ siempre dividida en partes iguales.</p>
        <div style="display:flex; width:100%; justify-content:center; gap: 40px; margin-top:20px;">
            <div style="display:flex; align-items:center; gap:20px;">
                <div class="frac-box"><div>1</div><div class="line"></div><div>5</div></div>
                <div class="read-as" style="width:120px;">Se lee como: <br>un quinto</div>
                <svg width="120" height="120" viewBox="0 0 120 120">
                    <circle cx="60" cy="60" r="58" fill="#fff" stroke="#555" stroke-width="2"/>
                    <path d="M60 60 L60 2 A58 58 0 0 0 5 42 Z" fill="#9de3bd" stroke="#555" stroke-width="2"/>
                    <path d="M60 60 L5 42 A58 58 0 0 0 26 107 Z" fill="#fff" stroke="#555" stroke-width="2"/>
                    <path d="M60 60 L26 107 A58 58 0 0 0 94 107 Z" fill="#fff" stroke="#555" stroke-width="2"/>
                    <path d="M60 60 L94 107 A58 58 0 0 0 115 42 Z" fill="#fff" stroke="#555" stroke-width="2"/>
                    <path d="M60 60 L115 42 A58 58 0 0 0 60 2 Z" fill="#fff" stroke="#555" stroke-width="2"/>
                </svg>
            </div>
            <div style="width:2px; background:#ddd;"></div>
            <div style="display:flex; align-items:center; gap:20px;">
                <div class="frac-box"><div>1</div><div class="line"></div><div>6</div></div>
                <div class="read-as" style="width:120px;">Se lee como: <br>un sexto</div>
                <svg width="120" height="120" viewBox="0 0 120 120">
                    <circle cx="60" cy="60" r="58" fill="#fff" stroke="#555" stroke-width="2"/>
                    <path d="M60 60 L60 2 A58 58 0 0 1 110 31 Z" fill="#fff" stroke="#555" stroke-width="2"/>
                    <path d="M60 60 L110 31 A58 58 0 0 1 110 89 Z" fill="#fff" stroke="#555" stroke-width="2"/>
                    <path d="M60 60 L110 89 A58 58 0 0 1 60 118 Z" fill="#fff" stroke="#555" stroke-width="2"/>
                    <path d="M60 60 L60 118 A58 58 0 0 1 10 89 Z" fill="#fbba55" stroke="#555" stroke-width="2"/>
                    <path d="M60 60 L10 89 A58 58 0 0 1 10 31 Z" fill="#fff" stroke="#555" stroke-width="2"/>
                    <path d="M60 60 L10 31 A58 58 0 0 1 60 2 Z" fill="#fff" stroke="#555" stroke-width="2"/>
                </svg>
            </div>
        </div>
    """)

    # Interactive Exercises (Lots of them to reach 28 slides)
    # Slides 9-20: Interactively paint different SVGs
    ex_list = [
        ("¡Pinta 2/3 en el rectángulo!", "2", "3", "rect", "#b993d6", 3),
        ("¡Pinta 3/4 en el círculo!", "3", "4", "circle4", "#f194b4", 4),
        ("¡Pinta 2/5 en el círculo!", "2", "5", "circle5", "#9de3bd", 5),
        ("¡Pinta 4/6 en el cuadro!", "4", "6", "grid2x3", "#6be3db", 6),
        ("¡Pinta 1/2 en las flechas!", "1", "2", "arrow", "#f3a033", 2),
        ("¡Pinta 3/8 en esta grilla!", "3", "8", "grid2x4", "#fc4d51", 8),
        ("¡Pinta 5/6 en el círculo!", "5", "6", "circle6", "#fbba55", 6)
    ]
    
    # SVG Generators for painting
    def get_svg(typ, color):
        s = f'<svg width="240" height="240" viewBox="0 0 240 240">'
        if typ == "rect":
            for i in range(3):
                s += f'<rect x="{i*80}" y="20" width="80" height="200" fill="#fff" stroke="#555" stroke-width="3" class="svg-pt" data-on="0" onclick="ptSVG(this,\\"{color}\\",\\"#fff\\",\\"cnt{len(slides)}\\")"/>'
        elif typ == "grid2x3":
            for i in range(2):
                for j in range(3):
                    s += f'<rect x="{j*80}" y="{i*120}" width="80" height="120" fill="#fff" stroke="#555" stroke-width="3" class="svg-pt" data-on="0" onclick="ptSVG(this,\\"{color}\\",\\"#fff\\",\\"cnt{len(slides)}\\")"/>'
        elif typ == "grid2x4":
            for i in range(2):
                for j in range(4):
                    s += f'<rect x="{j*60}" y="{i*120}" width="60" height="120" fill="#fff" stroke="#555" stroke-width="3" class="svg-pt" data-on="0" onclick="ptSVG(this,\\"{color}\\",\\"#fff\\",\\"cnt{len(slides)}\\")"/>'
        elif typ == "circle4":
            s += f'<circle cx="120" cy="120" r="115" fill="none" stroke="#555" stroke-width="3"/>'
            s += f'<path d="M120 120 L120 5 A115 115 0 0 1 235 120 Z" fill="#fff" stroke="#555" stroke-width="2" class="svg-pt" data-on="0" onclick="ptSVG(this,\\"{color}\\",\\"#fff\\",\\"cnt{len(slides)}\\")"/>'
            s += f'<path d="M120 120 L235 120 A115 115 0 0 1 120 235 Z" fill="#fff" stroke="#555" stroke-width="2" class="svg-pt" data-on="0" onclick="ptSVG(this,\\"{color}\\",\\"#fff\\",\\"cnt{len(slides)}\\")"/>'
            s += f'<path d="M120 120 L120 235 A115 115 0 0 1 5 120 Z" fill="#fff" stroke="#555" stroke-width="2" class="svg-pt" data-on="0" onclick="ptSVG(this,\\"{color}\\",\\"#fff\\",\\"cnt{len(slides)}\\")"/>'
            s += f'<path d="M120 120 L5 120 A115 115 0 0 1 120 5 Z" fill="#fff" stroke="#555" stroke-width="2" class="svg-pt" data-on="0" onclick="ptSVG(this,\\"{color}\\",\\"#fff\\",\\"cnt{len(slides)}\\")"/>'
        elif typ == "circle5":
            s += f'<circle cx="120" cy="120" r="115" fill="none" stroke="#555" stroke-width="3"/>'
            s += f'<path d="M120 120 L120 5 A115 115 0 0 0 10 84 Z" fill="#fff" stroke="#555" stroke-width="2" class="svg-pt" data-on="0" onclick="ptSVG(this,\\"{color}\\",\\"#fff\\",\\"cnt{len(slides)}\\")"/>'
            s += f'<path d="M120 120 L10 84 A115 115 0 0 0 52 213 Z" fill="#fff" stroke="#555" stroke-width="2" class="svg-pt" data-on="0" onclick="ptSVG(this,\\"{color}\\",\\"#fff\\",\\"cnt{len(slides)}\\")"/>'
            s += f'<path d="M120 120 L52 213 A115 115 0 0 0 188 213 Z" fill="#fff" stroke="#555" stroke-width="2" class="svg-pt" data-on="0" onclick="ptSVG(this,\\"{color}\\",\\"#fff\\",\\"cnt{len(slides)}\\")"/>'
            s += f'<path d="M120 120 L188 213 A115 115 0 0 0 230 84 Z" fill="#fff" stroke="#555" stroke-width="2" class="svg-pt" data-on="0" onclick="ptSVG(this,\\"{color}\\",\\"#fff\\",\\"cnt{len(slides)}\\")"/>'
            s += f'<path d="M120 120 L230 84 A115 115 0 0 0 120 5 Z" fill="#fff" stroke="#555" stroke-width="2" class="svg-pt" data-on="0" onclick="ptSVG(this,\\"{color}\\",\\"#fff\\",\\"cnt{len(slides)}\\")"/>'
        elif typ == "circle6":
            s += f'<circle cx="120" cy="120" r="115" fill="none" stroke="#555" stroke-width="3"/>'
            s += f'<path d="M120 120 L120 5 A115 115 0 0 1 220 62 Z" fill="#fff" stroke="#555" stroke-width="2" class="svg-pt" data-on="0" onclick="ptSVG(this,\\"{color}\\",\\"#fff\\",\\"cnt{len(slides)}\\")"/>'
            s += f'<path d="M120 120 L220 62 A115 115 0 0 1 220 178 Z" fill="#fff" stroke="#555" stroke-width="2" class="svg-pt" data-on="0" onclick="ptSVG(this,\\"{color}\\",\\"#fff\\",\\"cnt{len(slides)}\\")"/>'
            s += f'<path d="M120 120 L220 178 A115 115 0 0 1 120 235 Z" fill="#fff" stroke="#555" stroke-width="2" class="svg-pt" data-on="0" onclick="ptSVG(this,\\"{color}\\",\\"#fff\\",\\"cnt{len(slides)}\\")"/>'
            s += f'<path d="M120 120 L120 235 A115 115 0 0 1 20 178 Z" fill="#fff" stroke="#555" stroke-width="2" class="svg-pt" data-on="0" onclick="ptSVG(this,\\"{color}\\",\\"#fff\\",\\"cnt{len(slides)}\\")"/>'
            s += f'<path d="M120 120 L20 178 A115 115 0 0 1 20 62 Z" fill="#fff" stroke="#555" stroke-width="2" class="svg-pt" data-on="0" onclick="ptSVG(this,\\"{color}\\",\\"#fff\\",\\"cnt{len(slides)}\\")"/>'
            s += f'<path d="M120 120 L20 62 A115 115 0 0 1 120 5 Z" fill="#fff" stroke="#555" stroke-width="2" class="svg-pt" data-on="0" onclick="ptSVG(this,\\"{color}\\",\\"#fff\\",\\"cnt{len(slides)}\\")"/>'
        elif typ == "arrow":
            s += f'<polygon points="0,60 160,60 160,0 240,120 160,240 160,180 0,180" fill="#fff" stroke="#555" stroke-width="3"/>'
            s += f'<polygon points="0,60 160,60 160,0 240,120 120,120 0,120" fill="#fff" stroke="#555" stroke-width="2" class="svg-pt" data-on="0" onclick="ptSVG(this,\\"{color}\\",\\"#fff\\",\\"cnt{len(slides)}\\")"/>'
            s += f'<polygon points="0,120 120,120 240,120 160,240 160,180 0,180" fill="#fff" stroke="#555" stroke-width="2" class="svg-pt" data-on="0" onclick="ptSVG(this,\\"{color}\\",\\"#fff\\",\\"cnt{len(slides)}\\")"/>'
        s += '</svg>'
        return s

    for ex in ex_list:
        title, n, d, typ, col, tot = ex
        add_slide(f"""
        <div class="head-title">¡A Practicar!</div>
        <div style="display:flex; align-items:center; gap:30px; margin-top:30px;">
            <div style="display:flex; flex-direction:column; align-items:center;">
                <div style="font-size:28px; font-weight:800; margin-bottom:10px;">{title}</div>
                <div class="frac-box"><div>{n}</div><div class="line"></div><div>{d}</div></div>
                <div id="cnt{len(slides)}" style="margin-top:20px; font-size:24px; font-weight:800; color:var(--teal);">0/{tot}</div>
            </div>
            {get_svg(typ, col)}
        </div>
        """)

    # Identification Interactivity (Slides 16-22)
    id_list = [
        ("¿Qué fracción está pintada?", "grid2x3", "#6be3db", 3, ["3/6", "4/6", "6/3", "1/2"]),
        ("Elige la fracción correcta", "circle4", "#f194b4", 1, ["1/4", "3/4", "4/1", "1/3"]),
        ("Selecciona la fracción", "circle6", "#fbba55", 5, ["5/6", "1/6", "6/5", "6/6"]),
        ("¿Cuál es esta fracción?", "circle5", "#9de3bd", 2, ["2/5", "3/5", "5/2", "1/5"]),
        ("Mira el dibujo, ¿qué es?", "circle4", "#b993d6", 2, ["2/4", "1/4", "4/2", "3/4"]),
        ("Cuenta las partes y elige", "grid2x4", "#fc4d51", 4, ["4/8", "1/8", "8/4", "3/8"]),
    ]

    def draw_painted(typ, col, painted_cnt):
        s = f'<svg width="200" height="200" viewBox="0 0 240 240">'
        if typ == "grid2x3":
            for i in range(2):
                for j in range(3):
                    idx = i*3 + j
                    fill = col if idx < painted_cnt else "#fff"
                    s += f'<rect x="{j*80}" y="{i*120}" width="80" height="120" fill="{fill}" stroke="#555" stroke-width="3"/>'
        elif typ == "grid2x4":
            for i in range(2):
                for j in range(4):
                    idx = i*4 + j
                    fill = col if idx < painted_cnt else "#fff"
                    s += f'<rect x="{j*60}" y="{i*120}" width="60" height="120" fill="{fill}" stroke="#555" stroke-width="3"/>'
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

    for i, ex in enumerate(id_list):
        opts = "".join([f"<button class='btn' style='width:120px; font-size:24px;' onclick='this.style.background=\"#333\"'>{o}</button>" for o in ex[4]])
        add_slide(f"""
        <div class="head-title">Adivina la Fracción</div>
        <p class="sub-text">{ex[0]}</p>
        <div style="display:flex; align-items:center; gap:40px;">
            {draw_painted(ex[1], ex[2], ex[3])}
            <div style="display:grid; grid-template-columns: 1fr 1fr; gap:15px;">
                {opts}
            </div>
        </div>
        """)

    # Remaining slides to hit ~27 slides
    for title, problem in [
        ("Mismo Denominador", "Pensemos: ¿Qué pasa si comparamos 3/5 y 4/5? <br> Ambas partes están divididas igual (en 5).<br>El que tenga más partes puntadas gana -> 4/5 es mayor."),
        ("Mismo Numerador", "Pensemos: ¿Qué pasa si comparamos 1/3 y 1/4? <br> Una pizza dividida en 3 tiene trozos más grandes que una dividida en 4. <br>Por tanto, 1/3 es mayor."),
        ("Tipos de Fracciones", "Propia: El numerador es más pequeño que el denominador (Ej: 2/5).<br>Impropia: El numerador es más grande (Ej: 6/5).<br>Mixta: Un entero y una fracción (Ej: 1 1/2)"),
        ("Problema", "Si Juan comió 3/8 de la torta, y el pastel era de 8 trozos. ¿Cuántos comió? <br><br><b>¡Comió 3 trozos!</b>"),
        ("Resumen", "Excelente. Ahora sabes identificar, pintar y comprender bien las fracciones, y verlas representadas gráficamente de múltiples maneras.")
    ]:
        add_slide(f"""
        <div class="head-title">{title}</div>
        <div class="frac-box" style="padding:40px; font-size:28px; font-weight:600; text-align:center; max-width:800px; border: 4px dashed var(--teal);">
            {problem}
        </div>
        """)
    
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
    print("Módulo 09 generado con éxito! Slides:", len(slides))

if __name__ == '__main__':
    generate_html()
