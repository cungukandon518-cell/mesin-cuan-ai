import os
import smtplib
import random
import google.generativeai as genai
from email.message import EmailMessage

# 1. Ambil Rahasia GitHub
api_key = os.environ.get('GEMINI_API_KEY')
sender_email = os.environ.get('SENDER_EMAIL')
gmail_password = os.environ.get('GMAIL_PASSWORD')
blogger_email = os.environ.get('BLOGGER_EMAIL')

# 2. Konfigurasi "Otak" AI
genai.configure(api_key=api_key)

# 3. DAFTAR TOPIK MANUAL (Ganti judul di sini agar tidak kembar)
topik_list = [
    "Pilihan Saham AI Paling Prospektif di Tahun 2026",
    "Cara Aman Mengelola Aset Kripto untuk Pemula",
    "Rahasia Mengatur Keuangan di Tengah Ketidakpastian Ekonomi",
    "Tips Menabung Emas dengan Modal Gaji UMR",
    "Mengenal Instrumen Investasi Syariah yang Menguntungkan"
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
        # Memilih satu topik secara acak
        topik_pilihan = random.choice(topik_list)
        
        # Menggunakan model 1.5 Flash yang sangat stabil
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # Proses pembuatan artikel
        prompt = f"Tulis artikel blog SEO friendly yang mendalam tentang: {topik_pilihan}."
        response = model.generate_content(prompt)
        
        # Kirim ke Blogger
        kirim_ke_blogger(topik_pilihan, response.text)
        print(f"ALHAMDULILLAH! Centang Hijau Kembali! Terbit: {topik_pilihan}")
        
    except Exception as e:
        print(f"Gagal karena: {e}")
        exit(1)

if __name__ == "__main__":
    main()
