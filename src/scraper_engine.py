import asyncio
import random
from playwright.async_api import async_playwright
import playwright_stealth
from .auth_manager import AuthManager
from .data_parser import DataParser

class ScraperEngine:
    def __init__(self):
        self.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
        # --- CONFIGURACIÓN DE RED ---
        self.USAR_PROXY = True  # CAMBIA A False CUANDO ESTÉS EN CASA
        self.PROXY_SERVER = "http://192.168.25.222:8080"

    async def scrape_profile(self, username):
        async with async_playwright() as p:
            # Lógica de conexión inteligente
            launch_args = {"headless": False}
            if self.USAR_PROXY:
                launch_args["proxy"] = {"server": self.PROXY_SERVER}
                print(f"[*] Conectando vía Proxy: {self.PROXY_SERVER}")
            else:
                print("[*] Conexión directa detectada (Modo Casa/Datos).")

            browser = await p.chromium.launch(**launch_args)
            context = await browser.new_context(user_agent=self.user_agent)
            page = await context.new_page()

            # Evitar detección básica
            try:
                await playwright_stealth.stealth_async(page)
            except:
                pass

            auth = AuthManager()
            await auth.load_session(context)

            try:
                print(f"[*] Navegando al perfil: @{username}...")
                await page.goto(f"https://www.instagram.com/{username}/", wait_until="domcontentloaded", timeout=90000)
                await asyncio.sleep(6)

                # Extraer estadísticas generales
                profile_data = await DataParser.get_profile_stats(page)
                print(f"[+] Seguidores: {profile_data['followers']} | Siguiendo: {profile_data['following']}")

                # Forzar carga de publicaciones
                await page.mouse.wheel(0, 800)
                await asyncio.sleep(3)

                # Capturar links de posts
                raw_links = await page.eval_on_selector_all("a[href*='/p/']", "nodes => nodes.map(n => n.href)")
                final_links = list(dict.fromkeys([l for l in raw_links if "/p/" in l]))[:10]

                if not final_links:
                    print("[!] No se hallaron publicaciones en este perfil.")
                    return []

                print(f"[*] Procesando {len(final_links)} publicaciones para extraer métricas y comentarios...")
                results = []
                for link in final_links:
                    print(f"    - Analizando: {link}")
                    post_data = await DataParser.get_post_metrics(page, link)
                    results.append({**profile_data, **post_data})
                    await asyncio.sleep(random.uniform(2, 5))

                return results
            except Exception as e:
                print(f"[-] Error durante el proceso: {e}")
                return []
            finally:
                await browser.close()