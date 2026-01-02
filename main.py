import os
import random
import smtplib
import google.generativeai as genai
from email.message import EmailMessage
from datetime import datetime

# 1. Ambil Secret dari GitHub
api_key = os.environ.get('GEMINI_API_KEY')
sender_email = os.environ.get('SENDER_EMAIL')
gmail_password = os.environ.get('GMAIL_PASSWORD')
blogger_email = os.environ.get('BLOGGER_EMAIL')

# 2. Setup Google AI (Versi Stable)
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

topik_list = [
    "Best AI Tools for Passive Income 2026",
    "How to Build an Automated Blog with Gemini AI",
    "Future of Cloud Computing and AI Integration",
    "Strategi Menghasilkan Dolar dari Blog Otomatis"
]

def kirim_ke_blogger(subjek, isi):
    print(f"Mencoba mengirim email ke Blogger...")
    msg = EmailMessage()
    msg.set_content(isi)
    msg['Subject'] = subjek
    msg['From'] = sender_email
    msg['To'] = blogger_email

    # Kirim via SMTP Gmail
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender_email, gmail_password)
        smtp.send_message(msg)
    print("KONFIRMASI: Email berhasil terkirim!")

def jalankan_autopilot():
    topik = random.choice(topik_list)
    print(f"Memproses artikel: {topik}")
    
    try:
        # Generate konten
        response = model.generate_content(f"Tulis artikel blog SEO friendly tentang: {topik}. Gunakan Bahasa Indonesia.")
        
        # Kirim email
        kirim_ke_blogger(topik, response.text)
        print("Selesai! Cek blog Anda dalam 5 menit.")
        
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        # Jika kuota habis, script akan berhenti di sini dan memberi tanda merah
        exit(1)

if __name__ == "__main__":
    jalankan_autopilot()
                   
