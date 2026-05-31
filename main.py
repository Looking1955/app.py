import streamlit as st

# =====================================================================
# CONFIGURACIÓN DE LA PÁGINA
# =====================================================================
st.set_page_config(page_title="Evaluación Oral USS", layout="wide")

# =====================================================================
# ESTILOS CSS (Corregidos para evitar pantallas en blanco)
# =====================================================================
st.markdown("""
<style>
    .titulo-panel { font-size: 28px; font-weight: bold; margin-bottom: 20px; color: #0C2340; }
    .cuadro-cedula { background-color: #F0F4F8; padding: 20px; border-radius: 8px; border-left: 6px solid #0C2340; color: #102A43; font-size: 20px; font-weight: bold; margin-bottom: 25px;}
    .cuadro-pregunta { background-color: #FFFBEA; padding: 20px; border-radius: 8px; border-left: 6px solid #D97706; color: #78350F; font-size: 18px; margin-bottom: 20px; font-weight: 500; }
    .cuadro-resultado { background-color: #E6FFFA; padding: 25px; border-radius: 8px; border-left: 6px solid #319795; font-size: 22px; text-align: center; color: #234E52; }
    .feedback-correcta { color: #38A169; font-weight: bold; margin-top: 10px; }
    .feedback-incorrecta { color: #E53E3E; font-weight: bold; margin-top: 10px; }
</style>
""", unsafe_allow_html=True)

# =====================================================================
# BANCO DE DATOS DEL CEDULARIO OFICIAL (USS 2026)
# =====================================================================
# Mapeo de títulos de cédulas
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

# Subpreguntas y respuestas del examen
SUBPREGUNTAS = {
    1: [
        {
            "enunciado": "Respecto a las diferencias entre Derecho y Moral, ¿cuál es la distinción correcta según su autonomía o heteronomía?",
            "alternativas": [
                "A) La Moral es heterónoma y el Derecho es autónomo.",
                "B) La Moral es autónoma (surge del propio sujeto) y el Derecho es heterónomo (es impuesto por una voluntad externa/Estado).",
                "C) Ambos órdenes poseen la misma naturaleza del trato social obligatorio."
            ],
            "correcta": "B) La Moral es autónoma (surge del propio sujeto) y el Derecho es heterónomo (es impuesto por una voluntad externa/Estado)."
        }
    ],
    2: [
        {
            "enunciado": "¿Qué distingue radicalmente a una norma jurídica imperativa de una permisiva?",
            "alternativas": [
                "A) La imperativa ordena hacer algo de forma obligatoria; la permisiva concede una facultad o derecho al sujeto para actuar si lo desea.",
                "B) La imperativa puede ser modificada por la libre voluntad de las partes contratantes.",
                "C) Las normas permisivas conllevan sanciones de cárcel automáticas."
            ],
            "correcta": "A) La imperativa ordena hacer algo de forma obligatoria; la permisiva concede una facultad o derecho al sujeto para actuar si lo desea."
        }
    ],
    3: [
        {
            "enunciado": "¿Cuándo ocurre una derogación de tipo 'Tácita' de la ley en el ord
