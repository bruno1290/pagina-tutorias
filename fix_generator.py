import re
from pathlib import Path

content = Path("scripts/clases/generator_suma_resta.py").read_text()

# 1. FIX CSS
css_old = r"""\.unit\s*\{.*?\}.*?\.rod\s*\{.*?\}.*?\.flat\s*\{.*?\}"""
css_new = r""".unit {
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
content = re.sub(css_old, css_new, content, flags=re.DOTALL)

# 2. FIX cube_3d (make it scalable to visually match Unidades de Mil)
# 10x10x10 is hard in 2D CSS without being massive, so we make it look like a large block.
cube_old = r"""def cube_3d\(count: int, color: str = "#E1BEE7"\) -> str:.*?\)"""
cube_new = r"""def cube_3d(count: int, color: str = "#E1BEE7") -> str:
    return "".join(
        f'<div style="display:inline-block; position:relative; width:100px; height:120px; margin:4px; background:{color}; border:2px solid rgba(0,0,0,0.25); border-radius:8px; box-shadow: 12px -12px 0 rgba(0,0,0,0.1); transform: translateY(12px) translateX(-6px);">'
        f'<div style="position:absolute; inset:0; background:repeating-linear-gradient(0deg, transparent, transparent 11px, rgba(0,0,0,0.1) 11px, rgba(0,0,0,0.1) 12px), repeating-linear-gradient(90deg, transparent, transparent 19px, rgba(0,0,0,0.1) 19px, rgba(0,0,0,0.1) 20px);"></div>'
        f'</div>'
        for _ in range(count)
    )"""
content = re.sub(cube_old, cube_new, content, flags=re.DOTALL)

# 3. FIX alg_board
alg_old = r"""def alg_board\(rows: list\[list\[str\]\], side_title: str, side_notes: list\[str\], long: bool = False\) -> str:.*?</div>\s*</div>\s*"""
alg_new = r'''def alg_board(rows: list[list[str]], side_title: str, side_notes: list[str], long: bool = False) -> str:
    grid_rows = []
    max_cols = max(len(r) for r in rows)
    grid_style = f"grid-template-columns: 80px repeat({max_cols - 1}, 76px);"
    
    for row in rows:
        label, *cells = row
        grid_rows.append(f'<div class="alg-label">{label}</div>')
        for cell in cells:
            classes = ["alg-digit"]
            text = cell
            if cell.startswith("r:"):
                classes.append("reserve")
                text = cell[2:]
            elif cell == "_":
                classes.append("dim")
                text = ""
            grid_rows.append(f'<div class="{" ".join(classes)}">{esc(text)}</div>')
    
    lines_html = f'<div class="alg-line" style="grid-column: 2 / span {max_cols - 1};"></div>'
    notes_html = "".join(f'<p class="stp" style="margin-bottom:12px;">{note}</p>' for note in side_notes)
    
    return f"""
    <div class="column-wrap">
        <div class="alg-board">
            <div class="alg-grid" style="{grid_style}">
                {''.join(grid_rows)}
                {lines_html}
            </div>
        </div>
        <div class="side-panel">
            <h3>{esc(side_title)}</h3>
            {notes_html}
        </div>
    </div>
    """
'''
# I will use replace
content = content.replace(re.search(alg_old, content, flags=re.DOTALL).group(0), alg_new)

Path("scripts/clases/generator_suma_resta.py").write_text(content)
print("CSS, Cube, and AlgBoard updated")
