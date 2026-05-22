import os
import re

base_dir = "/Users/brunonattino/Desktop/PAGINA TUTORIAS/clases/tercero-basico/"
dirs = ["numeros", "suma", "resta", "multiplicacion", "division"]

# Updated CSS for multibase blocks
mb_css = """
/* Bloques multibase CSS puros con textura */
.mb-c {
    --bg-color: #9DE3BD;
    --border-color: #388E3C;
    width: 140px; height: 140px;
    background:
        repeating-linear-gradient(0deg, transparent, transparent 13px, rgba(0,0,0,0.15) 13px, rgba(0,0,0,0.15) 14px),
        repeating-linear-gradient(90deg, transparent, transparent 13px, rgba(0,0,0,0.15) 13px, rgba(0,0,0,0.15) 14px),
        var(--bg-color);
    border: 1px solid var(--border-color);
    display: inline-block; margin: 2px; border-radius: 3px;
}
.mb-d {
    --bg-color: #9DDEFF;
    --border-color: #1976D2;
    width: 14px; height: 140px;
    background: 
        repeating-linear-gradient(0deg, transparent, transparent 13px, rgba(0,0,0,0.2) 13px, rgba(0,0,0,0.2) 14px),
        var(--bg-color);
    border: 1px solid var(--border-color);
    display: inline-block; margin: 2px; border-radius: 2px;
}
.mb-u {
    --bg-color: #FFE082;
    --border-color: #F57F17;
    width: 14px; height: 14px;
    background: var(--bg-color);
    border: 1px solid var(--border-color);
    display: inline-block; margin: 2px; border-radius: 2px;
}
.mb-group {
    display: flex; align-items: flex-end; justify-content: center; gap: 8px;
    padding: 10px; background: #fff; border-radius: 12px; border: 2px dashed #ccc;
    flex-wrap: wrap;
}
"""

for d in dirs:
    dpath = os.path.join(base_dir, d)
    if not os.path.exists(dpath): continue
    for f in os.listdir(dpath):
        if not f.endswith(".html"): continue
        fpath = os.path.join(dpath, f)
        with open(fpath, "r", encoding="utf-8") as file:
            content = file.read()
        
        # Replace the old multibase block CSS if it exists
        content = re.sub(r'/\* Bloques multibase CSS puros con textura \*/.*?\.mb-group\s*\{[^}]*\}', mb_css, content, flags=re.DOTALL)
        
        # If it has .unit, .rod, .flat CSS, replace those usages
        if ".flat {" in content and "/* Bloques multibase" not in content:
            # We insert the mb_css before the end of style
            content = content.replace("</style>", mb_css + "\n</style>")
            
            # Replace html usages
            content = re.sub(r'<span class="flat" style="[^"]*"></span>', r'<div class="mb-c"></div>', content)
            content = re.sub(r'<span class="rod" style="[^"]*"></span>', r'<div class="mb-d"></div>', content)
            content = re.sub(r'<span class="unit" style="[^"]*"></span>', r'<div class="mb-u"></div>', content)
        
        # Fix the red decena in suma-2.html
        if f == "suma-2.html":
            content = content.replace('<div class="mb-d" style="--bg-color:#ffcdd2; --border-color:#d32f2f;"></div>', '<div class="mb-d"></div>')
            content = content.replace('<div class="mb-u" style="border-color:#d32f2f;"></div>', '<div class="mb-u"></div>')
        
        # Make the bubbles bigger in suma-1 if needed, or add algo-res explicitly 
        # But wait, algo-res is just CSS.
        
        with open(fpath, "w", encoding="utf-8") as file:
            file.write(content)
print("Done!")
