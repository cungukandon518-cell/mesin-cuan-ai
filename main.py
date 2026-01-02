import os
import random
import smtplib
import google.generativeai as genai
from email.message import EmailMessage

# 1. Setup
api_key = os.environ.get('GEMINI_API_KEY')
sender_email = os.environ.get('SENDER_EMAIL')
gmail_password = os.environ.get('GMAIL_PASSWORD')
blogger_email = os.environ.get('BLOGGER_EMAIL')

genai.configure(api_key=api_key)

def kirim_ke_blogger(subjek, isi):
    print("Mengirim ke Blogger...")
    msg = EmailMessage()
    msg.set_content(isi)
    msg['Subject'] = subjek
    msg['From'] = sender_email
    msg['To'] = blogger_email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender_email, gmail_password)
        smtp.send_message(msg)
    print("Email TERKIRIM!")

def main():
    # Daftar Topik
    topik = random.choice(["Tips Bisnis AI 2026", "Cara Cuan Blog Otomatis", "Masa Depan Kerja Remote"])
    
    # 2. Deteksi Model Otomatis (Anti-Error 404)
    try:
        models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        # Pilih gemini-1.5-flash jika ada, jika tidak pakai yang pertama tersedia
        model_id = 'models/gemini-1.5-flash' if 'models/gemini-1.5-flash' in models else models[0]
        print(f"Menggunakan model: {model_id}")
        
        model = genai.GenerativeModel(model_id.replace('models/', ''))
        response = model.generate_content(f"Tulis artikel blog SEO Indonesia: {topik}")
        
        kirim_ke_blogger(topik, response.text)
        print("Selesai!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
        
