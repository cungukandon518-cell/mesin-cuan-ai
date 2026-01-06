import os
import smtplib
import random
import google.generativeai as genai
from email.message import EmailMessage

# 1. Kredensial
api_key = os.environ.get('GEMINI_API_KEY')
sender_email = os.environ.get('SENDER_EMAIL')
gmail_password = os.environ.get('GMAIL_PASSWORD')
blogger_email = os.environ.get('BLOGGER_EMAIL')

genai.configure(api_key=api_key)

# 2. DAFTAR TOPIK MANUAL
topik_list = [
    "Cara Cerdas Mengatur Keuangan Pribadi di Tahun 2026",
    "Investasi Saham AI: Panduan Lengkap untuk Pemula",
    "Rahasia Menabung 50 Persen Gaji Tanpa Tersiksa",
    "Pentingnya Memiliki Dana Darurat Sejak Dini"
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
    topik_pilihan = random.choice(topik_list)
    
    # KUNCI PEMUTUS SIKLUS: Mencoba daftar model yang tersedia secara otomatis
    model_alternatif = ['gemini-1.5-flash', 'gemini-1.5-flash-latest', 'gemini-pro']
    
    berhasil = False
    for m_name in model_alternatif:
        try:
            print(f"Mencoba model: {m_name}...")
            model = genai.GenerativeModel(model_name=m_name)
            response = model.generate_content(f"Tulis artikel blog SEO friendly tentang: {topik_pilihan}.")
            
            # Jika berhasil generate, langsung kirim
            kirim_ke_blogger(topik_pilihan, response.text)
            print(f"AKHIRNYA SUKSES! Berhasil dengan {m_name}. Terbit: {topik_pilihan}")
            berhasil = True
            break 
        except Exception as e:
            print(f"Gagal di {m_name}: {e}")
            continue

    if not berhasil:
        print("Siklus berlanjut karena Google menolak semua model. Cek kuota API Key Anda.")
        exit(1)

if __name__ == "__main__":
    main()
            
