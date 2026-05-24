def generate_html():
    css = """
    @import url('https://fonts.googleapis.com/css2?family=Nunito:wght@600;800;900&display=swap');
    :root {--base: #1C4A82; --bg: #f5f6f8; --tx: #333;}
    * {margin:0; padding:0; box-sizing:border-box;}
    body {font-family: 'Nunito', sans-serif; background: var(--bg); overflow: hidden; height: 100vh; width: 100vw; display: flex; flex-direction: column; align-items: center; color: var(--tx);}
    .dk {position: relative; width: 100%; height: 100%; max-width: 1000px; display: flex;}
    
    .sl {position: absolute; inset: 0; display: flex; flex-direction: column; align-items: center; justify-content: flex-start; padding: 36px 40px 82px; opacity: 0; transform: scale(.96); transition: opacity .4s, transform .4s; pointer-events: none; z-index: 1;}
    .sl.on {opacity: 1; transform: scale(0.9); pointer-events: auto; z-index: 10;}
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

    # INTRODUCCIÓN GENERAL
    slide(f"""
        <div class="head-title" style="background:#F57C00;">El Siguiente Nivel</div>
        <div style="display:flex; gap:40px; align-items:center; width:100%; height:100%;">
            <div style="font-size:120px; animation: bounce 3s infinite;">🧠</div>
            <div style="flex:1;">
                <p style="font-size:28px; font-weight:800; margin-bottom:20px;">
                    Ya dominas las tablas básicas. Ahora necesitamos estrategias para números más grandes.
                </p>
                <div class="stp pnl" style="border-left:8px solid #F57C00;">
                    <p style="font-size:24px;">En vez de memorizar de memoria todas las tablas difíciles...</p>
                    <p style="font-size:26px; margin-top:10px; font-weight:900; color:#047857;">¡Aprenderemos "Estrategias Mentales" de Ninjas!</p>
                </div>
            </div>
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
    
    # --- TABLA DEL 4 ---
    slide(f"""
        <div class="head-title" style="background:#F57C00;">¿Qué pasa si duplicamos el doble?</div>
        <div style="display:flex; gap:40px; align-items:center; width:100%; height:100%;">
            <div style="font-size:120px; animation: bounce 3s infinite;">👯‍♂️</div>
            <div style="flex:1;">
                <p style="font-size:28px; font-weight:800; margin-bottom:20px;">
                    Ya eres experto calculando el doble (multiplicar por 2).
                </p>
                <div class="stp pnl" style="border-left:8px solid #F57C00;">
                    <p style="font-size:24px;">Imagina que calculas el doble de un número...</p>
                    <p style="font-size:24px; margin-top:10px;">¡Y luego a ese resultado le calculas el doble de nuevo!</p>
                    <p style="font-size:26px; margin-top:10px; font-weight:900; color:#047857;">Esta súper técnica se llama "Doble del Doble" y es el secreto de la tabla del 4.</p>
                </div>
            </div>
        </div>
    """)
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

    # --- ESTRATEGIA DOBLAR Y DIVIDIR POR 2 ---
    slide(f"""
        <div class="head-title" style="background:#9333EA;">Una Estrategia Secreta</div>
        <div style="display:flex; gap:40px; align-items:center; width:100%; height:100%;">
            <div style="font-size:120px; animation: bounce 3s infinite;">⚖️</div>
            <div style="flex:1;">
                <p style="font-size:28px; font-weight:800; margin-bottom:20px;">
                    ¿Qué pasa si a un factor lo partes por la mitad, y al otro lo multiplicas por 2?
                </p>
                <div class="stp pnl" style="border-left:8px solid #9333EA;">
                    <p style="font-size:26px; font-weight:900; color:#047857;">¡El resultado final se mantiene exactamente igual!</p>
                    <p style="font-size:24px; margin-top:10px;">A esto le llamamos la técnica de "Doblar y Dividir por 2".</p>
                </div>
            </div>
        </div>
    """)

    slide(f"""
        <div class="head-title" style="background:#9333EA;">Doblar y Dividir por 2</div>
        <p class="sub-text">Sirve para transformar una multiplicación difícil en una muy fácil.</p>
        <div class="pnl-border" style="border-color:#9333EA; background:#F3E8FF;">
            <p style="font-size:36px; font-weight:800; text-align:center;">Tenemos <b style="color:#c2185b;">12 x 4</b></p>
            
            <div style="display:flex; justify-content:center; gap:60px; margin-top:30px; width:100%;">
                <div class="stp" style="text-align:center;">
                    <p style="font-size:24px; font-weight:900; color:#0288D1;">La mitad de 12</p>
                    <div style="font-size:40px; margin-top:10px;">⬇️</div>
                    <div class="math-eq" style="color:#0288D1; font-size:48px;">6</div>
                </div>
                
                <div class="stp" style="font-size:50px; font-weight:900; align-self:center;">X</div>
                
                <div class="stp" style="text-align:center;">
                    <p style="font-size:24px; font-weight:900; color:#c2185b;">El doble de 4</p>
                    <div style="font-size:40px; margin-top:10px;">⬇️</div>
                    <div class="math-eq" style="color:#c2185b; font-size:48px;">8</div>
                </div>
            </div>
            
            <div class="stp math-eq" style="margin-top:30px; font-size:48px; background:#fff; color:#047857;">
                ¡6 x 8 = 48!
            </div>
            <p class="stp" style="font-size:24px; margin-top:10px;">(Por lo tanto, 12 x 4 también es 48)</p>
        </div>
    """)

    # --- QUIZZES Y PROBLEMAS ---
    quizzes = [
        ("¿Cuánto es 4 x 8?", ["28", "32", "36"], "32")
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

    # --- BLOQUE 3: EJERCICIOS PROPUESTOS (6 EJERCICIOS) ---
    slide(f"""
        <div class="head-title" style="background:#F57C00;">Misión de Entrenamiento ✍️</div>
        <p class="sub-text">¡Saca tu cuaderno! Resuelve estos 6 desafíos.</p>
        <div style="display:grid; grid-template-columns:1fr 1fr 1fr; grid-template-rows:1fr 1fr; gap:20px; width:100%;">
            <!-- Mecánicos -->
            <div style="background:#FFF9C4; border:4px solid #FBC02D; border-radius:15px; padding:15px; display:flex; flex-direction:column; align-items:center; text-align:center;">
                <div style="font-size:16px; font-weight:800; color:#FBC02D; margin-bottom:10px;">Cálculo Rápido</div>
                <div style="font-size:32px; font-weight:900;">6 x 6 = ?</div>
            </div>
            <div style="background:#FFF9C4; border:4px solid #FBC02D; border-radius:15px; padding:15px; display:flex; flex-direction:column; align-items:center; text-align:center;">
                <div style="font-size:16px; font-weight:800; color:#FBC02D; margin-bottom:10px;">Doble del Doble</div>
                <div style="font-size:32px; font-weight:900;">4 x 8 = ?</div>
            </div>
            <!-- Aplicados -->
            <div style="background:#E3F2FD; border:4px solid #0288D1; border-radius:15px; padding:15px; display:flex; flex-direction:column; align-items:center; text-align:center;">
                <div style="font-size:16px; font-weight:800; color:#0288D1; margin-bottom:10px;">Problema</div>
                <div style="font-size:20px; font-weight:900;">Un auto tiene 4 ruedas. ¿Cuántas ruedas hay en 7 autos?</div>
            </div>
            <div style="background:#E3F2FD; border:4px solid #0288D1; border-radius:15px; padding:15px; display:flex; flex-direction:column; align-items:center; text-align:center;">
                <div style="font-size:16px; font-weight:800; color:#0288D1; margin-bottom:10px;">El Mes</div>
                <div style="font-size:20px; font-weight:900;">Una semana tiene 7 días. ¿Cuántos días hay en 4 semanas?</div>
            </div>
            <!-- Creativos -->
            <div style="background:#F3E8FF; border:4px solid #9333EA; border-radius:15px; padding:15px; display:flex; flex-direction:column; align-items:center; text-align:center;">
                <div style="font-size:16px; font-weight:800; color:#9333EA; margin-bottom:10px;">Dato Faltante</div>
                <div style="font-size:32px; font-weight:900;">9 x ? = 81</div>
            </div>
            <div style="background:#F3E8FF; border:4px solid #9333EA; border-radius:15px; padding:15px; display:flex; flex-direction:column; align-items:center; text-align:center;">
                <div style="font-size:16px; font-weight:800; color:#9333EA; margin-bottom:10px;">Dividir por 2</div>
                <div style="font-size:24px; font-weight:900;">14 x 4 es lo mismo que 7 x 8. ¿Verdad o falso?</div>
            </div>
        </div>
    """)

    respuestas_2 = ["36", "32", "28 ruedas", "28 días", "9", "Verdad"]
    res_html_2 = ""
    for i, res in enumerate(respuestas_2):
        res_html_2 += f'''<div class="stp" style="background:#fff; border:4px solid #047857; border-radius:10px; padding:15px; font-size:30px; font-weight:900; text-align:center;">
            <span style="color:#888; font-size:20px; margin-right:10px;">#{i+1}</span> {res}
        </div>'''
        
    slide(f"""
        <div class="head-title" style="background:#047857;">Revisión de la Misión ✅</div>
        <p class="sub-text">Compara tus resultados. Haz un check (✔) en tu cuaderno si está correcta.</p>
        <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:20px; width:100%; margin-top:20px;">
            {res_html_2}
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
<div class="nv">
    <button class="nb" id="pv" onclick="go(-1)">⬅ Anterior</button>
    <div style="display:flex; flex-direction:column; align-items:center; gap:2px; max-width:200px; width:100%;">
        <span class="sc" id="sc">1 / {len(slides)}</span>
        <input type="range" id="slide-slider" style="width: 100%; cursor: pointer;" min="1" max="{len(slides)}" value="1" oninput="goToSlide(this.value)">
    </div>
    <button class="nb" id="nx" onclick="go(1)">Siguiente ➡</button>
</div>
<script>{js}</script></body></html>"""
    
    import os
    output_dir = '/Users/brunonattino/Desktop/PAGINA TUTORIAS/clases/cuarto-basico/multiplicacion'
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, 'multiplicaciones_2.html')
    with open(output_path, 'w', encoding='utf-8') as f: f.write(html)
    print(f"Módulo 2 generado: {len(slides)} slides en {output_path}")

if __name__ == '__main__':
    generate_html()
