import os
import smtplib
from email.message import EmailMessage
from google import genai # Memanggil library versi terbaru

# 1. Kredensial dari GitHub Secrets
api_key = os.environ.get('GEMINI_API_KEY')
sender_email = os.environ.get('SENDER_EMAIL')
gmail_password = os.environ.get('GMAIL_PASSWORD')
blogger_email = os.environ.get('BLOGGER_EMAIL')

# 2. Inisialisasi Robot dengan Jalur Stabil (Menghindari v1beta)
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
        # Menggunakan model Gemini 1.5 Flash jalur resmi
        model_id = "gemini-1.5-flash"
        
        # A. Membuat Judul Unik (Mencegah artikel ganda seperti di 6 Jan)
        prompt_j = "Buat satu judul unik artikel blog tentang tips keuangan cerdas 2026. Judul saja."
        res_j = client.models.generate_content(model=model_id, contents=prompt_j)
        topik = res_j.text.strip()
        
        # B. Menulis Artikel Lengkap
        prompt_a = f"Tulis artikel blog SEO friendly yang menarik berdasarkan judul: {topik}."
        res_a = client.models.generate_content(model=model_id, contents=p_a)
        
        # C. Publikasi
        kirim_ke_blogger(topik, res_a.text)
        print(f"AKHIRNYA SUKSES! Robot berhasil posting artikel: {topik}")
        
    except Exception as e:
        # Mencatat detail kendala jika masih terjadi error
        print(f"Robot menemui kendala teknis: {e}")
        exit(1)

if __name__ == "__main__":
    main()
    
