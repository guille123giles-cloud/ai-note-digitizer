import streamlit as st
import google.generativeai as genai
from PIL import Image

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="Traductor de Blasko", page_icon="📝", layout="centered")

# Configurar la IA usando la clave secreta que guardamos
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    # Usamos Flash 1.5 que es rapidísimo y excelente para leer imágenes
    modelo = genai.GenerativeModel('gemini-2.5-flash')
except Exception:
    st.error("⚠️ Falta configurar la API Key en la carpeta .streamlit/secrets.toml")

# --- INTERFAZ ---
st.title("El Traductor del virgo de Blasko")
st.markdown("Aprende a escribir bien Blasko la concha de tu madre.")
st.divider()

# ... (tu código de configuración de arriba queda exactamente igual)

# Subida de archivo
archivo_subido = st.file_uploader("Cargá la foto de la hoja", type=["jpg", "jpeg", "png"])

if archivo_subido:
    # 1. Abrimos y optimizamos la imagen para que sea rápido
    imagen = Image.open(archivo_subido)
    max_dimension = 1600
    if max(imagen.size) > max_dimension:
        imagen.thumbnail((max_dimension, max_dimension))
    
    st.divider() # Línea separadora estética
    
    # 2. Creamos dos columnas: Mitad izquierda (foto) y mitad derecha (texto)
    col_izq, col_der = st.columns(2)
    
    with col_izq:
        st.markdown("### Apunte de Blasko")
        st.image(imagen, use_container_width=True)

    with col_der:
        st.markdown("### Texto Limpio")
        
        # 1. INVENTAMOS LA MEMORIA: Si no existe, la creamos vacía
        if "texto_final" not in st.session_state:
            st.session_state.texto_final = ""
        
        # El botón ahora está en la columna derecha
        if st.button("Descifrar que mierda dice", use_container_width=True):
            with st.spinner("Traduciendo..."):
                try:
                    # Las instrucciones estrictas para mantener los renglones
                    instrucciones = """
                    Actúa como un motor de extracción de texto estricto. 
                    Tu único objetivo es transcribir y corregir la ortografía de la imagen adjunta, respetando ABSOLUTAMENTE la estructura física.
                    REGLAS:
                    1. Por cada renglón físico que veas en el papel, debes generar exactamente un salto de línea en tu respuesta.
                    2. Si una oración se corta a la mitad en la foto porque se terminó el papel, tu texto DEBE cortarse exactamente en esa misma palabra.
                    3. Corrige la ortografía y gramática, pero NO unas líneas ni agrupes en párrafos.
                    Devuelve únicamente el texto crudo resultante, línea por línea.
                    """
                    
                    # Llamamos a la IA
                    respuesta = modelo.generate_content([instrucciones, imagen])
                    
                    # 2. GUARDAMOS EN MEMORIA el resultado, en vez de una variable temporal
                    st.session_state.texto_final = respuesta.text
                    
                    st.success("¡Éxito!")
                    
                except Exception as e:
                    st.error(f"Ocurrió un error: {e}")
        
        # 3. LO SACAMOS AFUERA: Esto se muestra solo si la memoria tiene texto guardado
        if st.session_state.texto_final:
            # Mostramos el texto en una caja grande para que lo leas cómodo
            st.text_area("Resultado (Podés editarlo si querés):", value=st.session_state.texto_final, height=400, label_visibility="collapsed")
            
            # Agregamos el botón mágico para guardar el archivo
            st.download_button(
                label="Descargar como archivo .txt",
                data=st.session_state.texto_final,
                file_name="apunte_traducido.txt",
                mime="text/plain",
                use_container_width=True
            )