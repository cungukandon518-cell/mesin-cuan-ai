import os
import smtplib
import random
from google import genai # Memanggil identitas baru yang sudah terpasang
from email.message import EmailMessage

# 1. Kredensial
api_key = os.environ.get('GEMINI_API_KEY')
sender_email = os.environ.get('SENDER_EMAIL')
gmail_password = os.environ.get('GMAIL_PASSWORD')
blogger_email = os.environ.get('BLOGGER_EMAIL')

# 2. Inisialisasi Robot (Versi Stabil Masa Depan)
client = genai.Client(api_key=api_key)

# 3. DAFTAR TOPIK MANUAL (Agar Artikel Tidak Kembar)
topik_list = [
    "Tips Finansial 2026: Cara Mengatur Gaji Agar Tidak Cepat Habis",
    "Investasi AI: Mengapa Tahun Ini Adalah Waktu Terbaik Memulai",
    "Rahasia Dana Darurat yang Sering Dilupakan Orang",
    "Cara Melunasi Cicilan Tanpa Perlu Gali Lubang Tutup Lubang",
    "Strategi Cerdas Membeli Emas untuk Jangka Panjang"
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
        # Pilih judul secara acak agar tidak kembar
        topik_pilihan = random.choice(topik_list)
        
        # Menggunakan jalur stabil agar tidak terkena error 404
        response = client.models.generate_content(
            model="gemini-1.5-flash", 
            contents=f"Tulis artikel blog SEO friendly yang mendalam tentang: {topik_pilihan}."
        )
        
        # Kirim ke Blogger
        kirim_ke_blogger(topik_pilihan, response.text)
        print(f"AKHIRNYA SUKSES! Centang Hijau Kembali! Terbit: {topik_pilihan}")
        
    except Exception as e:
        print(f"Detail kendala: {e}")
        exit(1)

if __name__ == "__main__":
    main()
    
