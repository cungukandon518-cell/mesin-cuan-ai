import os
import random
import time
from datetime import datetime
from google import genai

# 1. Setup Client dengan SDK Terbaru 2026
api_key = os.environ.get('GEMINI_API_KEY')
if not api_key:
    print("Error: API Key tidak ditemukan!")
    exit(1)

client = genai.Client(api_key=api_key)

# 2. Daftar Topik Aset
topik_list = [
    "Cara Automasi Kerja Menggunakan AI Gratis 2026",
    "Strategi Menghasilkan $300 per Bulan Tanpa Modal",
    "Membangun Aset Digital Pasif dengan Python",
    "Peluang Cuan AI yang Belum Diketahui Banyak Orang"
]

def jalankan_autopilot():
    topik = random.choice(topik_list)
    print(f"Memproses topik: {topik}...")
    
    # Kita gunakan model 'gemini-2.0-flash' (Standar paling stabil 2026)
    model_id = "gemini-2.0-flash" 
    
    # Sistem Re-try (Mencoba sampai 3 kali jika server sibuk)
    for i in range(3):
        try:
            response = client.models.generate_content(
                model=model_id,
                contents=f"Tulis artikel blog SEO friendly Bahasa Indonesia tentang: {topik}. Format Markdown."
            )
            
            # Simpan File
            filename = f"artikel_{datetime.now().strftime('%Y%m%d_%H%M')}.md"
            with open(filename, "w", encoding="utf-8") as f:
                f.write(response.text)
            
            print(f"SUKSES! Aset lahir: {filename}")
            return # Keluar jika berhasil
            
        except Exception as e:
            print(f"Percobaan {i+1} gagal, mencoba lagi dalam 10 detik... (Error: {e})")
            time.sleep(10)
    
    print("Gagal setelah 3 kali percobaan.")
    exit(1)

if __name__ == "__main__":
    jalankan_autopilot()
    
