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

# 2. Inisialisasi
genai.configure(api_key=api_key)

# 3. DAFTAR TOPIK (Ganti judul di sini agar tidak kembar)
topik_list = [
    "Cara Cerdas Mengatur Keuangan Pribadi di Tahun 2026",
    "Investasi Saham AI: Panduan Lengkap untuk Pemula",
    "Rahasia Menabung 50 Persen Gaji Tanpa Tersiksa",
    "Mengenal Perbedaan Aset dan Liabilitas di Masa Depan",
    "Strategi Melunasi Hutang dengan Cepat dan Aman"
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
        # Pilih topik acak dari daftar
        topik_pilihan = random.choice(topik_list)
        
        # Gunakan model paling stabil
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(f"Tulis artikel blog SEO friendly tentang: {topik_pilihan}.")
        
        # Publikasi
        kirim_ke_blogger(topik_pilihan, response.text)
        print(f"AKHIRNYA SUKSES! Terbit artikel: {topik_pilihan}")
        
    except Exception as e:
        print(f"Detail kendala: {e}")
        exit(1)

if __name__ == "__main__":
    main()
    
