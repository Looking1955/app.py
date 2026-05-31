import streamlit as st

# =====================================================================
# CONFIGURACIÓN Y ESTILOS
# =====================================================================
st.set_page_config(page_title="Examen USS", layout="wide")

st.markdown("""
<style>
    .titulo { font-size: 26px; font-weight: bold; margin-bottom: 20px; color: #0C2340; }
    .box-c { background-color: #F0F4F8; padding: 15px; border-radius: 8px; border-left: 6px solid #0C2340; color: #102A43; font-size: 18px; font-weight: bold; margin-bottom: 20px;}
    .box-p { background-color: #FFFBEA; padding: 15px; border-radius: 8px; border-left: 6px solid #D97706; color: #78350F; font-size: 16px; margin-bottom: 15px; }
    .ok { color: #38A169; font-weight: bold; margin-top: 10px; }
    .fail { color: #E53E3E; font-weight: bold; margin-top: 10px; }
</style>
""", unsafe_allow_html=True)

# =====================================================================
# TEXTOS AUXILIARES CORTOS PARA EVITAR TRUNCAMIENTO
# =====================================================================
T1 = "La Moral es autónoma y el Derecho es heterónomo."
T2 = "La imperativa ordena; la permisiva concede facultad."
T3 = "Cuando la nueva ley es incompatible con la anterior."
T4 = "Obliga a jueces a resolver aun a falta de ley."
T5 = "Fuentes Materiales y Fuentes Formales."
T6 = "No constituye derecho sino cuando la ley se remite."
T7 = "Solo respecto de las causas que actualmente juzga."
T8 = "Al separarse de la madre y vivir un momento."
T9 = "La Ley N. 21.595 sobre Delitos Económicos."
T10 = "El que tenemos sobre una cosa sin respecto a persona."
T11 = "El principio de la Buena Fe."
T12 = "Muebles destinados al uso y beneficio de un fundo."
T13 = "Los inmuebles requieren inscripción en el CBR."
T14 = "Su dominio pertenece a la nación y su uso a todos."

# =====================================================================
# BANCO DE DATOS OFICIAL
# =====================================================================
DATOS_CEDULAS = {
    1: "CÉDULA 1: El Derecho y la Moral.",
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
    1: {"p": "¿Distinción por autonomía?", "ops": ["A) Moral heterónoma.", f"B) {T1}", "C) Son iguales."], "ok": f"B) {T1}"},
    2: {"p": "¿Norma imperativa vs permisiva?", "ops": [f"A) {T2}", "B) Se modifican.", "C) Tienen cárcel."], "ok": f"A) {T2}"},
    3: {"p": "¿Cuándo hay derogación tácita?", "ops": ["A) Si es expresa.", f"B) {T3}", "C) Por su plazo."], "ok": f"B) {T3}"},
    4: {"p": "¿Qué es la Inexcusabilidad?", "ops": ["A) No fallar.", "B) Leyes perfectas.", f"C) {T4}"], "ok": f"C) {T4}"},
    5: {"p": "¿Tipos de fuentes doctrinales?", "ops": [f"A) {T5}", "B) Internas.", "C) Municipales."], "ok": f"A) {T5}"},
    6: {"p": "¿Valor de costumbre en Civil?", "ops": ["A) Absoluto.", f"B) {T6}", "C) Rige en penal."], "ok": f"B) {T6}"},
    7: {"p": "¿Efecto de sentencias (Art 3)?", "ops": ["A) General.", f"B) {T7}", "C) Precedente."], "ok": f"B) {T7}"},
    8: {"p": "¿Cuándo nace la persona?", "ops": ["A) Concepción.", "B) A los 18.", f"C) {T8}"], "ok": f"C) {T8}"},
    9: {"p": "¿Qué ley rige marco económico?", "ops": [f"A) {T9}", "B) C. Comercio.", "C) Ordenanza."], "ok": f"A) {T9}"},
    10: {"p": "¿Qué es un Derecho Real?", "ops": [f"A) {T10}", "B) Contra deudores.", "C) Mercantil."], "ok": f"A) {T10}"},
    11: {"p": "¿Qué frena el abuso del derecho?", "ops": ["A) Autonomía.", f"B) {T11}", "C) Plazos."], "ok": f"B) {T11}"},
    12: {"p": "¿Qué es inmueble por destinación
