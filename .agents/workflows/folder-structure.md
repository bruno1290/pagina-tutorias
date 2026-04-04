---
description: Convención de estructura de carpetas del proyecto Tutorías La Obra UC
---

# Estructura de Carpetas — Regla Obligatoria

Toda modificación o creación de archivos **debe** respetar la siguiente organización.
Nunca crear archivos sueltos en la raíz salvo configuración (`.gitignore`, `AGENTS.md`, etc.).

## Árbol de referencia

```
/  (raíz del proyecto)
│
├── HTMLS pagina/                        ← HTMLs de la página web principal (landing / portal)
│   ├── index.html                       ← versión activa de la página
│   └── index_v2.html                    ← versiones de iteración
│
├── SLIDES/                              ← TODO el material de clases / presentaciones
│   │
│   ├── clases viejas/                   ← PDFs exportados de las clases ORIGINALES (archivo histórico)
│   │   ├── 01-descomposicion.pdf
│   │   ├── 02-suma.pdf
│   │   └── ...                          ← numeración correlativa XX-nombre.pdf
│   │
│   ├── Conectado aprendo/               ← PowerPoints FUENTE organizados por TEMA
│   │   └── fracciones/                  ← subcarpeta por unidad temática
│   │       ├── 1. Presentación fracciones (partes iguales).pptx
│   │       └── ...
│   │   (futuro: geometria/, medicion/, etc.)
│   │
│   └── fracciones HTMLS/                ← Slides HTML interactivos, organizados por TEMA
│       ├── 09-fracciones-1.html
│       ├── 10-fracciones-2.html
│       ├── 11-decimales.html
│       └── 12-ejercicios-frac-dec.html
│       (futuro: geometria HTMLS/, medicion HTMLS/, etc.)
│
├── assets/                              ← Recursos compartidos (imágenes, fuentes, íconos)
│   ├── fonts/
│   │   └── Buckwheat TC Rg.otf
│   ├── Logo.png
│   ├── TUTORÍAS.png
│   └── ...
│
├── .gitignore
├── AGENTS.md
└── prueba.py                            ← scripts auxiliares temporales
```

## Reglas clave

1. **`HTMLS pagina/`** — Solo contiene los archivos HTML de la **página web principal** (portal / landing). No mezclar con slides.

2. **`SLIDES/`** — Carpeta madre de **todo** el material de clases.
   - **`clases viejas/`** — Archivo histórico de los PDFs exportados. No borrar, solo agregar.
   - **`Conectado aprendo/`** — Archivos PPTX fuente, organizados en **subcarpetas por unidad temática** (ej: `fracciones/`, `geometria/`, `medicion/`).
   - **`<tema> HTMLS/`** — Slides HTML interactivos creados por nosotros. Cada tema tiene su propia carpeta con sufijo ` HTMLS` (ej: `fracciones HTMLS/`, `geometria HTMLS/`). Los archivos dentro conservan la **numeración correlativa** del plan de clases (`09-fracciones-1.html`, etc.).

3. **`assets/`** — Todo recurso visual o tipográfico compartido (logos, fuentes, imágenes de referencia). Los slides HTML deben referenciar assets desde aquí con rutas relativas (`../../assets/Logo.png`).

4. **Raíz `/`** — Solo archivos de configuración del proyecto (`.gitignore`, `AGENTS.md`, scripts auxiliares). No poner HTMLs ni slides aquí.

## Convención de nombres

| Tipo | Formato | Ejemplo |
|------|---------|---------|
| PDF clase vieja | `XX-nombre-tema.pdf` | `09-fracciones-1.pdf` |
| PPTX fuente | `N. Nombre descriptivo.pptx` | `1. Presentación fracciones (partes iguales).pptx` |
| HTML slide | `XX-nombre-tema.html` | `09-fracciones-1.html` |
| Carpeta tema HTMLS | `<tema> HTMLS` | `fracciones HTMLS` |
| Carpeta tema PPTX | `<tema>` (minúscula) | `fracciones` |

## Al agregar un nuevo tema

1. Crear subcarpeta en `SLIDES/Conectado aprendo/<nuevo-tema>/` para los PPTX fuente.
2. Crear subcarpeta en `SLIDES/<nuevo-tema> HTMLS/` para los slides HTML interactivos.
3. Los PDFs correspondientes ya deben estar en `SLIDES/clases viejas/`.
4. Mantener la numeración correlativa global (01-18 ya existentes).

## Al crear nuevos slides HTML

- Colocarlos en `SLIDES/<tema> HTMLS/`.
- Mantener el diseño visual coherente con los slides existentes (tipografía, colores, animaciones).
- Referenciar assets desde `../../assets/` con rutas relativas.
