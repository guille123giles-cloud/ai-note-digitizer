import streamlit as st
import google.generativeai as genai
from PIL import Image

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="AI Document Digitizer", 
    page_icon="📑", 
    layout="wide"
)

# --- ESTILOS PERSONALIZADOS ---
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #007bff;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# --- INICIALIZACIÓN DE IA ---
def init_gemini():
    try:
        if "GEMINI_API_KEY" in st.secrets:
            genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
            return genai.GenerativeModel('gemini-2.5-flash')
        else:
            st.warning("⚠️ Clave de API no detectada. Configure 'GEMINI_API_KEY' en sus secretos.")
            return None
    except Exception as e:
        st.error(f"Error de configuración: {e}")
        return None

modelo = init_gemini()

# --- INTERFAZ DE USUARIO ---
st.title("📑 Digitalizador de Apuntes Pro")
st.markdown("Transforme sus notas manuscritas en texto digital estructurado y corregido mediante Inteligencia Artificial.")
st.divider()

# Subida de archivo
archivo_subido = st.file_uploader("Cargue una imagen del documento (JPG, PNG)", type=["jpg", "jpeg", "png"])

if archivo_subido:
    # Optimización de imagen
    imagen = Image.open(archivo_subido)
    max_dimension = 1600
    if max(imagen.size) > max_dimension:
        imagen.thumbnail((max_dimension, max_dimension))
    
    # Diseño de dos columnas
    col_izq, col_der = st.columns([1, 1], gap="large")
    
    with col_izq:
        st.subheader("🖼️ Documento Original")
        st.image(imagen, use_container_width=True, caption="Imagen cargada")

    with col_der:
        st.subheader("📝 Texto Digitalizado")
        
        if "texto_final" not in st.session_state:
            st.session_state.texto_final = ""
        
        if st.button("Procesar e iniciar extracción"):
            if modelo:
                with st.spinner("Analizando caligrafía y estructurando texto..."):
                    try:
                        # Prompt profesional y preciso
                        instrucciones = """
                        Actúa como un experto en transcripción y paleografía digital.
                        Tu tarea es extraer el texto de la imagen adjunta siguiendo estas reglas:
                        1. Fidelidad Estructural: Mantén la disposición original de las líneas. Si una línea termina abruptamente, respeta ese salto.
                        2. Corrección Gramatical: Corrige errores ortográficos evidentes sin alterar el significado técnico.
                        3. Formato Limpio: No agregues comentarios personales ni introducciones. 
                        4. Output: Devuelve solo el texto transcrito de forma clara y legible.
                        """
                        
                        respuesta = modelo.generate_content([instrucciones, imagen])
                        st.session_state.texto_final = respuesta.text
                        st.success("Digitalización completada con éxito.")
                        
                    except Exception as e:
                        st.error(f"Error durante el procesamiento: {e}")
            else:
                st.error("El modelo no está inicializado. Verifique su API Key.")
        
        # Área de edición y descarga
        if st.session_state.texto_final:
            texto_editado = st.text_area(
                "Edite el resultado si es necesario:", 
                value=st.session_state.texto_final, 
                height=400
            )
            
            st.download_button(
                label="📥 Descargar como archivo .txt",
                data=texto_editado,
                file_name="documento_digitalizado.txt",
                mime="text/plain"
            )

# --- PIE DE PÁGINA ---
st.divider()
st.caption("Desarrollado con Streamlit y Google Gemini 2.5 Flash")
