import asyncio
from src.scraper_engine import ScraperEngine
from src.output_manager import OutputManager


async def main():
    print("--- Instagram Professional Scraper ---")
    target = input("Ingrese el nombre de usuario: ").strip()

    scraper = ScraperEngine()
    raw_data = await scraper.scrape_profile(target)

    if raw_data:
        OutputManager.save_data(raw_data, f"{target}_results")
        print(f"\n[!] PROCESO EXITOSO. Archivos listos en /data")
    else:
        print("\n[X] No se extrajeron datos. Revisa la conexión o las cookies.")


if __name__ == "__main__":
    asyncio.run(main())