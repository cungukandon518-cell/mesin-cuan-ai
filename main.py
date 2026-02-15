import os
import smtplib
from google import genai
from email.message import EmailMessage

# 1. Konfigurasi Secrets
api_key = os.environ.get('GEMINI_API_KEY')
sender_email = os.environ.get('SENDER_EMAIL')
gmail_password = os.environ.get('GMAIL_PASSWORD')
blogger_email = os.environ.get('BLOGGER_EMAIL')

# Inisialisasi Client Baru (SDK 2026)
client = genai.Client(api_key=api_key)

def kirim_ke_blogger(subjek, isi_html):
    print("Mengirim email HTML ke Blogger...")
    msg = EmailMessage()
    msg.set_content("Gunakan viewer HTML untuk melihat artikel ini.")
    msg.add_alternative(isi_html, subtype='html')
    
    msg['Subject'] = subjek
    msg['From'] = sender_email
    msg['To'] = blogger_email
    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender_email, gmail_password)
        smtp.send_message(msg)
    print("Artikel BERHASIL TERKIRIM!")

def main():
    # Daftar Topik Segar 2026
    topik_list = [
        "Sustainabilty Tech: AI sebagai Kunci Utama Melawan Perubahan Iklim",
        "Cara Mengelola AI Agent Pribadi untuk Produktivitas 10x Lipat",
        "Strategi Keamanan Finansial di Era Deepfake Voice Scam",
        "Peluang Cuan dari Carbon Trading Retail bagi Investor Pemula",
        "Masa Depan Pekerjaan Kerah Putih di Tengah Dominasi Autopilot AI"
        # ... tambahkan topik lainnya di sini
    ]
    
    run_number = int(os.environ.get('GITHUB_RUN_NUMBER', '1'))
    index = (run_number - 1) % len(topik_list)
    topik = topik_list[index]
    
    try:
        print(f"Memproses artikel ke-{run_number}: {topik}")
        
        # Menggunakan model terbaru (Gemini 2.0 Flash atau versi stabil 2026)
        prompt = f"""
        Tulis artikel blog mendalam tentang: {topik}.
        Format WAJIB HTML: gunakan <h2>, <h3>, <strong>, dan <ul>.
        Gunakan Bahasa Indonesia yang santai tapi edukatif. Minimal 700 kata.
        Sertakan bagian 'Rekomendasi Bacaan' di akhir.
        """

        response = client.models.generate_content(
            model='gemini-2.0-flash', # Update model ke versi terbaru
            contents=prompt
        )
        
        # Kirim hasil teks (response.text) ke Blogger
        kirim_ke_blogger(topik, response.text)
        print(f"PROSES SELESAI! (Topik: {topik})")
        
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        exit(1)

if __name__ == "__main__":
    main()
        
