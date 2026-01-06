import os
import smtplib
import random
from email.message import EmailMessage
# Menggunakan cara import paling aman untuk paket google-genai
try:
    from google import genai
except ImportError:
    import google.genai as genai

# 1. Kredensial
api_key = os.environ.get('GEMINI_API_KEY')
sender_email = os.environ.get('SENDER_EMAIL')
gmail_password = os.environ.get('GMAIL_PASSWORD')
blogger_email = os.environ.get('BLOGGER_EMAIL')

# 2. Inisialisasi Client Modern (Otomatis menggunakan jalur stabil v1, anti 404)
client = genai.Client(api_key=api_key)

# 3. DAFTAR TOPIK MANUAL
topik_list = [
    "Tips Finansial 2026: Cara Mengelola Gaji Agar Tidak Cepat Habis",
    "Investasi AI: Mengapa Tahun Ini Adalah Waktu Terbaik Memulai",
    "Rahasia Dana Darurat yang Sering Dilupakan Orang",
    "Cara Melunasi Cicilan Tanpa Gali Lubang Tutup Lubang"
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
        
        # Eksekusi dengan model Flash terbaru lewat jalur resmi
        response = client.models.generate_content(
            model="gemini-1.5-flash", 
            contents=f"Tulis artikel blog SEO friendly yang mendalam tentang: {topik}."
        )
        
        kirim_ke_blogger(topik, response.text)
        print(f"AKHIRNYA SUKSES! Robot Modern Berhasil Terbit: {topik}")
        
    except Exception as e:
        print(f"Kendala teknis: {e}")
        exit(1)

if __name__ == "__main__":
    main()
        
