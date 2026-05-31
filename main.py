import streamlit as st

# =====================================================================
# CONFIGURACIÓN DE LA PÁGINA Y ESTILOS
# =====================================================================
st.set_page_config(page_title="Evaluación Oral USS", layout="wide")

st.markdown("""
<style>
    .titulo-panel { font-size: 26px; font-weight: bold; margin-bottom: 20px; color: #0C2340; }
    .cuadro-cedula { background-color: #F0F4F8; padding: 18px; border-radius: 8px; border-left: 6px solid #0C2340; color: #102A43; font-size: 18px; font-weight: bold; margin-bottom: 20px;}
    .cuadro-pregunta { background-color: #FFFBEA; padding: 18px; border-radius: 8px; border-left: 6px solid #D97706; color: #78350F; font-size: 16px; margin-bottom: 15px; font-weight: 500; }
    .feedback-correcta { color: #38A169; font-weight: bold; margin-top: 10px; }
    .feedback-incorrecta { color: #E53E3E; font-weight: bold; margin-top: 10px; }
</style>
""", unsafe_allow_html=True)

# =====================================================================
# BANCO DE DATOS OFICIAL
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

CUESTIONARIO = {
    1: {
        "pregunta": "¿Cuál es la distinción correcta según autonomía o heteronomía?",
        "alternativas": [
            "A) La Moral es heterónoma y el Derecho es autónomo.",
            "B) La Moral es autónoma y el Derecho es heterónomo.",
            "C) Ambos órdenes poseen la misma naturaleza obligatoria."
        ],
        "correcta": "B) La Moral es autónoma y el Derecho es heterónomo."
    },
    2: {
        "pregunta": "¿Qué distingue a una norma imperativa de una permisiva?",
        "alternativas": [
            "A) La imperativa ordena; la permisiva concede una facultad.",
            "B) La imperativa se modifica por libre voluntad.",
            "C) Las normas permisivas conllevan sanciones de cárcel."
        ],
        "correcta": "A) La imperativa ordena; la permisiva concede una facultad."
    },
    3: {
        "pregunta": "¿Cuándo ocurre una derogación tácita en Chile?",
        "alternativas": [
            "A) Cuando una nueva ley declara abolida la anterior.",
            "B) Cuando la nueva ley es incompatible con la anterior.",
            "C) Cuando la ley cumple el plazo de su vigencia."
        ],
        "correcta": "B) Cuando la nueva ley es incompatible con la anterior."
    },
    4: {
        "pregunta": "¿En qué consiste el Principio de Inexcusabilidad judicial?",
        "alternativas": [
            "A) El juez puede negarse a fallar si hay contradicciones.",
            "B) El legislador debe redactar leyes perfectas sin lagunas.",
            "C) Obliga a jueces a resolver aun a falta de ley expresa."
        ],
        "correcta": "C) Obliga a jueces a resolver aun a falta de ley expresa."
    },
    5: {
        "pregunta": "¿Cuáles son los tipos de fuentes según la doctrina?",
        "alternativas": [
            "A) Fuentes Materiales y Fuentes Formales.",
            "B) Fuentes Internas y Fuentes Administrativas.",
            "C) Leyes penales ordinarias y decretos municipales."
        ],
        "correcta": "A) Fuentes Materiales y Fuentes Formales."
    },
    6: {
        "pregunta": "¿Cuál es el valor de la costumbre en e
