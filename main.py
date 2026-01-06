import os
import smtplib
import random
import google.generativeai as genai
from email.message import EmailMessage

# 1. Kredensial
api_key = os.environ.get('GEMINI_API_KEY')
sender_email = os.environ.get('SENDER_EMAIL')
gmail_password = os.environ.get('GMAIL_PASSWORD')
blogger_email = os.environ.get('BLOGGER_EMAIL')

# 2. Konfigurasi AI
genai.configure(api_key=api_key)

# 3. DAFTAR TOPIK MANUAL (Ubah di sini agar tidak kembar)
topik_list = [
    "Tips Mengelola Gaji Kecil Agar Bisa Nabung di 2026",
    "Cara Investasi Crypto Aman untuk Pemula Tahun Ini",
    "Rahasia Mengatur Keuangan Keluarga Tanpa Stres",
    "Daftar Saham AI Paling Menjanjikan Bulan Januari",
    "Cara Melunasi Hutang dengan Metode Snowball",
    "Aplikasi Keuangan Terbaik yang Wajib Ada di HP Anda",
    "Pentingnya Dana Darurat di Masa Depan"
]

def kirim_ke_blogger(subjek, isi):
    msg = EmailMessage()
    msg.set_content(isi)
    msg['Subject'] = subjek
    msg['From'] = sender_email
    msg['To'] = blogger_email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender_email, gmail_password)
        smtp.send_message(msg)

def main():
    try:
        # Memilih satu topik secara acak dari list di atas
        topik_pilihan = random.choice(topik_list)
        
        model = genai.GenerativeModel('gemini-pro') # Menggunakan pro yang sangat stabil
        
        # Membuat konten berdasarkan topik pilihan
        prompt = f"Tulis artikel blog SEO friendly yang mendalam tentang: {topik_pilihan}."
        response = model.generate_content(prompt)
        
        # Kirim ke Blogger
        kirim_ke_blogger(topik_pilihan, response.text)
        print(f"SUKSES! Centang Hijau Kembali! Terbit: {topik_pilihan}")
        
    except Exception as e:
        print(f"Gagal karena: {e}")
        exit(1)

if __name__ == "__main__":
    main()
    
