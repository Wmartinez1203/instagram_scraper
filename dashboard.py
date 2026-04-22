import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Instagram Analytics - UCE", layout="wide")

st.title("📊 Análisis de Engagement - Instagram")
st.markdown("---")

# Buscamos archivos en la carpeta data
if os.path.exists('data'):
    files = [f for f in os.listdir('data') if f.endswith('.xlsx')]

    if files:
        selected_file = st.sidebar.selectbox("Selecciona un reporte:", files)
        df = pd.read_excel(os.path.join('data', selected_file))

        # Métricas principales
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Seguidores", df['followers'].iloc[0])
        with col2:
            st.metric("Posts Analizados", len(df))
        with col3:
            # Promedio de engagement
            # Quitamos el símbolo % para promediar
            avg_eng = df['engagement_rate'].str.replace('%', '').astype(float).mean()
            st.metric("Engagement Promedio", f"{round(avg_eng, 2)}%")

        # Gráfica de Likes
        st.subheader("Interacciones por Publicación")
        st.bar_chart(df.set_index('url')[['likes', 'comentarios']])

        # Tabla detallada
        st.subheader("Datos Extraídos")
        st.dataframe(df)
    else:
        st.warning("No hay reportes en la carpeta /data todavía. ¡Corre el scraper primero!")
else:
    st.error("Carpeta /data no encontrada.")