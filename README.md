# AI Note Digitizer Pro: Transcriptor de Apuntes con IA

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Gemini](https://img.shields.io/badge/Google%20Gemini-8E75FF?style=for-the-badge&logo=googlegemini&logoColor=white)

**AI Note Digitizer Pro** es una aplicación avanzada que utiliza modelos de lenguaje de última generación (Google Gemini 1.5 Flash) para convertir imágenes de apuntes manuscritos en texto digital estructurado. A diferencia de un OCR tradicional, esta herramienta entiende el contexto, corrige la gramática y mantiene la jerarquía visual de las notas.

---

## Características Principales

* **Transcripción Inteligente:** Capacidad para interpretar caligrafía manuscrita compleja que los motores OCR estándar suelen fallar.
* **Fidelidad Estructural:** Mantiene la disposición original de las líneas y la estructura del documento.
* **Corrección Automática:** Corrige errores ortográficos y gramaticales en tiempo real sin alterar tecnicismos.
* **Preprocesamiento de Imagen:** Ajuste automático de dimensiones para optimizar el consumo de tokens y mejorar la precisión del análisis.
* **Exportación Directa:** Permite editar el resultado final y descargarlo instantáneamente en formato `.txt`.

---

## Stack Tecnológico

* **Core Engine:** [Google Gemini API](https://ai.google.dev/) (Model: gemini-1.5-flash)
* **Frontend:** [Streamlit](https://streamlit.io/)
* **Procesamiento de Imágenes:** [Pillow (PIL)](https://python-pillow.org/)
* **Despliegue:** Optimizado para Streamlit Cloud con manejo de secretos.

---

## Instalación y Configuración

Para ejecutar este proyecto localmente, seguí estos pasos:

1.  **Cloná el repositorio:**
    ```bash
    git clone [https://github.com/tu-usuario/ai-note-digitizer.git](https://github.com/tu-usuario/ai-note-digitizer.git)
    cd ai-note-digitizer
    ```

2.  **Instalá las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configurá tu API Key:**
    * Obtené una clave gratuita en [Google AI Studio](https://aistudio.google.com/).
    * Creá un archivo `.streamlit/secrets.toml` y agregá tu clave:
        ```toml
        GEMINI_API_KEY = "TU_API_KEY_AQUÍ"
        ```

4.  **Iniciá la aplicación:**
    ```bash
    streamlit run app.py
    ```

---

## Modo de Uso

1.  **Carga:** Subí una foto nítida de tu apunte o documento (JPG/PNG).
2.  **Visualización:** El sistema mostrará la imagen original a la izquierda para comparar.
3.  **Procesamiento:** Hacé clic en **"Procesar e iniciar extracción"**. La IA analizará la imagen y generará el texto en la columna derecha.
4.  **Edición y Descarga:** Revisá el texto en el editor integrado, realizá ajustes manuales si es necesario y descargá tu archivo digitalizado.

---
*Desarrollado para transformar el estudio analógico en un flujo de trabajo digital eficiente.*
