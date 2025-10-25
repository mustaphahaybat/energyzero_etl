import pandas as pd
from pathlib import Path

def transform_latest_json():
    # Raw data klasörü (konteyner içindeki path)
    raw_dir = Path("/opt/airflow/data/raw")
    json_files = sorted(raw_dir.glob("*.json"))
    
    if not json_files:
        print("Hiç JSON dosyası bulunamadı!")
        return
    
    latest_file = json_files[-1]
    print(f"Processing: {latest_file}")

    # JSON'u oku
    df_json = pd.read_json(latest_file)

    if "Prices" not in df_json.columns:
        print("JSON dosyasında 'Prices' anahtarı yok!")
        return

    # Prices listesini normalize et
    df = pd.json_normalize(df_json["Prices"])
    df.rename(columns={"readingDate": "ReadingDate", "price": "Price"}, inplace=True)

    # Tarih ve saat sütunlarını oluştur
    df["ReadingDate"] = pd.to_datetime(df["ReadingDate"])
    df["Date"] = df["ReadingDate"].dt.date
    df["Time"] = df["ReadingDate"].dt.time

    # Fiyatlara KDV ekle
    df["Price_with_VAT"] = df["Price"] * 1.21

    # Processed data klasörü (konteyner içindeki path)
    processed_dir = Path("/opt/airflow/data/processed")
    processed_dir.mkdir(parents=True, exist_ok=True)
    output_file = processed_dir / "energy_transformed.parquet"

    # Dosyayı kaydet
    df.to_parquet(output_file, index=False)
    print(f"Saved: {output_file}")

if __name__ == "__main__":
    transform_latest_json()
