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
    
    .decomp-flow {display: flex; justify-content: center; gap: 14px; flex-wrap: wrap; width: 100%; align-items: center;}
    .decomp-box {background: #fff; border: 3px solid #d4e6f7; border-radius: 18px; padding: 14px 18px; font-size: 28px; font-weight: 900; color: var(--base);}
    .arrow {font-size: 34px; font-weight: 900; color: #4d6d94;}
    
    .fact-grid {display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 16px; width: 100%;}
    .fact-box {background: linear-gradient(180deg, #ffffff 0%, #f8fbff 100%); border-radius: 18px; padding: 16px; border: 3px solid #d8e7f6; min-height: 170px;}
    .fact-box h4 {font-size: 24px; margin-bottom: 10px; text-align: center;}
    
    .story-card {width: 100%; border-radius: 28px; padding: 28px; display: grid; grid-template-columns: 120px 1fr; gap: 24px; align-items: center; background: #fff;}
    .story-emoji {font-size: 114px; text-align: center;}
    
    /* Para el algoritmo de la casita */
    .alg-container {font-family: 'Courier New', Courier, monospace; font-size: 44px; font-weight: 900; background: #fff; padding: 30px; border-radius: 20px; border: 3px solid #1C4A82; box-shadow: 0 10px 30px rgba(0,0,0,0.1); text-align: right; display: inline-block;}
    .alg-line {border-bottom: 4px solid #1C4A82; margin: 5px 0;}
    .alg-row {display: flex; justify-content: flex-end; align-items: center; gap: 15px;}
    .alg-step-box {background: #f4f9ff; border: 2px solid #b6d4f3; border-radius: 12px; padding: 15px; font-size: 22px; font-weight: 700; width: 100%; margin-bottom: 10px;}
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

    # 1. INTRO
    slide(f"""
        <div style="flex:1; display:flex; flex-direction:column; justify-content:center; align-items:center;">
            <h1 style="font-size:68px; color:var(--base); margin-bottom:18px; text-align:center; line-height:1;">¡División 2! 🏠</h1>
            <p style="font-size:28px; font-weight:700; text-align:center; max-width:720px;">El algoritmo de "la casita", divisiones exactas e inexactas, y el manejo del resto.</p>
            <div style="font-size:108px; margin-top:28px;">✏️</div>
        </div>
    """)

    # 2. Contextualización Inicial
    slide(f"""
        <div class="head-title">¿Por qué inventamos el Algoritmo?</div>
        <div class="story-card" style="border:5px solid #FFB74D; background:#fffbf4;">
            <div class="story-emoji">🤯</div>
            <div>
                <h2 style="color:#e65100; font-size:32px;">El problema gigante</h2>
                <p style="font-size:24px;">La tabla inversa sirve cuando quieres dividir 24 ÷ 3 o 45 ÷ 5.</p>
                <div class="stp" style="margin-top:15px;">
                    <p style="font-size:24px; font-weight:800; color:#e65100;">Pero... ¿Qué pasa si te piden repartir 84 galletas entre 4 personas o 96 dulces entre 3?</p>
                </div>
                <div class="stp" style="margin-top:15px; background:#FFE082; padding:15px; border-radius:10px;">
                    <p style="font-size:22px; font-weight:700;">Esos números son demasiado grandes para usar los dedos o las tablas. ¡Para eso existe la <b>herramienta definitiva</b> de los matemáticos!</p>
                </div>
            </div>
        </div>
    """)

    # 3. El algoritmo
    slide(f"""
        <div class="head-title">El Algoritmo de "La Casita"</div>
        <p class="sub-text">Cuando los números son muy grandes, usamos estos <b class="hl">5 pasos mágicos</b>.</p>
        <div class="fact-grid">
            <div class="fact-box stp" style="border-color:#FF9D9D;">
                <h4 style="color:#b91c1c;">1. Separar</h4>
                <p>Miro el primer dígito (de izquierda a derecha). Lo separo con una comita.</p>
            </div>
            <div class="fact-box stp" style="border-color:#FFB74D;">
                <h4 style="color:#e65100;">2. Dividir</h4>
                <p>Uso la tabla inversa: ¿Qué número por el divisor se acerca?</p>
            </div>
            <div class="fact-box stp" style="border-color:#FFE082;">
                <h4 style="color:#f57f17;">3. Multiplicar</h4>
                <p>Multiplico el número que encontré por el divisor y lo anoto.</p>
            </div>
            <div class="fact-box stp" style="border-color:#9DE3BD;">
                <h4 style="color:#047857;">4. Restar</h4>
                <p>Resto para ver cuánto me sobró en este paso.</p>
            </div>
            <div class="fact-box stp" style="border-color:#9DDEFF;">
                <h4 style="color:#1C4A82;">5. Bajar</h4>
                <p>Bajo el siguiente dígito y repito todo desde el paso 2.</p>
            </div>
        </div>
    """)

    # 4. Ejemplo paso a paso (84 : 2)
    slide(f"""
        <div class="head-title">Ejemplo Lento: 84 : 2</div>
        <div style="display:flex; gap:30px; width:100%;">
            <div style="flex:1;">
                <div class="alg-step-box stp"><b>Paso 1 y 2:</b> Separo el 8. ¿Qué por 2 da 8? ¡Es 4! Anoto el 4 en el resultado.</div>
                <div class="alg-step-box stp"><b>Paso 3 y 4:</b> Multiplico 4x2=8. Resto 8-8=0.</div>
                <div class="alg-step-box stp"><b>Paso 5:</b> Bajo el 4 al lado del 0.</div>
                <div class="alg-step-box stp"><b>Repito:</b> ¿Qué por 2 da 4? Es 2. Multiplico 2x2=4. Resto 4-4=0. ¡Terminé!</div>
            </div>
            <div style="flex:1; display:flex; justify-content:center; align-items:center;">
                <div class="alg-container">
                    <div class="alg-row"><span>8'4</span> <span>: 2 =</span> <span class="stp hl" style="color:#047857;">42</span></div>
                    <div class="alg-row stp"><span style="color:#b91c1c;">-8</span></div>
                    <div class="alg-line stp"></div>
                    <div class="alg-row stp"><span>04</span></div>
                    <div class="alg-row stp"><span style="color:#b91c1c;">-4</span></div>
                    <div class="alg-line stp"></div>
                    <div class="alg-row stp"><span>0</span></div>
                </div>
            </div>
        </div>
    """)

    # 5. División Exacta vs Inexacta
    slide(f"""
        <div class="head-title">El Final de la Historia: El Resto</div>
        <p class="sub-text">Observa el número que queda al final de la división (se llama <b class="hl">resto</b>).</p>
        <div style="display:flex; justify-content:space-around; width:100%; gap:20px;">
            <div class="pnl-border stp" style="border-color:#9DE3BD; width:48%;">
                <h3 style="margin-bottom:15px; color:#047857;">División Exacta ✔️</h3>
                <div class="alg-container" style="font-size:32px; margin-bottom:15px; padding:15px;">
                    <div class="alg-row"><span>68 : 4 = 17</span></div>
                    <div class="alg-row"><span style="color:#b91c1c;">-4</span></div>
                    <div class="alg-line"></div>
                    <div class="alg-row"><span>28</span></div>
                    <div class="alg-row"><span style="color:#b91c1c;">-28</span></div>
                    <div class="alg-line"></div>
                    <div class="alg-row"><span>0</span></div>
                </div>
                <div class="mini-chip" style="background:#D1FAE5; border-color:#059669; font-size:18px;">Resto = 0 (No sobró nada)</div>
            </div>
            <div class="pnl-border stp" style="border-color:#FFB74D; width:48%;">
                <h3 style="margin-bottom:15px; color:#e65100;">División Inexacta ⚠️</h3>
                <div class="alg-container" style="font-size:32px; margin-bottom:15px; padding:15px;">
                    <div class="alg-row"><span>38 : 5 = 7</span></div>
                    <div class="alg-row"><span style="color:#b91c1c;">-35</span></div>
                    <div class="alg-line"></div>
                    <div class="alg-row"><span>3</span></div>
                </div>
                <div class="mini-chip" style="background:#FEF3C7; border-color:#D97706; font-size:18px;">Resto = 3 (Sobran elementos)</div>
            </div>
        </div>
    """)

    # 6. La regla de oro del resto
    slide(f"""
        <div class="head-title">La regla de oro del resto 🥇</div>
        <div class="pnl-border" style="background:linear-gradient(135deg,#fff7e8 0%,#f4fff8 50%,#faf4ff 100%);">
            <div style="font-size:100px;">🕵️‍♂️</div>
            <div class="math-eq" style="font-size:36px; text-align:center;">El <b>RESTO</b> siempre, siempre, siempre debe ser <span style="color:#b91c1c;">MENOR</span> que el divisor.</div>
            <div class="stp" style="margin-top:20px;">
                <p style="font-size:24px; text-align:center;">Si estás dividiendo por 5, lo que te sobra solo puede ser <b>0, 1, 2, 3 o 4</b>. ¡Nunca te pueden sobrar 5 o más!</p>
            </div>
            <div class="stp" style="margin-top:20px; background:#FF9D9D; padding:10px; border-radius:10px; color:white;">
                <p style="font-size:20px; text-align:center;">Si te sobra algo más grande que el divisor... significa que el número cabía otra vez y te equivocaste en el Paso 2.</p>
            </div>
        </div>
    """)

    # 7. Abre tu cuaderno: Exacta
    slide(f"""
        <div class="head-title" style="background:#1976D2;">Abre tu cuaderno 📓</div>
        <div class="pnl-border" style="border-color:#1976D2;">
            <p style="font-size:32px; font-weight:800; margin-bottom:20px;">Intenta resolver esta división exacta usando "La Casita":</p>
            <div class="math-eq" style="font-size:64px;">72 ÷ 3 = ?</div>
            <div class="stp" style="display:flex; justify-content:center; width:100%; margin-top:20px;">
                <div class="alg-container" style="border-color:#047857; background:#f4fff7;">
                    <div class="alg-row"><span>7'2</span> <span>: 3 =</span> <span class="hl" style="color:#047857;">24</span></div>
                    <div class="alg-row"><span style="color:#b91c1c;">-6</span></div>
                    <div class="alg-line"></div>
                    <div class="alg-row"><span>12</span></div>
                    <div class="alg-row"><span style="color:#b91c1c;">-12</span></div>
                    <div class="alg-line"></div>
                    <div class="alg-row"><span>0</span></div>
                </div>
            </div>
        </div>
    """)

    # 8. Abre tu cuaderno: Inexacta
    slide(f"""
        <div class="head-title" style="background:#1976D2;">Abre tu cuaderno 📓</div>
        <div class="pnl-border" style="border-color:#1976D2;">
            <p style="font-size:32px; font-weight:800; margin-bottom:20px;">Ahora intenta esta que te dejará un resto:</p>
            <div class="math-eq" style="font-size:64px;">57 ÷ 5 = ?</div>
            <div class="stp" style="display:flex; justify-content:center; width:100%; margin-top:20px;">
                <div class="alg-container" style="border-color:#e65100; background:#fffbf4;">
                    <div class="alg-row"><span>5'7</span> <span>: 5 =</span> <span class="hl" style="color:#e65100;">11</span></div>
                    <div class="alg-row"><span style="color:#b91c1c;">-5</span></div>
                    <div class="alg-line"></div>
                    <div class="alg-row"><span>07</span></div>
                    <div class="alg-row"><span style="color:#b91c1c;">-5</span></div>
                    <div class="alg-line"></div>
                    <div class="alg-row"><span>2</span></div>
                </div>
            </div>
        </div>
    """)

    # 9. El Caso Difícil
    slide(f"""
        <div class="head-title">El Caso Difícil 🚨</div>
        <p class="sub-text">¿Qué pasa si el primer dígito es <b class="hl">menor</b> que el divisor?</p>
        <div style="display:flex; gap:30px; width:100%;">
            <div style="flex:1; display:flex; flex-direction:column; gap:15px;">
                <div class="alg-step-box">Queremos resolver <b>38 : 7</b></div>
                <div class="alg-step-box stp" style="border-color:#FF9D9D;">Paso 1: ¿Puedo separar solo el 3? <b>¡No! 3 es menor que 7.</b></div>
                <div class="alg-step-box stp" style="border-color:#9DE3BD;">Entonces <b>tomo dos dígitos al tiro</b>: Tomo el 38.</div>
                <div class="alg-step-box stp">¿Qué número por 7 se acerca a 38? 7x5=35. ¡Anoto el 5 en el resultado!</div>
            </div>
            <div style="flex:1; display:flex; justify-content:center; align-items:center;">
                <div class="alg-container stp">
                    <div class="alg-row"><span>38'</span> <span>: 7 =</span> <span class="hl" style="color:#047857;">5</span></div>
                    <div class="alg-row stp"><span style="color:#b91c1c;">-35</span></div>
                    <div class="alg-line stp"></div>
                    <div class="alg-row stp"><span>3</span></div>
                </div>
            </div>
        </div>
    """)

    # 10. Otro ejemplo del Caso Difícil
    slide(f"""
        <div class="head-title">Abre tu cuaderno: Caso Difícil 📓</div>
        <div class="pnl-border" style="border-color:#1976D2;">
            <p style="font-size:32px; font-weight:800; margin-bottom:20px;">Resuelve <b>45 ÷ 6</b> en tu cuaderno.</p>
            <div class="stp" style="width:100%; text-align:center;">
                <div class="mini-chip" style="margin-bottom:15px;">Pista: El 4 es menor que el 6, ¡toma los dos juntos!</div>
            </div>
            <div class="stp" style="display:flex; justify-content:center; width:100%; margin-top:20px;">
                <div class="alg-container" style="border-color:#1C4A82;">
                    <div class="alg-row"><span>45'</span> <span>: 6 =</span> <span class="hl" style="color:#1C4A82;">7</span></div>
                    <div class="alg-row"><span style="color:#b91c1c;">-42</span></div>
                    <div class="alg-line"></div>
                    <div class="alg-row"><span>3</span></div>
                </div>
            </div>
        </div>
    """)

    # 11. La Comprobación
    slide(f"""
        <div class="head-title">La Comprobación ✔️</div>
        <p class="sub-text">¿Cómo sé si mi división quedó buena y no me equivoqué?</p>
        <div class="pnl-border" style="border-color:#9DDEFF; background:#f4f9ff;">
            <div class="math-eq" style="font-size:42px;">(Cociente × Divisor) + Resto = Dividendo</div>
            <div class="stp" style="width:100%; display:flex; justify-content:space-around; margin-top:30px;">
                <div class="alg-container" style="font-size:28px;">
                    <div class="alg-row"><span>38 : 7 = 5</span></div>
                    <div class="alg-row"><span style="color:#b91c1c;">-35</span></div>
                    <div class="alg-line"></div>
                    <div class="alg-row"><span>3</span></div>
                </div>
                <div class="alg-container stp" style="font-size:32px; border-color:#047857; background:#D1FAE5;">
                    <div class="alg-row" style="color:#047857;"><span>(5 × 7) + 3</span></div>
                    <div class="alg-row" style="color:#047857;"><span>35 + 3 = 38</span></div>
                    <div class="alg-row" style="color:#047857;"><span>¡Correcto!</span></div>
                </div>
            </div>
        </div>
    """)

    # 12. Estimación
    slide(f"""
        <div class="head-title">Estimación de Cuocientes</div>
        <p class="sub-text">Antes de calcular exacto, estimar nos ayuda a no cometer errores horribles.</p>
        <div class="story-card" style="border:5px solid #FFE082;">
            <div class="story-emoji">🤔</div>
            <div>
                <h2 style="color:#e65100; font-size:32px;">Estimar 92 : 4</h2>
                <div class="stp" style="margin-top:15px;">
                    <p style="font-size:24px;">Redondeo el 92 a una decena más fácil... por ejemplo 80.</p>
                </div>
                <div class="stp" style="margin-top:15px;">
                    <p style="font-size:24px;"><b>80 : 4 = 20</b>. ¡El resultado real debe ser un poco mayor a 20!</p>
                </div>
                <div class="stp" style="margin-top:15px; background:#fff; padding:15px; border-radius:10px; border-left:5px solid #FFB74D;">
                    <p style="font-size:24px; font-weight:800; color:#e65100;">Calculamos exacto: 92 : 4 = 23. ¡Nuestra estimación funcionó, 23 está cerca de 20!</p>
                </div>
            </div>
        </div>
    """)

    # 13. Detección de error
    slide(f"""
        <div class="head-title" style="background:#e53935;">¡Encuentra el Error! 🚨</div>
        <div class="story-card" style="border:5px solid #FF9D9D;">
            <div class="story-emoji">🤷‍♂️</div>
            <div>
                <h2 style="color:#b91c1c; font-size:32px;">Lucas resolvió 73 ÷ 5</h2>
                <p style="font-size:24px;">Lucas hizo el algoritmo y obtuvo <b>Cociente 13 y Resto 8</b>.</p>
                <div class="stp" style="margin-top:15px;">
                    <p style="font-size:24px; font-weight:800; color:#047857;">¿Es esto posible según la regla de oro? ¿Cuál fue su error?</p>
                </div>
                <div class="stp" style="margin-top:15px; background:#D1FAE5; padding:15px; border-radius:10px;">
                    <p style="font-size:22px; font-weight:700;">¡Imposible! El resto (8) no puede ser mayor al divisor (5). Significa que le cabía una vez más. Lo correcto es Cociente 14 y Resto 3.</p>
                </div>
            </div>
        </div>
    """)

    # 14. Preparando Bloque 3
    slide(f"""
        <div class="head-title">¡Hora de entrenar en La Casita!</div>
        <p class="sub-text">A continuación, enfrentarás 6 ejercicios en tu cuaderno.</p>
        <div class="fact-grid">
            <div class="fact-box stp" style="border-color:#FFE082;">
                <h4>Exactas</h4>
                <p>Terminarán en un hermoso y redondo cero (0).</p>
            </div>
            <div class="fact-box stp" style="border-color:#9DE3BD;">
                <h4>Inexactas</h4>
                <p>Te sobrará algo. No olvides escribir tu resto.</p>
            </div>
            <div class="fact-box stp" style="border-color:#E1BEE7;">
                <h4>Caso Difícil</h4>
                <p>Ojo con el primer dígito. Si es muy chico, tómalos los dos de inmediato.</p>
            </div>
        </div>
    """)

    # 15. BLOQUE 3 - Misión de Entrenamiento
    slide(f"""
        <div class="head-title" style="background:#F57C00;">Misión de Entrenamiento ✍️</div>
        <p class="sub-text">Copia en tu cuaderno y resuelve usando el algoritmo de la casita.</p>
        <div style="display:grid; grid-template-columns: 1fr 1fr; gap:15px; width:100%;">
            <div class="pnl-border" style="display:flex; justify-content:space-between; align-items:center; padding:15px; border-color:#FF9D9D;">
                <div style="font-size:26px; font-weight:900;">1) 72 ÷ 4 =</div>
                <div style="font-size:26px; font-weight:900; color:#b91c1c; border-bottom:3px solid #b91c1c; width:120px; text-align:center;">?</div>
            </div>
            <div class="pnl-border" style="display:flex; justify-content:space-between; align-items:center; padding:15px; border-color:#FF9D9D;">
                <div style="font-size:26px; font-weight:900;">2) 84 ÷ 2 =</div>
                <div style="font-size:26px; font-weight:900; color:#b91c1c; border-bottom:3px solid #b91c1c; width:120px; text-align:center;">?</div>
            </div>
            <div class="pnl-border" style="display:flex; justify-content:space-between; align-items:center; padding:15px; border-color:#FFB74D;">
                <div style="font-size:26px; font-weight:900;">3) 47 ÷ 6 =</div>
                <div style="font-size:26px; font-weight:900; color:#e65100; border-bottom:3px solid #e65100; width:120px; text-align:center;">? r ?</div>
            </div>
            <div class="pnl-border" style="display:flex; justify-content:space-between; align-items:center; padding:15px; border-color:#FFB74D;">
                <div style="font-size:26px; font-weight:900;">4) 53 ÷ 8 =</div>
                <div style="font-size:26px; font-weight:900; color:#e65100; border-bottom:3px solid #e65100; width:120px; text-align:center;">? r ?</div>
            </div>
            <div class="pnl-border" style="display:flex; justify-content:space-between; align-items:center; padding:15px; border-color:#9DDEFF;">
                <div style="font-size:26px; font-weight:900;">5) 45 ÷ 3 =</div>
                <div style="font-size:26px; font-weight:900; color:#1C4A82; border-bottom:3px solid #1C4A82; width:120px; text-align:center;">?</div>
            </div>
            <div class="pnl-border" style="display:flex; justify-content:space-between; align-items:center; padding:15px; border-color:#9DDEFF;">
                <div style="font-size:26px; font-weight:900;">6) 36 ÷ 9 =</div>
                <div style="font-size:26px; font-weight:900; color:#1C4A82; border-bottom:3px solid #1C4A82; width:120px; text-align:center;">?</div>
            </div>
        </div>
    """)

    # 16. Resultados Bloque 3
    slide(f"""
        <div class="head-title" style="background:#047857;">Revisión de la Misión ✔️</div>
        <p class="sub-text">Hazte un check si tus resultados y restos coinciden:</p>
        <div style="display:grid; grid-template-columns: 1fr 1fr; gap:15px; width:100%;">
            <div class="pnl-border stp" style="display:flex; justify-content:center; align-items:center; padding:15px; background:#D1FAE5; border-color:#059669;">
                <div style="font-size:28px; font-weight:900; color:#059669;">1) 18 (Exacta)</div>
            </div>
            <div class="pnl-border stp" style="display:flex; justify-content:center; align-items:center; padding:15px; background:#D1FAE5; border-color:#059669;">
                <div style="font-size:28px; font-weight:900; color:#059669;">2) 42 (Exacta)</div>
            </div>
            <div class="pnl-border stp" style="display:flex; justify-content:center; align-items:center; padding:15px; background:#D1FAE5; border-color:#059669;">
                <div style="font-size:28px; font-weight:900; color:#059669;">3) 7 resto 5</div>
            </div>
            <div class="pnl-border stp" style="display:flex; justify-content:center; align-items:center; padding:15px; background:#D1FAE5; border-color:#059669;">
                <div style="font-size:28px; font-weight:900; color:#059669;">4) 6 resto 5</div>
            </div>
            <div class="pnl-border stp" style="display:flex; justify-content:center; align-items:center; padding:15px; background:#D1FAE5; border-color:#059669;">
                <div style="font-size:28px; font-weight:900; color:#059669;">5) 15</div>
            </div>
            <div class="pnl-border stp" style="display:flex; justify-content:center; align-items:center; padding:15px; background:#D1FAE5; border-color:#059669;">
                <div style="font-size:28px; font-weight:900; color:#059669;">6) 4 (Difícil)</div>
            </div>
        </div>
    """)

    # 17. Quiz Rápido
    quiz_slide(
        "Examen Ninja Rápido 🥷",
        "Sin calcular exacto, si divido 48 ÷ 6. ¿Será exacta o inexacta?",
        ["Exacta", "Inexacta", "No se puede saber"],
        0,
        "¡Exacta! Porque en la tabla el 6 × 8 da justo 48. El resto es 0."
    )

    # 18. Otro Quiz Rápido
    quiz_slide(
        "Examen Ninja de Reglas 🥷",
        "Si divides por 9, el resto más grande posible que te puede quedar es:",
        ["9", "8", "10"],
        1,
        "¡Perfecto! El resto debe ser estrictamente menor que el divisor."
    )

    # 19. ObraCraft Intro
    slide(f"""
        <div class="head-title" style="background:linear-gradient(90deg, #6a1b9a, #d50000);">Desafío Supremo ⚔️</div>
        <div style="flex:1; display:flex; flex-direction:column; justify-content:center; align-items:center; text-align:center;">
            <h1 style="font-size:64px; color:#4a148c; margin-bottom:20px;">Mundo ObraCraft ⛏️</h1>
            <p style="font-size:28px; font-weight:700; max-width:720px;">Has minado en una caverna profunda y encontraste muchísimos diamantes. Para guardarlos, necesitas usar cofres especiales y te llevarás en los bolsillos lo que te sobre.</p>
            <div style="font-size:120px; margin-top:20px;">💎</div>
            <p class="stp" style="font-size:24px; margin-top:20px; font-weight:800; color:#b91c1c;">¡Usa tu algoritmo de la casita para calcular tu botín!</p>
        </div>
    """)

    # 20. ObraCraft Problema
    slide(f"""
        <div class="head-title" style="background:linear-gradient(90deg, #6a1b9a, #d50000);">Desafío Supremo ⚔️</div>
        <div class="pnl-border" style="border-color:#8E44AD; background:#fdfaff;">
            <div style="font-size:80px; text-align:center;">⛏️</div>
            <p style="font-size:26px; text-align:center; font-weight:700; margin-bottom:20px;">Minaste un bloque gigante y obtuviste <b style="color:#1C4A82;">85 diamantes</b>. Cada cofre mágico tiene capacidad para guardar exactamente <b style="color:#1C4A82;">6 diamantes</b>.</p>
            <div class="stp" style="background:#fff; border:3px dashed #8E44AD; padding:20px; border-radius:15px; width:100%; text-align:center;">
                <p style="font-size:28px; font-weight:900; margin-bottom:10px;">1) ¿Cuántos cofres se llenarán enteros?</p>
                <p style="font-size:28px; font-weight:900; margin-bottom:10px;">2) ¿Cuántos diamantes te sobrarán para llevártelos sueltos en el bolsillo (el resto)?</p>
                <div class="math-eq" style="font-size:40px; margin:0; display:inline-block;">85 ÷ 6 = ?</div>
            </div>
            <div class="stp" style="margin-top:20px; text-align:center;">
                <p style="font-size:24px; font-weight:800; color:#4a148c;">¡Haz la casita en tu cuaderno para descubrir tu premio!</p>
            </div>
        </div>
    """)

    # 21. ObraCraft Solución
    slide(f"""
        <div class="head-title" style="background:linear-gradient(90deg, #6a1b9a, #d50000);">Desafío Supremo ⚔️</div>
        <div style="flex:1; display:flex; gap:40px; justify-content:center; align-items:center;">
            <div style="flex:1; text-align:center;">
                <div style="font-size:120px; margin-bottom:20px;">📦💎</div>
                <h1 style="font-size:44px; color:#4a148c; margin-bottom:20px;">Llenaste 14 cofres enteros</h1>
                <p style="font-size:26px; font-weight:700; color:#e65100;">Y te sobró 1 diamante en tu bolsillo (resto = 1).</p>
            </div>
            <div style="flex:1; display:flex; justify-content:center; align-items:center;">
                <div class="alg-container" style="border-color:#4a148c; background:#fdfaff; font-size:36px;">
                    <div class="alg-row"><span>8'5</span> <span>: 6 =</span> <span class="hl" style="color:#047857;">14</span></div>
                    <div class="alg-row"><span style="color:#b91c1c;">-6</span></div>
                    <div class="alg-line"></div>
                    <div class="alg-row"><span>25</span></div>
                    <div class="alg-row"><span style="color:#b91c1c;">-24</span></div>
                    <div class="alg-line"></div>
                    <div class="alg-row"><span>1</span></div>
                </div>
            </div>
        </div>
    """)

    # 22. Resumen
    slide(f"""
        <div class="head-title">Resumen de la Misión</div>
        <div style="display:flex; flex-direction:column; gap:15px; width:100%;">
            <div class="stp pnl" style="padding:15px; font-size:22px;"><b>1. La Casita:</b> Te sirve para esos números enormes. Los pasos son separar, dividir, multiplicar, restar y bajar.</div>
            <div class="stp pnl" style="padding:15px; font-size:22px;"><b>2. División exacta:</b> El resto es hermoso, siempre es 0.</div>
            <div class="stp pnl" style="padding:15px; font-size:22px;"><b>3. División inexacta:</b> Te sobra cantidad, el resto es siempre mayor a 0 pero menor que el divisor.</div>
            <div class="stp pnl" style="padding:15px; font-size:22px;"><b>4. Comprobación:</b> Multiplicas el resultado por el divisor y le sumas el resto. ¡Debe darte el número inicial!</div>
        </div>
    """)

    # 23. Cierre
    slide(f"""
        <div class="head-title" style="background:#047857;">¡Misión Cumplida!</div>
        <div style="flex:1; display:flex; flex-direction:column; justify-content:center; align-items:center; text-align:center;">
            <p style="font-size:38px; font-weight:800; max-width:780px;">Ahora tienes el poder del algoritmo vertical. Ningún número es demasiado grande para ti si sigues los 5 pasos.</p>
            <div style="font-size:120px; margin-top:30px;">🏠🚀</div>
        </div>
    """)

    html = f"""<!DOCTYPE html>
<html lang="es"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"><title>División Módulo 2</title><style>{css}</style>
<style>
@media print {
    body { overflow: visible !important; height: auto !important; display: block !important; background: white !important; }
    .dk { display: block !important; height: auto !important; max-width: none !important; margin: 0 !important; }
    .sl {
        position: relative !important;
        opacity: 1 !important;
        transform: none !important;
        page-break-after: always;
        page-break-inside: avoid;
        height: 100vh !important;
        max-height: 100vh !important;
        overflow: hidden !important;
        padding: 20px !important;
    }
    .sl.pv, .sl.nx, .sl.on { transform: none !important; opacity: 1 !important; }
    .pb, .nv, .print-btn { display: none !important; }
    * { animation: none !important; transition: none !important; }
}
</style>
</head>
<body><div class="pb" id="pb"></div><div class="dk">{"".join(slides)}</div>
<div class="nv">
    <button class="nb" id="pv" onclick="go(-1)">⬅ Anterior</button>
    <div style="display:flex; flex-direction:column; align-items:center; gap:2px; max-width:200px; width:100%;">
        <span class="sc" id="sc">1 / {len(slides)}</span>
        <input type="range" id="slide-slider" style="width: 100%; cursor: pointer;" min="1" max="{len(slides)}" value="1" oninput="goToSlide(this.value)">
    </div>
    <button class="nb" id="nx" onclick="go(1)">Siguiente ➡</button>
</div>
<script>{js}</script>
<button onclick="window.print()" class="print-btn" style="position:fixed; top:20px; right:20px; background:#1C4A82; color:white; border:none; padding:10px 15px; border-radius:8px; font-family:'Nunito',sans-serif; font-weight:bold; cursor:pointer; z-index:1000; box-shadow:0 4px 6px rgba(0,0,0,0.1);">📄 Descargar PDF</button>
</body></html>"""

    output_dir = '/Users/brunonattino/Desktop/PAGINA TUTORIAS/clases/cuarto-basico/division'
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, 'division_2.html')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Módulo 2 de división generado: {len(slides)} slides en {output_path}")

if __name__ == '__main__':
    generate_html()
