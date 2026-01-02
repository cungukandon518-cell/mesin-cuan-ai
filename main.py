import os
import random
import smtplib
import google.generativeai as genai
from email.message import EmailMessage

# 1. Ambil Secrets
api_key = os.environ.get('GEMINI_API_KEY')
sender_email = os.environ.get('SENDER_EMAIL')
gmail_password = os.environ.get('GMAIL_PASSWORD')
blogger_email = os.environ.get('BLOGGER_EMAIL')

genai.configure(api_key=api_key)

def kirim_ke_blogger(subjek, isi):
    print("Mencoba mengirim email...")
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
    topik_list = ["Cara Cuan dari AI 2026", "Panduan Blog Otomatis Python", "Strategi Affiliate Tanpa Modal"]
    topik = random.choice(topik_list)
    
    # 2. Cari Model yang Tersedia (Anti-404)
    model_name = 'gemini-1.5-flash' # Default
    try:
        # Kita tanya Google: "Model apa yang boleh saya pakai?"
        models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        print(f"Model tersedia: {models}")
        if 'models/gemini-1.5-flash' in models:
            model_name = 'gemini-1.5-flash'
        elif 'models/gemini-pro' in models:
            model_name = 'gemini-pro'
        else:
            model_name = models[0].replace('models/', '')
    except:
        print("Gagal list models, gunakan default.")

    print(f"Menggunakan model: {model_name}")
    model = genai.GenerativeModel(model_name)
    
    try:
        response = model.generate_content(f"Tulis artikel blog SEO Indonesia tentang: {topik}")
        kirim_ke_blogger(topik, response.text)
        print("PROSES SELESAI!")
    except Exception as e:
        print(f"Gagal generate: {e}")

if __name__ == "__main__":
    main()
        
