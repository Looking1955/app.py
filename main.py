import streamlit as st

# ==========================================
# CONFIGURACIÓN Y ESTILOS
# ==========================================
st.set_page_config(page_title="Examen USS", layout="wide")

st.markdown("""
<style>
    .titulo { font-size: 24px; font-weight: bold; color: #0C2340; }
    .cuadro { background-color: #F0F4F8; padding: 15px; border-radius: 8px; font-size: 16px; font-weight: bold; margin-bottom: 15px;}
    .pregunta { background-color: #FFFBEA; padding: 15px; border-radius: 8px; font-size: 15px; margin-bottom: 15px; }
    .ok { color: #38A169; font-weight: bold; }
    .fail { color: #E53E3E; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# ==========================================
# BANCO DE DATOS (TEXTO PLANO ULTRA CORTO)
# ==========================================
CEDULAS = {
    1: "CÉDULA 1: Derecho y Moral.",
    2: "CÉDULA 2: La norma jurídica.",
    3: "CÉDULA 3: Vigencia y validez.",
    4: "CÉDULA 4: Lagunas del Derecho.",
    5: "CÉDULA 5: Fuentes del Derecho.",
    6: "CÉDULA 6: La costumbre.",
    7: "CÉDULA 7: Jurisprudencia y doctrina.",
    8: "CÉDULA 8: La Relación Jurídica.",
    9: "CÉDULA 9: La persona jurídica.",
    10: "CÉDULA 10: Derechos reales y personales.",
    11: "CÉDULA 11: Abuso del derecho.",
    12: "CÉDULA 12: Los bienes.",
    13: "CÉDULA 13: Régimen de bienes raíces.",
    14: "CÉDULA 14: Bienes comerciables."
}

CUESTIONARIO = {
    1: {
        "p": "¿Distinción por autonomía?",
        "ops": ["A) Moral heterónoma.", "B) Moral autónoma, Derecho heterónomo.", "C) Son iguales."],
        "ok": "B) Moral autónoma, Derecho heterónomo."
    },
    2: {
        "p": "¿Norma imperativa vs permisiva?",
        "ops": ["A) Imperativa obliga; permisiva faculta.", "B) Se modifican por voluntad.", "C) Tienen cárcel."],
        "ok": "A) Imperativa obliga; permisiva faculta."
    },
    3: {
        "p": "¿Cuándo hay derogación tácita?",
        "ops": ["A) Si es expresa.", "B) Nueva ley es incompatible.", "C) Por cumplimiento de plazo."],
        "ok": "B) Nueva ley es incompatible."
    },
    4: {
        "p": "¿Qué es la Inexcusabilidad?",
        "ops": ["A) No fallar por dudas.", "B) Leyes sin lagunas.", "C) Juez debe resolver aun sin ley."],
        "ok": "C) Juez debe resolver aun sin ley."
    },
    5: {
        "p": "¿Tipos de fuentes doctrinales?",
        "ops": ["A) Materiales y Formales.", "B) Internas y Externas.", "C) Penales y Decretos."],
        "ok": "A) Materiales y Formales."
    },
    6: {
        "p": "¿Valor de costumbre en Civil?",
        "ops": ["A) Absoluto sobre ley.", "B) Solo cuando ley se remite.", "C) Rige en materia penal."],
        "ok": "B) Solo cuando ley se remite."
    },
    7: {
        "p": "¿Efecto de sentencias (Art 3)?",
        "ops": ["A) General ciudadano.", "B) Relativo a la causa juzgada.", "C) Precedente obligatorio."],
        "ok": "B) Relativo a la causa juzgada."
    },
    8: {
        "p": "¿Cuándo nace la persona?",
        "ops": ["A) Concepción.", "B) A los 18 años.", "C) Separación y vivir un instante."],
        "ok": "C) Separación y vivir un instante."
    },
    9: {
        "p": "¿Qué ley rige marco económico?",
        "ops": ["A) Ley 21.595 de delitos.", "B) Código de Comercio.", "C) Ordenanza municipal."],
        "ok": "A) Ley 21.595 de delitos."
    },
    10: {
        "p": "¿Qué es un Derecho Real?",
        "ops": ["A) Sobre una cosa sin respecto a persona.", "B) Contra personas obligadas.", "C) Vínculo mercantil."],
        "ok": "A) Sobre una cosa sin respecto a persona."
    },
    11: {
        "p": "¿Qué frena el abuso del derecho?",
        "ops": ["A) Autonomía.", "B) La Buena Fe.", "C) Plazos de prescripción."],
        "ok": "B) La Buena Fe."
    },
    12: {
        "p": "¿Qué es inmueble por destinación?",
        "ops": ["A) Muebles para uso del fundo.", "B) Adheridos al suelo.", "C) Acciones judiciales."],
        "ok": "A) Muebles para uso del fundo."
    },
    13: {
        "p": "¿Diferencia en enajenación?"
