import streamlit as st

def main():
    st.set_page_config(page_title="Bradescard", page_icon='logo.png')
    hide_st_style = """
        <style>
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        </style>
    """
    st.markdown(hide_st_style, unsafe_allow_html=True)

    with st.sidebar:
        st.image('logo_sidebar.png')
        st.page_link("main.py", label="Regresar a Inicio", icon="🏠")
        st.page_link("pages/compare.py", label="Comparar Modelos", icon="⚖️")
        st.page_link("pages/predict.py", label="Predecir (simulador)", icon="📈")

    st.markdown('# Enfoque del Proyecto')

    # 🎯 Objetivos
    st.markdown('### 🎯 Objetivos')
    st.markdown("""
    **CobraSmart** busca anticipar el comportamiento de pago de clientes, segmentando la cartera por producto y grupo (ABC), 
    generando predicciones de pago mensuales y ofreciendo estrategias de cobranza personalizadas, todo desde una interfaz clara e intuitiva.
    """)

    # 📚 Teoría
    st.markdown('### 📚 Teoría')

    st.markdown('##### Segmentación ABC')
    st.markdown("""
    Clasifica clientes por su contribución a la deuda:
    - **A**: 20% de clientes, ~80% de la deuda.
    - **B**: 15% de la deuda.
    - **C**: Resto de los clientes.
    """)

    st.markdown('##### Predicción y Modelos')
    st.markdown("""
    Se aplicaron modelos de regresión supervisada para estimar el pago mensual (`Pago_M1`) de cada cliente:
    - **Random Forest**: modelo basado en múltiples árboles de decisión.
    - **Red Neuronal**: red básica para patrones no lineales.
    - **Modelo Bayesiano**: enfoque probabilístico con intervalos de credibilidad.
    """)

    with st.expander("Ventajas y desventajas por modelo"):
        st.markdown("""
        **🌲 Random Forest**
        - ✔️ Robusto, no lineal, interpretable.
        - ❌ Menos eficaz en relaciones complejas.

        **🧠 Red Neuronal**
        - ✔️ Capta relaciones no lineales, buena precisión.
        - ❌ Difícil de interpretar, requiere más cómputo.

        **📊 Modelo Bayesiano**
        - ✔️ Probabilístico, flexible, incluye incertidumbre.
        - ❌ Computacionalmente costoso.
        """)

    # 📊 Resultados
    st.markdown('### 📊 Resultados')
    st.markdown("""
    Los modelos obtuvieron un rendimiento consistente ($R^2 > 0.80$). La segmentación y las predicciones permitieron diseñar 
    estrategias efectivas de cobranza personalizadas por perfil, mejorando la recuperación de deuda.
    """)
    st.image('PP_ABC.png', width=500, caption='Segmentación ABC en préstamos personales')

if __name__ == '__main__':
    main()