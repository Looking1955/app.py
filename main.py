import streamlit as st

# =====================================================================
# CONFIGURACIÓN DE LA PÁGINA Y ESTILOS
# =====================================================================
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

# =====================================================================
# BANCO DE DATOS DEL CEDULARIO OFICIAL (USS 2026)
# =====================================================================
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
    1: {
        "enunciado": "Respecto a las diferencias entre Derecho y Moral, ¿cuál es la distinción correcta según su autonomía o heteronomía?",
        "alternativas": [
            "A) La Moral es heterónoma y el Derecho es autónomo.",
            "B) La Moral es autónoma (surge del propio sujeto) y el Derecho es heterónomo (es impuesto por una voluntad externa/Estado).",
            "C) Ambos órdenes poseen la misma naturaleza del trato social obligatorio."
        ],
        "correcta": "B) La Moral es autónoma (surge del propio sujeto) y el Derecho es heterónomo (es impuesto por una voluntad externa/Estado)."
    },
    2: {
        "enunciado": "¿Qué distingue radicalmente a una norma jurídica imperativa de una permisiva?",
        "alternativas": [
            "A) La imperativa ordena hacer algo obligatorio; la permisiva concede una facultad o derecho al sujeto.",
            "B) La imperativa puede ser modificada por la libre voluntad de las partes contratantes.",
            "C) Las normas permisivas conllevan sanciones de cárcel automáticas."
        ],
        "correcta": "A) La imperativa ordena hacer algo obligatorio; la permisiva concede una facultad o derecho al sujeto."
    },
    3: {
        "enunciado": "¿Cuándo ocurre una derogación de tipo tácita de la ley en el ordenamiento jurídico chileno?",
        "alternativas": [
            "A) Cuando una nueva ley declara explícitamente abolida la ley anterior.",
            "B) Cuando la nueva ley contiene disposiciones incompatibles con la anterior, aunque no lo mencione explícitamente.",
            "C) Cuando la ley cumple el plazo de tiempo fijado para su propia vigencia."
        ],
        "correcta": "B) Cuando la nueva ley contiene disposiciones incompatibles con la anterior, aunque no lo mencione explícitamente."
    },
    4: {
        "enunciado": "¿En qué consiste el Principio de Inexcusabilidad judicial con
