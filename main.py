import os
import smtplib
import random
from google import genai # Memanggil library yang sudah Anda pasang
from email.message import EmailMessage

# 1. Kredensial
api_key = os.environ.get('GEMINI_API_KEY')
sender_email = os.environ.get('SENDER_EMAIL')
gmail_password = os.environ.get('GMAIL_PASSWORD')
blogger_email = os.environ.get('BLOGGER_EMAIL')

# 2. Inisialisasi Client (Jalur Baru Anti-404)
client = genai.Client(api_key=api_key)

# 3. DAFTAR TOPIK MANUAL (Ubah di sini agar tidak kembar)
topik_list = [
    "Tips Mengelola Keuangan Pribadi di Tahun 2026",
    "Cara Investasi Saham AI untuk Pemula",
    "Rahasia Menabung 50 Persen dari Gaji Bulanan",
    "Mengenal Perbedaan Aset dan Liabilitas",
    "Strategi Melunasi Cicilan Lebih Cepat",
    "Aplikasi Pencatat Keuangan Gratis di Android",
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
    try:
        # Robot memilih satu topik secara acak
        topik_pilihan = random.choice(topik_list)
        
        # Menggunakan model 1.5 Flash jalur resmi
        response = client.models.generate_content(
            model="gemini-1.5-flash", 
            contents=f"Tulis artikel blog SEO friendly yang mendalam tentang: {topik_pilihan}."
        )
        
        # Kirim ke Blogger
        kirim_ke_blogger(topik_pilihan, response.text)
        print(f"AKHIRNYA SUKSES! Centang Hijau Kembali! Terbit: {topik_pilihan}")
        
    except Exception as e:
        print(f"Robot gagal karena: {e}")
        exit(1)

if __name__ == "__main__":
    main()
    
