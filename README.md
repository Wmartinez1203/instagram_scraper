📸 Instagram Scraper
Herramienta de automatización y extracción de datos para Instagram desarrollada en Python utilizando Playwright. Este proyecto permite la recolección eficiente de información pública mediante la simulación de navegación humana y gestión de sesiones.

🚀 Características
Autenticación Segura: Gestión de sesiones mediante cookies.json para evitar logins repetitivos y reducir el riesgo de baneo.

Motor Playwright: Navegación automatizada de alto rendimiento compatible con Chromium.

Arquitectura Modular: Código organizado en módulos (auth_manager, scraper_engine, data_parser) para facilitar el mantenimiento.

Manejo de Datos: Exportación y procesamiento de la información recolectada de manera estructurada.

🛠️ Tecnologías Utilizadas
Lenguaje: Python 3.x

Automatización: Playwright (Chromium)

Gestión de Sesiones: JSON Web Tokens/Cookies

Entorno: Virtualenv

📋 Requisitos Previos
Asegúrate de tener instalado Python y el gestor de paquetes pip. Luego, instala las dependencias necesarias:
# Clonar el repositorio
git clone https://github.com/Wmartinez1203/instagram_scraper.git
cd instagram_scraper

# Instalar dependencias
pip install -r requirements.txt

# Instalar los navegadores de Playwright
playwright install chromium

⚙️ Configuración y Uso
Credenciales: Asegúrate de configurar tus credenciales o cargar tu sesión en la carpeta session/. (Nota: No compartas tu archivo cookies.json en el repositorio público).

Ejecución:
python main.py
📁 Estructura del Proyecto
instagram_scraper/
├── src/                # Lógica central del scraper
│   ├── auth_manager.py  # Gestión de login y cookies
│   ├── scraper_engine.py # Motor de navegación
│   ├── data_parser.py    # Procesamiento de datos HTML/JSON
│   └── output_manager.py # Guardado de resultados
├── session/            # Almacenamiento de sesiones (ignorado en git)
├── main.py             # Punto de entrada principal
└── .gitignore          # Archivos excluidos del control de versiones
⚖️ Aviso Legal
Este proyecto fue desarrollado únicamente con fines educativos y de investigación. El uso de este script para extraer datos de Instagram debe cumplir con los Términos de Servicio de la plataforma. El autor no se hace responsable del mal uso de esta herramienta.
