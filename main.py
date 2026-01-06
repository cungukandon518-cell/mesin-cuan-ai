import os
import smtplib
from email.message import EmailMessage
import google.genai as genai_new # Menggunakan identitas baru agar tidak bentrok

# 1. Ambil Rahasia
api_key = os.environ.get('GEMINI_API_KEY')
sender_email = os.environ.get('SENDER_EMAIL')
gmail_password = os.environ.get('GMAIL_PASSWORD')
blogger_email = os.environ.get('BLOGGER_EMAIL')

# 2. Inisialisasi Client Jalur Resmi (Anti-404)
client = genai_new.Client(api_key=api_key)

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
        # Menggunakan model paling stabil untuk tahun 2026
        model_id = "gemini-1.5-flash"
        
        # A. Buat Judul
        p_judul = "Tulis satu judul artikel blog unik tentang tips finansial 2026. Judul saja."
        res_judul = client.models.generate_content(model=model_id, contents=p_judul)
        topik = res_judul.text.strip()
        
        # B. Tulis Artikel
        p_artikel = f"Tulis artikel blog SEO friendly yang mendalam berdasarkan judul: {topik}."
        res_artikel = client.models.generate_content(model=model_id, contents=p_artikel)
        
        # C. Posting
        kirim_ke_blogger(topik, res_artikel.text)
        print(f"AKHIRNYA BERHASIL! Robot terbit artikel: {topik}")
        
    except Exception as e:
        # Jika masih error, robot akan memberitahu detail aslinya
        print(f"Detail kendala: {e}")
        exit(1)

if __name__ == "__main__":
    main()
        
