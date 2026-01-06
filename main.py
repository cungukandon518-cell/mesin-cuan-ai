import os
import smtplib
import google.generativeai as genai
from email.message import EmailMessage

# 1. Kredensial dari GitHub Secrets
api_key = os.environ.get('GEMINI_API_KEY')
sender_email = os.environ.get('SENDER_EMAIL')
gmail_password = os.environ.get('GMAIL_PASSWORD')
blogger_email = os.environ.get('BLOGGER_EMAIL')

# 2. Konfigurasi "Otak" AI
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
        # Menggunakan model Gemini 1.5 Flash yang paling kompatibel
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # A. Mencari Judul Baru (Mencegah Duplikat)
        prompt_judul = "Berikan satu judul unik tentang tips keuangan atau investasi tahun 2026. Hanya judul saja."
        res_judul = model.generate_content(prompt_judul)
        topik = res_judul.text.strip()
        
        # B. Menulis Konten
        prompt_artikel = f"Tulis artikel blog yang menarik dan SEO friendly berdasarkan judul ini: {topik}."
        res_artikel = model.generate_content(prompt_artikel)
        
        # C. Kirim ke Blog
        kirim_ke_blogger(topik, res_artikel.text)
        print(f"Sukses! Artikel terbit: {topik}")
        
    except Exception as e:
        # Menampilkan pesan jika terjadi kendala teknis
        print(f"Ada kendala: {e}")
        exit(1)

if __name__ == "__main__":
    main()
        
