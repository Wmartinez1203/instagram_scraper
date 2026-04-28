# Instagram Data Analytics & Engagement Scraper (UCE 2026) 📊

Este proyecto es una herramienta de **Ingeniería de Datos** diseñada para automatizar la extracción de métricas de perfiles de Instagram y calcular el **Engagement Rate** en tiempo real. 

Utiliza **Playwright** para la simulación de navegación humana y **Pandas** para el procesamiento analítico.

## 🚀 Características principales
- **Renderizado Dinámico:** Uso de Chromium para procesar Single Page Applications (SPA).
- **Inyección de Sesión:** Autenticación segura mediante el uso de Cookies (sin manejo de contraseñas).
- **Métricas de Marketing:** Cálculo automático del Engagement Rate basado en Seguidores vs. Interacciones.
- **Visualización Pro:** Dashboard interactivo desarrollado en Streamlit.
- **Exportación Dual:** Generación de reportes en formatos Excel (BI) y JSON (Estructurado).

## 🛠️ Instalación y Configuración

1. **Clonar el repositorio:**
   ```bash
   git clone <tu-repositorio>
   cd instagram_scraper

2. **Instalar dependencias:**
    ```bash
    py -m pip install -r requirements.txt
    py -m playwright install chromium

3. **Configurar Sesión:**
    Extraer las cookies de Instagram en formato JSON y guardarlas en session/cookies.json.

Ejecución
    **Fase 1: Extracción de Datos**
    Ejecuta el scraper principal para recolectar información:
    ```bash
    py main.py
    ```
    **Fase 2: Visualización del Dashboard**
    Levanta el servidor web para analizar los resultados gráficamente:
    ```bash
    py -m streamlit run dashboard.py
    ```
**📐 Arquitectura del Proyecto**
El sistema sigue un diseño modular bajo el principio de responsabilidad única:

src/scraper_engine.py: Orquestación del navegador y flujo de navegación.

src/data_parser.py: Lógica de transformación de datos (ETL) y expresiones regulares.

src/auth_manager.py: Gestión de persistencia de sesión.

src/output_manager.py: Capa de persistencia en archivos físicos.

**🛡️ Seguridad y Vulnerabilidades**
Este proyecto implementa un archivo .gitignore estricto para evitar la filtración de Cookies de sesión y tokens de acceso. Se recomienda rotar las cookies periódicamente.
