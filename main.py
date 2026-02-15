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
    # DAFTAR TOPIK BARU 2026 (Fresh & High Interest)
    topik_list = [
        "Panduan Membangun AI Agent Pribadi untuk Automasi Tugas Harian",
        "Masa Depan Investasi: Mengapa Karbon Kredit Menjadi Aset Berharga",
        "Cara Melindungi Aset Digital dari Serangan Deepfake Scan",
        "Strategi Passive Income: Menyewakan Komputasi GPU untuk Jaringan AI",
        "Transformasi E-Commerce: Belanja Menggunakan Asisten Virtual Berbasis Voice",
        "Mengenal Bio-Hacking: Teknologi AI untuk Memperpanjang Usia Produktif",
        "Peluang Bisnis di Sektor Humanoid Robot Service untuk UMKM",
        "Cara Kerja Decentralized AI: Menjaga Privasi Data di Era Generative AI",
        "Panduan Investasi Real Estate di Kota Pintar (Smart City) Indonesia",
        "Strategi Mengelola Portofolio Kripto di Era Pasca-Halving 2024-2026",
        "Etika Menggunakan AI dalam Pekerjaan Kreatif agar Tetap Orisinal",
        "Masa Depan Transportasi: Bagaimana Taksi Terbang Mengubah Ekonomi Lokal",
        "Cara Memanfaatkan AI untuk Deteksi Dini Peluang Saham Blue Chip",
        "Personalized Medicine: Bagaimana AI Merancang Suplemen Sesuai DNA Anda",
        "Tips Sukses Freelance di Global Market dengan Bantuan Tool AI Agent",
        "Mengenal Konsep 'Digital Twin' untuk Perencanaan Keuangan Keluarga",
        "Dampak Teknologi Quantum Computing terhadap Keamanan Perbankan Digital",
        "Cara Membuat Konten Edukasi yang Viral dengan Hyper-Personalization AI",
        "Strategi Mengahadapi Inflasi Digital: Mengapa Aset Fisik Tetap Penting",
        "Review Gadget Wearable 2026: Hidup Tanpa Smartphone dengan Kacamata AR",
        "Peluang Karir sebagai AI Auditor: Pekerjaan Paling Dicari Tahun Ini",
        "Cara Menggunakan AI untuk Optimalisasi Pajak dan Laporan Keuangan",
        "Dampak Integrasi Chip Neural pada Produktivitas Kerja Manusia",
        "Pemanfaatan AI dalam Pertanian Presisi untuk Ketahanan Pangan Rumah Tangga",
        "Micro-SaaS: Membangun Aplikasi AI Spesifik Tanpa Harus Jago Coding",
        "Mengapa Literasi Prompt Engineering Kini Menjadi Skill Dasar di Sekolah",
        "Strategi Exit Plan Investasi di Tengah Volatilitas Ekonomi Global",
        "Membangun Brand Pribadi di Era AI: Menjadi Manusia yang Tak Tergantikan",
        "Cara AI Membantu Menemukan Hobi yang Menghasilkan Cuan",
        "Masa Depan Konsultasi Psikologi: AI Sebagai Pendengar 24 Jam"
    ]
    
    # LOGIKA PENGAMBILAN URUT
    run_number = int(os.environ.get('GITHUB_RUN_NUMBER', '1'))
    index = (run_number - 1) % len(topik_list)
    topik = topik_list[index]
    
    try:
        # Perbaikan inisialisasi model agar tidak error 404
        # Menggunakan model flash terbaru yang stabil
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        prompt = f"""
        Tulis artikel blog SEO friendly dalam Bahasa Indonesia tentang: {topik}.
        Gunakan format teks biasa yang rapi dengan sub-judul.
        Sertakan poin-poin penting agar mudah dibaca.
        Berikan informasi yang edukatif dan terbaru di tahun 2026.
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
    
