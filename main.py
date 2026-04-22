import asyncio
from src.scraper_engine import ScraperEngine
from src.output_manager import OutputManager


async def main():
    print("--- INSTAGRAM DATA ANALYTICS (UCE 2026) ---")
    user = input("Usuario (sin @): ").strip()

    scraper = ScraperEngine()
    data = await scraper.scrape_profile(user)

    if data:
        OutputManager.save_data(data, user)
    else:
        print("[X] No se pudo extraer información. Revisa la red.")


if __name__ == "__main__":
    asyncio.run(main())