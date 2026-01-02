import os
import random
import smtplib
from email.message import EmailMessage
from google import genai

# 1. Konfigurasi
api_key = os.environ.get('GEMINI_API_KEY')
sender_email = os.environ.get('SENDER_EMAIL')
gmail_password = os.environ.get('GMAIL_PASSWORD')
blogger_email = os.environ.get('BLOGGER_EMAIL')

client = genai.Client(api_key=api_key)

topik_list = [
    "Peluang Bisnis AI 2026 yang Belum Banyak Diketahui",
    "Cara Automasi Kerja Menggunakan AI Gratis 2026",
    "Strategi Menghasilkan $300 per Bulan Tanpa Modal",
    "Membangun Aset Digital Pasif dengan Python"
]

def kirim_ke_blogger(subjek, isi):
    msg = EmailMessage()
    msg.set_content(isi) # Blogger akan memproses Markdown/Text ini
    msg['Subject'] = subjek
    msg['From'] = sender_email
    msg['To'] = blogger_email

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender_email, gmail_password)
        smtp.send_message(msg)
    print("Artikel telah dikirim ke Blogger!")

def jalankan_autopilot():
    topik = random.choice(topik_list)
    try:
        # Minta Gemini menulis artikel
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=f"Tulis artikel blog SEO friendly Bahasa Indonesia tentang: {topik}. Gunakan format teks biasa yang rapi."
        )
        
        # Kirim langsung ke Blogger
        kirim_ke_blogger(topik, response.text)
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    jalankan_autopilot()
    
