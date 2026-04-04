def generate_html():
    css = """
    @import url('https://fonts.googleapis.com/css2?family=Nunito:wght@600;800;900&display=swap');
    :root {--base: #1C4A82; --bg: #f5f6f8; --tx: #333;}
    * {margin:0; padding:0; box-sizing:border-box;}
    body {font-family: 'Nunito', sans-serif; background: var(--bg); overflow: hidden; height: 100vh; width: 100vw; display: flex; flex-direction: column; align-items: center; color: var(--tx);}
    .dk {position: relative; width: 100%; height: 100%; max-width: 1000px; display: flex;}
    
    .sl {position: absolute; inset: 0; display: flex; flex-direction: column; align-items: center; justify-content: flex-start; padding: 40px; opacity: 0; transform: scale(.96); transition: opacity .4s, transform .4s; pointer-events: none; z-index: 1;}
    .sl.on {opacity: 1; transform: scale(1); pointer-events: auto; z-index: 10;}
    .sl.pv {opacity: 0; transform: translateX(-50px) scale(.95);}
    .sl.nx {opacity: 0; transform: translateX(50px) scale(.95);}
    
    .head-title {background: var(--base); color: white; padding: 10px 40px; font-size: 32px; font-weight: 900; margin-bottom: 30px; display: inline-block; border-radius: 12px; text-align:center;}
    .sub-text {font-size: 26px; font-weight: 600; margin-bottom: 25px; text-align: center;}
    
    /* Navigation */
    .pb {position: fixed; top: 0; left: 0; height: 6px; background: var(--base); transition: width .4s; z-index: 100;}
    .nv {position: fixed; bottom: 0; left: 0; right: 0; height: 60px; background: white; border-top: 1px solid #ddd; display: flex; align-items: center; justify-content: space-between; padding: 0 40px; z-index: 100;}
    .nb {background: #eee; color: var(--base); border: none; padding: 10px 20px; border-radius: 8px; font-family: 'Nunito', sans-serif; font-size: 16px; font-weight: 900; cursor: pointer; transition: all .2s;}
    .nb:hover {background: #ddd;}
    .nb:disabled {opacity: 0.3; cursor: not-allowed;}
    .sc {color: #888; font-size: 16px; font-weight: 900;}
    
    /* Steps Engine */
    .stp {opacity: 0; transform: translateY(20px); transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1); pointer-events: none;}
    .stp.shwn {opacity: 1; transform: translateY(0); pointer-events: auto;}
    
    .pnl {background: #fff; padding: 30px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); border: 3px solid #eaeaea; width: 100%; margin-bottom: 20px;}
    .pnl-border {background: #fff; border: 4px solid var(--base); border-radius: 20px; padding: 30px; display: flex; flex-direction: column; align-items: center;}
    .hl {color: var(--base); font-weight: 900;}
    .btn {background: var(--base); color: white; border: none; padding: 14px 28px; border-radius: 12px; font-size: 20px; font-weight: 900; cursor: pointer; transition: transform .2s;}
    .btn:hover {transform: translateY(-2px); box-shadow: 0 4px 12px rgba(28,74,130,0.3);}
    .math-eq {font-size: 48px; font-weight: 900; color: var(--base); background: #fff; padding: 10px 30px; border-radius: 20px; box-shadow: 0 8px 20px rgba(0,0,0,0.1); border: 3px dashed #bbdefb; margin: 15px;}
    """
    
    js = """
    const S=document.querySelectorAll('.sl'); let c=0; const T=S.length;
    function ui() {
        S.forEach((s,i)=>{ s.classList.remove('on','pv','nx'); if(i===c) s.classList.add('on'); else if(i<c) s.classList.add('pv'); else s.classList.add('nx'); });
        document.getElementById('pb').style.width=((c+1)/T*100)+'%'; document.getElementById('sc').textContent=`${c+1} / ${T}`;
        document.getElementById('pv').disabled=c===0; document.getElementById('nx').disabled=c===T-1;
    }
    function go(d) {
        if(d>0) { const hid = S[c].querySelectorAll('.stp:not(.shwn)'); if(hid.length > 0) { hid[0].classList.add('shwn'); return; } }
        else { const shw = S[c].querySelectorAll('.stp.shwn'); if(shw.length > 0) { shw[shw.length-1].classList.remove('shwn'); return; } }
        const n=c+d; if(n>=0 && n<T) { c=n; ui(); }
    }
    document.addEventListener('keydown', e => { if(e.key==='ArrowRight' || e.key===' ') go(1); if(e.key==='ArrowLeft') go(-1); });
    ui();
    function chkAns(btn, correct) {
        let p = btn.parentElement; let msg = btn.closest('.sl').querySelector('.msg-area');
        for (let b of p.children) b.style.transform = 'scale(1)';
        if (correct) { btn.style.background = '#047857'; btn.style.transform = 'scale(1.1)'; msg.innerHTML = '¡Excelente! ✅ ¡Lo lograste!'; msg.style.color = '#047857'; }
        else { btn.style.background = '#b91c1c'; let frases = ["¡Sigue intentándolo! 💪", "Usa tus estrategias 🧐", "¡Casi! Intentemos de nuevo 🚀"]; msg.innerHTML = frases[Math.floor(Math.random()*frases.length)]; msg.style.color = '#b91c1c'; }
    }
    """
    
    slides = []
    def slide(html): slides.append(f'<div class="sl">{html}</div>')
    
    # 1. INTRO
    slide(f"""
        <div style="flex:1; display:flex; flex-direction:column; justify-content:center; align-items:center;">
            <h1 style="font-size: 70px; color: var(--base); margin-bottom: 20px; text-align:center;">¡Multiplicaciones 2!</h1>
            <p class="sub-text">Los Maestros de las Tablas 💡</p>
            <p style="font-size:100px; margin-top:30px; animation: bounce 2s infinite;">🥷</p>
            <style>@keyframes bounce {{ 0%, 100%{{transform:translateY(0);}} 50%{{transform:translateY(-20px);}} }}</style>
        </div>
    """)
    
    # --- TABLA DEL 3 ---
    slide(f"""
        <div class="head-title">La Tabla del 3</div>
        <p class="sub-text">Multiplicar por 3 es calcular el <b style="color:var(--base);">TRIPLE</b>.</p>
        <div style="display:flex; justify-content:center; gap:20px; font-size:100px; margin:20px 0;">
            🐾 🐾 🐾
        </div>
        <div class="stp pnl" style="font-size:28px; text-align:center; border: 4px solid #FF9D9D;">
            <p style="margin-bottom:15px;">Si tenemos <b class="hl">4 perros</b>, el triple sería sumar 4 + 4 + 4.</p>
            <div class="math-eq stp">3 x 4 = 12</div>
        </div>
    """)
    
    def multi_practice(title, ops):
        # ops = [(eq, ans), (eq, ans)]
        rows = ""
        for eq, ans in ops:
            rows += f'<div class="stp math-eq" style="width:400px; display:flex; justify-content:space-between; padding:20px 40px;"><span>{eq} =</span> <span class="stp hl">{ans}</span></div>'
        return f"""
        <div class="head-title" style="background:#F57C00;">Abre tu cuaderno: {title}</div>
        <p class="sub-text">Calcula el resultado...</p>
        <div style="display:flex; flex-direction:column; gap:20px; align-items:center; width:100%; margin-top:20px;">
            {rows}
        </div>
        """

    slide(multi_practice("Tabla del 3", [("3 x 3", "9"), ("3 x 5", "15"), ("3 x 7", "21")]))

    # --- TABLA DEL 4 ---
    slide(f"""
        <div class="head-title">La Tabla del 4</div>
        <p class="sub-text">¡El 4 es amigo del 2! Es el <b style="color:var(--base);">Doble del Doble</b>.</p>
        
        <div class="pnl-border" style="background:#e3f2fd; border-color:#0288D1; margin-top:10px;">
            <p style="font-size:28px; font-weight:800; text-align:center;">Queremos calcular <b style="font-size:36px; color:#c2185b;">4 x 6</b></p>
            
            <div class="stp" style="margin-top:20px; font-size:24px; text-align:center;">
                <b class="hl">Paso 1:</b> El doble de 6 es <b style="font-size:32px;">12</b>.<br>
                <span style="font-size:20px; color:#666;">(Eso es 2 x 6)</span>
            </div>
            
            <div class="stp" style="margin-top:20px; font-size:24px; text-align:center;">
                <b class="hl">Paso 2:</b> ¡Calculamos el doble de ese resultado!<br>
                El doble de 12 es <b style="font-size:40px; color:#047857;">24</b>.
            </div>
            
            <div class="math-eq stp" style="margin-top:20px;">4 x 6 = 24</div>
        </div>
    """)
    
    slide(multi_practice("Tabla del 4", [("4 x 4", "16"), ("4 x 7", "28"), ("4 x 9", "36")]))

    # --- TABLA DEL 6 ---
    slide(f"""
        <div class="head-title">La Tabla del 6</div>
        <p class="sub-text">El 6 es igual a calcular la tabla del 5... ¡y sumarle uno más!</p>
        
        <div style="display:flex; flex-direction:column; align-items:center; width:100%;">
            <div class="stp math-eq" style="font-size:40px; background:#f9fbff;">
                Si sabemos que <span class="hl">6 x 4</span>...
            </div>
            
            <div class="stp pnl" style="border: 4px dashed #9DE3BD; width:80%; text-align:center; margin-top:20px; font-size:28px;">
                Cálculo fácil con 5:<br>
                <b>5 x 4 = 20</b>
            </div>
            
            <div class="stp pnl" style="border: 4px dashed #FF9D9D; width:80%; text-align:center; font-size:28px;">
                Le sumamos "un 4" más:<br>
                <b>20 + 4 = 24</b>
            </div>
            
            <div class="stp math-eq" style="border-color:var(--base); color:#047857;">¡6 x 4 = 24!</div>
        </div>
    """)
    
    slide(multi_practice("Tabla del 6", [("6 x 5", "30"), ("6 x 6", "36"), ("6 x 8", "48")]))

    # --- TABLA DEL 7 ---
    slide(f"""
        <div class="head-title">La Tabla del 7</div>
        <p class="sub-text">Siete, como los días de la semana. 📅</p>
        <div style="font-size:80px; margin:10px 0; display:flex; gap:20px;">☀️ 🌙 ☀️ 🌙 ☀️ 🌙 ☀️</div>
        
        <div class="stp pnl-border" style="background:#fff0f5; border-color:#c2185b; margin-top:10px; font-size:28px; text-align:center;">
            Aquí la memoria es la clave.<br>Un clásico muy conocido es el:<br>
            <div style="font-size:56px; font-weight:900; color:#c2185b; margin-top:15px;">7 x 7 = 49</div>
        </div>
        <div class="stp" style="font-size:24px; text-align:center; margin-top:20px; font-weight:800;">
            Si conocemos ese, ¿Cuánto es 7x8?<br>
            ¡Simplemente le sumamos 7 a 49! ➔ <span style="font-size:36px; color:#047857;">56</span>
        </div>
    """)

    slide(multi_practice("Tabla del 7", [("7 x 3", "21"), ("7 x 5", "35"), ("7 x 9", "63")]))

    # --- TABLA DEL 8 ---
    slide(f"""
        <div class="head-title">La Tabla del 8</div>
        <p class="sub-text">La araña multiplicadora 🕷️</p>
        
        <div class="stp pnl" style="border: 4px solid var(--base); display:flex; align-items:center; gap:40px;">
            <div style="font-size:100px;">🕷️</div>
            <div style="font-size:26px;">
                Las arañas tienen 8 patas.<br><br>
                El 8 es el <b>doble del 4</b>.<br>
                Si quieres calcular <b class="hl">8 x 6</b>, puedes pensar en <b class="hl">4 x 6 (24)</b> y sacarle el doble = <b style="color:#047857; font-size:36px;">48</b>.
            </div>
        </div>
    """)

    # --- TABLA DEL 9 ---
    slide(f"""
        <div class="head-title">La Magia del 9</div>
        <p class="sub-text">La tabla del 9 esconde un truco increíble con las manos.</p>
        <div style="font-size:100px; padding:20px;">🤲</div>
        <div class="stp pnl-border" style="font-size:24px; text-align:center; border-color:#F57C00;">
            Extiende tus 10 dedos. Si quieres multiplicar <b class="hl">9 x 4</b>,<br>esconde el dedo número 4 contando desde la izquierda.<br><br>
            <div class="stp" style="margin-top:15px;">Te quedan <b>3</b> dedos a la izquierda (decenas = 30)<br>y <b>6</b> dedos a la derecha (unidades = 6).</div>
            <div class="stp math-eq" style="font-size:50px; margin-top:20px;">= 36!</div>
        </div>
    """)

    slide(multi_practice("Tabla del 9", [("9 x 3", "27"), ("9 x 7", "63"), ("9 x 8", "72")]))

    # --- QUIZZES Y PROBLEMAS ---
    quizzes = [
        ("¿Cuánto es 4 x 8?", ["28", "32", "36"], "32"),
        ("Si usamos la regla del 'doble del doble', ¿qué número multiplicamos?", ["Tabla del 3", "Tabla del 6", "Tabla del 4"], "Tabla del 4"),
        ("¿Cuál es el resultado de 7 x 6?", ["42", "48", "36"], "42"),
        ("La tabla del 6 es calcular la del 5... ¿y luego qué?", ["Le sumo 1", "Le sumo el otro factor", "Le resto 1"], "Le sumo el otro factor"),
        ("¡Desafío! 9 x 9 =", ["81", "72", "99"], "81")
    ]
    
    for q_idx, q in enumerate(quizzes):
        question, options, correct_ans = q
        btns = ""
        for opt in options:
            is_corr = 'true' if opt == correct_ans else 'false'
            btns += f"<button class='btn' style='font-size:24px; padding:20px; flex:1;' onclick='chkAns(this, {is_corr})'>{opt}</button>"
            
        slide(f"""
        <div class="head-title">Examen Ninja 🥷 ({q_idx+1}/{len(quizzes)})</div>
        <div class="pnl-border" style="width:100%; border-color:#d63384; background:#FFF3E0;">
            <p style="font-size:32px; font-weight:800; text-align:center; margin-bottom:40px;">{question}</p>
            <div style="display:flex; justify-content:center; gap:20px; width:100%; margin-bottom:20px;">
                {btns}
            </div>
            <div class="msg-area" style="font-size:26px; font-weight:900; height:40px; margin-top:20px; text-align:center;"></div>
        </div>
        """)

    problemas = [
        ("Cajas de Zapatos", "En una zapatería hay <b>6 estantes</b>. En cada estante caben <b>8 cajas</b>. ¿Cuántas cajas hay?", "6 x 8 = <br><span style='font-size:46px; color:var(--base);'>48 cajas</span>", "👟", "#E3F2FD", "#1976D2"),
        ("Ramos de Flores", "Para el día de la madre, compramos <b>9 ramos</b> con <b>5 flores</b> cada uno. ¿Cuántas flores son?", "9 x 5 = <br><span style='font-size:46px; color:var(--base);'>45 flores</span>", "💐", "#FCE4EC", "#C2185B")
    ]
    
    for tit, prob, ans, emoji, bg, border in problemas:
        slide(f"""
        <div class="head-title">Resolución de Problemas 🧩</div>
        <div style="background:{bg}; border: 5px solid {border}; border-radius: 40px; padding:40px; display:flex; gap:40px; align-items:center; width:100%;">
            <div style="font-size:120px; animation: pulse 2s infinite;">{emoji}</div>
            <div style="flex:1;">
                <h2 style="font-size:32px; color:{border}; margin-bottom:15px;">{tit}</h2>
                <p style="font-size:26px; font-weight:600; line-height:1.4;">{prob}</p>
                
                <div class="stp" style="margin-top:20px; background:#fff; padding:20px; border-radius:20px; border-left: 10px solid {border}; box-shadow: 0 10px 20px rgba(0,0,0,0.05);">
                    <p style="font-size:22px; font-weight:800; color:#555;">La respuesta es:</p>
                    <div style="font-size:32px; font-weight:900; margin-top:10px;">{ans}</div>
                </div>
            </div>
        </div>
        <style>@keyframes pulse {{ 0% {{ transform: scale(1); }} 50% {{ transform: scale(1.1); }} 100% {{ transform: scale(1); }} }}</style>
        """)

    slide(f"""
        <div class="head-title" style="background: var(--base);">📋 Resumen de Maestros</div>
        <div style="display:flex; flex-direction:column; gap:20px; width:100%;">
            <div class="stp pnl" style="padding:15px; font-size:20px;"><b>Tabla del 3:</b> El triple.</div>
            <div class="stp pnl" style="padding:15px; font-size:20px;"><b>Tabla del 4:</b> El Doble del Doble.</div>
            <div class="stp pnl" style="padding:15px; font-size:20px;"><b>Tabla del 6:</b> Calcular x5 y agregar una vez más.</div>
            <div class="stp pnl" style="padding:15px; font-size:20px;"><b>Tabla del 8:</b> El doble de la tabla del 4.</div>
            <div class="stp pnl" style="padding:15px; font-size:20px;"><b>Tabla del 9:</b> Puedes usar el increíble truco de las manos. 🤲</div>
        </div>
    """)
    
    slide(f"""
        <div class="head-title" style="background: #047857;">🏆 ¡Tablas Dominadas!</div>
        <div style="font-size:36px; font-weight:800; text-align:center; margin-top:30px; line-height:1.5;">
            ¡Eres un experto multiplicador!<br>Recuerda practicar constantemente para no olvidarlas.
        </div>
        <div style="font-size:120px; margin-top:50px; animation: bounce 2s infinite;">🎉</div>
    """)

    html = f"""<!DOCTYPE html>
<html lang="es"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"><title>Multiplicación 2 - Interactivo</title><style>{css}</style></head>
<body><div class="pb" id="pb"></div><div class="dk">{"".join(slides)}</div>
<div class="nv"><button class="nb" id="pv" onclick="go(-1)">⬅ Anterior</button><div class="sc" id="sc">1 / {len(slides)}</div><button class="nb" id="nx" onclick="go(1)">Siguiente ➡</button></div>
<script>{js}</script></body></html>"""
    
    output_path = '/Users/brunonattino/Desktop/PAGINA TUTORIAS/SLIDES/multiplicaciones HTMLS/multiplicaciones_2.html'
    with open(output_path, 'w', encoding='utf-8') as f: f.write(html)
    print(f"Módulo 2 generado: {len(slides)} slides.")

if __name__ == '__main__':
    generate_html()
