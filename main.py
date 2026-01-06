import os
import smtplib
from email.message import EmailMessage
from google import genai # Memanggil library masa depan

# 1. Ambil Kredensial
api_key = os.environ.get('GEMINI_API_KEY')
sender_email = os.environ.get('SENDER_EMAIL')
gmail_password = os.environ.get('GMAIL_PASSWORD')
blogger_email = os.environ.get('BLOGGER_EMAIL')

# 2. Inisialisasi Client (Tanpa v1beta, langsung Jalur Utama)
client = genai.Client(api_key=api_key)

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
        # Menggunakan model Gemini 1.5 Flash jalur stabil
        model_name = "gemini-1.5-flash"
        
        # A. Mencari Judul (Anti-Duplikat)
        prompt_j = "Berikan satu judul unik artikel blog tentang finansial 2026. Judul saja."
        res_j = client.models.generate_content(model=model_name, contents=prompt_j)
        topik = res_j.text.strip()
        
        # B. Menulis Artikel
        prompt_a = f"Tulis artikel blog SEO friendly berdasarkan judul ini: {topik}."
        res_a = client.models.generate_content(model=model_name, contents=prompt_a)
        
        # C. Kirim
        kirim_ke_blogger(topik, res_a.text)
        print(f"Alhamdulillah! Centang Hijau! Terbit: {topik}")
        
    except Exception as e:
        print(f"Sistem menyerah karena: {e}")
        exit(1)

if __name__ == "__main__":
    main()
        
