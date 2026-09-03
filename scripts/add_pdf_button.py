import os
import glob

print_css = """
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
"""

print_btn = """
<button onclick="window.print()" class="print-btn" style="position:fixed; top:20px; right:20px; background:#1C4A82; color:white; border:none; padding:10px 15px; border-radius:8px; font-family:'Nunito',sans-serif; font-weight:bold; cursor:pointer; z-index:1000; box-shadow:0 4px 6px rgba(0,0,0,0.1);">📄 Descargar PDF</button>
"""

def modify_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    modified = False
    
    # Check if already added to avoid duplication
    if "📄 Descargar PDF" in content or "@media print" in content:
        return False

    # Find </head> to inject style
    if "</head>" in content:
        # replace the LAST occurrence of </head> (just in case, though usually only 1)
        parts = content.rsplit("</head>", 1)
        content = parts[0] + print_css + "</head>" + parts[1]
        modified = True
        
    # Find </body> to inject button
    if "</body>" in content:
        parts = content.rsplit("</body>", 1)
        content = parts[0] + print_btn + "</body>" + parts[1]
        modified = True

    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def process_directory(directory, extension):
    count = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                filepath = os.path.join(root, file)
                if modify_file(filepath):
                    count += 1
                    print(f"Modificado: {filepath}")
    return count

if __name__ == "__main__":
    base_dir = "/Users/brunonattino/Desktop/PAGINA TUTORIAS"
    
    html_count = process_directory(os.path.join(base_dir, "clases"), ".html")
    py_count = process_directory(os.path.join(base_dir, "scripts", "clases"), ".py")
    
    print(f"Total HTML files modified: {html_count}")
    print(f"Total Python files modified: {py_count}")
