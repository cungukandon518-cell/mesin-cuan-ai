import os
import smtplib
import random
import google.generativeai
from email.message import EmailMessage

# 1. Kredensial
api_key = os.environ.get('GEMINI_API_KEY')
sender_email = os.environ.get('SENDER_EMAIL')
gmail_password = os.environ.get('GMAIL_PASSWORD')
blogger_email = os.environ.get('BLOGGER_EMAIL')

genai.configure(api_key=api_key)

# 2. DAFTAR TOPIK MANUAL (Agar tidak kembar)
topik_list = [
    "Cara Cerdas Mengatur Keuangan di Tahun 2026",
    "Investasi Saham untuk Pemula: Mulai dari Mana?",
    "Tips Menabung 50 Persen Gaji Tanpa Tersiksa",
    "Mengenal Aset yang Cocok untuk Masa Depan"
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
    # DAFTAR MODEL YANG AKAN DICOBA SATU PER SATU
    daftar_model = ['gemini-1.5-flash', 'gemini-1.5-flash-latest', 'gemini-pro']
    
    berhasil = False
    for nama_model in daftar_model:
        try:
            print(f"Mencoba mengetuk pintu model: {nama_model}...")
            model = genai.GenerativeModel(nama_model)
            response = model.generate_content(f"Tulis artikel blog SEO friendly tentang: {topik_pilihan}.")
            
            # Jika sampai sini tidak error, berarti berhasil
            kirim_ke_blogger(topik_pilihan, response.text)
            print(f"ALHAMDULILLAH! Berhasil dengan model {nama_model}. Terbit: {topik_pilihan}")
            berhasil = True
            break # Berhenti mencari jika sudah sukses
        except Exception as e:
            print(f"Model {nama_model} menolak (404/Error). Mencoba model berikutnya...")
            continue

    if not berhasil:
        print("Semua model menolak. Harap cek apakah API Key di GitHub Secrets sudah benar.")
        exit(1)

if __name__ == "__main__":
    main()
            
