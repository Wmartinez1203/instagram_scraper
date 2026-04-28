import re
import asyncio


class DataParser:
    @staticmethod
    def parse_abbreviated_number(text):
        """Convierte formatos como '4,9 M' o '10 K' en números enteros reales."""
        if not text: return 0
        # Limpieza inicial: quitar espacios y normalizar comas a puntos
        text = text.replace(' ', '').replace(',', '.').upper()

        try:
            if 'M' in text:
                return int(float(text.replace('M', '')) * 1_000_000)
            if 'K' in text:
                return int(float(text.replace('K', '')) * 1_000)
            # Si es un número normal, quitamos cualquier punto de miles
            return int(re.sub(r'[^\d]', '', text))
        except:
            return 0

    @staticmethod
    def clean_number(text):
        """Limpia números de likes/comentarios que vienen del meta tag."""
        if not text or text == "N/A": return 0
        clean = re.sub(r'[^\d]', '', str(text))
        return int(clean) if clean else 0

    @staticmethod
    async def get_profile_stats(page):
        try:
            # Esperamos a que el encabezado sea visible
            await page.wait_for_selector("header", timeout=15000)
            header_text = await page.locator("header").inner_text()

            # Buscamos los patrones de texto
            posts = re.search(r'([\d,.\sMK]+)\spublicaciones', header_text, re.I)
            followers = re.search(r'([\d,.\sMK]+)\sseguidores', header_text, re.I)
            following = re.search(r'([\d,.\sMK]+)\sseguidos', header_text, re.I)

            # Convertimos las abreviaturas a números reales
            foll_count = DataParser.parse_abbreviated_number(followers.group(1) if followers else "0")

            return {
                "total_posts": posts.group(1).strip() if posts else "0",
                "followers": foll_count,  # Ahora es un número entero real
                "following": following.group(1).strip() if following else "0"
            }
        except Exception as e:
            print(f"[DataParser] Error en stats: {e}")
            return {"total_posts": "0", "followers": 0, "following": "0"}

    @staticmethod
    async def get_post_metrics(page, post_url, followers_count):
        try:
            await page.goto(post_url, wait_until="domcontentloaded", timeout=60000)
            await asyncio.sleep(3)
            meta = await page.get_attribute('meta[property="og:description"]', "content")

            likes_txt, comm_txt = "0", "0"
            if meta:
                # El meta tag suele decir "623 mil Me gusta" o "1,234 Likes"
                # Intentamos capturar el número antes de la palabra clave
                l_match = re.search(r'([\d,.\sMK]+)\s(?:Me gusta|Likes)', meta, re.I)
                c_match = re.search(r'([\d,.\sMK]+)\s(?:comentarios|Comments)', meta, re.I)

                likes_txt = l_match.group(1) if l_match else "0"
                comm_txt = c_match.group(1) if c_match else "0"

            n_likes = DataParser.parse_abbreviated_number(likes_txt)
            n_comm = DataParser.parse_abbreviated_number(comm_txt)

            # Engagement Rate real
            engagement = ((n_likes + n_comm) / followers_count * 100) if followers_count > 0 else 0

            # Comentarios (texto)
            comments = await page.locator('ul span._ap3a, ul div[role="button"] span').evaluate_all(
                "nodes => nodes.map(n => n.innerText).filter(t => t.length > 5).slice(0, 5)"
            )

            return {
                "url": post_url,
                "likes": n_likes,
                "comentarios": n_comm,
                "engagement_rate": f"{round(engagement, 4)}%",
                "comentarios_texto": " | ".join(comments) if comments else "N/A"
            }
        except:
            return {"url": post_url, "likes": 0, "comentarios": 0, "engagement_rate": "0%", "comentarios_texto": "N/A"}