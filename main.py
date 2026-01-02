import os
import random
import smtplib
import time
from email.message import EmailMessage
from google import genai

# Ambil Secret dari GitHub
api_key = os.environ.get('GEMINI_API_KEY')
sender_email = os.environ.get('SENDER_EMAIL')
gmail_password = os.environ.get('GMAIL_PASSWORD')
blogger_email = os.environ.get('BLOGGER_EMAIL')

client = genai.Client(api_key=api_key)

topik_list = [
    "Best AI Tools for Passive Income 2026",
    "How to Build an Automated Blog with Gemini AI",
    "Future of Cloud Computing and AI Integration"
]

def kirim_ke_blogger(subjek, isi):
    print(f"Mencoba mengirim email dari {sender_email} ke {blogger_email}...")
    msg = EmailMessage()
    msg.set_content(isi)
    msg['Subject'] = subjek
    msg['From'] = sender_email
    msg['To'] = blogger_email

    # Menggunakan SMTP SSL Port 465
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender_email, gmail_password)
        smtp.send_message(msg)
    print("KONFIRMASI: Email berhasil keluar dari server Gmail!")

def jalankan_autopilot():
    topik = random.choice(topik_list)
    print(f"Topik terpilih: {topik}")
    
    # Generate Konten
    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=f"Tulis artikel blog SEO friendly tentang: {topik}. Gunakan Bahasa Indonesia."
    )
    
    # Kirim Email (Tanpa try-except agar error terlihat di GitHub Actions)
    kirim_ke_blogger(topik, response.text)

if __name__ == "__main__":
    jalankan_autopilot()
    
