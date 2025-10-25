# ⚡ EnergyZero ETL Pipeline (Docker + Apache Airflow + Python) ## 🧩 Proje Özeti Bu proje, **EnergyZero API** üzerinden enerji fiyat verilerini çekip, **Apache Airflow** ile zamanlanmış şekilde işleyip, veriyi **Parquet formatına** dönüştürür. Tüm bileşenler **Docker** üzerinde çalışır. Böylece her sistemde kolayca tekrarlanabilir bir veri hattı (ETL pipeline) kurulabilir. --- ## 🚀 Proje Yapısı energyzero_etl/ │ ├── docker-compose.yml ├── requirements.txt │ ├── dags/ │ └── energyzero_etl.py # Airflow DAG (zamanlama ve görev akışı) │ ├── scripts/ │ ├── extract_energyzero.py # API'den veri çekme (JSON) │ └── transform_pandas.py # JSON'u Parquet'e dönüştürme │ ├── data/ │ ├── raw/ # Ham JSON verileri │ └── processed/ # İşlenmiş Parquet dosyaları │ └── README.md yaml Kodu kopyala --- ## ⚙️ Çalıştırma Adımları ### 1️⃣ Docker Ortamını Başlat
bash
docker-compose up -d
Bu komut, aşağıdakileri başlatır:

Airflow webserver

Airflow scheduler

PostgreSQL veritabanı

Airflow arayüzü:
👉 http://localhost:8080

Kullanıcı adı: airflow
Şifre: airflow

2️⃣ Airflow Arayüzünden DAG’i Çalıştır
energyzero_etl isimli DAG’i "On" konumuna getir.

Manuel olarak Trigger DAG diyerek başlat.

Görevler:

extract_energyzero_json → EnergyZero API'den JSON dosyası çeker.

transform_json_to_parquet → JSON'u Parquet formatına dönüştürür.

3️⃣ Çıktılar
Ham veriler → data/raw/

İşlenmiş veriler → data/processed/energy_transformed.parquet

🧠 Öğrenilenler
Docker ortamında çok bileşenli veri hattı oluşturmak

Airflow ile görev akışı (DAG) planlamak

Pandas ile veri dönüştürmek

JSON → Parquet dönüşümü

Kapsüllenmiş (containerized) veri mühendisliği projesi geliştirmek

💡 Geliştirme Fikirleri
Parquet dosyasını PostgreSQL veya DuckDB’ye yükle

Airflow DAG’e hata loglaması ekle

API tarih aralıklarını genişlet

Matplotlib veya Plotly ile görselleştirme ekle

📷 Örnek Görseller
(İsteğe bağlı: Airflow arayüzü, terminal çıktısı veya klasör yapısı ekran görüntüsü eklenebilir)

👨‍💻 Geliştirici
Mustapha Haybat
📍 Netherlands
🔗 [LinkedIn profilini buraya ekle]
📦 Proje yapısı: Python, Airflow, Docker, PostgreSQL, Pandas