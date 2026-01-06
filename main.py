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

# 2. Konfigurasi "Otak" AI
genai.configure(api_key=api_key)

# 3. DAFTAR TOPIK (Ubah judul di sini secara rutin agar tidak kembar)
topik_list = [
    "Cara Cerdas Mengatur Gaji Bulanan Agar Tetap Bisa Menabung",
    "Pilihan Investasi Terbaik untuk Pemula di Tahun 2026",
    "Pentingnya Dana Darurat dan Cara Mengumpulkannya",
    "Tips Memilih Saham yang Menguntungkan untuk Jangka Panjang",
    "Rahasia Sukses Mengelola Keuangan Keluarga Tanpa Konflik"
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
        # Robot memilih satu judul secara acak dari daftar
        topik_pilihan = random.choice(topik_list)
        
        # Menggunakan model paling stabil
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # Proses pembuatan artikel
        prompt = f"Tulis artikel blog SEO friendly yang mendalam tentang: {topik_pilihan}."
        response = model.generate_content(prompt)
        
        # Kirim ke Blogger
        kirim_ke_blogger(topik_pilihan, response.text)
        print(f"ALHAMDULILLAH! Centang Hijau Kembali! Terbit: {topik_pilihan}")
        
    except Exception as e:
        print(f"Gagal karena: {e}")
        exit(1)

if __name__ == "__main__":
    main()
    
