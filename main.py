import os
import smtplib
from email.message import EmailMessage
# Menggunakan pemanggilan langsung untuk menghindari bentrokan sistem
try:
    import google.genai as genai_api
except ImportError:
    # Jika masih gagal, robot akan memberikan info yang jelas
    print("Pustaka google-genai belum terpasang dengan benar.")
    exit(1)

# 1. Kredensial
api_key = os.environ.get('GEMINI_API_KEY')
sender_email = os.environ.get('SENDER_EMAIL')
gmail_password = os.environ.get('GMAIL_PASSWORD')
blogger_email = os.environ.get('BLOGGER_EMAIL')

# 2. Inisialisasi Client
client = genai_api.Client(api_key=api_key)

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
        # Menggunakan model 1.5 Flash yang paling stabil
        model_id = "gemini-1.5-flash"
        
        # A. Membuat Judul Unik (Anti-Duplikat)
        p_judul = "Buatkan satu judul unik artikel blog tentang Keuangan/Investasi 2026. Judul saja."
        res_judul = client.models.generate_content(model=model_id, contents=p_judul)
        topik = res_judul.text.strip()
        
        # B. Menulis Artikel
        p_artikel = f"Tulis artikel blog SEO friendly berdasarkan judul ini: {topik}."
        res_artikel = client.models.generate_content(model=model_id, contents=p_artikel)
        
        # C. Publikasi
        kirim_ke_blogger(topik, res_artikel.text)
        print(f"Berhasil! Artikel terbit: {topik}")
        
    except Exception as e:
        print(f"Terjadi kesalahan teknis: {e}")
        exit(1)

if __name__ == "__main__":
    main()
