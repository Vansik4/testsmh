import streamlit as st
import pandas as pd

# Crear un DataFrame de pandas con dos columnas y 10 filas
data = {
    'id cliente': ['1234567', '2345678', '3456789', '4567890', '5678901', '6789012', '7890123', '8901234', '9012345', '0123456'],
    'invoice number': ['0000001', '0000002', '0000003', '0000004', '0000005', '0000006', '0000007', '0000008', '0000009', '0000010']
}

df = pd.DataFrame(data)

# Configurar la página
st.set_page_config(page_title='Invoices Without PDF', page_icon=':file_folder:', layout='centered')

# Estilos CSS
st.markdown("""
    <style>
        body {
            background-color: #000000;
            color: #ffffff;
        }
        .main {
            background-color: #000000;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(255, 255, 255, 0.1);
        }
        .stDataFrame {
            border: 1px solid #ffffff;
            border-radius: 5px;
            overflow: hidden;
        }
        .stImage {
            border-radius: 10px;
        }
        .report-view {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }
        h1, h2, h3, h4, h5, h6, p {
            color: #ffffff;
        }
    </style>
    """, unsafe_allow_html=True)

# Aplicar estilo a la página principal
st.markdown("""
    <div class="report-view">
        <div class="main">
""", unsafe_allow_html=True)

# Mostrar el título y subtítulo
st.title('List of Invoices Without PDF in OneDrive')
st.markdown('### A report of invoices missing their associated PDF files.')
st.write('This report helps you identify the invoices that need their PDF files uploaded to OneDrive.')

# Crear una columna para la imagen y otra para la tabla
col1, col2 = st.columns([1, 3])

# Mostrar la imagen en la primera columna
with col1:
    st.image('https://revistacentrozaragoza.com/wp-content/uploads/2019/09/mann-2.jpg', use_column_width=True)

# Mostrar la tabla en la segunda columna
with col2:
    st.markdown('#### Invoices Missing PDFs')
    st.dataframe(df.style.set_properties(**{
        'background-color': '#000000',
        'color': '#ffffff',
        'border-color': '#ffffff',
        'border-style': 'solid',
        'border-width': '1px',
        'border-radius': '5px',
        'padding': '10px',
        'font-size': '14px',
        'text-align': 'center'
    }))

# Footer
st.markdown("""
        </div>
    </div>
    <hr>
    <footer>
        <p style="text-align: center; color: #ffffff;">&copy; 2024 MANN+HUMMEL. All rights reserved.</p>
    </footer>
    """, unsafe_allow_html=True)


