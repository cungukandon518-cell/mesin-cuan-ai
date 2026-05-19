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
    # DAFTAR TOPIK BARU 2026
    topik_list = [
        "Panduan Membangun AI Agent Pribadi untuk Automasi Tugas Harian",
        "Masa Depan Investasi: Mengapa Karbon Kredit Menjadi Aset Berharga",
        "Cara Melindungi Aset Digital dari Serangan Deepfake Scan",
        "Strategi Passive Income: Menyewakan Komputasi GPU untuk Jaringan AI",
        "Transformasi E-Commerce: Belanja Menggunakan Asisten Virtual Berbasis Voice",
        "Mengenal Bio-Hacking: Teknologi AI untuk Memperpanjang Usia Produktif",
        "Peluang Bisnis di Sektor Humanoid Robot Service untuk UMKM",
        "Cara Kerja Decentralized AI: Menjaga Privasi Data di Era Generative AI",
        "Panduan Investasi Real Estate di Kota Pintar (Smart City) Indonesia",
        "Strategi Mengelola Portofolio Kripto di Era Pasca-Halving 2024-2026",
        "Etika Menggunakan AI dalam Pekerjaan Kreatif agar Tetap Orisinal",
        "Masa Depan Transportasi: Bagaimana Taksi Terbang Mengubah Ekonomi Lokal",
        "Cara Memanfaatkan AI untuk Deteksi Dini Peluang Saham Blue Chip",
        "Personalized Medicine: Bagaimana AI Merancang Suplemen Sesuai DNA Anda",
        "Tips Sukses Freelance di Global Market dengan Bantuan Tool AI Agent",
        "Mengenal Konsep 'Digital Twin' untuk Perencanaan Keuangan Keluarga",
        "Dampak Teknologi Quantum Computing terhadap Keamanan Perbankan Digital",
        "Cara Membuat Konten Edukasi yang Viral dengan Hyper-Personalization AI",
        "Strategi Mengahadapi Inflasi Digital: Mengapa Aset Fisik Tetap Penting",
        "Review Gadget Wearable 2026: Hidup Tanpa Smartphone dengan Kacamata AR",
        "Peluang Karir sebagai AI Auditor: Pekerjaan Paling Dicari Tahun Ini",
        "Cara Menggunakan AI untuk Optimalisasi Pajak dan Laporan Keuangan",
        "Dampak Integrasi Chip Neural pada Produktivitas Kerja Manusia",
        "Pemanfaatan AI dalam Pertanian Presisi untuk Ketahanan Pangan Rumah Tangga",
        "Micro-SaaS: Membangun Aplikasi AI Spesifik Tanpa Harus Jago Coding",
        "Menggunakan AI untuk Riset Tren Jualan Online yang Cepat Laku",
        "Strategi Exit Plan Investasi di Tengah Volatilitas Ekonomi Global",
        "Membangun Brand Pribadi di Era AI: Menjadi Manusia yang Tak Tergantikan",
        "Cara AI Membantu Menemukan Hobi yang Menghasilkan Cuan",
        "Masa Depan Konsultasi Psikologi: AI Sebagai Pendengar 24 Jam"
    ]
    
    run_number = int(os.environ.get('GITHUB_RUN_NUMBER', '1'))
    index = (run_number - 1) % len(topik_list)
    topik = topik_list[index]
    
    # --- LOGIKA PENENTUAN IKLAN PRODUK DIGITAL (80% PEMBAHASAN UTAMA) ---
    topik_lower = topik.lower()
    if "keuangan" in topik_lower or "investasi" in topik_lower or "pajak" in topik_lower or "ekonomi" in topik_lower:
        nama_produk = "25+ Template Excel Keuangan Premium"
        detail_produk = """
        - Berisi lebih dari 25 template siap pakai untuk laporan keuangan harian, bulanan, analisis profit-loss, hingga budgeting otomatis.
        - Keunggulan: Praktis, otomatis, mudah digunakan bahkan untuk pemula, dan membantu mengambil keputusan finansial lebih akurat tanpa pusing rumus matematika.
        - Harga Promo Spesial: Hanya IDR 11,000 (Diskon dari IDR 22,000).
        """
    elif "konten" in topik_lower or "brand" in topik_lower or "viral" in topik_lower or "jualan" in topik_lower:
        nama_produk = "1000+ Ide Konten Jualan Siap Pakai & 3000+ Desain Template Promosi"
        detail_produk = """
        - Berisi 1000+ ide konten jualan harian yang praktis, siap pakai, dan sudah teruji menaikkan interaksi di media sosial.
        - Dilengkapi dengan bundel 3000+ desain template promosi yang mudah diedit di Canva untuk berbagai kebutuhan bisnis online dan UMKM.
        - Keunggulan: Hemat waktu, bikin jualan makin laris, desain berkualitas tinggi, dan langsung pakai instant download.
        - Harga Promo Spesial: Hanya IDR 10,000 - IDR 11,000 saja.
        """
    else:
        nama_produk = "Bundle Mega Pack 500++ Produk Digital Premium (Siap Jual Kembali)"
        detail_produk = """
        - Paket terlengkap berisi 500++ produk digital siap pakai mulai dari e-book, template Canva, template website, ecourse jualan online, hingga aplikasi hitung keuangan.
        - Keunggulan: Dilengkapi dengan hak PLR/MRR (Bisa Diperjualbelikan Kembali), artinya pembeli bisa menjual ulang paket ini dan mendapatkan PROFIT 100% penuh tanpa bagi hasil. Dapat bonus video cara jualan dan bimbingan lewat WhatsApp.
        - Harga Promo Spesial: Hanya IDR 29,000 (Harga Normal IDR 319,000).
        """

    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # PROMPT STRATEGI 80% PRODUK DIGITAL : 20% NICHE AWAL
        prompt = f"""
        Tulis artikel blog SEO friendly dalam Bahasa Indonesia dengan ketentuan struktur bobot bahasan berikut:
        
        1. TOPiK UTAMA PEMBUKA (Bobot 20%): {topik}. 
           Tulis bagian pengantar atau latar belakang masalah secara singkat, padat, dan menarik mengenai topik ini di 1-2 paragraf awal saja.
        
        2. PEMBAHASAN SOLUSI & PRODUK DIGITAL (Bobot 80%): 
           Hubungkan masalah di atas langsung dengan pentingnya memiliki tools instan. Gunakan sisa porsi artikel (paling besar) untuk membedah secara mendalam dan merekomendasikan produk digital berikut:
           - Nama Produk: {nama_produk}
           - Detail & Manfaat yang harus diulas: 
           {detail_produk}
           
           Buat ulasan yang sangat detail mengenai manfaat produk ini, mengapa pembaca wajib memilikinya sekarang juga untuk mempermudah hidup/bisnis mereka, dan mengapa harganya sangat murah dan menguntungkan. Gunakan sub-judul (heading) yang menarik untuk membedah produk ini.
        
        3. CALL TO ACTION (CTA):
           Di akhir ulasan produk, berikan kalimat ajakan yang kuat untuk membeli, lalu tuliskan teks penanda tautan persis seperti ini: '[KLIK DI SINI UNTUK AMBIL SEKARANG: https://lynk.id/planifyid]'.
        
        4. REKOMENDASI BACAAN:
           Di bagian paling akhir artikel, tambahkan bagian 'Baca Juga Rekomendasi Artikel Lainnya:' lalu berikan 3 judul artikel terkait keuangan/AI lainnya dalam bentuk daftar poin.
        
        Gunakan format teks biasa yang rapi dengan sub-judul. Gunakan poin-poin penting agar mudah dibaca. Jangan pakai markdown bold bintang ganda di dalam tanda kurung link.
        """
        
        print(f"Memproses artikel urut ke-{run_number}: {topik}")
        response = model.generate_content(prompt)
        
        # Kirim ke Blogger
        kirim_ke_blogger(topik, response.text)
        print(f"PROSES SELESAI! (Index: {index})")
        
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        exit(1)

if __name__ == "__main__":
    main()
    
