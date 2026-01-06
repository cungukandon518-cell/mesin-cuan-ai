import os
import smtplib
import random
import google.generativeai as genai # Sinkronisasi Identitas 2026
from email.message import EmailMessage

# 1. Kredensial
api_key = os.environ.get('GEMINI_API_KEY')
sender_email = os.environ.get('SENDER_EMAIL')
gmail_password = os.environ.get('GMAIL_PASSWORD')
blogger_email = os.environ.get('BLOGGER_EMAIL')

# 2. Inisialisasi
genai.configure(api_key=api_key)

# 3. DAFTAR TOPIK MANUAL (Agar Artikel Tidak Kembar)
topik_list = [
    "Tips Mengatur Keuangan di Tahun 2026 Agar Cepat Kaya",
    "Cara Investasi Aman untuk Pemula Tahun Ini",
    "Rahasia Menabung yang Jarang Diketahui Orang",
    "Strategi Melunasi Hutang Tanpa Stres"
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
        topik = random.choice(topik_list)
        
        # MENGGUNAKAN MODEL STABIL UNTUK MENGHINDARI 404
        # Kami memanggil model secara eksplisit untuk jalur v1 resmi
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        response = model.generate_content(f"Tulis artikel blog SEO friendly tentang: {topik}.")
        
        kirim_ke_blogger(topik, response.text)
        print(f"AKHIRNYA SUKSES! Centang Hijau Terbit: {topik}")
        
    except Exception as e:
        # Jika masih 404, narator akan menganalisis pesan di bawah ini
        print(f"Detail kendala: {e}")
        exit(1)

if __name__ == "__main__":
    main()
    
