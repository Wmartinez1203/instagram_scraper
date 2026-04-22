import asyncio
import random
from playwright.async_api import async_playwright
import playwright_stealth
from .auth_manager import AuthManager
from .data_parser import DataParser


class ScraperEngine:
    def __init__(self):
        self.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"

    async def scrape_profile(self, username):
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=False)
            context = await browser.new_context(user_agent=self.user_agent)
            page = await context.new_page()

            auth = AuthManager()
            await auth.load_session(context)

            posts_data = []
            try:
                print(f"[*] Accediendo a @{username}...")
                # Cargamos la página
                await page.goto(f"https://www.instagram.com/{username}/", wait_until="domcontentloaded", timeout=60000)

                # Espera humana para que carguen las miniaturas
                await asyncio.sleep(6)

                # Extraer Stats Generales
                profile_stats = await DataParser.get_profile_stats(page)
                print(f"[+] Seguidores detectados: {profile_stats['followers']}")

                # --- MEJORA AQUÍ: Esperar específicamente por los posts ---
                print("[*] Buscando publicaciones...")
                try:
                    # Esperamos hasta 10 segundos a que aparezca al menos un link de post
                    await page.wait_for_selector('article a', timeout=10000)
                except:
                    print("[!] Los posts tardan en cargar, forzando scroll...")
                    await page.mouse.wheel(0, 800)
                    await asyncio.sleep(3)

                # Capturar los enlaces
                post_links = await page.locator('article a').evaluate_all(
                    "nodes => nodes.map(n => n.href)"
                )

                # Filtrar solo los que son posts reales (/p/)
                final_links = list(dict.fromkeys([l for l in post_links if "/p/" in l]))[:10]

                if not final_links:
                    print("[X] No se encontraron enlaces de posts. Revisa si la cuenta es pública.")
                    return []

                print(f"[+] ¡Éxito! Se encontraron {len(final_links)} posts. Extrayendo métricas...")

                for link in final_links:
                    print(f"    - Analizando post: {link}")
                    data = await DataParser.get_post_metrics(page, link)
                    data.update(profile_stats)
                    posts_data.append(data)
                    await asyncio.sleep(random.uniform(2, 4))

                return posts_data

            except Exception as e:
                print(f"[-] Error durante el scraping: {e}")
                return []
            finally:
                await browser.close()