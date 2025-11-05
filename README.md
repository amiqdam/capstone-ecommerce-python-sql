# capstone-ecommerce-python-sql
# 🛒 Capstone Project Module 1 — E-Commerce Data Analysis

Mini aplikasi berbasis **Python + SQL** untuk menganalisis data transaksi e-commerce.  
Dibuat sebagai project Capstone Module 1, dengan tujuan memahami integrasi database, statistik, dan visualisasi data.

---

## 🚀 Fitur Utama

1. **Read Table** – Menampilkan seluruh transaksi dari database.  
2. **Show Statistik** – Menampilkan statistik deskriptif (mean, median, dll).  
3. **Data Visualization** – Menampilkan grafik penjualan per kategori, metode pembayaran, dsb.  
4. **Add Data** – Menambahkan transaksi baru ke database.  
5. (Bonus) **Filter & Insight Analysis** – Analisis channel & kota paling aktif.

---

## 🧱 Struktur Database

Nama tabel: `data_transaksi_ecommerce`

Kolom utama:
- tanggal, produk, kategori_produk, jumlah, harga_satuan, total_harga
- diskon_persen, biaya_pengiriman, total_akhir
- metode_pembayaran, kota, rating_pelanggan, status_pengiriman, channel_penjualan

---

## ⚙️ Teknologi yang Digunakan

- Python (pandas, matplotlib, seaborn, mysql-connector)
- MySQL
- Git & GitHub

---

## ▶️ Cara Menjalankan

1. Import database ke MySQL:
   ```sql
   SOURCE database_capstone_module1_ecommerce.sql;