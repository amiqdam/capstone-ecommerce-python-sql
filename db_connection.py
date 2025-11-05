import mysql.connector
from dotenv import load_dotenv
import os

# Load variabel dari file .env
load_dotenv()

def connect_db():
    """
    Membuat koneksi ke database MySQL menggunakan konfigurasi dari .env
    """
    try:
        db = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        return db
    except mysql.connector.Error as e:
        print(f"❌ Gagal konek ke database: {e}")
        return None