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

def dapatkan_model_tersedia():
    """Mencari model Gemini yang aktif untuk API Key ini"""
    try:
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                # Kita cari model gemini-1.5 atau gemini-pro
                if 'gemini-1.5-flash' in m.name or 'gemini-1.5-pro' in m.name or 'gemini-pro' in m.name:
                    print(f"Menggunakan model ditemukan: {m.name}")
                    return m.name
        return None
    except Exception as e:
        print(f"Gagal melacak model: {e}")
        return "gemini-1.5-flash" # Fallback terakhir

def jalankan_autopilot():
    try:
        model_name = dapatkan_model_tersedia()
        model = genai.GenerativeModel(model_name)
        
        topik_list = [
            "Peluang Bisnis AI 2026 yang Belum Banyak Diketahui",
            "Cara Automasi Kerja Menggunakan Gemini AI Gratis",
            "Strategi Menghasilkan $300 per Bulan Tanpa Modal",
            "Membangun Aset Digital Menggunakan Python dan AI"
        ]
        
        topik = random.choice(topik_list)
        prompt = f"Tulis artikel blog SEO friendly dalam Bahasa Indonesia tentang: {topik}. Gunakan format Markdown."
        
        print(f"Sedang memproses topik: {topik}...")
        response = model.generate_content(prompt)
        
        # Simpan file
        filename = f"artikel_{datetime.now().strftime('%Y%m%d_%H%M')}.md"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(response.text)
        
        print(f"BERHASIL! Aset dibuat: {filename}")
        
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        exit(1)

if __name__ == "__main__":
    jalankan_autopilot()
        
