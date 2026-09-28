import streamlit as st
from PIL import Image
st.title("Aplicaciones de Inteligencia Artificial.")

with st.sidebar:
  st.subheader("Aplicaciones con Inteligencia Artificial.")
  parrafo = (
    "La inteligencia artificial permite mejorar la toma de decisiones con el uso de datos, "
    "automatizar tareas rutinarias y proporcionar análisis avanzados en tiempo real, lo que "
    "resulta en una mayor eficiencia y precisión en diversos campos."
  )
  st.write(parrafo)

url_ia="https://sites.google.com/view/aplicacionesdeia/inicio"
st.subheader("En el siguiente enlace puedes encontrar páginas y ejercicios prácticos")
st.write(f"Enlace para páginas y ejercicios: [Enlace]({url_ia})")
col1, col2, col3 = st.columns(3)

with col1:
 
 st.subheader("Intro")
 image = Image.open('txt_to_audio2.png')
 st.image(image, width=190)
 st.write("En la siguiente enlace veremos la intro") 
 url = "https://phantomintro-mscypzjs6a3mkwf2du2y2k.streamlit.app/"
 st.write(f"Texto a voz: [Enlace]({url})")

 st.subheader("Texto a voz")
 image = Image.open('txt_to_audio.png')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos como convertir texto a voz") 
 url = "https://fsdxiwrsor7vrpbprzbzd8.streamlit.app/"
 st.write(f"YOLO: [Enlace]({url})")

 st.subheader("Traductor")
 image = Image.open('OIG5.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos un traductor") 
 url = "https://traductorphantom-bomqwzggxb5qf6cmm2fcsa.streamlit.app/"
 st.write(f"YOLO: [Enlace]({url})")

with col2: 
 st.subheader("OCR")
 image = Image.open('OIG8.jpg')
 st.image(image, width=200)
 st.write("En la siguiente veremos una aplicación de OCR") 
 url = "https://imagenrecog-tetnebtvpzjqebsuxhevgw.streamlit.app/"
 st.write(f"Voz a texto: [Enlace]({url})")

 st.subheader("OCR 2")
 image = Image.open('data_analisis.png')
 st.image(image, width=190)
 st.write("En la siguiente enlace veremos otra aplicacion de OCR") 
 url = "https://ocrcoso-4uqcesxske8iy8gsj3f9mu.streamlit.app/"
 st.write(f"Datos: [Enlace]({url})")

 st.subheader("Nube")
 image = Image.open('OIG3.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos una nube de palabras") 
 url = "https://wordcloudcoso-l7vz4ykl3tfdsjxeiof2cv.streamlit.app/"
 st.write(f"Transcriptor: [Enlace]({url})")

 st.subheader("Sentimientos")
 image = Image.open('OIG9.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos un análisis de sentimientos") 
 url = "https://sentimenta-mzapeebtgm4ysecazdwqny.streamlit.app/"
 st.write(f"Transcriptor: [Enlace]({url})")

 st.subheader("TF-IDF")
 image = Image.open('OIG10.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos un análisis de texto") 
 url = "https://tdfesp-drqgijv5t8tzd7wrxhzado.streamlit.app/"
 st.write(f"Transcriptor: [Enlace]({url})")

 st.subheader("Yolo")
 image = Image.open('OIG5.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos como usar YOLO") 
 url = "https://yolov5profe-pvibkrfl3nvpzax9yostns.streamlit.app/"
 st.write(f"Transcriptor: [Enlace]({url})")

 st.subheader("Teachable machine")
 image = Image.open('OIG2.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos como usar TM") 
 url = "https://tmprofe-mwizzaqtqk82tjftjn8rva.streamlit.app/"
 st.write(f"Transcriptor: [Enlace]({url})")

with col3: 
 st.subheader("Generación en Contexto")
 image = Image.open('Chat_pdf.png')
 st.image(image, width=190)
 st.write("En la siguiente veremos una aplicación que usa RAG a partir de un documento (PDF).") 
 url = "https://chatpdf-cc.streamlit.app/"
 st.write(f"RAG: [Enlace]({url})")

 st.subheader("Análisis de Imagen")
 image = Image.open('OIG4.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos la capacidad de análisis en Imágenes.") 
 url = "https://vision2-gpt4o.streamlit.app/"
 st.write(f"Vision: [Enlace]({url})")
 
 st.subheader("Sistema Ciberfísico")
 image = Image.open('OIG6.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos la capacidad de interacción con el mundo físico.") 
 url = "https://vision2-gpt4o.streamlit.app/"
 st.write(f"Vision: [Enlace]({url})")


