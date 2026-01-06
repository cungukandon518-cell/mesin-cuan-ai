import os
import smtplib
from email.message import EmailMessage

# Deteksi otomatis jalur pustaka AI terbaru
try:
    from google import genai
except (ImportError, AttributeError):
    try:
        import google.genai as genai
    except ImportError:
        print("Pustaka google-genai tidak ditemukan. Periksa requirements.txt.")
        exit(1)

# 1. Ambil Kredensial
api_key = os.environ.get('GEMINI_API_KEY')
sender_email = os.environ.get('SENDER_EMAIL')
gmail_password = os.environ.get('GMAIL_PASSWORD')
blogger_email = os.environ.get('BLOGGER_EMAIL')

# 2. Inisialisasi Client
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
        # Menggunakan model paling stabil untuk mengatasi error 404
        m_id = "gemini-1.5-flash"
        
        # A. Buat Judul Unik (Anti-Duplikat)
        p_judul = "Berikan satu judul unik artikel blog tentang tips finansial cerdas 2026. Judul saja."
        res_judul = client.models.generate_content(model=m_id, contents=p_judul)
        topik = res_judul.text.strip()
        
        # B. Tulis Konten Lengkap
        p_artikel = f"Tulis artikel blog SEO friendly yang menarik berdasarkan judul: {topik}."
        res_artikel = client.models.generate_content(model=m_id, contents=p_artikel)
        
        # C. Publikasi
        kirim_ke_blogger(topik, res_artikel.text)
        print(f"Alhamdulillah! Artikel berhasil terbit: {topik}")
        
    except Exception as e:
        print(f"Terjadi kendala teknis: {e}")
        exit(1)

if __name__ == "__main__":
    main()
    
