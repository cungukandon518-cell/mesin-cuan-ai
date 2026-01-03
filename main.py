import os
import random
import smtplib
import google.generativeai as genai
from email.message import EmailMessage

# 1. Konfigurasi Secrets
api_key = os.environ.get('GEMINI_API_KEY')
sender_email = os.environ.get('SENDER_EMAIL')
gmail_password = os.environ.get('GMAIL_PASSWORD')
blogger_email = os.environ.get('BLOGGER_EMAIL')

genai.configure(api_key=api_key)

def kirim_ke_blogger(subjek, isi):
    print("Mengirim email ke Blogger...")
    msg = EmailMessage()
    msg.set_content(isi)
    msg['Subject'] = subjek
    msg['From'] = sender_email
    msg['To'] = blogger_email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender_email, gmail_password)
        smtp.send_message(msg)
    print("Artikel TERKIRIM!")

def main():
    # Daftar Topik Emas (High CPC)
    topik_list = [
        "Best AI Tools for Passive Income 2026",
        "How to Build an Automated Blog with Gemini AI",
        "Future of Cloud Computing and AI Integration",
        "Strategi Menghasilkan Dolar dari Blog Otomatis",
        "Peluang Bisnis AI 2026 yang Belum Banyak Diketahui"
    ]
    topik = random.choice(topik_list)
    
    # Deteksi Model Otomatis
    try:
        models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        model_id = 'models/gemini-1.5-flash' if 'models/gemini-1.5-flash' in models else models[0]
        model = genai.GenerativeModel(model_id.replace('models/', ''))
        
        # PROMPT: Meminta Gemini menulis artikel + Rekomendasi Link
        prompt = f"""
        Tulis artikel blog SEO friendly dalam Bahasa Indonesia tentang: {topik}.
        Gunakan format teks biasa yang rapi dengan sub-judul.
        
        Di bagian paling akhir artikel, tambahkan bagian bernama 'Baca Juga Rekomendasi Artikel Lainnya:' 
        lalu berikan 3 judul artikel terkait keuangan/AI lainnya dalam bentuk daftar poin.
        """
        
        print(f"Memproses artikel: {topik} menggunakan {model_id}")
        response = model.generate_content(prompt)
        
        # Kirim ke Blogger
        kirim_ke_blogger(topik, response.text)
        print("PROSES SELESAI!")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    main()
    
