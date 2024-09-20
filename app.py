import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import StringIO
import time

st.set_page_config(
    page_title="¿Qué voy a comer hoy?",
    page_icon="🍰",
    layout="wide",
    initial_sidebar_state="expanded"
)



def main():
    """
    Main function to set up the Streamlit app layout.
    """
    cs_sidebar()
    cs_body()
    return None

@st.cache_data
def load_data():
    # Supongamos que tu DataFrame está almacenado en un archivo CSV
    df = pd.read_csv("data/recetas.csv")
    return df




# Funciones
def cs_sidebar():
    """
    Populate the sidebar with various content sections related to Python.
    """
    st.sidebar.title("¿Qué voy a comer hoy?")

   
    logo_url = "https://raw.githubusercontent.com/Seth-Nut/st_recipes/main/images/icons/cake.png"
    st.sidebar.image(logo_url, width=200)

    with st.sidebar:
        with st.expander("📄 Descripción del Proyecto"):
         st.write(
            """
            Explora el uso de Python, la API de OpenAI y Streamlit para crear recetas personalizadas y visualmente atractivas. 
            Esta aplicación utiliza inteligencia artificial para recomendar recetas que se ajustan a tus preferencias y momentos del día, 
            destacando opciones chilenas, saludables y veganas. Disfruta de una demostración en vivo de cómo se generan y presentan las recetas automáticamente.
            """
            )
    with st.sidebar:
        with st.expander("🎯 Objetivos"):
            st.write(
            """
            - Facilitar la creación de recetas personalizadas utilizando inteligencia artificial.
            - Demostrar la integración efectiva de tecnologías avanzadas en aplicaciones culinarias.
            - Promover opciones alimenticias saludables y variadas para distintos estilos de vida.
            """
        )
    






def cs_body():
    """
    Create content sections for the main body of the
    Streamlit cheat sheet with Python examples.
    """

    st.title("👨‍🍳👩‍🍳 Explora, cocina y disfruta!")  # Título de la sección

    df = load_data()

    # Crear opciones de filtrado
    tipo_receta = st.selectbox("Selecciona un Tipo de Receta:", ['Todos'] + sorted(df['Tipo_Receta'].unique().tolist()))
    if tipo_receta != 'Todos':
        df = df[df['Tipo_Receta'] == tipo_receta]
    
    receta = st.selectbox("Selecciona una Receta:", ['Todos'] + sorted(df['Receta'].unique().tolist()))
    if receta != 'Todos':
        df = df[df['Receta'] == receta]

    # Iteramos sobre las filas del DataFrame para mostrar cada receta con su imagen
    for index, row in df.iterrows():
        with st.container():
            col1, col2 = st.columns([1, 3])
            # Asumimos que las imágenes están en una subcarpeta llamada 'images/' dentro del directorio donde se ejecuta Streamlit
            image_path = f"images/{row['images']}"
            col1.image(image_path, width=200)  # Ajusta el tamaño según necesites
            col2.subheader(f"{row['Receta']} (Dificultad: {row['Dificultad']}, Tiempo: {row['Tiempo']} minutos)")
            col2.write(f"**Ingredientes:** {row['Ingredientes']}")
            col2.write(f"**Preparación:** {row['Preparacion']}")

   

if __name__ == "__main__":
    main()