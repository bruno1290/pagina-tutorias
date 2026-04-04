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
    .pnl-border {background: #fff; padding: 30px; border-radius: 20px; border: 4px solid var(--base); width: 100%; margin-bottom: 20px;}
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
    function chkAns(btn, correct) {
        let p = btn.parentElement;
        let msg = p.nextElementSibling;
        for (let b of p.children) b.style.transform = 'scale(1)';
        if (correct) {
            btn.style.background = '#047857';
            btn.style.transform = 'scale(1.1)';
            msg.innerHTML = '¡Excelente! ✅ ¡Lo lograste!';
            msg.style.color = '#047857';
        } else {
            btn.style.background = '#b91c1c';
            let frases = ["¡Vuelve a intentarlo! 💪", "Verifica bien 🧐", "Con calma, tú puedes 🚀"];
            msg.innerHTML = frases[Math.floor(Math.random()*frases.length)];
            msg.style.color = '#b91c1c';
        }
    }
    """
    
    slides = []
    def slide(html): slides.append(f'<div class="sl">{html}</div>')

    # Intro
    slide(f"""
        <div style="flex:1; display:flex; flex-direction:column; justify-content:center; align-items:center;">
            <h1 style="font-size: 70px; color: var(--base); margin-bottom: 20px;">Módulo 9: Qué es una fracción</h1>
            <p class="sub-text">Paso a paso para dominar las figuras divididas.</p>
            <p style="font-size:90px; margin-top:30px;">🍕</p>
        </div>
    """)
    
    # ¿Qué es una fracción?
    slide(f"""
        <div class="head-title">Qué es una fracción</div>
        <div class="pnl-border" style="display:flex; flex-direction:column; align-items:center;">
            <p class="sub-text" style="margin-bottom:10px;">Es una forma de representar partes de algo entero.</p>
            <div style="display:flex; align-items: center; justify-content: center; gap: 40px; margin-top: 20px; width:100%;">
                <svg width="300" height="200" viewBox="0 0 300 200" style="border:3px solid var(--base); background: #fff; border-radius:15px;">
                    <rect x="0" y="0" width="100" height="100" fill="#9DDEFF" stroke="var(--base)" stroke-width="3"/>
                    <rect x="100" y="0" width="100" height="100" fill="#9DDEFF" stroke="var(--base)" stroke-width="3"/>
                    <rect x="200" y="0" width="100" height="100" fill="#fff" stroke="var(--base)" stroke-width="3"/>
                    <rect x="0" y="100" width="100" height="100" fill="#9DDEFF" stroke="var(--base)" stroke-width="3"/>
                    <rect x="100" y="100" width="100" height="100" fill="#fff" stroke="var(--base)" stroke-width="3"/>
                    <rect x="200" y="100" width="100" height="100" fill="#fff" stroke="var(--base)" stroke-width="3"/>
                </svg>
                <div class="frac-box" style="position:relative;">
                    <div>3</div><div class="line"></div><div>6</div>
                    <div class="stp" style="position:absolute; top:25px; left:100%; width:220px; font-size:18px; margin-left:30px; border-left: 4px solid #9DDEFF; padding-left: 15px;">
                        <b style="color:#0288D1; font-weight:900;">NUMERADOR:</b><br>Cantidad de partes pintadas o tomadas.
                    </div>
                    <div class="stp" style="position:absolute; bottom:15px; left:100%; width:220px; font-size:18px; margin-left:30px; border-left: 4px solid var(--base); padding-left: 15px;">
                        <b class="hl">DENOMINADOR:</b><br>Cantidad de partes totales en las que se dividió.
                    </div>
                </div>
            </div>
        </div>
    """)

    # Partes iguales
    slide(f"""
        <div class="head-title">¡Deben ser partes IGUALES!</div>
        <p class="sub-text">Para que sea una fracción real, cada pedacito debe ser <b>exactamente del mismo tamaño</b>.</p>
        <div style="display:flex; width:100%; justify-content:center; gap: 40px; margin-top:20px;">
            <div class="pnl stp" style="display:flex; flex-direction:column; align-items:center; width: 45%;">
                <div style="font-size:24px; font-weight:800; margin-bottom: 20px;">¿Esto es 1/4?</div>
                <svg width="150" height="150" viewBox="0 0 150 150">
                    <circle cx="75" cy="75" r="70" fill="#fff" stroke="var(--base)" stroke-width="3"/>
                    <path d="M75 75 L75 5 A70 70 0 0 1 145 75 Z" fill="#FF9D9D" stroke="var(--base)" stroke-width="3"/>
                    <path d="M75 75 L145 75 A70 70 0 0 1 75 145 Z" fill="#fff" stroke="var(--base)" stroke-width="3"/>
                    <path d="M75 75 L75 145 A70 70 0 0 1 5 75 Z" fill="#fff" stroke="var(--base)" stroke-width="3"/>
                    <path d="M75 75 L5 75 A70 70 0 0 1 75 5 Z" fill="#fff" stroke="var(--base)" stroke-width="3"/>
                </svg>
                <div class="stp" style="margin-top:20px; font-size:20px; font-weight:800; color:#047857;">✅ ¡Sí! Están todos iguales.</div>
            </div>
            
            <div class="pnl stp" style="display:flex; flex-direction:column; align-items:center; width: 45%;">
                <div style="font-size:24px; font-weight:800; margin-bottom: 20px;">¿Y esto es 1/4?</div>
                <svg width="150" height="150" viewBox="0 0 150 150">
                    <rect x="5" y="5" width="140" height="140" fill="#fff" stroke="var(--base)" stroke-width="3"/>
                    <rect x="5" y="5" width="40" height="140" fill="#FFE082" stroke="var(--base)" stroke-width="3"/>
                    <line x1="100" y1="5" x2="100" y2="145" stroke="var(--base)" stroke-width="3"/>
                    <line x1="120" y1="5" x2="120" y2="145" stroke="var(--base)" stroke-width="3"/>
                </svg>
                <div class="stp" style="margin-top:20px; font-size:20px; font-weight:800; color:#b91c1c;">❌ ¡No! Tienen distinto tamaño.</div>
            </div>
        </div>
    """)

    slide(f"""
        <div class="head-title">Más Práctica: ¿Son partes iguales?</div>
        <p class="sub-text">Analicemos con cuidado las siguientes imágenes.</p>
        <div style="display:flex; width:100%; justify-content:center; gap: 40px; margin-top:20px;">
            <div class="pnl stp" style="display:flex; flex-direction:column; align-items:center; width: 45%;">
                <div style="font-size:24px; font-weight:800; margin-bottom: 20px;">¿Esto es 1/3?</div>
                <svg width="150" height="150" viewBox="0 0 150 150">
                    <polygon points="75,5 5,145 145,145" fill="#fff" stroke="var(--base)" stroke-width="3"/>
                    <polygon points="75,5 5,145 75,145" fill="#E1BEE7" stroke="var(--base)" stroke-width="3"/>
                    <line x1="40" y1="75" x2="110" y2="75" stroke="var(--base)" stroke-width="3"/>
                </svg>
                <div class="stp" style="margin-top:20px; font-size:20px; font-weight:800; color:#b91c1c;">❌ ¡No! Algunas piezas son diferentes.</div>
            </div>
            
            <div class="pnl stp" style="display:flex; flex-direction:column; align-items:center; width: 45%;">
                <div style="font-size:24px; font-weight:800; margin-bottom: 20px;">¿Y esto es 1/3?</div>
                <svg width="150" height="150" viewBox="0 0 150 150">
                    <rect x="5" y="5" width="140" height="140" fill="#fff" stroke="var(--base)" stroke-width="3"/>
                    <rect x="5" y="5" width="46" height="140" fill="#9DE3BD" stroke="var(--base)" stroke-width="3"/>
                    <line x1="51" y1="5" x2="51" y2="145" stroke="var(--base)" stroke-width="3"/>
                    <line x1="98" y1="5" x2="98" y2="145" stroke="var(--base)" stroke-width="3"/>
                </svg>
                <div class="stp" style="margin-top:20px; font-size:20px; font-weight:800; color:#047857;">✅ ¡Sí! Tienen la misma forma y tamaño.</div>
            </div>
        </div>
    """)

    # Abre tu cuaderno functions
    def cuaderno_slide(typ, count, n, d, extra_w=240, extra_h=80):
        # build custom SVG
        s = f'<svg width="{extra_w}" height="{extra_h}" viewBox="0 0 {extra_w} {extra_h}" style="border: 2px solid var(--base);">'
        if typ == "hbar":
            w = extra_w / d
            for i in range(d):
                fill = "#FF9D9D" if i < count else "#fff"
                s += f'<rect x="{i*w}" y="0" width="{w}" height="{extra_h}" fill="{fill}" stroke="var(--base)" stroke-width="2"/>'
        elif typ == "vbar":
            h = extra_h / d
            for i in range(d):
                fill = "#9DDEFF" if i < count else "#fff"
                s += f'<rect x="0" y="{i*h}" width="{extra_w}" height="{h}" fill="{fill}" stroke="var(--base)" stroke-width="2"/>'
        elif typ == "circle":
            s = f'<svg width="240" height="240" viewBox="0 0 240 240">'
            s += f'<circle cx="120" cy="120" r="115" fill="none" stroke="var(--base)" stroke-width="3"/>'
            if d == 4:
                paths = ['M120 120 L120 5 A115 115 0 0 1 235 120 Z','M120 120 L235 120 A115 115 0 0 1 120 235 Z','M120 120 L120 235 A115 115 0 0 1 5 120 Z','M120 120 L5 120 A115 115 0 0 1 120 5 Z']
                for i, p in enumerate(paths): s += f'<path d="{p}" fill="{"#9DE3BD" if i<count else "#fff"}" stroke="var(--base)" stroke-width="3"/>'
            if d == 8:
                paths = [
                    'M120 120 L120 5 A115 115 0 0 1 201 39 Z',
                    'M120 120 L201 39 A115 115 0 0 1 235 120 Z',
                    'M120 120 L235 120 A115 115 0 0 1 201 201 Z',
                    'M120 120 L201 201 A115 115 0 0 1 120 235 Z',
                    'M120 120 L120 235 A115 115 0 0 1 39 201 Z',
                    'M120 120 L39 201 A115 115 0 0 1 5 120 Z',
                    'M120 120 L5 120 A115 115 0 0 1 39 39 Z',
                    'M120 120 L39 39 A115 115 0 0 1 120 5 Z'
                ]
                for i, p in enumerate(paths): s += f'<path d="{p}" fill="{"#FFE082" if i<count else "#fff"}" stroke="var(--base)" stroke-width="2"/>'
        elif typ == "grid_2x2":
            s = f'<svg width="240" height="240" viewBox="0 0 240 240">'
            for i in range(2):
                for j in range(2):
                    idx = i*2 + j
                    s += f'<rect x="{j*120}" y="{i*120}" width="120" height="120" fill="{"#E1BEE7" if idx<count else "#fff"}" stroke="var(--base)" stroke-width="3"/>'
        elif typ == "grid_2x5":
            s = f'<svg width="300" height="120" viewBox="0 0 300 120">'
            for i in range(2):
                for j in range(5):
                    idx = i*5 + j
                    s += f'<rect x="{j*60}" y="{i*60}" width="60" height="60" fill="{"#FFB74D" if idx<count else "#fff"}" stroke="var(--base)" stroke-width="2"/>'
        s += '</svg>'
        
        return f"""
        <div class="head-title">Abre Tu Cuaderno ✍️</div>
        <p class="sub-text">Anota: ¿Qué fracción representa el dibujo?</p>
        <div style="display:flex; flex-direction:column; align-items:center; width:100%; gap: 30px; margin-top:20px;">
            <div class="pnl" style="display:flex; justify-content:center; align-items:center; width:auto; border-color:var(--base);">
                {s}
            </div>
            <div class="stp">
                <div class="frac-box" style="padding:10px 20px; font-size:50px; margin:0;"><div>{n}</div><div class="line"></div><div>{d}</div></div>
            </div>
        </div>
        """

    # Abre Tu Cuaderno (5 slides)
    slide(cuaderno_slide("hbar", 3, 3, 5, 300, 80))
    slide(cuaderno_slide("circle", 1, 1, 4))
    slide(cuaderno_slide("vbar", 2, 2, 6, 120, 240))
    slide(cuaderno_slide("circle", 5, 5, 8))
    slide(cuaderno_slide("grid_2x5", 7, 7, 10))

    # Diferentes Formas / Representaciones
    def rep_slide(n, d, text, svgs):
        return f"""
        <div class="head-title">Múltiples Formas 🎨</div>
        <p class="sub-text">La fracción <b>{n}/{d}</b> puede dividirse en distintas figuras pero mantiene su proporción.</p>
        <div style="display:flex; width:100%; justify-content:center; gap: 60px; margin-top:40px;">
            <div class="pnl" style="display:flex; align-items:center; gap:20px; border-color:var(--base); width:auto;">
                <div class="frac-box"><div>{n}</div><div class="line"></div><div>{d}</div></div>
                <div class="read-as" style="font-size:28px;">{text}</div>
            </div>
            <div class="stp" style="display:flex; flex-direction:column; align-items:center;">
                <div style="font-size:24px; font-weight:800; margin-bottom:30px;">Representaciones:</div>
                <div style="display:flex; flex-direction:column; gap:20px; align-items:center;">
                    {svgs}
                </div>
            </div>
        </div>
        """

    slide(rep_slide("1", "2", "Un<br>medio", """
        <div style="display:flex; gap:20px; align-items:flex-end;">
            <svg width="100" height="100" viewBox="0 0 100 100"><rect x="0" y="0" width="50" height="100" fill="#FF9D9D" stroke="var(--base)" stroke-width="3"/><rect x="50" y="0" width="50" height="100" fill="#fff" stroke="var(--base)" stroke-width="3"/></svg>
            <svg width="120" height="100" viewBox="0 0 140 120"><polygon points="70,0 0,120 70,120" fill="#fff" stroke="var(--base)" stroke-width="3"/><polygon points="70,0 140,120 70,120" fill="#9DDEFF" stroke="var(--base)" stroke-width="3"/></svg>
            <svg width="140" height="60" viewBox="0 0 160 60"><polygon points="0,15 120,15 120,0 160,30 120,60 120,45 0,45" fill="#f5f6f8" stroke="var(--base)" stroke-width="3"/><polygon points="0,15 120,15 120,0 160,30 110,30 0,30" fill="#FFE082" stroke-width="0"/><polygon points="0,15 120,15 120,0 160,30 120,60 120,45 0,45" fill="none" stroke="var(--base)" stroke-width="3"/></svg>
        </div>
    """))

    slide(rep_slide("1", "4", "Un<br>cuarto", """
        <div style="display:flex; gap:20px; align-items:flex-end;">
            <svg width="100" height="100" viewBox="0 0 120 120"><circle cx="60" cy="60" r="58" fill="#fff" stroke="var(--base)" stroke-width="3"/><path d="M60 60 L60 2 A58 58 0 0 1 118 60 Z" fill="#E1BEE7" stroke="var(--base)" stroke-width="3"/><path d="M60 60 L118 60 A58 58 0 0 1 60 118 Z" fill="#fff" stroke="var(--base)" stroke-width="3"/><path d="M60 60 L60 118 A58 58 0 0 1 2 60 Z" fill="#fff" stroke="var(--base)" stroke-width="3"/><path d="M60 60 L2 60 A58 58 0 0 1 60 2 Z" fill="#fff" stroke="var(--base)" stroke-width="3"/></svg>
            <svg width="180" height="40" viewBox="0 0 180 40"><rect x="0" y="0" width="45" height="40" fill="#fff" stroke="var(--base)" stroke-width="2"/><rect x="45" y="0" width="45" height="40" fill="#9DE3BD" stroke="var(--base)" stroke-width="2"/><rect x="90" y="0" width="45" height="40" fill="#fff" stroke="var(--base)" stroke-width="2"/><rect x="135" y="0" width="45" height="40" fill="#fff" stroke="var(--base)" stroke-width="2"/></svg>
        </div>
    """))

    # SVG Gen Helpers
    def get_blank_svg(typ, color):
        s = f'<svg width="240" height="240" viewBox="0 0 240 240">'
        if typ == "rect":
            for i in range(3): s += f'<rect x="{i*80}" y="20" width="80" height="200" fill="#fff" stroke="var(--base)" stroke-width="3" class="svg-pt" data-on="0" onclick="ptSVG(this,\\"{color}\\",\\"#fff\\")"/>'
        elif typ == "rect_5":
            for i in range(5): s += f'<rect x="{i*48}" y="30" width="48" height="180" fill="#fff" stroke="var(--base)" stroke-width="3" class="svg-pt" data-on="0" onclick="ptSVG(this,\\"{color}\\",\\"#fff\\")"/>'
        elif typ == "grid2x3":
            for i in range(2):
                for j in range(3): s += f'<rect x="{j*80}" y="{i*120}" width="80" height="120" fill="#fff" stroke="var(--base)" stroke-width="3" class="svg-pt" data-on="0" onclick="ptSVG(this,\\"{color}\\",\\"#fff\\")"/>'
        elif typ == "circle4":
            s += f'<circle cx="120" cy="120" r="115" fill="none" stroke="var(--base)" stroke-width="3"/>'
            paths = ['M120 120 L120 5 A115 115 0 0 1 235 120 Z','M120 120 L235 120 A115 115 0 0 1 120 235 Z','M120 120 L120 235 A115 115 0 0 1 5 120 Z','M120 120 L5 120 A115 115 0 0 1 120 5 Z']
            for p in paths: s += f'<path d="{p}" fill="#fff" stroke="var(--base)" stroke-width="2" class="svg-pt" data-on="0" onclick="ptSVG(this,\\"{color}\\",\\"#fff\\")"/>'
        elif typ == "circle5":
            s += f'<circle cx="120" cy="120" r="115" fill="none" stroke="var(--base)" stroke-width="3"/>'
            paths = ['M120 120 L120 5 A115 115 0 0 0 10 84 Z','M120 120 L10 84 A115 115 0 0 0 52 213 Z','M120 120 L52 213 A115 115 0 0 0 188 213 Z','M120 120 L188 213 A115 115 0 0 0 230 84 Z','M120 120 L230 84 A115 115 0 0 0 120 5 Z']
            for p in paths: s += f'<path d="{p}" fill="#fff" stroke="var(--base)" stroke-width="2" class="svg-pt" data-on="0" onclick="ptSVG(this,\\"{color}\\",\\"#fff\\")"/>'
        elif typ == "circle6":
            s += f'<circle cx="120" cy="120" r="115" fill="none" stroke="var(--base)" stroke-width="3"/>'
            paths = ['M120 120 L120 5 A115 115 0 0 1 220 62 Z','M120 120 L220 62 A115 115 0 0 1 220 178 Z','M120 120 L220 178 A115 115 0 0 1 120 235 Z','M120 120 L120 235 A115 115 0 0 1 20 178 Z','M120 120 L20 178 A115 115 0 0 1 20 62 Z','M120 120 L20 62 A115 115 0 0 1 120 5 Z']
            for p in paths: s += f'<path d="{p}" fill="#fff" stroke="var(--base)" stroke-width="2" class="svg-pt" data-on="0" onclick="ptSVG(this,\\"{color}\\",\\"#fff\\")"/>'
        return s + '</svg>'

    def draw_painted(typ, col, painted_cnt):
        s = f'<svg width="240" height="240" viewBox="0 0 240 240">'
        if typ == "rect":
            for i in range(3): s += f'<rect x="{i*80}" y="20" width="80" height="200" fill="{col if i<painted_cnt else "#fff"}" stroke="var(--base)" stroke-width="3"/>'
        elif typ == "rect_5":
            for i in range(5): s += f'<rect x="{i*48}" y="30" width="48" height="180" fill="{col if i<painted_cnt else "#fff"}" stroke="var(--base)" stroke-width="3"/>'
        elif typ == "grid2x3":
            for i in range(2):
                for j in range(3): s += f'<rect x="{j*80}" y="{i*120}" width="80" height="120" fill="{col if (i*3+j)<painted_cnt else "#fff"}" stroke="var(--base)" stroke-width="3"/>'
        elif typ == "circle6":
            paths = ['M120 120 L120 5 A115 115 0 0 1 220 62 Z','M120 120 L220 62 A115 115 0 0 1 220 178 Z','M120 120 L220 178 A115 115 0 0 1 120 235 Z','M120 120 L120 235 A115 115 0 0 1 20 178 Z','M120 120 L20 178 A115 115 0 0 1 20 62 Z','M120 120 L20 62 A115 115 0 0 1 120 5 Z']
            for i, p in enumerate(paths): s += f'<path d="{p}" fill="{col if i<painted_cnt else "#fff"}" stroke="var(--base)" stroke-width="2"/>'
        elif typ == "circle4":
            paths = ['M120 120 L120 5 A115 115 0 0 1 235 120 Z','M120 120 L235 120 A115 115 0 0 1 120 235 Z','M120 120 L120 235 A115 115 0 0 1 5 120 Z','M120 120 L5 120 A115 115 0 0 1 120 5 Z']
            for i, p in enumerate(paths): s += f'<path d="{p}" fill="{col if i<painted_cnt else "#fff"}" stroke="var(--base)" stroke-width="2"/>'
        elif typ == "circle5":
            paths = ['M120 120 L120 5 A115 115 0 0 0 10 84 Z','M120 120 L10 84 A115 115 0 0 0 52 213 Z','M120 120 L52 213 A115 115 0 0 0 188 213 Z','M120 120 L188 213 A115 115 0 0 0 230 84 Z','M120 120 L230 84 A115 115 0 0 0 120 5 Z']
            for i, p in enumerate(paths): s += f'<path d="{p}" fill="{col if i<painted_cnt else "#fff"}" stroke="var(--base)" stroke-width="2"/>'
        s += '</svg>'
        return s

    # Ejercicios PINTAR (6 slides)
    ex_list = [
        ("¡Pinta 2/3 en el rectángulo!", "2", "3", "rect", "#E1BEE7", 2),
        ("¡Pinta 3/4 en el círculo!", "3", "4", "circle4", "#FF9D9D", 3),
        ("¡Pinta 2/5 en el círculo!", "2", "5", "circle5", "#9DE3BD", 2),
        ("¡Pinta 4/6 en el cuadro!", "4", "6", "grid2x3", "#9DDEFF", 4),
        ("¡Pinta 1/4 en este pastel!", "1", "4", "circle4", "#FFB74D", 1),
        ("¡Pinta 4/5 en estas barras!", "4", "5", "rect_5", "#9DE3BD", 4)
    ]

    for title, n, d, typ, col, correct_n in ex_list:
        svg_blank = get_blank_svg(typ, col)
        svg_solved = draw_painted(typ, col, correct_n)
        slide(f"""
        <div class="head-title">¡A Pintar! 🖍️</div>
        <div style="font-size:28px; font-weight:800; margin-bottom:10px;">{title}</div>
        <div style="display:flex; justify-content:center; align-items:center; gap:50px; margin-top:20px;">
            <div style="display:flex; flex-direction:column; align-items:center; gap:20px;">
                <div class="frac-box"><div>{n}</div><div class="line"></div><div>{d}</div></div>
                {svg_blank}
            </div>
            <div class="stp" style="display:flex; flex-direction:column; align-items:center; border: 4px solid var(--base); padding:30px; border-radius:30px; background:#fff;">
                <div style="font-size:24px; font-weight:900; color:#555; margin-bottom:20px;">✅ Así debía quedar:</div>
                {svg_solved}
            </div>
        </div>
        """)
        
    # Ejercicios ADIVINAR (6 slides)
    id_list = [
        ("¿Qué fracción está pintada?", "grid2x3", "#9DDEFF", 3, ["3/6", "4/6", "6/3"], "3/6"),
        ("Elige la fracción correcta", "circle4", "#FF9D9D", 1, ["1/4", "3/4", "1/3"], "1/4"),
        ("¿Cuál es esta fracción?", "circle5", "#9DE3BD", 2, ["2/5", "3/5", "5/2"], "2/5"),
        ("Identifica esta fracción", "rect_5", "#FFE082", 4, ["4/5", "1/5", "5/4"], "4/5"),
        ("Cuenta cuidadosamente", "circle6", "#E1BEE7", 4, ["4/6", "2/6", "6/4"], "4/6"),
        ("Cuenta rápido", "circle4", "#FFB74D", 3, ["3/4", "1/4", "4/3"], "3/4"),
    ]

    for title, typ, col, p_cnt, opts_list, ans in id_list:
        btns = ""
        for o in opts_list:
            correct_flag = "true" if o == ans else "false"
            btns += f"<button class='btn' style='min-width:120px; font-size:24px; margin:5px;' onclick='chkAns(this, {correct_flag})'>{o}</button>"
            
        svg = draw_painted(typ, col, p_cnt)
        slide(f"""
        <div class="head-title">Adivina la Fracción 🤔</div>
        <p class="sub-text">{title}</p>
        <div style="display:flex; align-items:center; justify-content:center; gap:60px;">
            {svg}
            <div style="display:flex; flex-direction:column; gap:15px; text-align:center;">
                <p style="font-size:24px; font-weight: 800;">Opciones:</p>
                <div style="display:flex; flex-direction:column;">
                    {btns}
                </div>
                <div class="msg-area" style="font-size:22px; font-weight:800; height:30px; margin-top:20px;"></div>
            </div>
        </div>
        """)

    # Problemas de Resolución Diaria (Aplicados) (3 slides)
    verb_prob = [
        ("La caja de lápices 🖍️", "En una caja hay <b>8</b> lápices. <b>3</b> son rojos y el resto son azules. ¿Qué fracción de la caja son lápices rojos?", "Los rojos son 3.<br>El total de la caja es 8.<br><span style='color:var(--base); font-size:36px; font-weight:900;'>3/8</span>"),
        ("Juego de cartas 🃏", "Juan repartió <b>5</b> cartas. Tú obtuviste <b>2</b>. ¿Qué fracción de las cartas repartidas tienes tú?", "Tienes 2 cartas.<br>El total repartido fue 5.<br><span style='color:var(--base); font-size:36px; font-weight:900;'>2/5</span>"),
        ("La caminata al colegio 🏫", "El camino a la escuela se divide en <b>4</b> cuadras largas. Si ya caminaste <b>1</b> cuadra, ¿qué fracción del camino falta?", "La escuela son 4 cuadras (4/4).<br>Caminaste 1 cuadra (1/4).<br>Quedan <span style='color:var(--base); font-size:36px; font-weight:900;'>3/4</span> del camino.")
    ]
    for tit, prob, ans in verb_prob:
        slide(f"""
        <div class="head-title">Resolución de Problemas 💡</div>
        <div class="pnl-border" style="text-align:center; padding:50px;">
            <p style="font-size:36px; font-weight:800; margin-bottom:20px; color:var(--base);">{tit}</p>
            <p style="font-size:26px; line-height:1.6; margin-bottom:20px;">{prob}</p>
            
            <div class="stp" style="margin-top:30px; border-top: 2px dashed #ccc; padding-top:20px;">
                <p style="font-size:22px; color:#555; font-weight:800; margin-bottom:10px;">Respuesta:</p>
                <div style="font-size:24px;">{ans}</div>
            </div>
        </div>
        """)

    # Resumen y Cierre (2 slides finales)
    slide(f"""
        <div class="head-title">📋 Resumen de Anatomía</div>
        <div style="display:flex; flex-direction:column; gap:20px; width:100%;">
            <div class="stp pnl" style="padding:20px; font-size:24px; border-left: 8px solid var(--base);">
                📏 <b>Partes iguales:</b> Toda fracción requiere que la figura se corte en pedazos exactamente iguales.
            </div>
            <div class="stp pnl" style="padding:20px; font-size:24px; border-left: 8px solid var(--base);">
                🎨 <b>Numerador (Arriba):</b> La cantidad de partes que pintamos o seleccionamos del total.
            </div>
            <div class="stp pnl" style="padding:20px; font-size:24px; border-left: 8px solid var(--base);">
                🍕 <b>Denominador (Abajo):</b> El TOTAL de partes en las que se dividió toda la figura.
            </div>
        </div>
    """)
    
    slide(f"""
        <div class="head-title" style="background: #047857;">🏆 ¡Misión Cumplida!</div>
        <div style="font-size:32px; font-weight:800; text-align:center; margin-top:20px;">
            ¡Has entendido las bases perfectas de las fracciones!<br>Estás listo para avanzar.
        </div>
        <div style="font-size:80px; margin-top:40px; animation: bounce 2s infinite;">🌟</div>
        <style>@keyframes bounce {{ 0%, 100%{{transform:translateY(0);}} 50%{{transform:translateY(-20px);}} }}</style>
    """)

    # Output Gen
    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
    <title>Fracciones I - Anatomia Básica</title>
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

if __name__ == '__main__':
    generate_html()
