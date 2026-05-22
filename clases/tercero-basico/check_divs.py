import os
import re

base_dir = "/Users/brunonattino/Desktop/PAGINA TUTORIAS/clases/tercero-basico/"
dirs = ["numeros", "suma", "resta", "multiplicacion", "division"]

def check_file(fpath):
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split content by '<div class="sl">'
    parts = content.split('<div class="sl">')
    
    # parts[0] is everything before the first slide
    for i, p in enumerate(parts[1:], 1):
        # Count <div> and </div> in this slide block
        # Note: this is a heuristic, it might include the closing div of the slide itself
        open_divs = len(re.findall(r'<div\b[^>]*>', p))
        close_divs = len(re.findall(r'</div>', p))
        
        # A proper slide block (assuming it doesn't contain the closing div of the parent)
        # usually ends with the </div> of the slide itself.
        # But wait, splitting by '<div class="sl">' means the slide's opening tag is REMOVED from `p`.
        # So inside `p`, the number of closing divs should be exactly 1 MORE than the number of opening divs!
        if close_divs != open_divs + 1:
            print(f"Mismatch in {os.path.basename(fpath)} Slide {i}: +{open_divs} -{close_divs} (Diff: {close_divs - open_divs})")

for d in dirs:
    dpath = os.path.join(base_dir, d)
    if not os.path.exists(dpath): continue
    for f in os.listdir(dpath):
        if not f.endswith('.html'): continue
        check_file(os.path.join(dpath, f))

