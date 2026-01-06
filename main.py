import os
import smtplib
from email.message import EmailMessage
import google.genai as genai # Memanggil langsung tanpa folder tambahan

# Ambil rahasia dari GitHub Secrets
api_key = os.environ.get('GEMINI_API_KEY')
sender_email = os.environ.get('SENDER_EMAIL')
gmail_password = os.environ.get('GMAIL_PASSWORD')
blogger_email = os.environ.get('BLOGGER_EMAIL')

# Inisialisasi client AI
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
        # Menggunakan model paling stabil untuk tahun 2026
        m_id = "gemini-1.5-flash"
        
        # A. Mencari judul unik agar tidak duplikat
        p_judul = "Berikan satu judul unik artikel blog tentang tips finansial masa depan 2026. Judul saja."
        res_judul = client.models.generate_content(model=m_id, contents=p_judul)
        topik = res_judul.text.strip()
        
        # B. Menulis artikel lengkap
        p_artikel = f"Tulis artikel blog SEO friendly yang mendalam berdasarkan judul: {topik}."
        res_artikel = client.models.generate_content(model=m_id, contents=p_artikel)
        
        # C. Publikasi otomatis
        kirim_ke_blogger(topik, res_artikel.text)
        print(f"Sukses! Robot berhasil posting artikel: {topik}")
        
    except Exception as e:
        print(f"Robot menemui kendala: {e}")
        exit(1)

if __name__ == "__main__":
    main()
    
