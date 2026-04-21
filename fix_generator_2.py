import re
from pathlib import Path

content = Path("scripts/clases/generator_suma_resta.py").read_text()

# 1. SCALE CSS DOWN TO 12px
css_old = r""".unit {
    width: 18px;
    height: 18px;
    border-radius: 4px;
    background: var(--fill, #9DDEFF);
    border: 1px solid rgba(0,0,0,0.25);
}
.rod {
    width: 18px;
    height: 180px;
    border-radius: 4px;
    background: 
        repeating-linear-gradient(0deg, transparent, transparent 17px, rgba(0,0,0,0.2) 17px, rgba(0,0,0,0.2) 18px),
        var(--fill, #9DE3BD);
    border: 1px solid rgba(0,0,0,0.25);
}
.flat {
    width: 180px;
    height: 180px;
    border-radius: 6px;
    background:
        repeating-linear-gradient(0deg, transparent, transparent 17px, rgba(0,0,0,0.15) 17px, rgba(0,0,0,0.15) 18px),
        repeating-linear-gradient(90deg, transparent, transparent 17px, rgba(0,0,0,0.15) 17px, rgba(0,0,0,0.15) 18px),
        var(--fill, #FFE082);
    border: 1px solid rgba(0,0,0,0.25);
}"""

css_new = r""".unit {
    width: 12px;
    height: 12px;
    border-radius: 2px;
    background: var(--fill, #9DDEFF);
    border: 1px solid rgba(0,0,0,0.25);
}
.rod {
    width: 12px;
    height: 120px;
    border-radius: 3px;
    background: 
        repeating-linear-gradient(0deg, transparent, transparent 11px, rgba(0,0,0,0.2) 11px, rgba(0,0,0,0.2) 12px),
        var(--fill, #9DE3BD);
    border: 1px solid rgba(0,0,0,0.25);
}
.flat {
    width: 120px;
    height: 120px;
    border-radius: 4px;
    background:
        repeating-linear-gradient(0deg, transparent, transparent 11px, rgba(0,0,0,0.15) 11px, rgba(0,0,0,0.15) 12px),
        repeating-linear-gradient(90deg, transparent, transparent 11px, rgba(0,0,0,0.15) 11px, rgba(0,0,0,0.15) 12px),
        var(--fill, #FFE082);
    border: 1px solid rgba(0,0,0,0.25);
}"""

content = content.replace(css_old, css_new)

# Cube to 80x100
cube_old = r"""f'<div style="display:inline-block; position:relative; width:100px; height:120px; margin:4px; background:{color}; border:2px solid rgba(0,0,0,0.25); border-radius:8px; box-shadow: 12px -12px 0 rgba(0,0,0,0.1); transform: translateY(12px) translateX(-6px);">'
        f'<div style="position:absolute; inset:0; background:repeating-linear-gradient(0deg, transparent, transparent 11px, rgba(0,0,0,0.1) 11px, rgba(0,0,0,0.1) 12px), repeating-linear-gradient(90deg, transparent, transparent 19px, rgba(0,0,0,0.1) 19px, rgba(0,0,0,0.1) 20px);"></div>'"""
cube_new = r"""f'<div style="display:inline-block; position:relative; width:80px; height:100px; margin:4px; background:{color}; border:2px solid rgba(0,0,0,0.25); border-radius:6px; box-shadow: 8px -8px 0 rgba(0,0,0,0.1); transform: translateY(8px) translateX(-4px);">'
        f'<div style="position:absolute; inset:0; background:repeating-linear-gradient(0deg, transparent, transparent 9px, rgba(0,0,0,0.1) 9px, rgba(0,0,0,0.1) 10px), repeating-linear-gradient(90deg, transparent, transparent 15px, rgba(0,0,0,0.1) 15px, rgba(0,0,0,0.1) 16px);"></div>'"""
content = content.replace(cube_old, cube_new)

# 2. ADD SLIDER HTML
nav_old = r"""<div class="nv">
    <button class="nb" id="pvBtn" onclick="go(-1)" disabled>← Anterior</button>
    <span class="sc" id="sc">1 / ?</span>
    <button class="nb" id="nxBtn" onclick="go(1)">Siguiente →</button>
</div>"""
nav_new = r"""<div class="nv">
    <button class="nb" id="pvBtn" onclick="go(-1)" disabled>← Anterior</button>
    <div style="display:flex; flex-direction:column; align-items:center; gap:2px; max-width:200px; width:100%;">
        <span class="sc" id="sc">1 / ?</span>
        <input type="range" id="slide-slider" style="width: 100%; cursor: pointer;" min="1" max="100" value="1" oninput="goToSlide(this.value)">
    </div>
    <button class="nb" id="nxBtn" onclick="go(1)">Siguiente →</button>
</div>"""
content = content.replace(nav_old, nav_new)

# 3. ADD SLIDER JS
js_old = r"""function showSlide(n) {
        slides[cur].className = 'sl ' + (n > cur ? 'pv' : 'nx');
        cur = n;
        const s = slides[cur];
        s.className = 'sl on';
        s.scrollTop = 0;
        
        // reveal first stp
        const stps = s.querySelectorAll('.stp');
        if (stps.length > 0 && !stps[0].classList.contains('shwn')) {
            stps[0].classList.add('shwn');
        }

        document.getElementById('pvBtn').disabled = cur === 0;
        document.getElementById('nxBtn').disabled = cur === total - 1;
        document.getElementById('sc').textContent = `${cur + 1} / ${total}`;
        document.getElementById('pb').style.width = `${((cur + 1) / total) * 100}%`;
    }"""
js_new = r"""function showSlide(n) {
        slides[cur].className = 'sl ' + (n > cur ? 'pv' : 'nx');
        cur = n;
        const s = slides[cur];
        s.className = 'sl on';
        s.scrollTop = 0;
        
        // reveal first stp
        const stps = s.querySelectorAll('.stp');
        if (stps.length > 0 && !stps[0].classList.contains('shwn')) {
            stps[0].classList.add('shwn');
        }

        document.getElementById('pvBtn').disabled = cur === 0;
        document.getElementById('nxBtn').disabled = cur === total - 1;
        document.getElementById('sc').textContent = `${cur + 1} / ${total}`;
        document.getElementById('pb').style.width = `${((cur + 1) / total) * 100}%`;
        
        let sl = document.getElementById('slide-slider');
        if(sl) { sl.max = total; sl.value = cur + 1; }
    }
    
    function goToSlide(n) {
        let val = parseInt(n) - 1;
        if (val >= 0 && val < total) {
            showSlide(val);
        }
    }"""
content = content.replace(js_old, js_new)

# Make sure slider gets initialized properly in JS
js_init_old = r"""document.getElementById('sc').textContent = `1 / ${total}`;"""
js_init_new = r"""document.getElementById('sc').textContent = `1 / ${total}`;
    let init_sl = document.getElementById('slide-slider');
    if(init_sl) { init_sl.max = total; init_sl.value = 1; }"""
content = content.replace(js_init_old, js_init_new)


# Function to generate an "ejercicios" slide
propuestos_fn = r"""def quiz_slide("""
propuestos_new = r"""def ejercicios_propuestos(titulo: str, subtitulo: str, ejercicios: list[str]) -> str:
    html = f'<div class="head-title">{esc(titulo)}</div>'
    html += f'<p class="sub-text">{esc(subtitulo)}</p>'
    html += '<div class="stp quiz-row" style="flex-direction:column; gap:20px;">'
    for i, ej in enumerate(ejercicios):
        html += f'''
        <div class="pnl-border" style="display:flex; justify-content:space-between; align-items:center; padding:16px;">
            <div style="font-size:28px; font-weight:900; color:var(--base);">{ej} =</div>
            <div class="stp" style="font-size:28px; font-weight:900; color:#059669; border-bottom:3px solid #059669; width:120px; text-align:center;">?</div>
        </div>
        '''
    html += '</div>'
    return html

def ejercicios_respuestas(titulo: str, respuestas: list[str]) -> str:
    html = f'<div class="head-title">{esc(titulo)}</div>'
    html += '<p class="sub-text">Revisa tus respuestas:</p>'
    html += '<div class="stp quiz-row" style="flex-direction:column; gap:20px;">'
    for resp in respuestas:
        html += f'''
        <div class="pnl-border" style="display:flex; justify-content:center; align-items:center; padding:16px; background:#D1FAE5; border-color:#059669;">
            <div style="font-size:32px; font-weight:900; color:#059669;">{resp}</div>
        </div>
        '''
    html += '</div>'
    return html

def quiz_slide("""
content = content.replace(propuestos_fn, propuestos_new)


Path("scripts/clases/generator_suma_resta.py").write_text(content)
print("Updated generator logic")
