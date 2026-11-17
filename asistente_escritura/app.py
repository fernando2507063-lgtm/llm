
import streamlit as st
import google.generativeai as genai

# Configuración de la página
st.set_page_config(
    page_title="Asistente de Escritura IA",
    page_icon="✍️",
    layout="centered"
)

st.title("✍️ Asistente de Escritura Automática")
st.write(
    "Proyecto de Inteligencia Artificial - Hybridge. "
    "Mejora tus textos, continúa ideas y genera contenido con Gemini."
)

# Configuración de la API
api_key = st.text_input(
    "Ingresa tu API Key de Google Gemini:",
    type="password"
)

MODELO = "gemini-2.5-flash"

def generar_respuesta(prompt):
    genai.configure(api_key=api_key)
    modelo = genai.GenerativeModel(MODELO)
    respuesta = modelo.generate_content(prompt)
    return respuesta.text

if api_key:
    st.success("Clave ingresada. Puedes utilizar el asistente.")

    tarea = st.selectbox(
        "¿En qué te puedo ayudar?",
        (
            "Mejorar redacción y ortografía",
            "Sugerir continuación",
            "Escribir un texto desde cero"
        )
    )

    if tarea == "Mejorar redacción y ortografía":
        texto = st.text_area(
            "Escribe o pega el texto que deseas mejorar:",
            height=180
        )

        if st.button("Mejorar texto"):
            if texto.strip():
                prompt = (
                    "Corrige la ortografía, gramática y redacción "
                    "del siguiente texto. Conserva su significado "
                    "y devuelve únicamente el texto mejorado:\n\n"
                    + texto
                )

                with st.spinner("Mejorando texto..."):
                    try:
                        resultado = generar_respuesta(prompt)
                        st.subheader("Texto mejorado")
                        st.write(resultado)
                    except Exception as e:
                        st.error(f"Error al generar respuesta: {e}")
            else:
                st.warning("Ingresa un texto para continuar.")

    elif tarea == "Sugerir continuación":
        texto = st.text_area(
            "Escribe el inicio de tu texto:",
            height=180
        )

        if st.button("Generar continuación"):
            if texto.strip():
                prompt = (
                    "Continúa el siguiente texto de manera "
                    "coherente, natural y creativa. "
                    "Genera un párrafo adicional:\n\n"
                    + texto
                )

                with st.spinner("Generando continuación..."):
                    try:
                        resultado = generar_respuesta(prompt)
                        st.subheader("Continuación sugerida")
                        st.write(resultado)
                    except Exception as e:
                        st.error(f"Error al generar respuesta: {e}")
            else:
                st.warning("Ingresa el inicio de un texto.")

    elif tarea == "Escribir un texto desde cero":
        tema = st.text_input(
            "¿Sobre qué tema deseas escribir?"
        )

        tono = st.selectbox(
            "Selecciona el tono:",
            (
                "Profesional",
                "Casual",
                "Creativo",
                "Persuasivo"
            )
        )

        if st.button("Generar texto"):
            if tema.strip():
                prompt = (
                    f"Escribe un texto completo sobre: {tema}. "
                    f"Utiliza un tono {tono.lower()}. "
                    "El texto debe ser claro, coherente "
                    "y estar bien estructurado."
                )

                with st.spinner("Escribiendo..."):
                    try:
                        resultado = generar_respuesta(prompt)
                        st.subheader("Texto generado")
                        st.write(resultado)
                    except Exception as e:
                        st.error(f"Error al generar respuesta: {e}")
            else:
                st.warning("Ingresa un tema para generar el texto.")

else:
    st.info(
        "Ingresa tu API Key de Gemini para comenzar."
    )

st.divider()
st.caption(
    "Proyecto académico - Inteligencia Artificial | Hybridge"
)
