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

def kirim_ke_blogger(subjek, isi_html):
    print("Mengirim email HTML ke Blogger...")
    msg = EmailMessage()
    msg.set_content("Silakan aktifkan tampilan HTML untuk melihat artikel ini.") # Fallback
    msg.add_alternative(isi_html, subtype='html') # Versi HTML agar rapi di Blogspot
    
    msg['Subject'] = subjek
    msg['From'] = sender_email
    msg['To'] = blogger_email
    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender_email, gmail_password)
        smtp.send_message(msg)
    print("Artikel HTML TERKIRIM!")

def main():
    # DAFTAR TOPIK TERBARU 2026 (High CPC & Trending)
    topik_list = [
        "Cara Mengelola AI Agent Pribadi untuk Produktivitas 10x Lipat",
        "Panduan Investasi Real Estate di Metaverse yang Masih Prospektif",
        "Mengenal Bio-Hacking: Optimasi Kesehatan Berbasis Data AI dan DNA",
        "Strategi Keamanan Finansial di Era Deepfake Voice Scam",
        "Peluang Cuan dari Carbon Trading Retail bagi Investor Pemula",
        "Mengapa Keterampilan Prompt Engineering Kini Digantikan oleh Agentic AI",
        "Cara Membangun Passive Income dengan Menyewakan GPU untuk Latihan AI",
        "Dampak Hyper-Personalization AI pada Kebiasaan Belanja Generasi Alpha",
        "Masa Depan Pekerjaan Kerah Putih di Tengah Dominasi Autopilot AI",
        "Review Kacamata AR Terbaik 2026 untuk Bekerja Secara Remote",
        "Sistem Barter Digital: Apakah Crypto Akan Kembali ke Fungsi Aslinya?",
        "Eksplorasi AI dalam Mempercepat Penemuan Obat-obatan Penyakit Langka",
        "Bagaimana AI Membantu Gen Z Meraih Kebebasan Finansial Sebelum Usia 30",
        "Etika AI: Siapa yang Bertanggung Jawab Jika AI Mengalami Kerugian Finansial?",
        "Pemanfaatan Robot Humanoid dalam Industri Logistik dan UMKM",
        "Analisis Prediktif AI untuk Menemukan Koin Kripto 'Micin' Berkualitas",
        "Cara Proteksi Data Pribadi dari Scraping Massal Perusahaan AI",
        "Transformasi Pendidikan: Guru sebagai Mentor, AI sebagai Pengajar",
        "Strategi Bisnis Dropshipping Berbasis Prediksi Tren AI 2026",
        "Micro-SaaS: Membangun Aplikasi Kecil Berbasis AI Tanpa Coding",
        "Masa Depan Transportasi: Taksi Terbang dan Integrasi Navigasi AI",
        "Pengaruh Kedaulatan Data (Data Sovereignty) terhadap Harga Saham Teknologi",
        "Menggunakan AI untuk Deteksi Dini Penyakit Mental dari Pola Ketikan",
        "Smart Home 2.0: Ketika Rumahmu Bisa Mengatur Budget Belanja Sendiri",
        "Peluang Ekonomi di Sektor Wisata Luar Angkasa dan Peran AI",
        "Digital Twin: Memiliki Kembaran Digital untuk Uji Coba Strategi Bisnis",
        "Cara Menggunakan AI untuk Menulis Buku Non-Fiksi dalam 24 Jam",
        "Dampak Integrasi Chip Otak (Neural Interface) pada Interaksi Manusia",
        "Sustainabilty Tech: AI sebagai Kunci Utama Melawan Perubahan Iklim",
        "Self-Sovereign Identity: Cara Mengontrol Identitas Digital di Web4"
    ]
    
    run_number = int(os.environ.get('GITHUB_RUN_NUMBER', '1'))
    index = (run_number - 1) % len(topik_list)
    topik = topik_list[index]
    
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # PROMPT YANG DIPERTANJAM (Output HTML)
        prompt = f"""
        Tulis artikel blog yang mendalam dan informatif tentang: {topik}.
        Gunakan Bahasa Indonesia yang santai tapi profesional.
        
        WAJIB: Gunakan format HTML.
        - Gunakan tag <h2> dan <h3> untuk sub-judul.
        - Gunakan <strong> untuk poin penting.
        - Gunakan <ul> dan <li> untuk daftar/list.
        - Sertakan kesimpulan yang kuat di akhir.
        - Tambahkan bagian 'Rekomendasi Bacaan:' dengan 3 judul terkait dalam bentuk list HTML.
        
        Pastikan artikel minimal 600 kata dan SEO friendly.
        """
        
        print(f"Memproses artikel ke-{run_number}: {topik}")
        response = model.generate_content(prompt)
        
        # Kirim dalam format HTML
        kirim_ke_blogger(topik, response.text)
        print(f"PROSES SELESAI! (Index: {index})")
        
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        exit(1)

if __name__ == "__main__":
    main()
    
