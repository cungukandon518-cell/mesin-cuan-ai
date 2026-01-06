import os
import smtplib
import google.generativeai as genai
from email.message import EmailMessage

# 1. Ambil Kredensial
api_key = os.environ.get('GEMINI_API_KEY')
sender_email = os.environ.get('SENDER_EMAIL')
gmail_password = os.environ.get('GMAIL_PASSWORD')
blogger_email = os.environ.get('BLOGGER_EMAIL')

# 2. Konfigurasi AI
genai.configure(api_key=api_key)

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
        # Menggunakan model Flash yang paling kompatibel di awal 2026
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # A. Buat Judul Unik
        p_judul = "Buat satu judul unik tentang tips keuangan cerdas 2026. Judul saja."
        res_judul = model.generate_content(p_judul)
        topik = res_judul.text.strip()
        
        # B. Tulis Artikel
        p_artikel = f"Tulis artikel blog SEO friendly berdasarkan judul: {topik}."
        res_artikel = model.generate_content(p_artikel)
        
        # C. Posting
        kirim_ke_blogger(topik, res_artikel.text)
        print(f"Berhasil! Artikel terbit: {topik}")
        
    except Exception as e:
        # Menampilkan pesan error agar kita tahu masalahnya
        print(f"Robot menemui kendala: {e}")
        exit(1)

if __name__ == "__main__":
    main()
    
