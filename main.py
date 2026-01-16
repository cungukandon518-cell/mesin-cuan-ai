import os
import random
import smtplib
import google.generativeai as genai
from email.message import EmailMessage

# 1. Konfigurasi Secrets
api_key = os.environ.get('GEMINI_API_KEY')
sender_email = os.environ.get('SENDER_EMAIL')
gmail_password = os.environ.get('GMAIL_PASSWORD')
blogger_email = os.environ.get('BLOGGER_EMAIL')

genai.configure(api_key=api_key)

def kirim_ke_blogger(subjek, isi):
    print("Mengirim email ke Blogger...")
    msg = EmailMessage()
    msg.set_content(isi)
    msg['Subject'] = subjek
    msg['From'] = sender_email
    msg['To'] = blogger_email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender_email, gmail_password)
        smtp.send_message(msg)
    print("Artikel TERKIRIM!")

def main():
    # DAFTAR TOPIK (Teknologi, Keuangan, AI)
    topik_list = [
        "Peluang Investasi di Era Web3 dan Kecerdasan Buatan",
        "Bagaimana AI Mengubah Wajah Perbankan Syariah di Masa Depan",
        "Strategi Yield Farming Kripto yang Aman dengan Optimasi AI",
        "Peran Machine Learning dalam Memprediksi Pergerakan IHSG",
        "Memanfaatkan AI untuk Perencanaan Keuangan UMKM agar Cepat Naik Kelas",
        "Mengenal Algo-Trading untuk Pemula: Cuan Konsisten dengan Robot",
        "Transformasi Asuransi Jiwa Berbasis Data Gaya Hidup dan AI",
        "Cara Menghasilkan Dolar dari Konten Video yang Dibuat Sepenuhnya oleh AI",
        "Masa Depan Pembayaran: Dari Scan QR ke Pengenalan Wajah Berbasis AI",
        "Strategi Mengelola Dana Darurat di Tengah Ketidakpastian Ekonomi Digital",
        "Peluang Karir Baru di Sektor FinTech yang Didorong oleh AI",
        "Cara Memilih Reksa Dana Terbaik Menggunakan Analisis Robot Advisor",
        "Dampak Integrasi AI pada Efisiensi Operasional Bank Digital",
        "Mengungkap Rahasia Sukses Investor Institusi yang Menggunakan Big Data AI",
        "Peran AI dalam Memitigasi Risiko Investasi di Pasar Kripto yang Volatil",
        "Inovasi Perbankan: Mengapa Chatbot AI Menjadi Sahabat Baru Nasabah",
        "Strategi Membangun Portofolio Saham Teknologi di Tengah AI Boom",
        "Bagaimana AI Membantu Menemukan Peluang Arbitrase di Pasar Modal",
        "Pentingnya Literasi Keuangan Digital di Era Otomasi Kecerdasan Buatan",
        "Review Tools AI Terbaru untuk Pencatatan Keuangan Otomatis",
        "Masa Depan Properti: Bagaimana AI Memprediksi Lokasi Investasi Terbaik",
        "Menggunakan AI untuk Perbandingan Kurs Valas Secara Real-Time",
        "Cara Efektif Menabung Emas Digital dengan Bantuan Prediksi Harga AI",
        "Etika dan Keamanan: Menjaga Privasi Data Keuangan di Era AI",
        "Strategi Melunasi Hutang KPR Lebih Cepat dengan Simulasi Pintar AI",
        "Dampak Adopsi AI pada Kinerja Perusahaan Sektor Konsumsi",
        "Mengenal Konsep Digital Twin dalam Manajemen Kekayaan Pribadi",
        "Tips Sukses Berbisnis Dropship dengan Riset Produk Berbasis AI",
        "Bagaimana AI Mengubah Cara Kita Berinvestasi di Sektor Energi Hijau",
        "Masa Depan Konsultasi Keuangan: Apakah Manusia Akan Digantikan AI?"
    ]
    
    # LOGIKA PENGAMBILAN URUT
    # Mengambil nomor urut eksekusi dari GitHub (default 1 jika tidak ada)
    run_number = int(os.environ.get('GITHUB_RUN_NUMBER', '1'))
    
    # Menghitung index (Jika run ke-31 dan topik cuma 30, dia akan balik ke topik ke-1)
    index = (run_number - 1) % len(topik_list)
    topik = topik_list[index]
    
    try:
        # Deteksi Model Otomatis (Gaya Klasik Stabil Anda)
        models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        model_id = 'models/gemini-1.5-flash' if 'models/gemini-1.5-flash' in models else models[0]
        model = genai.GenerativeModel(model_id.replace('models/', ''))
        
        prompt = f"""
        Tulis artikel blog SEO friendly dalam Bahasa Indonesia tentang: {topik}.
        Gunakan format teks biasa yang rapi dengan sub-judul.
        Sertakan poin-poin penting agar mudah dibaca.
        Di bagian paling akhir artikel, tambahkan bagian 'Baca Juga Rekomendasi Artikel Lainnya:' 
        lalu berikan 3 judul artikel terkait keuangan/AI lainnya dalam bentuk daftar poin.
        """
        
        print(f"Memproses artikel urut ke-{run_number}: {topik}")
        response = model.generate_content(prompt)
        
        # Kirim ke Blogger
        kirim_ke_blogger(topik, response.text)
        print(f"PROSES SELESAI! (Index: {index})")
        
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        exit(1)

if __name__ == "__main__":
    main()
    
