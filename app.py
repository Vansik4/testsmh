import streamlit as st
import pandas as pd

# Crear un DataFrame de pandas con dos columnas y 10 filas
data = {
    'Columna 1': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Columna 2': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
}

df = pd.DataFrame(data)

# Mostrar el DataFrame en Streamlit
st.title('Mi tabla de pandas en Streamlit')
st.write(df)
