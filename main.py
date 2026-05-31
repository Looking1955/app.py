import streamlit as st

# =====================================================================
# CONFIGURACIÓN Y ESTILOS
# =====================================================================
st.set_page_config(page_title="Evaluación Oral USS", layout="wide")

st.markdown("""
<style>
    .titulo-panel { font-size: 26px; font-weight: bold; margin-bottom: 20px; color: #0C2340; }
    .cuadro-cedula { background-color: #F0F4F8; padding: 15px; border-radius: 8px; border-left: 6px solid #0C2340; color: #102A43; font-size: 18px; font-weight: bold; margin-bottom: 20px;}
    .cuadro-pregunta { background-color: #FFFBEA; padding: 15px; border-radius: 8px; border-left: 6px solid #D97706; color: #78350F; font-size: 16px; margin-bottom: 15px; font-weight: 500; }
    .feedback-correcta { color: #38A169; font-weight: bold; margin-top: 10px; }
    .feedback-incorrecta { color: #E53E3E; font-weight: bold; margin-top: 10px; }
</style>
""", unsafe_allow_html=True)

# =====================================================================
# BANCO DE DATOS REDUCIDO (LÍNEAS CORTAS ANTI-CORTE)
# =====================================================================
DATOS_CEDULAS = {
    1: "CÉDULA 1.- El Derecho y la Moral. Normas de trato social.",
    2: "CÉDULA 2.- La norma jurídica.",
    3: "CÉDULA 3.- Vigencia, validez y eficacia.",
    4: "CÉDULA 4.- Plenitud hermética y lagunas del Derecho.",
    5: "CÉDULA 5.- Fuentes del ordenamiento jurídico.",
    6: "CÉDULA 6.- La costumbre.",
    7: "CÉDULA 7.- La jurisprudencia y la doctrina.",
    8: "CÉDULA 8.- La Relación Jurídica.",
    9: "CÉDULA 9.- La persona jurídica.",
    10: "CÉDULA 10.- Derechos reales y derechos personales.",
    11: "CÉDULA 11.- Límites y el abuso del derecho.",
    12: "CÉDULA 12.- Los bienes. Clasificación.",
    13: "CÉDULA 13.- Régimen de bienes y específicos.",
    14: "CÉDULA 14.- Bienes comerciables e incomerciables."
}

SUBPREGUNTAS = {
    1: {
        "enunciado": "¿Cuál es la distinción correcta según autonomía o heteronomía?",
        "alternativas": [
            "A) La Moral es heterónoma y el Derecho es autónomo.",
            "B) La Moral es autónoma y el Derecho es heterónomo (impuesto externamente).",
            "C) Ambos órdenes poseen la misma naturaleza obligatoria."
        ],
        "correcta": "B) La Moral es autónoma y el Derecho es heterónomo (impuesto externamente)."
    },
    2: {
        "enunciado": "¿Qué distingue a una norma imperativa de una permisiva?",
        "alternativas": [
            "A) La imperativa ordena; la permisiva concede una facultad o derecho.",
            "B) La imperativa se modifica por libre voluntad de las partes.",
            "C) Las normas permisivas conllevan sanciones de cárcel."
        ],
        "correcta": "A) La imperativa ordena; la permisiva concede una facultad o derecho."
    },
    3: {
        "enunciado": "¿Cuándo ocurre una derogación tácita en Chile?",
        "alternativas": [
            "A) Cuando una nueva ley declara explícitamente abolida la anterior.",
            "B) Cuando la nueva ley es incompatible con la anterior, sin mencionarla.",
            "C) Cuando la ley cumple el plazo fijado para su vigencia."
        ],
        "correcta": "B) Cuando la nueva ley es incompatible con la anterior, sin mencionarla."
    },
    4: {
        "enunciado": "¿En qué consiste el Principio de Inexcusabilidad judicial?",
        "alternativas": [
            "A) El juez puede negarse a fallar si hay contradicciones.",
            "B) El legislador debe redactar leyes perfectas sin lagunas.",
            "C) Obliga a jueces a resolver aun a falta de ley expresa."
        ],
        "correcta": "C) Obliga a jueces a resolver aun a falta de ley expresa."
    },
    5: {
        "enunciado": "¿Cuáles son los tipos de fuentes según la doctrina?",
        "alternativas": [
            "A) Fuentes Materiales (factores) y Fuentes Formales (textos expresos).",
            "B) Fuentes Internas y Fuentes Administrativas.",
            "C) Leyes penale
