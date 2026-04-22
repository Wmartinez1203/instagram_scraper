import asyncio
import re


class DataParser:
    @staticmethod
    async def get_profile_stats(page):
        """Extrae seguidores y seguidos desde el encabezado del perfil."""
        try:
            # Buscamos los elementos que contienen el texto 'seguidores' y 'seguidos'
            stats_text = await page.locator("header").inner_text()

            followers = re.search(r'([\d,.]+)\sseguidores', stats_text)
            following = re.search(r'([\d,.]+)\sseguidos', stats_text)
            posts_count = re.search(r'([\d,.]+)\spublicaciones', stats_text)

            return {
                "total_posts": posts_count.group(1) if posts_count else "0",
                "followers": followers.group(1) if followers else "0",
                "following": following.group(1) if following else "0"
            }
        except Exception as e:
            print(f"[DataParser] Error en stats de perfil: {e}")
            return {"followers": "N/A", "following": "N/A"}

    @staticmethod
    async def get_post_metrics(page, post_url):
        """Extrae likes y comentarios de un post específico."""
        try:
            await page.goto(post_url, wait_until="networkidle")
            await asyncio.sleep(2)

            # Extraer del meta tag og:description es lo más seguro en IG
            meta_content = await page.get_attribute('meta[property="og:description"]', "content")

            likes, comments = "0", "0"
            if meta_content:
                # Regex ajustada para detectar números antes de Likes/Comments
                l_match = re.search(r'([\d,.]+)\sLikes', meta_content, re.I)
                c_match = re.search(r'([\d,.]+)\sComments', meta_content, re.I)
                likes = l_match.group(1) if l_match else "0"
                comments = c_match.group(1) if c_match else "0"

            return {
                "url": post_url,
                "likes": likes,
                "comments": comments,
                "caption_preview": meta_content.split("-")[1].strip() if "-" in meta_content else "N/A"
            }
        except Exception as e:
            return {"url": post_url, "error": str(e)}