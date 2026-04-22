import asyncio
from src.scraper_engine import ScraperEngine
from src.output_manager import OutputManager


async def main():
    print("--- Instagram Professional Scraper (Versión Universitaria) ---")
    target = input("Ingrese el nombre de usuario (sin @): ").strip()

    scraper = ScraperEngine()
    print("[*] Iniciando motor de extracción...")
    raw_data = await scraper.scrape_profile(target)

    if raw_data:
        OutputManager.save_data(raw_data, f"reporte_{target}")
    else:
        print("\n[X] No se pudo obtener la información. Verifica la red o el usuario.")


if __name__ == "__main__":
    asyncio.run(main())