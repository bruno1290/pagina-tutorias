import os
from pathlib import Path

# Verifica si se tiene instalada la librería Pillow, de lo contrario sugiere instalarla.
try:
    from PIL import Image
except ImportError:
    print("Para usar este script, instala Pillow ejecutando:")
    print("pip install Pillow")
    exit(1)

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
ASSETS_DIR = PROJECT_ROOT / "assets"

def convert_to_webp(directory: Path):
    """
    Busca imágenes recursivamente y, si son jpg o png, las convierte a webp
    con compresión optimizada, sin eliminar el original.
    """
    count = 0
    print(f"Buscando imágenes en: {directory}")
    for ext in ("*.png", "*.jpg", "*.jpeg", "*.PNG", "*.JPG", "*.JPEG"):
        for file_path in directory.rglob(ext):
            original_size = os.path.getsize(file_path) / 1024 # KB
            webp_path = file_path.with_suffix(".webp")
            
            if webp_path.exists():
                print(f"Saltando (webp ya existe): {webp_path.name}")
                continue

            try:
                with Image.open(file_path) as img:
                    # Convertimos de formato y guardamos con compresión ideal para la web 
                    img.save(webp_path, "webp", optimize=True, quality=80)

                new_size = os.path.getsize(webp_path) / 1024 # KB
                print(f"Convertida: {file_path.name}")
                print(f"   Peso original: {original_size:.2f} KB  ->  Peso WebP: {new_size:.2f} KB")
                count += 1
            except Exception as e:
                print(f"Error convirtiendo {file_path.name}: {e}")

    print(f"\\n¡Proceso finalizado! Se han convertido {count} imágenes a formato WebP.")
    print("Recuerda actualizar las referencias en tus archivos HTML (ej: src=\"assets/imagen.webp\")")

if __name__ == "__main__":
    convert_to_webp(ASSETS_DIR)
