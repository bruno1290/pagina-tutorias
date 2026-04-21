import re
from pathlib import Path

content = Path("scripts/clases/generator_suma_resta.py").read_text()

# Agregamos la función cube_3d
cube_fn = """
def cube_3d(count: int, color: str = "#E1BEE7") -> str:
    return "".join(
        f'<div style="display:inline-block; position:relative; width:54px; height:54px; margin:4px; background:{color}; border:2px solid rgba(0,0,0,0.18); border-radius:8px; box-shadow: 4px -4px 0 rgba(0,0,0,0.08); transform: translateY(4px);">'
        f'<div style="position:absolute; inset:2px; border:2px dashed rgba(255,255,255,0.6); border-radius:4px;"></div>'
        f'</div>'
        for _ in range(count)
    )
"""

if "def cube_3d" not in content:
    content = content.replace("def base_ten_card", cube_fn + "\n\ndef base_ten_card")

# Reemplazamos base_ten_card para soportar 4 dígitos y colores consistentes
new_base_ten = """def base_ten_card(number: int, title: str, colors: tuple[str, str, str, str] = ("#E1BEE7", "#9DE3BD", "#9DDEFF", "#FFE082")) -> str:
    thousands = number // 1000
    hundreds = (number % 1000) // 100
    tens = (number % 100) // 10
    units = number % 10
    
    grid_cols = "repeat(4, 1fr)" if thousands > 0 else "repeat(3, 1fr)"
    
    html = f'<div class="base-card"><h3>{esc(title)}</h3><div class="place-grid" style="grid-template-columns:{grid_cols};">'
    
    if thousands > 0:
        html += f'''
            <div class="place-box">
                <div class="place-title" style="color:#7B1FA2;">U. Mil</div>
                <div class="block-stack">{cube_3d(thousands, colors[0])}</div>
                <div class="number-tag">{thousands}</div>
            </div>
        '''
        
    if thousands > 0 or hundreds > 0:
        html += f'''
            <div class="place-box">
                <div class="place-title" style="color:#388E3C;">Centenas</div>
                <div class="block-stack">{flats(hundreds, colors[1])}</div>
                <div class="number-tag">{hundreds}</div>
            </div>
        '''
        
    html += f'''
            <div class="place-box">
                <div class="place-title" style="color:#1976D2;">Decenas</div>
                <div class="block-stack">{rods(tens, colors[2])}</div>
                <div class="number-tag">{tens}</div>
            </div>
            <div class="place-box">
                <div class="place-title" style="color:#F57F17;">Unidades</div>
                <div class="block-stack">{unit_blocks(units, colors[3])}</div>
                <div class="number-tag">{units}</div>
            </div>
        </div>
        <div class="math-eq" style="font-size:34px;">{number}</div>
    </div>
    '''
    return html"""

content = re.sub(r'def base_ten_card.*?(?=def notebook_slide)', new_base_ten + "\n\n\n", content, flags=re.DOTALL)

Path("scripts/clases/generator_suma_resta.py").write_text(content)
print("Base functions updated")
