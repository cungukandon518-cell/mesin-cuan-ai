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
    # Daftar Topik Emas (Sesuai Kategori Tentang Kami Anda)
    topik_list = [
        "Panduan Investasi Saham AI untuk Pemula 2026",
        "Cara Memilih Asset Crypto yang Aman untuk Jangka Panjang",
        "Strategi Diversifikasi Portofolio di Era Digital",
        "5 Aplikasi AI Terbaik untuk Mengatur Keuangan Bulanan",
        "Cara Menghemat Pengeluaran dengan Bantuan Asisten Virtual",
        "Tips Melunasi Hutang dengan Metode Snowball Digital",
        "Review Tools AI untuk Analisis Pasar Keuangan Terakurat",
        "Top 10 AI Tools yang Bisa Menghasilkan Passive Income",
        "Masa Depan Perbankan: Bagaimana AI Mengelola Uang Kita",
        "Strategi Menghasilkan Dolar dari Blog Otomatis",
        "Peluang Bisnis AI 2026 yang Belum Banyak Diketahui"
    ]
    
    topik = random.choice(topik_list)
    
    try:
        # Deteksi Model Otomatis
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
    
