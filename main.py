import os
import smtplib
import random
from google import genai 
from email.message import EmailMessage

# 1. Kredensial
api_key = os.environ.get('GEMINI_API_KEY')
sender_email = os.environ.get('SENDER_EMAIL')
gmail_password = os.environ.get('GMAIL_PASSWORD')
blogger_email = os.environ.get('BLOGGER_EMAIL')

# 2. Inisialisasi Robot (Gunakan jalur otomatis)
client = genai.Client(api_key=api_key)

# 3. DAFTAR TOPIK MANUAL (Agar Artikel Tidak Kembar)
topik_list = [
    "Cara Cerdas Mengatur Keuangan di Tahun 2026",
    "Investasi Saham untuk Pemula: Mulai dari Mana?",
    "Tips Menabung 50 Persen Gaji Tanpa Tersiksa",
    "Mengenal Aset yang Cocok untuk Masa Depan",
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
        topik_pilihan = random.choice(topik_list)
        
        # MENGGUNAKAN GEMINI-1.0-PRO UNTUK MENGHINDARI 404
        # Jika model 1.5-flash menolak, model 1.0-pro biasanya selalu terbuka
        response = client.models.generate_content(
            model="gemini-1.0-pro", 
            contents=f"Tulis artikel blog SEO friendly tentang: {topik_pilihan}."
        )
        
        kirim_ke_blogger(topik_pilihan, response.text)
        print(f"AKHIRNYA SUKSES! Centang Hijau Terbit: {topik_pilihan}")
        
    except Exception as e:
        print(f"Detail kendala: {e}")
        exit(1)

if __name__ == "__main__":
    main()
        
