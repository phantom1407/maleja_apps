import base64
from pathlib import Path

import streamlit as st

# ------------------------------------------------------------
# Configuración general de la página
# ------------------------------------------------------------
st.set_page_config(
    page_title="Aplicaciones de Inteligencia Artificial",
    page_icon="🌸",
    layout="wide",
)

# ------------------------------------------------------------
# Paleta pastel
# ------------------------------------------------------------
ROSA = "#FFB5D2"
ROSA_SUAVE = "#FFE3EE"
MORADO = "#C9B2FF"
MORADO_SUAVE = "#EFE6FF"
AZUL = "#A8D4FF"
AZUL_SUAVE = "#E3F1FF"
TINTA = "#4B3F72"

# ------------------------------------------------------------
# Estilos
# ------------------------------------------------------------
st.markdown(
    f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&family=Nunito:wght@400;600;700&display=swap');

html, body, [class*="css"], .stApp {{
    font-family: 'Nunito', sans-serif;
    color: {TINTA};
}}

.stApp {{
    background:
        radial-gradient(circle at 10% 10%, {ROSA_SUAVE} 0%, transparent 40%),
        radial-gradient(circle at 90% 20%, {AZUL_SUAVE} 0%, transparent 45%),
        radial-gradient(circle at 50% 90%, {MORADO_SUAVE} 0%, transparent 50%),
        #FFFAFD;
}}

/* ---------- Forzar tema claro sin config.toml ---------- */
:root, .stApp {{
    color-scheme: light;
}}
[data-testid="stHeader"] {{
    background: transparent;
}}
[data-testid="stToolbar"] * , [data-testid="stSidebarCollapseButton"] *,
[data-testid="stSidebarCollapsedControl"] *, [data-testid="stExpandSidebarButton"] * {{
    color: {TINTA} !important;
}}
.stApp p, .stApp span, .stApp div, .stApp label {{
    color: {TINTA};
}}
::selection {{
    background: {MORADO};
    color: {TINTA};
}}

/* ---------- Barra lateral ---------- */
[data-testid="stSidebar"] {{
    background: linear-gradient(180deg, {ROSA_SUAVE} 0%, {MORADO_SUAVE} 50%, {AZUL_SUAVE} 100%);
    border-right: 3px solid #FFFFFF;
}}
[data-testid="stSidebar"] * {{
    color: {TINTA};
}}
.sidebar-title {{
    font-family: 'Fredoka', sans-serif;
    font-size: 1.4rem;
    font-weight: 600;
    margin-bottom: 0.6rem;
}}
.sidebar-text {{
    line-height: 1.6;
    font-size: 0.98rem;
}}
.legend {{
    margin-top: 1.4rem;
    background: rgba(255, 255, 255, 0.7);
    border-radius: 18px;
    padding: 0.9rem 1rem;
}}
.legend-item {{
    display: flex;
    align-items: center;
    gap: 0.6rem;
    margin: 0.35rem 0;
    font-weight: 600;
}}
.dot {{
    width: 14px;
    height: 14px;
    border-radius: 50%;
    display: inline-block;
}}

/* ---------- Encabezado principal ---------- */
.hero {{
    text-align: center;
    padding: 2.6rem 1.5rem 2.2rem;
    margin-bottom: 2rem;
    border-radius: 36px;
    background: rgba(255, 255, 255, 0.65);
    border: 3px solid #FFFFFF;
    box-shadow: 0 18px 40px rgba(201, 178, 255, 0.25);
}}
.hero-title {{
    font-family: 'Fredoka', sans-serif;
    font-size: clamp(2.2rem, 5vw, 3.6rem);
    font-weight: 700;
    line-height: 1.1;
    background: linear-gradient(90deg, #F48FB8, #A98BFF, #6FB2FF);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
    margin: 0 0 0.8rem;
}}
.hero-sub {{
    font-size: 1.1rem;
    max-width: 640px;
    margin: 0 auto 1.6rem;
    line-height: 1.6;
}}
.hero-buttons {{
    display: flex;
    gap: 0.8rem;
    justify-content: center;
    flex-wrap: wrap;
}}

/* ---------- Botones ---------- */
a.btn {{
    display: inline-block;
    padding: 0.6rem 1.3rem;
    border-radius: 999px;
    font-weight: 700;
    text-decoration: none !important;
    color: {TINTA} !important;
    border: 2px solid #FFFFFF;
    transition: transform 0.15s ease, box-shadow 0.15s ease;
}}
a.btn:hover {{
    transform: translateY(-2px);
    box-shadow: 0 8px 18px rgba(75, 63, 114, 0.15);
}}
a.btn:focus-visible {{
    outline: 3px solid {TINTA};
    outline-offset: 3px;
}}
.btn-rosa   {{ background: {ROSA}; }}
.btn-morado {{ background: {MORADO}; }}
.btn-azul   {{ background: {AZUL}; }}
.btn-grad   {{ background: linear-gradient(90deg, {ROSA}, {MORADO}, {AZUL}); }}

/* ---------- Secciones ---------- */
.section-head {{
    display: flex;
    align-items: center;
    gap: 0.8rem;
    margin: 1.4rem 0 1rem;
}}
.section-bar {{
    width: 10px;
    height: 38px;
    border-radius: 999px;
}}
.section-title {{
    font-family: 'Fredoka', sans-serif;
    font-size: 1.7rem;
    font-weight: 600;
    margin: 0;
}}
.section-desc {{
    font-size: 0.98rem;
    opacity: 0.85;
    margin: -0.4rem 0 1.2rem 1.4rem;
}}

/* ---------- Tarjetas ---------- */
.card {{
    border-radius: 26px;
    padding: 1rem 1rem 1.3rem;
    margin-bottom: 1.6rem;
    border: 3px solid #FFFFFF;
    transition: transform 0.2s ease;
}}
.card:hover {{
    transform: translateY(-4px);
}}
.card-rosa   {{ background: {ROSA_SUAVE};   box-shadow: 0 12px 28px rgba(255, 181, 210, 0.35); }}
.card-morado {{ background: {MORADO_SUAVE}; box-shadow: 0 12px 28px rgba(201, 178, 255, 0.35); }}
.card-azul   {{ background: {AZUL_SUAVE};   box-shadow: 0 12px 28px rgba(168, 212, 255, 0.35); }}

.card-img {{
    width: 100%;
    height: 180px;
    object-fit: cover;
    border-radius: 20px;
    border: 3px solid #FFFFFF;
    background: #FFFFFF;
}}
.card-img-empty {{
    width: 100%;
    height: 180px;
    border-radius: 20px;
    border: 3px dashed #FFFFFF;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 3rem;
    background: rgba(255, 255, 255, 0.5);
}}
.card-title {{
    font-family: 'Fredoka', sans-serif;
    font-size: 1.3rem;
    font-weight: 600;
    margin: 0.9rem 0 0.35rem;
}}
.card-text {{
    font-size: 0.95rem;
    line-height: 1.5;
    margin-bottom: 1rem;
    min-height: 3em;
}}

/* ---------- Pie de página ---------- */
.footer {{
    text-align: center;
    margin-top: 2.5rem;
    padding: 1.2rem;
    font-size: 0.9rem;
    opacity: 0.8;
}}

@media (prefers-reduced-motion: reduce) {{
    .card, a.btn {{ transition: none; }}
    .card:hover, a.btn:hover {{ transform: none; }}
}}
</style>
""",
    unsafe_allow_html=True,
)

# ------------------------------------------------------------
# Datos de las aplicaciones
# ------------------------------------------------------------
URL_SITIO = "https://sites.google.com/view/aplicacionesdeia/inicio"
URL_INTRO = "https://phantomintro-mscypzjs6a3mkwf2du2y2k.streamlit.app/"

SECCIONES = [
    {
        "titulo": "Voz y lenguaje",
        "descripcion": "Apps que hablan, escuchan y traducen.",
        "color": "rosa",
        "apps": [
            {
                "titulo": "Texto a voz",
                "emoji": "🔊",
                "imagen": "txt_to_audio.png",
                "texto": "Convierte cualquier texto en audio con una voz natural.",
                "url": "https://fsdxiwrsor7vrpbprzbzd8.streamlit.app/",
            },
            {
                "titulo": "Traductor",
                "emoji": "🌍",
                "imagen": "OIG5.jpg",
                "texto": "Traduce textos entre distintos idiomas en segundos.",
                "url": "https://traductorphantom-bomqwzggxb5qf6cmm2fcsa.streamlit.app/",
            },
        ],
    },
    {
        "titulo": "Análisis de texto",
        "descripcion": "Apps que leen, resumen y entienden lo que escribimos.",
        "color": "morado",
        "apps": [
            {
                "titulo": "Nube de palabras",
                "emoji": "☁️",
                "imagen": "OIG3.jpg",
                "texto": "Muestra de un vistazo las palabras más frecuentes de un texto.",
                "url": "https://wordcloudcoso-l7vz4ykl3tfdsjxeiof2cv.streamlit.app/",
            },
            {
                "titulo": "Análisis de sentimientos",
                "emoji": "💗",
                "imagen": "OIG9.jpg",
                "texto": "Identifica si un texto expresa algo positivo, negativo o neutral.",
                "url": "https://sentimenta-mzapeebtgm4ysecazdwqny.streamlit.app/",
            },
            {
                "titulo": "TF-IDF",
                "emoji": "📊",
                "imagen": "OIG10.jpg",
                "texto": "Mide qué tan importante es cada palabra dentro de un conjunto de textos.",
                "url": "https://tdfesp-drqgijv5t8tzd7wrxhzado.streamlit.app/",
            },
            {
                "titulo": "Chat con PDF (RAG)",
                "emoji": "📄",
                "imagen": "Chat_pdf.png",
                "texto": "Hazle preguntas a un documento PDF usando generación aumentada por recuperación.",
                "url": "https://chatpdf-cc.streamlit.app/",
            },
        ],
    },
    {
        "titulo": "Visión y mundo físico",
        "descripcion": "Apps que ven, reconocen y se conectan con objetos reales.",
        "color": "azul",
        "apps": [
            {
                "titulo": "OCR",
                "emoji": "🔎",
                "imagen": "OIG8.jpg",
                "texto": "Extrae el texto que aparece dentro de una imagen.",
                "url": "https://imagenrecog-tetnebtvpzjqebsuxhevgw.streamlit.app/",
            },
            {
                "titulo": "OCR 2",
                "emoji": "🧾",
                "imagen": "data_analisis.png",
                "texto": "Otra forma de reconocer y extraer texto de imágenes.",
                "url": "https://ocrcoso-4uqcesxske8iy8gsj3f9mu.streamlit.app/",
            },
            {
                "titulo": "YOLO",
                "emoji": "🎯",
                "imagen": "OIG5.jpg",
                "texto": "Detecta y señala objetos dentro de una imagen en tiempo real.",
                "url": "https://yolov5profe-pvibkrfl3nvpzax9yostns.streamlit.app/",
            },
            {
                "titulo": "Teachable Machine",
                "emoji": "🧠",
                "imagen": "OIG2.jpg",
                "texto": "Usa un modelo entrenado por ti para clasificar imágenes.",
                "url": "https://tmprofe-mwizzaqtqk82tjftjn8rva.streamlit.app/",
            },            
        ],
    },
]


# ------------------------------------------------------------
# Funciones auxiliares
# ------------------------------------------------------------
@st.cache_data
def imagen_a_base64(ruta: str):
    """Convierte una imagen local en data URI para usarla dentro del HTML."""
    archivo = Path(ruta)
    if not archivo.exists():
        return None
    extension = archivo.suffix.lower().replace(".", "")
    tipo = "jpeg" if extension in ("jpg", "jpeg") else extension
    datos = base64.b64encode(archivo.read_bytes()).decode()
    return f"data:image/{tipo};base64,{datos}"


def tarjeta(app: dict, color: str) -> str:
    """Genera el HTML de una tarjeta de aplicación."""
    src = imagen_a_base64(app["imagen"])
    if src:
        imagen_html = f'<img class="card-img" src="{src}" alt="{app["titulo"]}">'
    else:
        imagen_html = f'<div class="card-img-empty">{app["emoji"]}</div>'

    return (
        f'<div class="card card-{color}">'
        f"{imagen_html}"
        f'<div class="card-title">{app["emoji"]} {app["titulo"]}</div>'
        f'<div class="card-text">{app["texto"]}</div>'
        f'<a class="btn btn-{color}" href="{app["url"]}" target="_blank" rel="noopener">Abrir app</a>'
        f"</div>"
    )


COLORES_BARRA = {"rosa": ROSA, "morado": MORADO, "azul": AZUL}

# ------------------------------------------------------------
# Barra lateral
# ------------------------------------------------------------
with st.sidebar:
    st.markdown(
        '<div class="sidebar-title">🌸 Aplicaciones con inteligencia artificial</div>'
        '<div class="sidebar-text">'
        "La inteligencia artificial permite mejorar la toma de decisiones con el uso de datos, "
        "automatizar tareas rutinarias y proporcionar análisis avanzados en tiempo real, lo que "
        "resulta en una mayor eficiencia y precisión en diversos campos."
        "</div>"
        '<div class="legend">'
        f'<div class="legend-item"><span class="dot" style="background:{ROSA}"></span>Voz y lenguaje</div>'
        f'<div class="legend-item"><span class="dot" style="background:{MORADO}"></span>Análisis de texto</div>'
        f'<div class="legend-item"><span class="dot" style="background:{AZUL}"></span>Visión y mundo físico</div>'
        "</div>",
        unsafe_allow_html=True,
    )

# ------------------------------------------------------------
# Encabezado principal
# ------------------------------------------------------------
st.markdown(
    '<div class="hero">'
    '<div class="hero-title">Aplicaciones de Inteligencia Artificial</div>'
    '<div class="hero-sub">Explora apps que convierten texto en voz, leen imágenes, '
    "analizan sentimientos y mucho más. Haz clic en cualquiera para probarla.</div>"
    '<div class="hero-buttons">'
    f'<a class="btn btn-grad" href="{URL_INTRO}" target="_blank" rel="noopener">✨ Ver la intro</a>'
    f'<a class="btn btn-morado" href="{URL_SITIO}" target="_blank" rel="noopener">📚 Páginas y ejercicios prácticos</a>'
    "</div>"
    "</div>",
    unsafe_allow_html=True,
)

# ------------------------------------------------------------
# Secciones con tarjetas
# ------------------------------------------------------------
for seccion in SECCIONES:
    color = seccion["color"]
    st.markdown(
        '<div class="section-head">'
        f'<span class="section-bar" style="background:{COLORES_BARRA[color]}"></span>'
        f'<div class="section-title">{seccion["titulo"]}</div>'
        "</div>"
        f'<div class="section-desc">{seccion["descripcion"]}</div>',
        unsafe_allow_html=True,
    )

    columnas = st.columns(3, gap="large")
    for i, app in enumerate(seccion["apps"]):
        with columnas[i % 3]:
            st.markdown(tarjeta(app, color), unsafe_allow_html=True)

# ------------------------------------------------------------
# Pie de página
# ------------------------------------------------------------
st.markdown(
    '<div class="footer">Hecho con 💜 en Streamlit</div>',
    unsafe_allow_html=True,
)
