import streamlit as st

st.title('¿Cuántos paneles caben?')

st.write(
    'Entrega las dimensiones de un área y de los paneles solares, y te mostraremos cuántos paneles caben en esa área.'
)

st.subheader('Área rectangular')

st.write('Dimensiones del área rectuangular')

col1, col2 = st.columns(2)

with col1:
    area_dim1 = st.number_input('Ancho', value=0.0)

with col2:
    area_dim2 = st.number_input('Largo', value=0.0)
