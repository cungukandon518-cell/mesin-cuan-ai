import os
import google.generativeai as genai
import random
from datetime import datetime

# 1. Koneksi API (Mengambil dari Secrets GitHub)
api_key = os.environ.get('GEMINI_API_KEY')
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-pro')

# 2. Daftar Topik Otomatis (Aset Anda)
topik_list = [
    "Peluang Bisnis AI 2026 yang Belum Banyak Diketahui",
    "Cara Automasi Kerja Menggunakan Gemini AI Gratis",
    "Strategi Menghasilkan $300 per Bulan Tanpa Modal",
    "Tools AI Terbaik untuk Produktivitas Kerja Remote",
    "Membangun Aset Digital Menggunakan Python dan AI",
    "Masa Depan Content Creator di Era Kecerdasan Buatan"
]

def jalankan_autopilot():
    # Pilih topik secara acak
    topik = random.choice(topik_list)
    
    prompt = f"Tulis artikel blog SEO friendly dalam Bahasa Indonesia tentang: {topik}. Buat minimal 500 kata, gaya bahasa santai, informatif, dan berikan tips praktis di akhir. Gunakan format Markdown."
    
    print(f"Sedang memproses topik: {topik}...")
    response = model.generate_content(prompt)
    konten = response.text
    
    # Simpan sebagai file markdown dengan nama unik
    filename = f"artikel_{datetime.now().strftime('%Y%m%d_%H%M')}.md"
    with open(filename, "w") as f:
        f.write(konten)
    
    print(f"Berhasil! File {filename} telah dibuat.")

if __name__ == "__main__":
    jalankan_autopilot()
        
