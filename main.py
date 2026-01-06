import os
import smtplib
import google.generativeai as genai
from email.message import EmailMessage

# 1. Mengambil kredensial dari GitHub Secrets
api_key = os.environ.get('GEMINI_API_KEY')
sender_email = os.environ.get('SENDER_EMAIL')
gmail_password = os.environ.get('GMAIL_PASSWORD')
blogger_email = os.environ.get('BLOGGER_EMAIL')

# 2. Konfigurasi AI Gemini
genai.configure(api_key=api_key)

def kirim_ke_blogger(subjek, isi):
    """Fungsi untuk mengirim artikel ke email khusus Blogger"""
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
        # Inisialisasi model AI
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # LANGKAH A: Membuat Judul Unik (Anti-Duplikat)
        # Robot meminta AI menentukan topik yang sedang tren agar konten selalu segar
        prompt_judul = (
            "Buatkan satu judul artikel blog yang sangat menarik, unik, dan sedang tren "
            "tentang Keuangan, Investasi, atau Teknologi AI di tahun 2026. "
            "Hanya berikan judulnya saja tanpa tanda petik dan tanpa penjelasan tambahan."
        )
        respon_judul = model.generate_content(prompt_judul)
        topik = respon_judul.text.strip()
        
        # LANGKAH B: Menulis Artikel Berdasarkan Judul
        prompt_artikel = (
            f"Tulis artikel blog yang mendalam, SEO friendly, dan informatif "
            f"berdasarkan judul ini: {topik}. Gunakan struktur yang rapi dengan "
            f"pendahuluan, poin-poin penting, dan kesimpulan."
        )
        response_artikel = model.generate_content(prompt_artikel)
        
        # LANGKAH C: Proses Publikasi
        kirim_ke_blogger(topik, response_artikel.text)
        print(f"Berhasil posting artikel baru: {topik}")
        
    except Exception as e:
        # Mencatat error jika terjadi kendala teknis
        print(f"Terjadi kesalahan: {e}")
        exit(1)

if __name__ == "__main__":
    main()
