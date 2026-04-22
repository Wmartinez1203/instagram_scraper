# 📸 Instagram Scraper

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Playwright](https://img.shields.io/badge/Playwright-Automated-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

Herramienta de automatización y extracción de datos para Instagram desarrollada en Python utilizando **Playwright**. Este proyecto permite la recolección eficiente de información pública mediante la simulación de navegación humana y gestión avanzada de sesiones.

## 🚀 Características
- **Autenticación Segura:** Gestión de sesiones mediante `cookies.json` para evitar logins repetitivos y reducir el riesgo de baneo.
- **Motor Playwright:** Navegación automatizada de alto rendimiento compatible con Chromium.
- **Arquitectura Modular:** Código organizado en módulos (`auth_manager`, `scraper_engine`, `data_parser`) para facilitar el mantenimiento y escalabilidad.
- **Manejo de Datos:** Exportación y procesamiento de la información recolectada de manera estructurada.

## 🛠️ Tecnologías Utilizadas
- **Lenguaje:** Python 3.x
- **Automatización:** Playwright (Chromium)
- **Gestión de Sesiones:** JSON Web Tokens/Cookies
- **IDE:** PyCharm / VS Code

## 📋 Requisitos Previos
Asegúrate de tener instalado Python y el gestor de paquetes pip. Luego, instala las dependencias necesarias:

```bash
# Clonar el repositorio
git clone [https://github.com/Wmartinez1203/instagram_scraper.git](https://github.com/Wmartinez1203/instagram_scraper.git)
cd instagram_scraper

# Instalar dependencias (asegúrate de tener tu venv activo)
pip install -r requirements.txt

# Instalar los navegadores necesarios para Playwright
playwright install chromium
