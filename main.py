import os
import smtplib
from google import genai  # Menggunakan library terbaru sesuai instruksi log
from email.message import EmailMessage

# 1. Mengambil kredensial dari GitHub Secrets
api_key = os.environ.get('GEMINI_API_KEY')
sender_email = os.environ.get('SENDER_EMAIL')
gmail_password = os.environ.get('GMAIL_PASSWORD')
blogger_email = os.environ.get('BLOGGER_EMAIL')

# 2. Inisialisasi Client GenAI Terbaru
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
        # Menggunakan model terbaru yang stabil di 2026
        model_name = "gemini-2.0-flash" 
        
        # LANGKAH A: Membuat Judul Unik (Anti-Duplikat)
        prompt_judul = "Buatkan satu judul artikel blog yang sangat menarik dan sedang tren tentang Keuangan atau Teknologi AI di tahun 2026. Berikan judul saja."
        respon_judul = client.models.generate_content(model=model_name, contents=prompt_judul)
        topik = respon_judul.text.strip()
        
        # LANGKAH B: Menulis Artikel Lengkap
        prompt_artikel = f"Tulis artikel blog yang mendalam dan SEO friendly berdasarkan judul ini: {topik}."
        response_artikel = client.models.generate_content(model=model_name, contents=prompt_artikel)
        
        # LANGKAH C: Publikasi
        kirim_ke_blogger(topik, response_artikel.text)
        print(f"Berhasil posting artikel unik: {topik}")
        
    except Exception as e:
        # Mencatat detail kesalahan jika terjadi kegagalan
        print(f"Terjadi kesalahan: {e}")
        exit(1)

if __name__ == "__main__":
    main()
        
