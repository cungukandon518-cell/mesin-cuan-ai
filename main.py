import os
import smtplib
from email.message import EmailMessage
from google import genai # Menggunakan library modern sesuai instruksi

# 1. Kredensial
api_key = os.environ.get('GEMINI_API_KEY')
sender_email = os.environ.get('SENDER_EMAIL')
gmail_password = os.environ.get('GMAIL_PASSWORD')
blogger_email = os.environ.get('BLOGGER_EMAIL')

# 2. Inisialisasi Client (Memaksa Jalur Resmi)
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
        # Menggunakan model flash terbaru untuk menghindari error 404
        m_id = "gemini-1.5-flash"
        
        # A. Buat Judul Unik
        p_j = "Buat satu judul unik artikel blog tentang tips keuangan masa depan 2026. Judul saja."
        res_j = client.models.generate_content(model=m_id, contents=p_j)
        topik = res_j.text.strip()
        
        # B. Tulis Artikel
        p_a = f"Tulis artikel blog SEO friendly berdasarkan judul: {topik}."
        res_a = client.models.generate_content(model=m_id, contents=p_a)
        
        # C. Posting
        kirim_ke_blogger(topik, res_a.text)
        print(f"AKHIRNYA SUKSES! Robot berhasil terbit: {topik}")
        
    except Exception as e:
        # Mencetak detail asli agar narator bisa menganalisis lebih dalam jika gagal
        print(f"Detail kendala: {e}")
        exit(1)

if __name__ == "__main__":
    main()
    
