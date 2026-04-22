import asyncio
import random
from playwright.async_api import async_playwright
import playwright_stealth
from .auth_manager import AuthManager
from .data_parser import DataParser


class ScraperEngine:
    def __init__(self):
        self.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
        self.USAR_PROXY = False  # <--- ¡IMPORTANTE! Ponlo en False si vas a usar tus datos del cel
        self.PROXY_SERVER = "http://192.168.25.222:8080"

    async def scrape_profile(self, username):
        async with async_playwright() as p:
            launch_args = {"headless": False}
            if self.USAR_PROXY:
                launch_args["proxy"] = {"server": self.PROXY_SERVER}
                print(f"[*] Usando Proxy IESS...")

            browser = await p.chromium.launch(**launch_args)
            # ignore_https_errors ayuda a que el proxy no bloquee el certificado
            context = await browser.new_context(user_agent=self.user_agent, ignore_https_errors=True)
            page = await context.new_page()

            try:
                await playwright_stealth.stealth_async(page)
            except:
                pass

            auth = AuthManager()
            await auth.load_session(context)

            try:
                print(f"[*] Navegando a @{username}...")
                await page.goto(f"https://www.instagram.com/{username}/", wait_until="domcontentloaded", timeout=90000)
                await asyncio.sleep(6)

                profile_data = await DataParser.get_profile_stats(page)

                await page.mouse.wheel(0, 800)
                await asyncio.sleep(3)

                raw_links = await page.eval_on_selector_all("a[href*='/p/']", "nodes => nodes.map(n => n.href)")
                final_links = list(dict.fromkeys([l for l in raw_links if "/p/" in l]))[:10]

                if not final_links: return []

                results = []
                for link in final_links:
                    print(f"    - Analizando post...")
                    post_data = await DataParser.get_post_metrics(page, link, profile_data['followers'])
                    results.append({**profile_data, **post_data})
                    await asyncio.sleep(random.uniform(2, 4))

                return results
            except Exception as e:
                print(f"[-] Error: {e}")
                return []
            finally:
                await browser.close()