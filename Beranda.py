import streamlit as st

# Konfigurasi halaman
st.set_page_config(
    page_title="Peringkas Meta SEO | Beranda",
    page_icon="🏠",
    layout="wide"
)

# Konten Halaman
st.title("Selamat Datang di Aplikasi Peringkas Meta SEO")
st.markdown("---")

st.header("Masalah: Inefisiensi Pembuatan Meta Deskripsi SEO")

st.markdown("""
Dalam optimasi mesin pencari (SEO), proses pembuatan meta deskripsi sering kali dilakukan secara manual. Pendekatan ini terbukti tidak efisien, memakan waktu, serta sulit untuk menjaga konsistensi kualitas, terutama untuk situs web dengan skala konten yang besar [17]. Akibatnya, banyak situs web memiliki meta deskripsi yang kurang relevan atau bahkan tidak ada sama sekali, yang dapat berdampak negatif pada visibilitas dan peringkat di halaman hasil mesin pencari (SERP) [17, 263]. Kualitas ringkasan yang subjektif juga belum tentu optimal untuk menarik perhatian pengguna di mesin pencari [262].
""")

st.header("Solusi: Otomatisasi dengan Kecerdasan Buatan (AI)")

st.markdown("""
Aplikasi ini hadir untuk menjembatani celah tersebut dengan mengimplementasikan model **Transformer T5-small**, sebuah teknologi canggih dalam bidang *Natural Language Processing* (NLP) [265]. Model ini telah terbukti efektif untuk tugas peringkasan teks secara abstraktif, yaitu dengan menghasilkan kalimat baru yang koheren, bukan sekadar menyalin dari teks asli [8, 173].

Dengan memanfaatkan model ini, proses pembuatan meta deskripsi dapat diotomatisasi. Tujuannya adalah untuk menyediakan solusi praktis yang dapat meningkatkan efisiensi kerja dan kualitas konten SEO bagi pengelola situs web, penulis konten, dan praktisi pemasaran digital [63, 267].
""")

st.info("""
**Catatan:** Nomor sitasi seperti `[17]` merujuk pada daftar pustaka yang digunakan dalam penelitian yang mendasari aplikasi ini. Daftar referensi lengkap tersedia di halaman **Panduan & Praktik Terbaik**.
""", icon="ℹ️")
