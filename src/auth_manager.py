import json
import os

class AuthManager:
    def __init__(self, session_path="session/cookies.json"):
        self.session_path = session_path

    async def load_session(self, context):
        if not os.path.exists(self.session_path):
            return False
        try:
            with open(self.session_path, 'r', encoding='utf-8') as f:
                cookies = json.load(f)
                if cookies:
                    await context.add_cookies(cookies)
                    print(f"[AuthManager] {len(cookies)} cookies inyectadas con éxito.")
                    return True
        except Exception as e:
            print(f"[AuthManager] Error al cargar cookies: {e}")
        return False