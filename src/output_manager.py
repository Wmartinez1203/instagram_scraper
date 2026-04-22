import json
import csv
import os


class OutputManager:
    @staticmethod
    def save_data(data, filename):
        folder = 'data'
        if not os.path.exists(folder):
            os.makedirs(folder)

        json_path = os.path.join(folder, f"{filename}.json")
        csv_path = os.path.join(folder, f"{filename}.csv")

        # Guardar JSON
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

        # Guardar CSV (Ideal para Excel)
        if data:
            keys = data[0].keys()
            with open(csv_path, 'w', newline='', encoding='utf-8') as f:
                dw = csv.DictWriter(f, fieldnames=keys)
                dw.writeheader()
                dw.writerows(data)

        print(f"\n[OK] Reportes generados con éxito en: {os.path.abspath(folder)}")