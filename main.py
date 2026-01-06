import os
import smtplib
import random
from google import genai # Memanggil identitas 2026 agar tidak ModuleNotFoundError
from email.message import EmailMessage

# 1. Ambil Kunci Rahasia
api_key = os.environ.get('GEMINI_API_KEY')
sender_email = os.environ.get('SENDER_EMAIL')
gmail_password = os.environ.get('GMAIL_PASSWORD')
blogger_email = os.environ.get('BLOGGER_EMAIL')

# 2. Inisialisasi Robot (MEMAKSA PINTU UTAMA 'v1')
client = genai.Client(api_key=api_key, http_options={'api_version': 'v1'})

# 3. DAFTAR TOPIK MANUAL (Agar Tidak Kembar)
topik_list = [
    "Tips Keuangan 2026: Cara Mengatur Gaji Agar Tidak Cepat Habis",
    "Investasi AI: Mengapa Tahun Ini Adalah Waktu Terbaik Memulai",
    "Rahasia Dana Darurat yang Sering Dilupakan Orang"
]

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
        topik = random.choice(topik_list)
        
        # Eksekusi AI lewat jalur resmi v1 (Anti 404)
        response = client.models.generate_content(
            model="gemini-1.5-flash", 
            contents=f"Tulis artikel blog SEO friendly tentang: {topik}."
        )
        
        kirim_ke_blogger(topik, response.text)
        print(f"AKHIRNYA SUKSES! Siklus Putus. Terbit: {topik}")
        
    except Exception as e:
        print(f"Detail kendala: {e}")
        exit(1)

if __name__ == "__main__":
    main()
        
