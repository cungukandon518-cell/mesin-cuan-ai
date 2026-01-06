import os
import smtplib
import random
import google.generativeai as genai
from email.message import EmailMessage

# 1. Identitas Rahasia
api_key = os.environ.get('GEMINI_API_KEY')
sender_email = os.environ.get('SENDER_EMAIL')
gmail_password = os.environ.get('GMAIL_PASSWORD')
blogger_email = os.environ.get('BLOGGER_EMAIL')

# 2. Aktifkan Otak AI
genai.configure(api_key=api_key)

# 3. DAFTAR JUDUL (Ubah di sini kapan saja lewat HP agar tidak kembar)
topik_list = [
    "Tips Mengelola Keuangan Pribadi yang Efektif di Tahun 2026",
    "Investasi Saham untuk Pemula: Cara Memulai dengan Modal Kecil",
    "Rahasia Menabung 50 Persen dari Gaji Tanpa Harus Sengsara",
    "Mengenal Aset Masa Depan yang Cocok untuk Investasi Jangka Panjang",
    "Strategi Melunasi Hutang dan Cicilan dengan Cepat"
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
        # Memilih satu judul secara acak dari daftar di atas
        topik_pilihan = random.choice(topik_list)
        
        # Menggunakan model paling stabil (Jalur Centang Hijau)
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # Membuat isi artikel
        prompt = f"Tulis artikel blog SEO friendly yang mendalam tentang: {topik_pilihan}."
        response = model.generate_content(prompt)
        
        # Kirim ke Blogger
        kirim_ke_blogger(topik_pilihan, response.text)
        print(f"ALHAMDULILLAH! Centang Hijau Kembali! Terbit: {topik_pilihan}")
        
    except Exception as e:
        print(f"Robot gagal karena: {e}")
        exit(1)

if __name__ == "__main__":
    main()
    
