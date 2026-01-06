import os
import smtplib
import random
from google import genai # Identitas resmi terbaru
from email.message import EmailMessage

# 1. Kredensial
api_key = os.environ.get('GEMINI_API_KEY')
sender_email = os.environ.get('SENDER_EMAIL')
gmail_password = os.environ.get('GMAIL_PASSWORD')
blogger_email = os.environ.get('BLOGGER_EMAIL')

# 2. Inisialisasi Client Modern (Otomatis menggunakan jalur stabil v1)
client = genai.Client(api_key=api_key)

# 3. Daftar Topik Manual
topik_list = [
    "Strategi Mengatur Gaji Agar Bisa Investasi di Tahun 2026",
    "Tips Memilih Saham AI untuk Tabungan Masa Tua",
    "Cara Efektif Melunasi Hutang Tanpa Stres Berlebihan",
    "Pentingnya Memiliki Dana Darurat di Masa Depan"
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
        
        # Menggunakan sintaks modern: client.models.generate_content
        response = client.models.generate_content(
            model="gemini-1.5-flash", 
            contents=f"Tulis artikel blog SEO friendly yang menarik tentang: {topik_pilihan}."
        )
        
        # Kirim artikel
        kirim_ke_blogger(topik_pilihan, response.text)
        print(f"AKHIRNYA SUKSES! Robot Modern Terbit: {topik_pilihan}")
        
    except Exception as e:
        print(f"Detail kendala: {e}")
        exit(1)

if __name__ == "__main__":
    main()
    
