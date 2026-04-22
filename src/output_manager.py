import pandas as pd
import json
import os


class OutputManager:
    @staticmethod
    def save_data(data, username):
        folder = 'data'
        if not os.path.exists(folder): os.makedirs(folder)

        df = pd.DataFrame(data)
        base_path = os.path.join(folder, f"reporte_{username}")

        # Guardamos en Excel (para el Dashboard) y JSON (para el profe)
        df.to_excel(f"{base_path}.xlsx", index=False)
        with open(f"{base_path}.json", 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

        print(f"\n[OK] ¡Reportes listos! Carpeta: {os.path.abspath(folder)}")