import os
import random
import time
from datetime import datetime
from google import genai

# Setup
api_key = os.environ.get('GEMINI_API_KEY')
client = genai.Client(api_key=api_key)

# Daftar Topik
topik_list = [
    "Cara Automasi Kerja Menggunakan AI Gratis 2026",
    "Strategi Menghasilkan $300 per Bulan Tanpa Modal",
    "Membangun Aset Digital Pasif dengan Python",
    "Peluang Cuan AI yang Belum Diketahui Banyak Orang"
]

def jalankan_autopilot():
    topik = random.choice(topik_list)
    print(f"Mencoba memproses topik: {topik}...")
    
    # KUNCI: Gunakan 1.5-flash untuk kuota yang lebih longgar
    model_id = "gemini-1.5-flash" 
    
    # Mencoba 3 kali dengan jeda 60 detik (agar kuota RPM reset)
    for i in range(3):
        try:
            response = client.models.generate_content(
                model=model_id,
                contents=f"Tulis artikel blog SEO friendly Bahasa Indonesia tentang: {topik}. Format Markdown."
            )
            
            filename = f"artikel_{datetime.now().strftime('%Y%m%d_%H%M')}.md"
            with open(filename, "w", encoding="utf-8") as f:
                f.write(response.text)
            
            print(f"SUKSES! Aset lahir: {filename}")
            return 
            
        except Exception as e:
            print(f"Google sedang sibuk (Quota). Menunggu 60 detik sebelum mencoba lagi... (Percobaan {i+1}/3)")
            time.sleep(60) # Menunggu 1 menit penuh
    
    print("Gagal total setelah menunggu 3 menit. Silakan coba lagi nanti.")
    exit(1)

if __name__ == "__main__":
    jalankan_autopilot()
            
