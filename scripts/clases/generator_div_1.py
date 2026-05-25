import os

def generate_html():
    css = """
    @import url('https://fonts.googleapis.com/css2?family=Nunito:wght@600;800;900&display=swap');
    :root {
        --base: #1C4A82;
        --bg: #f5f6f8;
        --tx: #333;
    }
    * {margin:0; padding:0; box-sizing:border-box;}
    body {font-family: 'Nunito', sans-serif; background: var(--bg); overflow: hidden; height: 100vh; width: 100vw; display: flex; flex-direction: column; align-items: center; color: var(--tx);}
    .dk {position: relative; width: 100%; height: 100%; max-width: 1000px; display: flex;}
    
    .sl {position: absolute; inset: 0; display: flex; flex-direction: column; align-items: center; justify-content: flex-start; padding: 36px 40px 82px; opacity: 0; transform: scale(.96); transition: opacity .4s, transform .4s; pointer-events: none; z-index: 1;}
    .sl.on {opacity: 1; transform: scale(0.9); pointer-events: auto; z-index: 10;}
    .sl.pv {opacity: 0; transform: translateX(-50px) scale(.95);}
    .sl.nx {opacity: 0; transform: translateX(50px) scale(.95);}
    
    .head-title {background: var(--base); color: white; padding: 10px 40px; font-size: 32px; font-weight: 900; margin-bottom: 30px; display: inline-block; border-radius: 12px; text-align: center;}
    .sub-text {font-size: 26px; font-weight: 600; margin-bottom: 25px; text-align: center;}
    
    .pb {position: fixed; top: 0; left: 0; height: 6px; background: var(--base); transition: width .4s; z-index: 100;}
    .nv {position: fixed; bottom: 0; left: 0; right: 0; height: 60px; background: white; border-top: 1px solid #ddd; display: flex; align-items: center; justify-content: space-between; padding: 0 40px; z-index: 100;}
    .nb {background: #eee; color: var(--base); border: none; padding: 10px 20px; border-radius: 8px; font-family: 'Nunito', sans-serif; font-size: 16px; font-weight: 900; cursor: pointer; transition: all .2s;}
    .nb:hover {background: #ddd;}
    .nb:disabled {opacity: 0.3; cursor: not-allowed;}
    .sc {color: #888; font-size: 16px; font-weight: 900;}
    
    .stp {opacity: 0; transform: translateY(20px); transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1); pointer-events: none;}
    .stp.shwn {opacity: 1; transform: translateY(0); pointer-events: auto;}
    
    .pnl {background: #fff; padding: 30px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); border: 3px solid #eaeaea; width: 100%; margin-bottom: 20px;}
    .pnl-border {background: #fff; border: 4px solid var(--base); border-radius: 20px; padding: 30px; display: flex; flex-direction: column; align-items: center; width: 100%;}
    .hl {color: var(--base); font-weight: 900;}
    
    .btn {background: var(--base); color: white; border: none; padding: 14px 28px; border-radius: 12px; font-size: 20px; font-weight: 900; cursor: pointer; transition: transform .2s; font-family: 'Nunito', sans-serif;}
    .btn:hover {transform: translateY(-2px); box-shadow: 0 4px 12px rgba(28,74,130,0.3);}
    
    .math-eq {font-size: 48px; font-weight: 900; color: var(--base); background: #fff; padding: 10px 30px; border-radius: 20px; box-shadow: 0 8px 20px rgba(0,0,0,0.1); border: 3px dashed #bbdefb; margin: 15px;}
    
    .card-row {display: flex; justify-content: center; gap: 18px; width: 100%; flex-wrap: wrap;}
    .idea-card {flex: 1 1 220px; background: linear-gradient(180deg, #ffffff 0%, #f7fbff 100%); border-radius: 18px; padding: 18px; border: 3px solid #d7e7f7; min-height: 220px;}
    .idea-card h3 {font-size: 28px; color: var(--base); margin-bottom: 10px; text-align: center;}
    
    .count-board {display: flex; justify-content: center; gap: 20px; width: 100%; flex-wrap: wrap;}
    .count-card {flex: 1 1 260px; background: linear-gradient(180deg, #ffffff 0%, #f6fbff 100%); border-radius: 22px; padding: 20px; border: 4px solid #d6e8f8; box-shadow: 0 12px 24px rgba(0,0,0,0.06); text-align: center;}
    .count-card h3 {font-size: 28px; margin-bottom: 12px; color: var(--base);}
    .emoji-pack {display: flex; flex-wrap: wrap; justify-content: center; gap: 10px; min-height: 86px; margin-bottom: 12px;}
    
    .mini-chip {background: #eef5ff; border: 2px solid #b6d4f3; border-radius: 999px; padding: 12px 18px; font-size: 20px; font-weight: 800;}
    
    .fact-grid {display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 16px; width: 100%;}
    .fact-box {background: linear-gradient(180deg, #ffffff 0%, #f8fbff 100%); border-radius: 18px; padding: 16px; border: 3px solid #d8e7f6; min-height: 170px;}
    .fact-box h4 {font-size: 24px; margin-bottom: 10px; text-align: center;}
    
    .story-card {width: 100%; border-radius: 28px; padding: 28px; display: grid; grid-template-columns: 120px 1fr; gap: 24px; align-items: center; background: #fff;}
    .story-emoji {font-size: 114px; text-align: center;}
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
        let sl = document.getElementById('slide-slider');
        if(sl) { sl.max = T; sl.value = c + 1; }
    }
    function goToSlide(n) {
        let val = parseInt(n) - 1;
        if (val >= 0 && val < T) {
            c = val;
            ui();
        }
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
    
    function chkAns(btn, correct, exp) {
        let wrap = btn.closest('.sl');
        let msg = wrap.querySelector('.msg-area');
        let buttons = wrap.querySelectorAll('.btn');
        buttons.forEach(b => { b.disabled = false; b.style.transform = 'scale(1)'; b.style.background = 'var(--base)'; });
        
        if (correct) {
            btn.style.background = '#047857';
            btn.style.transform = 'scale(1.06)';
            msg.innerHTML = `¡Excelente! ✅ ${exp}`;
            msg.style.color = '#047857';
        } else {
            btn.style.background = '#b91c1c';
            msg.innerHTML = '¡Inténtalo de nuevo! Revisa tu cálculo.';
            msg.style.color = '#b91c1c';
        }
    }
    """
    
    slides = []
    def slide(html): slides.append(f'<div class="sl">{html}</div>')
    def esc(s): return s.replace('"', '&quot;')
    
    def emoji_pack(emoji: str, count: int, size: int = 52) -> str:
        return "".join(f'<span style="font-size:{size}px; line-height:1;">{emoji}</span>' for _ in range(count))

    def picture_operation_slide(title, subtitle, left_title, left_visual, right_title, right_visual, operator, result_text, note, left_border, right_border, result_border):
        slide(f"""
            <div class="head-title">{title}</div>
            <p class="sub-text">{subtitle}</p>
            <div class="count-board">
                <div class="count-card" style="border-color:{left_border}; background:linear-gradient(180deg,#fffdf1 0%,#ffffff 100%);">
                    <h3>{left_title}</h3>
                    <div class="emoji-pack">{left_visual}</div>
                </div>
                <div class="math-eq" style="font-size:60px; display:flex; align-items:center;">{operator}</div>
                <div class="count-card stp" style="border-color:{right_border}; background:linear-gradient(180deg,#f4fff7 0%,#ffffff 100%);">
                    <h3>{right_title}</h3>
                    <div class="emoji-pack">{right_visual}</div>
                </div>
            </div>
            <div class="stp math-eq" style="border-color:{result_border}; background:#faf4ff;">{result_text}</div>
            <div class="stp mini-chip">{note}</div>
        """)

    def exercise_cards_slide(title, subtitle, items):
        cards = []
        for emoji, expr, ans, border in items:
            cards.append(f"""
                <div class="idea-card" style="border-color:{border}; background:linear-gradient(180deg,#ffffff 0%,#fbfcff 100%); display:flex; flex-direction:column; justify-content:center; align-items:center;">
                    <div style="font-size:60px; text-align:center; margin-bottom:10px;">{emoji}</div>
                    <div style="font-size:34px; font-weight:900; text-align:center; color:#234c7c; margin-bottom:10px;">{expr}</div>
                    <div class="stp math-eq" style="font-size:38px; border-color:{border}; margin:0; padding: 10px;">{ans}</div>
                </div>
            """)
        slide(f"""
            <div class="head-title">{title}</div>
            <p class="sub-text">{subtitle}</p>
            <div class="card-row">{''.join(cards)}</div>
        """)

    def quiz_slide(title, question, options, ok_index, exp):
        buttons = "".join(f'<button class="btn" onclick="chkAns(this, {str(i == ok_index).lower()}, \'{esc(exp)}\')">{opt}</button>' for i, opt in enumerate(options))
        slide(f"""
            <div class="head-title">{title}</div>
            <div class="pnl-border" style="border-color:#d63384; background:#fff7fb;">
                <p style="font-size:32px; font-weight:800; text-align:center; margin-bottom:24px;">{question}</p>
                <div style="display:flex; justify-content:center; gap:20px; flex-wrap:wrap;">{buttons}</div>
                <div class="msg-area" style="font-size:24px; font-weight:900; text-align:center; margin-top:20px; min-height:40px;"></div>
            </div>
        """)

    # 1. Portada
    slide(f"""
        <div style="flex:1; display:flex; flex-direction:column; justify-content:center; align-items:center;">
            <h1 style="font-size:68px; color:var(--base); margin-bottom:18px; text-align:center; line-height:1;">¡División 1! ➗</h1>
            <p style="font-size:28px; font-weight:700; text-align:center; max-width:720px;">Repartir en partes iguales, la familia de operaciones y el truco de la tabla inversa.</p>
            <div style="font-size:108px; margin-top:28px;">🍊</div>
        </div>
    """)

    # 2. Contextualización
    slide(f"""
        <div class="head-title">¿Por qué inventamos la división?</div>
        <div class="story-card" style="border:5px solid #FFB74D; background:#fffbf4;">
            <div class="story-emoji">🍕</div>
            <div>
                <h2 style="color:#e65100; font-size:32px;">El problema de la pizza</h2>
                <p style="font-size:24px;">Imagina que tienes una pizza de 8 pedazos y tú y 3 amigos quieren comer.</p>
                <div class="stp" style="margin-top:15px;">
                    <p style="font-size:24px; font-weight:800; color:#e65100;">Si uno come más que el resto, ¡habrá una gran pelea! Necesitamos que sea JUSTO.</p>
                </div>
                <div class="stp" style="margin-top:15px; background:#FFE082; padding:15px; border-radius:10px;">
                    <p style="font-size:22px; font-weight:700;">Para evitar peleas en el universo, las matemáticas inventaron la <b>División</b>: el arte de repartir en partes exactamente iguales.</p>
                </div>
            </div>
        </div>
    """)

    # 3. ¿Qué significa dividir?
    picture_operation_slide(
        "¿Qué significa dividir?",
        "Dividir es <b class=\"hl\">repartir el total en partes iguales</b>.",
        "Tengo 12 naranjas",
        emoji_pack("🍊", 12, 46),
        "Las repartiré en 3 canastos",
        emoji_pack("🧺", 3, 56),
        "÷",
        "12 ÷ 3 = 4",
        "Todos los canastos reciben la misma cantidad.",
        "#FFB74D", "#9DE3BD", "#FFE082"
    )

    # 4. Visualización Grupos
    slide(f"""
        <div class="head-title">Repartimos 12 en 3 grupos</div>
        <p class="sub-text">Cada grupo debe quedar con la <b class="hl">misma cantidad</b>.</p>
        <div class="count-board">
            <div class="count-card stp" style="border-color:#FFE082; max-width:220px;">
                <h3>Grupo 1</h3><div class="emoji-pack">{emoji_pack('🍊',4)}</div><div class="mini-chip">4 naranjas</div>
            </div>
            <div class="count-card stp" style="border-color:#FFE082; max-width:220px;">
                <h3>Grupo 2</h3><div class="emoji-pack">{emoji_pack('🍊',4)}</div><div class="mini-chip">4 naranjas</div>
            </div>
            <div class="count-card stp" style="border-color:#FFE082; max-width:220px;">
                <h3>Grupo 3</h3><div class="emoji-pack">{emoji_pack('🍊',4)}</div><div class="mini-chip">4 naranjas</div>
            </div>
        </div>
        <div class="stp math-eq">12 ÷ 3 = 4</div>
    """)

    # 5. Multiplicación y división son familia
    picture_operation_slide(
        "Multiplicación y división son familia",
        "Están totalmente conectadas. Son como dos caras de una moneda.",
        "3 × 4",
        emoji_pack("⭐", 12, 42),
        "Repartido en 3 grupos",
        emoji_pack("🧺", 3, 54),
        "↔",
        "12 ÷ 3 = 4",
        "La multiplicación arma el total. La división lo reparte.",
        "#FFE082", "#9DE3BD", "#FFB74D"
    )

    # 6. Familia de Operaciones
    slide(f"""
        <div class="head-title">La familia de operaciones</div>
        <p class="sub-text">Una sola multiplicación te regala <b class="hl">dos divisiones gratis</b>.</p>
        <div class="card-row">
            <div class="idea-card" style="border-color:#FFE082; display:flex; flex-direction:column; justify-content:center; align-items:center;">
                <h3 style="font-size:40px;">3 × 5 = 15</h3>
            </div>
            <div class="idea-card stp" style="border-color:#9DE3BD; display:flex; flex-direction:column; justify-content:center; align-items:center;">
                <h3 style="font-size:40px;">15 ÷ 3 = 5</h3>
                <div class="mini-chip">Buscas un factor</div>
            </div>
            <div class="idea-card stp" style="border-color:#FFB74D; display:flex; flex-direction:column; justify-content:center; align-items:center;">
                <h3 style="font-size:40px;">15 ÷ 5 = 3</h3>
                <div class="mini-chip">Buscas el otro factor</div>
            </div>
        </div>
    """)

    # 7. La tabla inversa
    slide(f"""
        <div class="head-title">El truco de la Tabla Inversa 🔄</div>
        <p class="sub-text">¡El mejor truco para dividir rápido es usar las tablas de multiplicar!</p>
        <div class="pnl-border" style="background:linear-gradient(135deg,#fff7e8 0%,#f4fff8 50%,#faf4ff 100%);">
            <div class="math-eq" style="font-size:54px;">Para resolver: <b>24 ÷ 3 = ?</b></div>
            <div class="stp math-eq" style="font-size:46px; border-color:#FF9D9D;">Me pregunto: <b>¿Qué número multiplicado por 3 da 24?</b></div>
            <div class="stp math-eq" style="font-size:46px; border-color:#9DE3BD;">¡Es el 8! Porque <b>8 × 3 = 24</b></div>
            <div class="stp mini-chip">Por lo tanto: 24 ÷ 3 = 8.</div>
        </div>
    """)

    # 8. Abre tu cuaderno: Tabla inversa 1
    slide(f"""
        <div class="head-title" style="background:#1976D2;">Abre tu cuaderno 📓</div>
        <div class="pnl-border" style="border-color:#1976D2;">
            <p style="font-size:32px; font-weight:800;">Calcula en tu cuaderno usando la tabla inversa:</p>
            <div class="math-eq" style="font-size:64px;">45 ÷ 5 = ?</div>
            <div class="stp" style="margin-top:20px; display:flex; flex-direction:column; align-items:center;">
                <div class="mini-chip" style="font-size:24px;">Pregúntate: ¿Qué número multiplicado por 5 da 45?</div>
                <div class="math-eq" style="font-size:54px; border-color:#047857; color:#047857; background:#D1FAE5; margin-top:20px;">9</div>
                <div style="font-size:24px; font-weight:700; color:#047857;">Porque 9 × 5 = 45</div>
            </div>
        </div>
    """)

    # 9. Práctica tabla inversa
    exercise_cards_slide(
        "Pasa de multiplicación a división",
        "Usa las tablas que ya conoces para encontrar la respuesta.",
        [
            ("🌈", "10 ÷ 5 = ?", "2 (2x5=10)", "#FFB74D"),
            ("🧩", "12 ÷ 4 = ?", "3 (3x4=12)", "#9DE3BD"),
            ("🎈", "36 ÷ 6 = ?", "6 (6x6=36)", "#E1BEE7"),
        ]
    )

    # 10. Propiedad del 1 en división - Contexto
    slide(f"""
        <div class="head-title">Casos especiales: El número 1</div>
        <div class="story-card" style="border:5px solid #E1BEE7; background:#fbf4ff;">
            <div class="story-emoji">🍬</div>
            <div>
                <h2 style="color:#8E44AD; font-size:32px;">Una fiesta solitaria</h2>
                <p style="font-size:24px;">Imagina que tienes <b>10 dulces</b> y los quieres repartir equitativamente entre... <b>¡solo 1 niño (tú)!</b></p>
                <div class="stp" style="margin-top:15px;">
                    <p style="font-size:24px; font-weight:800;">¿Cuántos dulces recibe ese niño?</p>
                </div>
                <div class="stp" style="margin-top:15px; background:#E1BEE7; padding:15px; border-radius:10px;">
                    <p style="font-size:24px; font-weight:800; color:#4a148c;">¡Se los lleva TODOS! 10 ÷ 1 = 10.</p>
                </div>
            </div>
        </div>
    """)

    # 11. Propiedad del 1 en división - Contexto 2
    slide(f"""
        <div class="head-title">Casos especiales: Dividir por sí mismo</div>
        <div class="story-card" style="border:5px solid #9DE3BD; background:#f4fff7;">
            <div class="story-emoji">🧒</div>
            <div>
                <h2 style="color:#047857; font-size:32px;">La fiesta equitativa</h2>
                <p style="font-size:24px;">Ahora tienes los mismos <b>10 dulces</b>, pero llegaron a la fiesta <b>10 niños</b>.</p>
                <div class="stp" style="margin-top:15px;">
                    <p style="font-size:24px; font-weight:800;">¿Cuántos dulces recibe cada niño para que sea justo?</p>
                </div>
                <div class="stp" style="margin-top:15px; background:#9DE3BD; padding:15px; border-radius:10px;">
                    <p style="font-size:24px; font-weight:800; color:#004d40;">¡Apenas 1 para cada uno! 10 ÷ 10 = 1.</p>
                </div>
            </div>
        </div>
    """)

    # 12. Reglas del 1 (Formal)
    slide(f"""
        <div class="head-title">Las Reglas del 1 ☝️</div>
        <p class="sub-text">Apréndete estas dos reglas y resolverás estas divisiones en un segundo.</p>
        <div class="fact-grid">
            <div class="fact-box" style="border-color:#FF9D9D;">
                <h4 style="color:#FF9D9D; font-size:32px;">N ÷ 1</h4>
                <p>Cualquier número dividido en 1 da el <b>mismo número</b> (te llevas todo).</p>
                <div class="stp math-eq" style="font-size:30px;">87 ÷ 1 = 87</div>
            </div>
            <div class="fact-box stp" style="border-color:#9DE3BD;">
                <h4 style="color:#047857; font-size:32px;">N ÷ N</h4>
                <p>Cualquier número dividido por sí mismo da <b>1</b> (alcanza justo para uno).</p>
                <div class="stp math-eq" style="font-size:30px;">26 ÷ 26 = 1</div>
            </div>
        </div>
    """)

    # 13. Abre tu cuaderno: Reglas del 1
    slide(f"""
        <div class="head-title" style="background:#1976D2;">Abre tu cuaderno 📓</div>
        <div class="pnl-border" style="border-color:#1976D2;">
            <p style="font-size:32px; font-weight:800;">Calcula en tu cuaderno estas dos divisiones al instante:</p>
            <div style="display:flex; justify-content:center; gap:40px; margin-top:20px;">
                <div class="math-eq" style="font-size:48px;">145 ÷ 1 = ?</div>
                <div class="math-eq" style="font-size:48px;">32 ÷ 32 = ?</div>
            </div>
            <div class="stp" style="margin-top:20px; display:flex; gap:40px;">
                <div class="math-eq" style="font-size:54px; border-color:#047857; color:#047857; background:#D1FAE5; margin:0;">145</div>
                <div class="math-eq" style="font-size:54px; border-color:#047857; color:#047857; background:#D1FAE5; margin:0;">1</div>
            </div>
        </div>
    """)

    # 14. Quiz de comprobación
    quiz_slide(
        "Examen Ninja Rápido 🥷",
        "Si sé que 7 × 8 = 56, ¿cuál es la división que me ayuda a saber cuántos elementos hay en 8 grupos iguales?",
        ["56 ÷ 8 = 7", "56 ÷ 7 = 8", "8 ÷ 7 = 56"],
        0,
        "¡Bien! 56 total dividido en 8 grupos, da 7 por grupo."
    )

    # 15. Detección de error
    slide(f"""
        <div class="head-title" style="background:#e53935;">¡Encuentra el Error! 🚨</div>
        <div class="story-card" style="border:5px solid #FF9D9D;">
            <div class="story-emoji">🤷‍♂️</div>
            <div>
                <h2 style="color:#b91c1c; font-size:32px;">Pedro resolvió 54 ÷ 6</h2>
                <p style="font-size:24px;">Pedro pensó: <i>"Ah, uso la tabla inversa... 6 por 8 es 54, así que la respuesta es 8"</i>.</p>
                <div class="stp" style="margin-top:15px;">
                    <p style="font-size:24px; font-weight:800; color:#047857;">¿Qué hizo mal Pedro y cuál es el resultado correcto?</p>
                </div>
                <div class="stp" style="margin-top:15px; background:#D1FAE5; padding:15px; border-radius:10px;">
                    <p style="font-size:22px; font-weight:700;">Error de tabla: 6x8=48, no 54. La respuesta correcta es 9, porque 6x9=54.</p>
                </div>
            </div>
        </div>
    """)

    # 16. Preparando Bloque 3
    slide(f"""
        <div class="head-title">¡Hora de entrenar!</div>
        <p class="sub-text">A continuación, enfrentarás 6 ejercicios en tu cuaderno.</p>
        <div class="fact-grid">
            <div class="fact-box stp" style="border-color:#FFE082;">
                <h4>Tabla Inversa</h4>
                <p>Usa la multiplicación en tu cabeza para resolver la división.</p>
            </div>
            <div class="fact-box stp" style="border-color:#9DE3BD;">
                <h4>Familia</h4>
                <p>Acuérdate que una multiplicación genera dos divisiones.</p>
            </div>
            <div class="fact-box stp" style="border-color:#E1BEE7;">
                <h4>Reglas del 1</h4>
                <p>No lo pienses demasiado si divides por 1 o por el mismo número.</p>
            </div>
        </div>
    """)

    # 17. BLOQUE 3 - Misión de Entrenamiento
    slide(f"""
        <div class="head-title" style="background:#F57C00;">Misión de Entrenamiento ✍️</div>
        <p class="sub-text">Escribe estas 6 divisiones en tu cuaderno y resuélvelas.</p>
        <div style="display:grid; grid-template-columns: 1fr 1fr; gap:15px; width:100%;">
            <div class="pnl-border" style="display:flex; justify-content:space-between; align-items:center; padding:15px; border-color:#FF9D9D;">
                <div style="font-size:26px; font-weight:900;">1) 32 ÷ 4 =</div>
                <div style="font-size:26px; font-weight:900; color:#b91c1c; border-bottom:3px solid #b91c1c; width:80px; text-align:center;">?</div>
            </div>
            <div class="pnl-border" style="display:flex; justify-content:space-between; align-items:center; padding:15px; border-color:#FF9D9D;">
                <div style="font-size:26px; font-weight:900;">2) 45 ÷ 5 =</div>
                <div style="font-size:26px; font-weight:900; color:#b91c1c; border-bottom:3px solid #b91c1c; width:80px; text-align:center;">?</div>
            </div>
            <div class="pnl-border" style="display:flex; justify-content:space-between; align-items:center; padding:15px; border-color:#FFB74D;">
                <div style="font-size:26px; font-weight:900;">3) 63 ÷ 9 =</div>
                <div style="font-size:26px; font-weight:900; color:#e65100; border-bottom:3px solid #e65100; width:80px; text-align:center;">?</div>
            </div>
            <div class="pnl-border" style="display:flex; justify-content:space-between; align-items:center; padding:15px; border-color:#FFB74D;">
                <div style="font-size:26px; font-weight:900;">4) 28 ÷ 7 =</div>
                <div style="font-size:26px; font-weight:900; color:#e65100; border-bottom:3px solid #e65100; width:80px; text-align:center;">?</div>
            </div>
            <div class="pnl-border" style="display:flex; justify-content:space-between; align-items:center; padding:15px; border-color:#9DDEFF;">
                <div style="font-size:26px; font-weight:900;">5) 89 ÷ 89 =</div>
                <div style="font-size:26px; font-weight:900; color:#1C4A82; border-bottom:3px solid #1C4A82; width:80px; text-align:center;">?</div>
            </div>
            <div class="pnl-border" style="display:flex; justify-content:space-between; align-items:center; padding:15px; border-color:#9DDEFF;">
                <div style="font-size:26px; font-weight:900;">6) 145 ÷ 1 =</div>
                <div style="font-size:26px; font-weight:900; color:#1C4A82; border-bottom:3px solid #1C4A82; width:80px; text-align:center;">?</div>
            </div>
        </div>
    """)

    # 18. Resultados Bloque 3
    slide(f"""
        <div class="head-title" style="background:#047857;">Revisión de la Misión ✔️</div>
        <p class="sub-text">Hazte un check si tus resultados coinciden:</p>
        <div style="display:grid; grid-template-columns: 1fr 1fr; gap:15px; width:100%;">
            <div class="pnl-border stp" style="display:flex; justify-content:center; align-items:center; padding:15px; background:#D1FAE5; border-color:#059669;">
                <div style="font-size:28px; font-weight:900; color:#059669;">1) 8</div>
            </div>
            <div class="pnl-border stp" style="display:flex; justify-content:center; align-items:center; padding:15px; background:#D1FAE5; border-color:#059669;">
                <div style="font-size:28px; font-weight:900; color:#059669;">2) 9</div>
            </div>
            <div class="pnl-border stp" style="display:flex; justify-content:center; align-items:center; padding:15px; background:#D1FAE5; border-color:#059669;">
                <div style="font-size:28px; font-weight:900; color:#059669;">3) 7</div>
            </div>
            <div class="pnl-border stp" style="display:flex; justify-content:center; align-items:center; padding:15px; background:#D1FAE5; border-color:#059669;">
                <div style="font-size:28px; font-weight:900; color:#059669;">4) 4</div>
            </div>
            <div class="pnl-border stp" style="display:flex; justify-content:center; align-items:center; padding:15px; background:#D1FAE5; border-color:#059669;">
                <div style="font-size:28px; font-weight:900; color:#059669;">5) 1</div>
            </div>
            <div class="pnl-border stp" style="display:flex; justify-content:center; align-items:center; padding:15px; background:#D1FAE5; border-color:#059669;">
                <div style="font-size:28px; font-weight:900; color:#059669;">6) 145</div>
            </div>
        </div>
    """)

    # 19. Problema contextualizado
    slide(f"""
        <div class="head-title">Problema en la Feria</div>
        <div class="story-card" style="border:5px solid #9DDEFF; background:#f4f9ff;">
            <div class="story-emoji">🍅</div>
            <div>
                <h2 style="color:#1C4A82; font-size:32px;">Canastos de tomates</h2>
                <p style="font-size:24px;">En la feria, el casero tiene 48 tomates y quiere armar canastos iguales. Cada canasto lleva 6 tomates.</p>
                <div class="stp" style="margin-top:15px;">
                    <p style="font-size:24px; font-weight:800;">¿Cuántos canastos puede llenar usando la tabla inversa?</p>
                </div>
                <div class="stp" style="margin-top:15px; background:#fff; padding:15px; border-radius:10px; border-left:5px solid #9DDEFF;">
                    <p style="font-size:24px; font-weight:800; color:#1C4A82;">Pienso: ¿Qué número por 6 da 48? ¡Es 8! Entonces, 48 ÷ 6 = 8 canastos.</p>
                </div>
            </div>
        </div>
    """)

    # 20. Problema contextualizado 2
    slide(f"""
        <div class="head-title">Problema de Empanadas</div>
        <div class="story-card" style="border:5px solid #FFE082; background:#fffbf4;">
            <div class="story-emoji">🥟</div>
            <div>
                <h2 style="color:#e65100; font-size:32px;">Docenas de empanadas</h2>
                <p style="font-size:24px;">Una panadería preparó 72 empanadas de pino y las debe guardar en cajas que aguantan 8 empanadas.</p>
                <div class="stp" style="margin-top:15px;">
                    <p style="font-size:24px; font-weight:800;">¿Cuántas cajas necesitan? Usa la tabla inversa.</p>
                </div>
                <div class="stp" style="margin-top:15px; background:#fff; padding:15px; border-radius:10px; border-left:5px solid #FFE082;">
                    <p style="font-size:24px; font-weight:800; color:#e65100;">Pienso: ¿Qué número por 8 da 72? ¡Es 9! Entonces, 72 ÷ 8 = 9 cajas.</p>
                </div>
            </div>
        </div>
    """)

    # 21. ObraCraft Intro
    slide(f"""
        <div class="head-title" style="background:linear-gradient(90deg, #6a1b9a, #d50000);">Desafío Supremo ⚔️</div>
        <div style="flex:1; display:flex; flex-direction:column; justify-content:center; align-items:center; text-align:center;">
            <h1 style="font-size:64px; color:#4a148c; margin-bottom:20px;">Mundo ObraCraft ⛏️</h1>
            <p style="font-size:28px; font-weight:700; max-width:720px;">Estás en el laboratorio de pociones mágicas. Necesitas preparar frascos exactos para tu gremio usando la tabla inversa de la magia.</p>
            <div style="font-size:120px; margin-top:20px;">🧪</div>
            <p class="stp" style="font-size:24px; margin-top:20px; font-weight:800; color:#b91c1c;">¡Prepárate para abrir los cofres!</p>
        </div>
    """)

    # 22. ObraCraft Problema
    slide(f"""
        <div class="head-title" style="background:linear-gradient(90deg, #6a1b9a, #d50000);">Desafío Supremo ⚔️</div>
        <div class="pnl-border" style="border-color:#8E44AD; background:#fdfaff;">
            <div style="font-size:80px; text-align:center;">🧙‍♂️</div>
            <p style="font-size:26px; text-align:center; font-weight:700; margin-bottom:20px;">Tienes el gran caldero con <b style="color:#6a1b9a;">56 litros</b> de poción de invisibilidad. Debes repartirla en frascos mágicos. Cada frasco hace efecto si tiene exactamente <b style="color:#6a1b9a;">7 litros</b>.</p>
            <div class="stp" style="background:#fff; border:3px dashed #8E44AD; padding:20px; border-radius:15px; width:100%; text-align:center;">
                <p style="font-size:28px; font-weight:900; margin-bottom:10px;">¿Cuántos frascos podrás llenar para tu gremio?</p>
                <div class="math-eq" style="font-size:40px; margin:0; display:inline-block;">56 ÷ 7 = ?</div>
            </div>
            <div class="stp" style="margin-top:20px; text-align:center;">
                <p style="font-size:24px; font-weight:800; color:#4a148c;">Usa la tabla inversa de la magia (qué número por 7 da 56).</p>
            </div>
        </div>
    """)

    # 23. ObraCraft Solución
    slide(f"""
        <div class="head-title" style="background:linear-gradient(90deg, #6a1b9a, #d50000);">Desafío Supremo ⚔️</div>
        <div style="flex:1; display:flex; flex-direction:column; justify-content:center; align-items:center; text-align:center;">
            <div style="font-size:120px; margin-bottom:20px;">✨🏺✨</div>
            <h1 style="font-size:54px; color:#4a148c; margin-bottom:20px;">¡Llenaste 8 frascos!</h1>
            <p style="font-size:28px; font-weight:700; max-width:720px;">Porque <b>8 × 7 = 56</b>. Tu gremio ahora es completamente invisible y listo para la misión secreta.</p>
        </div>
    """)

    # 24. Resumen y Cierre
    slide(f"""
        <div class="head-title" style="background:#047857;">¡Misión Cumplida! 🏆</div>
        <div style="flex:1; display:flex; flex-direction:column; justify-content:center; width:100%;">
            <p style="font-size:32px; font-weight:800; color:#047857; text-align:center; margin-bottom:30px;">¡Ya dominas la base de la división!</p>
            <div style="display:flex; flex-direction:column; gap:15px;">
                <div class="stp pnl" style="padding:15px; font-size:22px;"><b>1. Dividir es ser justo:</b> Repartir un total en partes exactamente iguales.</div>
                <div class="stp pnl" style="padding:15px; font-size:22px;"><b>2. Familia conectada:</b> La división es la hermana inversa de la multiplicación.</div>
                <div class="stp pnl" style="padding:15px; font-size:22px;"><b>3. Tabla inversa:</b> Si quieres saber 45:5, solo pregúntate "qué número por 5 da 45". ¡Es 9!</div>
                <div class="stp pnl" style="padding:15px; font-size:22px;"><b>4. El número 1:</b> Si divides por 1, todo queda igual. Si divides por sí mismo, da 1.</div>
            </div>
        </div>
    """)


    html = f"""<!DOCTYPE html>
<html lang="es"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"><title>División Módulo 1</title><style>{css}</style></head>
<body><div class="pb" id="pb"></div><div class="dk">{"".join(slides)}</div>
<div class="nv">
    <button class="nb" id="pv" onclick="go(-1)">⬅ Anterior</button>
    <div style="display:flex; flex-direction:column; align-items:center; gap:2px; max-width:200px; width:100%;">
        <span class="sc" id="sc">1 / {len(slides)}</span>
        <input type="range" id="slide-slider" style="width: 100%; cursor: pointer;" min="1" max="{len(slides)}" value="1" oninput="goToSlide(this.value)">
    </div>
    <button class="nb" id="nx" onclick="go(1)">Siguiente ➡</button>
</div>
<script>{js}</script></body></html>"""

    output_dir = '/Users/brunonattino/Desktop/PAGINA TUTORIAS/clases/cuarto-basico/division'
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, 'division_1.html')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Módulo 1 de división generado: {len(slides)} slides en {output_path}")

if __name__ == '__main__':
    generate_html()
