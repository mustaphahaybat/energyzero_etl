import requests, json
from datetime import datetime, timedelta
import os

def fetch_energy_data():
    # Tarihler
    end_date = datetime.utcnow()
    start_date = end_date - timedelta(days=7)
    
    # API URL
    url = f"https://api.energyzero.nl/v1/energyprices?fromDate={start_date.date()}T00:00:00.000Z&tillDate={end_date.date()}T23:59:59.999Z&interval=4&usageType=1&inclBtw=false"
    data = requests.get(url).json()

    # Dosya yolu - Airflow konteynerine uygun
    base_dir = os.path.dirname(os.path.dirname(__file__))  # scripts klasöründen bir üst dizin
    raw_dir = os.path.join(base_dir, "data/raw")
    os.makedirs(raw_dir, exist_ok=True)  # klasör yoksa oluştur
    file_name = os.path.join(raw_dir, f"energy_{end_date.strftime('%Y%m%d_%H%M%S')}.json")

    # Kaydetme
    with open(file_name, "w") as f:
        json.dump(data, f)
    print(f"Saved: {file_name}")

if __name__ == "__main__":
    fetch_energy_data()
