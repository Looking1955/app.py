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
    1: "CÉDULA 1.- El Derecho y la Moral. Normas de uso y trato social.[span_0](start_span)[span_0](end_span)",
    2: "CÉDULA 2.- La norma jurídica.[span_1](start_span)[span_1](end_span)",
    3: "CÉDULA 3.- Vigencia, validez y eficacia del Derecho positivo.[span_2](start_span)[span_2](end_span)",
    4: "CÉDULA 4.- La plenitud hermética del ordenamiento jurídico y las lagunas del Derecho.[span_3](start_span)[span_3](end_span)",
    5: "CÉDULA 5.- Fuentes del ordenamiento jurídico.[span_4](start_span)[span_4](end_span)",
    6: "CÉDULA 6.- La costumbre.[span_5](start_span)[span_5](end_span)",
    7: "CÉDULA 7.- La jurisprudencia y la doctrina, como fuentes formales del Derecho.[span_6](start_span)[span_6](end_span)",
    8: "CÉDULA 8.- La Relación Jurídica.[span_7](start_span)[span_7](end_span)",
    9: "CÉDULA 9.- La persona jurídica.[span_8](start_span)[span_8](end_span)",
    10: "CÉDULA 10.- Derechos reales y derechos personales.[span_9](start_span)[span_9](end_span)",
    11: "CÉDULA 11.- Límites en el ejercicio de los derechos subjetivos y el abuso del derecho.[span_10](start_span)[span_10](end_span)",
    12: "CÉDULA 12.- Los bienes (o cosas). Clasificación.[span_11](start_span)[span_11](end_span)",
    13: "CÉDULA 13.- Régimen de bienes, bienes registrables y específicos.[span_12](start_span)[span_12](end_span)",
    14: "CÉDULA 14.- Bienes o cosas comerciables e incomerciables.[span_13](start_span)[span_13](end_span)"
}

SUBPREGUNTAS = {
    1: {
        "enunciado": "Respecto a las diferencias entre Derecho y Moral, ¿cuál es la distinción correcta según su autonomía o heteronomía?[span_14](start_span)[span_14](end_span)",
        "alternativas": [
            "A) La Moral es heterónoma y el Derecho es autónomo.",
            "B) La Moral es autónoma (surge del propio sujeto) y el Derecho es heterónomo (es impuesto por una voluntad externa/Estado).",
            "C) Ambos órdenes poseen la misma naturaleza del trato social obligatorio."
        ],
        "correcta": "B) La Moral es autónoma (surge del propio sujeto) y el Derecho es heterónomo (es impuesto por una voluntad externa/Estado)."
    },
    2: {
        "enunciado": "¿Qué distingue radicalmente a una norma jurídica imperativa de una permisiva?[span_15](start_span)[span_15](end_span)",
        "alternativas": [
            "A) La imperativa ordena hacer algo obligatorio; la permisiva concede una facultad o derecho al sujeto.[span_16](start_span)[span_16](end_span)",
            "B) La imperativa puede ser modificada por la libre voluntad de las partes contratantes.",
            "C) Las normas permisivas conllevan sanciones de cárcel automáticas."
        ],
        "correcta": "A) La imperativa ordena hacer algo obligatorio; la permisiva concede una facultad o derecho al sujeto.[span_17](start_span)[span_17](end_span)"
    },
    3: {
