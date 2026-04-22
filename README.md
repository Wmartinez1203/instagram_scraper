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
```
⚙️ Configuración y Uso
Credenciales: Configura tu sesión inicial para generar el archivo en la carpeta session/.

Nota importante: El archivo cookies.json contiene datos sensibles y está excluido del control de versiones por seguridad.

Ejecución:
```bash
python main.py
```
## 📁 Estructura del Proyecto

```text
instagram_scraper/
├── src/                  # Lógica central del scraper
│   ├── auth_manager.py   # Gestión de login y cookies
│   ├── scraper_engine.py # Motor de navegación y scraping
│   ├── data_parser.py    # Procesamiento de datos recolectados
│   └── output_manager.py # Manejo de archivos de salida
├── session/              # Almacenamiento de sesiones (ignorado en git)
├── main.py               # Punto de entrada principal del script
└── .gitignore            # Archivos y carpetas excluidos
```
⚖️ Aviso Legal
Este proyecto fue desarrollado únicamente con fines educativos y de investigación. El uso de este script para extraer datos de Instagram debe cumplir con los Términos de Servicio de la plataforma. El autor no se hace responsable del mal uso de esta herramienta o de posibles sanciones en las cuentas utilizadas.

Desarrollado por Fernando Martínez Figueroa - Estudiante de Ingeniería en Sistemas de Información.
