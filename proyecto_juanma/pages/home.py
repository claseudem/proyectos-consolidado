import streamlit as st

# Configuración básica de la app
st.set_page_config(
    page_title="Calculadora Ganadera",
    page_icon="🐄",
    layout="centered"
)

# --- Contenido principal del Home ---
st.title("🐄 Bienvenido a la Calculadora Ganadera")
st.markdown("---")

st.subheader("📘 ¿Qué es esta aplicación?")
st.write("""
Esta herramienta está diseñada para **productores ganaderos, técnicos y estudiantes** 
que deseen **evaluar las condiciones de producción bovina** y estimar el valor económico 
total de su hato de forma rápida e interactiva.

Podrás:
- Seleccionar parámetros como topografía, clima, tipo de pastura, y calidad animal.
- Ingresar datos económicos (precio, peso, cantidad, tiempo).
- Obtener automáticamente:
  - Un **puntaje de condiciones productivas**.
  - El **valor económico total** de tu lote.
  - Y una evaluación general de tus condiciones.

Todo esto en una interfaz sencilla y amigable.
""")

st.subheader("🧭 Cómo navegar en la aplicación")
st.write("""
En el menú lateral (a la izquierda de tu pantalla) encontrarás las siguientes secciones:

1. **Parámetros** → Ingreso de datos técnicos y económicos.  
2. **Resultados** → Visualización de los cálculos realizados.  
3. **Documentación** → Explicación técnica del modelo de cálculo y sus fundamentos.  
""")

st.subheader("💡 Recomendación")
st.info("""
Si es tu primera vez usando la app, comienza por la pestaña **Parámetros** 
para ingresar la información de tu sistema productivo.
""")

st.markdown("---")
st.caption("Desarrollado con ❤️ en Streamlit – Proyecto educativo de cálculo ganadero.")
