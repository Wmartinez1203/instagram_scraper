import asyncio
import re


class DataParser:
    @staticmethod
    async def get_profile_stats(page):
        try:
            await page.wait_for_selector("header", timeout=15000)
            text = await page.locator("header").inner_text()

            posts = re.search(r'([\d,.]+)\spublicaciones', text)
            followers = re.search(r'([\d,.]+)\sseguidores', text)
            following = re.search(r'([\d,.]+)\sseguidos', text)

            return {
                "total_posts": posts.group(1) if posts else "0",
                "followers": followers.group(1) if followers else "0",
                "following": following.group(1) if following else "0"
            }
        except:
            return {"total_posts": "N/A", "followers": "N/A", "following": "N/A"}

    @staticmethod
    async def get_post_metrics(page, post_url):
        try:
            await page.goto(post_url, wait_until="domcontentloaded", timeout=60000)
            await asyncio.sleep(4)

            # Likes y conteo desde Metadata
            meta = await page.get_attribute('meta[property="og:description"]', "content")
            likes, comm_count = "0", "0"
            if meta:
                l_match = re.search(r'([\d,.]+)\sLikes', meta, re.I)
                c_match = re.search(r'([\d,.]+)\sComments', meta, re.I)
                likes = l_match.group(1) if l_match else "0"
                comm_count = c_match.group(1) if c_match else "0"

            # Extracción de comentarios (texto real)
            # Buscamos elementos comunes de comentarios en el DOM de Instagram
            comments = await page.locator('ul span._ap3a, ul div[role="button"] span').evaluate_all(
                "nodes => nodes.map(n => n.innerText).filter(t => t.length > 5).slice(0, 5)"
            )

            return {
                "post_url": post_url,
                "likes": likes,
                "total_comments": comm_count,
                "comentarios_extraidos": " | ".join(comments) if comments else "Sin comentarios visibles"
            }
        except:
            return {"post_url": post_url, "likes": "N/A", "total_comments": "0", "comentarios_extraidos": "N/A"}