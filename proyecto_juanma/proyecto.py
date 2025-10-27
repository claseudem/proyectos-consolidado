import streamlit as st

st.set_page_config(page_title="Cálculo Ganadero", layout="centered")

st.title("🐄 Calculadora de Parámetros Ganaderos")

st.markdown("Completa los siguientes parámetros para calcular el valor total de tu producción.")

# --- Parámetros seleccionables ---
st.header("Parámetros productivos")

topografia = st.selectbox(
    "Topografía",
    options={"Plana": 4, "Ondulada": 3, "Montañoso": 2}
)

clima = st.selectbox(
    "Clima",
    options={"Frío (>18°C)": 2, "Templado (18-24°C)": 3, "Calor (<24°C)": 4}
)

pasturas = st.selectbox(
    "Tipo de pasturas",
    options={"Braquiaria": 4, "Strella africana": 5, "Sabana": 3}
)

calidad_animal = st.selectbox(
    "Calidad del animal",
    options={
        "Cebú puro": 5,
        "Cebú cruzado": 3,
        "Criollos fríos": 4,
        "Cárnicas": 2,
        "Otros": 2
    }
)

suplementacion = st.radio(
    "¿Hay suplementación?",
    options={"Sí": 2, "No": 0}
)

# --- Parámetros numéricos ---
st.header("Datos económicos y de producción")

precio_kg = st.number_input("Precio por kg de animal ($)", min_value=0.0, value=9000.0, step=500.0)
peso_animal = st.number_input("Peso del animal (kg)", min_value=0.0, value=200.0, step=10.0)
meses = st.number_input("Cantidad de meses", min_value=1, value=8, step=1)
cantidad_animales = st.number_input("Cantidad de animales", min_value=1, value=20, step=1)

# --- Cálculo ---
if st.button("Calcular valor total"):
    # Sumatoria de los parámetros cualitativos
    puntaje_total = (
        topografia
        + clima
        + pasturas
        + calidad_animal
        + suplementacion
    )

    # Valor económico por animal
    valor_animal = precio_kg * peso_animal

    # Valor total del lote
    valor_total = valor_animal * cantidad_animales

    st.success("✅ Resultados del cálculo:")

    st.write(f"**Puntaje total de condiciones:** {puntaje_total}")
    st.write(f"**Valor por animal:** ${valor_animal:,.2f}")
    st.write(f"**Valor total ({cantidad_animales} animales):** ${valor_total:,.2f}")
    st.write(f"**Periodo de evaluación:** {meses} meses")

    st.info("Puedes ajustar los valores para simular distintos escenarios.")

