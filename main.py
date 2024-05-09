import streamlit as st

from utils import get_rect_area_panels_count_and_fig

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

st.text('')
st.write('Dimensiones de los paneles solares')
col1, col2 = st.columns(2)

with col1:
    panel_dim1 = st.number_input('Ancho', value=0.0, key='panel_dim1_input')

with col2:
    panel_dim2 = st.number_input('Largo', value=0.0, key='panel_dim2_input')

st.text('')
if st.button('Calcular cuántos paneles caben', type='primary'):
    panels_count, fig = get_rect_area_panels_count_and_fig(
        panel_dim1, panel_dim2, area_dim1, area_dim2
    )

    st.write(f'### Caben {panels_count} paneles')

    st.pyplot(None)
