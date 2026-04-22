import re


class DataParser:
    @staticmethod
    def clean_number(text):
        if not text or text == "N/A": return 0
        # Elimina cualquier cosa que no sea dígito
        clean = re.sub(r'[^\d]', '', str(text))
        return int(clean) if clean else 0

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
            return {"total_posts": "0", "followers": "0", "following": "0"}

    @staticmethod
    async def get_post_metrics(page, post_url, followers_raw):
        try:
            await page.goto(post_url, wait_until="domcontentloaded", timeout=60000)
            await asyncio.sleep(3)
            meta = await page.get_attribute('meta[property="og:description"]', "content")

            likes_txt, comm_txt = "0", "0"
            if meta:
                l_match = re.search(r'([\d,.]+)\sLikes', meta, re.I)
                c_match = re.search(r'([\d,.]+)\sComments', meta, re.I)
                likes_txt = l_match.group(1) if l_match else "0"
                comm_txt = c_match.group(1) if c_match else "0"

            # Conversión a números para cálculos
            n_likes = DataParser.clean_number(likes_txt)
            n_comm = DataParser.clean_number(comm_txt)
            n_foll = DataParser.clean_number(followers_raw)

            # Cálculo Engagement
            engagement = ((n_likes + n_comm) / n_foll * 100) if n_foll > 0 else 0

            # Comentarios (texto)
            comments = await page.locator('ul span._ap3a, ul div[role="button"] span').evaluate_all(
                "nodes => nodes.map(n => n.innerText).filter(t => t.length > 5).slice(0, 5)"
            )

            return {
                "url": post_url,
                "likes": n_likes,
                "comentarios": n_comm,
                "engagement_rate": f"{round(engagement, 2)}%",
                "comentarios_texto": " | ".join(comments) if comments else "N/A"
            }
        except:
            return {"url": post_url, "likes": 0, "comentarios": 0, "engagement_rate": "0%", "comentarios_texto": "N/A"}