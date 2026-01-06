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
    # Daftar Topik Emas Terbaru (Teknologi, Keuangan, AI)
    topik_list = [
        "Dampak AI terhadap Sistem Pajak Pribadi di Tahun 2026",
        "Etika Penggunaan AI dalam Manajemen Aset Keluarga",
        "Cara Menggunakan AI untuk Memprediksi Inflasi Lokal",
        "Transformasi Pekerjaan Sektor Finansial Akibat Otomasi AI",
        "Keamanan Data Biometrik dalam Transaksi Digital Masa Depan",
        "Memanfaatkan AI untuk Mendeteksi Penipuan (Scam) Keuangan",
        "Membangun Dana Pensiun dengan Bantuan Algoritma AI",
        "Sistem Kredit Skor Berbasis Perilaku Digital dan AI",
        "Investasi di Perusahaan Start-up Infrastruktur AI",
        "Cara Kerja Smart Contracts dalam Pinjaman Peer-to-Peer",
        "Mengelola Anggaran Liburan Keluarga Menggunakan ChatGPT",
        "Masa Depan Uang Tunai di Tengah Perkembangan Digital ID",
        "Peran AI dalam Memilih Skema Asuransi Kesehatan Terbaik",
        "Strategi Arbitrase Kripto Menggunakan Bot AI Sederhana",
        "Pengaruh Metaverse terhadap Ekonomi Ritel Tradisional",
        "Cara AI Membantu UMKM Melakukan Pembukuan Otomatis",
        "Mengoptimalkan Portofolio Reksa Dana dengan Analisis Sentiment AI",
        "Tantangan Regulasi AI di Sektor Perbankan Global",
        "Memahami Konsep Tokenisasi Aset Fisik (Real World Assets)",
        "Menggunakan AI untuk Mencari Beasiswa Pendidikan Luar Negeri",
        "Dampak Komputasi Kuantum terhadap Enkripsi Dompet Kripto",
        "Strategi Side Hustle sebagai Prompt Engineer AI",
        "AI dalam Perencanaan Warisan dan Distribusi Aset Digital",
        "Analisis Tren Pasar Saham Berbasis Data Satelit dan AI",
        "Cara Memproteksi Kekayaan dari Ancaman Deepfake Perbankan",
        "Evolusi E-wallet Menjadi Super-App Berbasis Kecerdasan Buatan",
        "Potensi Investasi Sektor Energi Hijau untuk Data Center AI",
        "Menggunakan AI untuk Meminimalkan Biaya Operasional Bisnis",
        "Prediksi Ekonomi Pasca-Otomasi: Apakah Kita Siap untuk UBI?",
        "Panduan Keamanan Siber untuk Investor Retail Tahun 2026"
    ]
    
    # Baris ini sekarang sudah lurus (Indentation Fixed)
    topik = random.choice(topik_list)
    
    try:
        # Deteksi Model Otomatis (Gaya Klasik Stabil Anda)
        models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        model_id = 'models/gemini-1.5-flash' if 'models/gemini-1.5-flash' in models else models[0]
        model = genai.GenerativeModel(model_id.replace('models/', ''))
        
        prompt = f"""
        Tulis artikel blog SEO friendly dalam Bahasa Indonesia tentang: {topik}.
        Gunakan format teks biasa yang rapi dengan sub-judul.
        Di bagian paling akhir artikel, tambahkan bagian 'Baca Juga Rekomendasi Artikel Lainnya:' 
        lalu berikan 3 judul artikel terkait keuangan/AI lainnya dalam bentuk daftar poin.
        """
        
        print(f"Memproses artikel: {topik}")
        response = model.generate_content(prompt)
        
        # Kirim ke Blogger
        kirim_ke_blogger(topik, response.text)
        print("PROSES SELESAI!")
        
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        exit(1)

if __name__ == "__main__":
    main()
        
