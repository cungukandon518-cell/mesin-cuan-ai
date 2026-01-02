import os
import google.generativeai as genai
import random
from datetime import datetime

# 1. Ambil API Key dari Secrets GitHub
api_key = os.environ.get('GEMINI_API_KEY')

if not api_key:
    print("Error: GEMINI_API_KEY tidak ditemukan!")
    exit(1)

genai.configure(api_key=api_key)

# 2. PERBAIKAN UTAMA: Gunakan model 'gemini-1.5-flash' 
# Model ini lebih baru, lebih cepat, dan jarang terkena error 404
model = genai.GenerativeModel('gemini-1.5-flash')

topik_list = [
    "Cara Automasi Kerja Menggunakan Gemini AI Gratis",
    "Strategi Menghasilkan $300 per Bulan Tanpa Modal",
    "Tools AI Terbaik untuk Produktivitas Kerja Remote",
    "Membangun Aset Digital Menggunakan Python dan AI",
    "Masa Depan Content Creator di Era Kecerdasan Buatan"
]

def jalankan_autopilot():
    try:
        topik = random.choice(topik_list)
        prompt = f"Tulis artikel blog SEO friendly dalam Bahasa Indonesia tentang: {topik}. Buat minimal 500 kata, gaya bahasa santai, informatif, dan berikan tips praktis di akhir. Gunakan format Markdown."
        
        print(f"Sedang memproses topik: {topik}...")
        
        # Memanggil API dengan penanganan error
        response = model.generate_content(prompt)
        
        if not response.text:
            print("Error: Gemini memberikan respons kosong.")
            return

        filename = f"artikel_{datetime.now().strftime('%Y%m%d_%H%M')}.md"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(response.text)
        
        print(f"Berhasil membuat: {filename}")
        
    except Exception as e:
        print(f"Terjadi kesalahan teknis: {e}")
        exit(1)

if __name__ == "__main__":
    jalankan_autopilot()
        
