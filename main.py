import streamlit as st

# =====================================================================
# CONFIGURACIÓN DE LA PÁGINA
# =====================================================================
st.set_page_config(page_title="Evaluación Oral USS", layout="wide")

# =====================================================================
# ESTILOS CSS
# =====================================================================
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
            "enunciado": "¿Cuándo ocurre una derogación de tipo tacita de la ley en el ordenamiento jurídico chileno?",
            "alternativas": [
                "A) Cuando una nueva ley declara explícitamente abolida la ley anterior.",
                "B) Cuando la nueva ley contiene disposiciones que no pueden conciliarse con la ley anterior, aunque no la mencione expresamente.",
                "C) Cuando la ley cumple el plazo de tiempo fijado para su propia vigencia."
            ],
            "correcta": "B) Cuando la nueva ley contiene disposiciones que no pueden conciliarse con la ley anterior, aunque no la mencione expresamente."
        }
    ],
    4: [
        {
            "enunciado": "¿En qué consiste el Principio de Inexcusabilidad judicial consagrado en Chile?",
            "alternativas": [
                "A) El juez puede negarse a fallar si las leyes civiles presentan contradicciones de jerarquía.",
                "B) El legislador tiene la obligación de redactar leyes perfectas sin ningún tipo de lagunas del derecho.",
                "C) Mandata a los jueces a resolver los conflictos sometidos a su conocimiento aun a falta de ley expresa que resuelva la contienda."
            ],
            "correcta": "C) Mandata a los jueces a resolver los conflictos sometidos a su conocimiento aun a falta de ley expresa que resuelva la contienda."
        }
    ],
    5: [
        {
            "enunciado": "¿Cuáles son los tipos de fuentes del ordenamiento jurídico según la doctrina?",
            "alternativas": [
                "A) Fuentes Materiales (factores sociales, políticos, morales) y Fuentes Formales (los modos o textos de expresión del derecho positivo).",
                "B) Fuentes Internas y Fuentes Administrativas territoriales.",
                "C) Leyes penales ordinarias y decretos municipales."
            ],
            "correcta": "A) Fuentes Materiales (factores sociales, políticos, morales) y Fuentes Formales (los modos o textos de expresión del derecho positivo)."
        }
    ],
    6: [
        {
            "enunciado": "¿Cuál es el valor general de la costumbre como fuente en el Derecho Civil chileno?",
            "alternativas": [
                "A) Tiene valor absoluto en cualquier caso por sobre la ley escrita.",
                "B) No constituye derecho sino en los casos en que la ley se remite a ella (costumbre según la ley).",
                "C) Rige plenamente en el Derecho Penal para crear nuevos delitos."
            ],
            "correcta": "B) No constituye derecho sino en los casos en que la ley se remite a ella (costumbre según la ley)."
        }
    ],
    7: [
        {
            "enunciado": "Respecto a la jurisprudencia en Chile, ¿cuál es el alcance de la fuerza obligatoria de las sentencias judiciales (Art. 3 del Código Civil)?",
            "alternativas": [
                "A) Tienen fuerza obligatoria de carácter general para toda la ciudadanía.",
                "B) Las sentencias judiciales solo tienen fuerza obligatoria respecto de las causas en que actualmente se pronunciaren (efecto relativo).",
                "C) Vinculan obligatoriamente a todos los jueces del país bajo la doctrina del precedente obligatorio."
            ],
            "correcta": "B) Las sentencias judiciales solo tienen fuerza obligatoria respecto de las causas en que actualmente se pronunciaren (efecto relativo)."
        }
    ],
    8: [
        {
            "enunciado": "Según el Código Civil chileno, ¿cuándo comienza legalmente la existencia de la persona natural?",
            "alternativas": [
                "A) Desde el momento de la concepción en el vientre materno.",
                "B) Al cumplir los 18 años de edad mediante la capacidad de ejercicio.",
                "C) Al separarse completamente de la madre, habiendo sobrevivido a la separación un momento siquiera."
            ],
            "correcta": "C) Al separarse completamente de la madre, habiendo sobrevivido a la separación un momento siquiera."
        }
    ],
    9: [
        {
            "enunciado": "Respecto a la responsabilidad penal de las personas jurídicas en Chile, ¿qué ley regula el marco de delitos económicos actualmente?",
            "alternativas": [
                "A) La Ley N. 21.595 sobre Delitos Económicos y atentados contra el medio ambiente.",
                "B) El Código de Comercio exclusivamente.",
                "C) La ordenanza tributaria de corporaciones municipales."
            ],
            "correcta": "A) La Ley N. 21.595 sobre Delitos Económicos y atentados contra el medio ambiente."
        }
    ],
    10: [
        {
            "enunciado": "De acuerdo al artículo 577 del Código Civil, ¿cuál es la definición legal de Derecho Real?",
            "alternativas": [
                "A) El que tenemos sobre una cosa sin respecto a determinada persona.",
                "B) El que solo puede reclamarse de ciertas personas que por un hecho suyo o la sola disposición de la ley han contraído las obligaciones correlativas.",
                "C) El contrato vinculante que genera derechos mercantiles líquidos."
            ],
            "correcta": "A) El que tenemos sobre una cosa sin respecto a determinada persona."
        }
    ],
    11: [
        {
            "enunciado": "¿Qué principio actúa como una limitación intrínseca al ejercicio de los derechos subjetivos previniendo el abuso del derecho?",
            "alternativas": [
                "A) El principio de la autonomía absoluta del derecho real.",
                "B) El principio de la Buena Fe.",
                "C) La irretroactividad de las leyes de orden público."
            ],
            "correcta": "B) El principio de la Buena Fe."
        }
    ],
    12: [
        {
            "enunciado": "¿Qué categoría corresponde a los inmuebles por destinación según la ley chilena (Art. 570 CC)?",
            "alternativas": [
                "A) Cosas muebles que se encuentran permanentemente destinadas al uso, cultivo y beneficio de un inmueble.",
                "B) Cosas que adhieren permanentemente al suelo, como los edificios o árboles.",
                "C) Los derechos y las acciones judiciales que se ejercen sobre fincas."
            ],
            "correcta": "A) Cosas muebles que se encuentran permanentemente destinadas al uso, cultivo y beneficio de un inmueble."
        }
    ],
    13: [
        {
            "enunciado": "¿Cuál es la principal diferencia formal en el régimen jurídico de enajenación entre bienes muebles e inmuebles?",
            "alternativas": [
                "A) Los bienes muebles requieren escritura pública obligatoria en todos los casos.",
                "B) Los bienes inmuebles requieren por regla general solemnidades especiales (como Escritura Pública e Inscripción en el Conservador de Bienes Raíces) para su tradición.",
                "C) Los bienes raíces se transfieren mediante la simple entrega material o manual de la llave del predio."
            ],
            "correcta": "B) Los bienes inmuebles requieren por regla general solemnidades especiales (como Escritura Pública e Inscripción en el Conservador de Bienes Raíces) para su tradición."
        }
    ],
    14: [
        {
            "enunciado": "¿Qué caracteriza jurídicamente a los Bienes Nacionales de Uso Público?",
            "alternativas": [
                "A) Pertenecen al Estado de forma privada y funcionan igual que los bienes fiscales.",
                "B) Son aquellos cuyo dominio pertenece a la nación toda y su uso pertenece a todos los habitantes (ej. calles, plazas, playas).",
                "C) Son bienes incomerciables absolutos que no admiten ningún tipo de concesión administrativa."
            ],
            "correcta": "B) Son aquellos cuyo dominio pertenece a la nación toda y su uso pertenece a todos los habitantes (ej. calles, plazas, playas)."
        }
    ]
}

# =====================================================================
# LÓGICA DE CONTROL DE ESTADOS DE SESIÓN
# =====================================================================
if "cedula_actual" not in st.session_state:
    st.session_state.cedula_actual = 1
if "fase" not in st.session_state:
    st.session_state.fase = "SELECCION_CEDULA"
if "respuestas_usuario" not in st.session_state:
    st.session_state.respuestas_usuario = {}

# =====================================================================
# RENDERIZADO DE LA INTERFAZ
# =====================================================================
cedula = st.session_state.cedula_actual

if st.session_state.fase == "SELECCION_CEDULA":
    st.markdown("<div class='titulo-panel'>Examen de Introducción al Derecho (USS) ⚖️</div>", unsafe_allow_html=True)
    st.write("Selecciona una Cédula del examen académico para responder:")
    
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
    st.markdown(f"<div class='titulo-panel'>Evaluando: Cédula N. {cedula}</div>", unsafe_allow_html=True)
    
    pregunta = SUBPREGUNTAS[cedula][0]
    st.markdown(f"<div class='cuadro-pregunta'>{pregunta['enunciado']}</div>", unsafe_allow_html=True)
    
    llave_guardado = f"res_{cedula}"
    respuesta_elegida = st.radio(
        "Selecciona la opción correcta:",
        options=pregunta["alternativas"],
        key=llave_guardado
    )
    
    st.write("---")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅️ Cambiar Cédula", use_container_width=True):
            st.session_state.fase = "SELECCION_CEDULA"
            st.rerun()
    with col2:
        if st.button("Verificar Respuesta Enviar 🎯", use_container_width=True):
            st.session_state.respuestas_usuario[cedula] = respuesta_elegida
            st.session_state.fase = "RESULTADOS"
            st.rerun()

elif st.session_state.fase == "RESULTADOS":
    st.markdown("<div class='titulo-panel'>Resultado y Feedback Académico</div>", unsafe_allow_html=True)
    
    pregunta = SUBPREGUNTAS[cedula][0]
    resp_usuario = st.session_state.respuestas_usuario.get(cedula)
    resp_correcta = pregunta["correcta"]
    
    st.markdown(f"<div class='cuadro-cedula'>{DATOS_CEDULAS[cedula]}</div>", unsafe_allow_html=True)
    st.markdown(f"**Pregunta planteada:** {pregunta['enunciado']}")
    st.write(f"**Tu respuesta:** {resp_usuario}")
    
    if resp_usuario == resp_correcta:
        st.markdown("<div class='feedback-correcta'>🟢 ¡CORRECTO! Enfoque doctrinal impecable.</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div class='feedback-incorrecta'>🔴 INCORRECTO. Criterio erróneo según el Código Civil.</div>", unsafe_allow_html=True)
        st.write(f"💡 **La respuesta correcta es:** {resp_correcta}")
        
    st.write("---")
    
    if st.button("Volver al Menú de Cédulas 🔄", use_container_width=True):
        st.session_state.fase = "SELECCION_CEDULA"
        st.rerun()
