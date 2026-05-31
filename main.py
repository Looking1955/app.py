import streamlit as st

st.set_page_config(page_title="Evaluación Oral USS", layout="wide")

st.markdown("""
<style>
    .titulo-panel { font-size: 28px; font-weight: bold; margin-bottom: 20px; color: #0C2340; }
    .cuadro-cedula { background-color: #F0F4F8; padding: 20px; border-radius: 8px; border-left: 6px solid #0C2340; color: #102A43; font-size: 20px; font-weight: bold; margin-bottom: 25px;}
    .cuadro-pregunta { background-color: #FFFBEA; padding: 20px; border-radius: 8px; border-left: 6px solid #D97706; color: #78350F; font-size: 18px; margin-bottom: 20px; font-weight: 500; }
    .feedback-correcta { color: #38A169; font-weight: bold; margin-top: 10px; }
    .feedback-incorrecta { color: #E53E3E; font-weight: bold; margin-top: 10px; }
</style>
""", unsafe_allow_html=True)

DATOS_CEDULAS = {
    1: "CÉDULA 1.- El Derecho y la Moral. Normas de uso y trato social.",
    2: "CÉDULA 2.- La norma jurídica.",
    3: "CÉDULA 3.- Vigencia, validez y eficacia del Derecho positivo.",
    4: "CÉDULA 4.- La plenitud hermética del ordenamiento jurídico y las lagunas del Derecho.",
    5: "CÉDULA 5.- Fuentes del ordenamiento jurídico.",
    6: "CÉDULA 6.- La costumbre.",
    7: "CÉDULA 7.- La jurisprudencia y la doctrina, como fuentes formales del Derecho.",
    8: "CÉDULA 8.- La Relación Jurídica.",
    9: "CÉDULA 9.- La persona jurídica.",
    10: "CÉDULA 10.- Derechos reales y derechos personales.",
    11: "CÉDULA 11.- Límites en el ejercicio de los derechos subjetivos y el abuso del derecho.",
    12: "CÉDULA 12.- Los bienes (o cosas). Clasificación.",
    13: "CÉDULA 13.- Régimen de bienes, bienes registrables y específicos.",
    14: "CÉDULA 14.- Bienes o cosas comerciables e incomerciables."
}

SUBPREGUNTAS = {
    1: [{
        "enunciado": "Respecto a las diferencias entre Derecho y Moral, ¿cuál es la distinción correcta según su autonomía o heteronomía?",
        "alternativas": [
            "A) La Moral es heterónoma y el Derecho es autónomo.",
            "B) La Moral es autónoma (surge del propio sujeto) y el Derecho es heterónomo (es impuesto por una voluntad externa/Estado).",
            "C) Ambos órdenes poseen la misma naturaleza del trato social obligatorio."
        ],
        "correcta": "B) La Moral es autónoma (surge del propio sujeto) y el Derecho es heterónomo (es impuesto por una voluntad externa/Estado)."
    }]
}

defaults = {
    "cedula_actual": 1,
    "fase": "SELECCION_CEDULA",
    "respuestas_usuario": {}
}

for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v

cedula = st.session_state.cedula_actual

if st.session_state.fase == "SELECCION_CEDULA":
    st.markdown("<div class='titulo-panel'>Examen de Introducción al Derecho (USS) ⚖️</div>", unsafe_allow_html=True)

    opcion_cedula = st.selectbox(
        "Listado Oficial de Cédulas:",
        options=list(DATOS_CEDULAS.keys()),
        format_func=lambda x: DATOS_CEDULAS[x]
    )

    st.session_state.cedula_actual = opcion_cedula

    st.markdown(f"<div class='cuadro-cedula'>{DATOS_CEDULAS[opcion_cedula]}</div>", unsafe_allow_html=True)

    if st.button("Comenzar a Responder esta Cédula 🚀", use_container_width=True):
        st.session_state.fase = "SUBPREGUNTAS"
        st.rerun()

elif st.session_state.fase == "SUBPREGUNTAS":
    if cedula not in SUBPREGUNTAS:
        st.error("No existen preguntas configuradas para esta cédula.")
        st.stop()

    pregunta = SUBPREGUNTAS[cedula][0]

    st.markdown(f"<div class='titulo-panel'>Evaluando: Cédula N. {cedula}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='cuadro-pregunta'>{pregunta['enunciado']}</div>", unsafe_allow_html=True)

    respuesta = st.radio(
        "Selecciona la opción correcta:",
        pregunta["alternativas"],
        key=f"res_{cedula}"
    )

    if st.button("Verificar Respuesta 🎯"):
        st.session_state.respuestas_usuario[cedula] = respuesta
        st.session_state.fase = "RESULTADOS"
        st.rerun()

elif st.session_state.fase == "RESULTADOS":
    pregunta = SUBPREGUNTAS[cedula][0]
    usuario = st.session_state.respuestas_usuario.get(cedula)

    st.markdown("<div class='titulo-panel'>Resultado</div>", unsafe_allow_html=True)

    if usuario == pregunta["correcta"]:
        st.markdown("<div class='feedback-correcta'>🟢 Respuesta correcta.</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div class='feedback-incorrecta'>🔴 Respuesta incorrecta.</div>", unsafe_allow_html=True)
        st.success(f"Respuesta correcta: {pregunta['correcta']}")

    if st.button("Volver al Menú"):
        st.session_state.fase = "SELECCION_CEDULA"
        st.rerun()
