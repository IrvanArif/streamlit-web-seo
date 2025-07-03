import streamlit as st

# Konfigurasi halaman
st.set_page_config(
    page_title="Peringkas Meta SEO | Beranda",
    page_icon="🏠",
    layout="wide"
)

# --- KONTEN HALAMAN ---

st.title("Selamat Datang di Aplikasi Peringkas Meta SEO")
st.markdown("---")

st.header("Otomatisasi Deskripsi Meta SEO dengan Kecerdasan Buatan")

st.markdown("""
Aplikasi ini adalah alat bantu yang dirancang untuk **mempercepat dan mempermudah proses pembuatan meta deskripsi SEO**. Dengan memanfaatkan model kecerdasan buatan (AI) **T5-small** yang telah di-*fine-tuning*, aplikasi ini mampu menganalisis artikel Anda dan menghasilkan draf ringkasan yang relevan dan efektif secara otomatis.

Tujuannya adalah untuk membantu Anda menghemat waktu dan meningkatkan kualitas konten SEO tanpa perlu membuat deskripsi dari nol.
""")

st.subheader("Untuk Siapa Aplikasi Ini?")
st.markdown("""
Aplikasi ini sangat cocok untuk:
- **Penulis Konten & Blogger**: Mempercepat alur kerja saat mempublikasikan artikel baru.
- **Praktisi SEO & Digital Marketer**: Mengoptimalkan puluhan hingga ratusan halaman web dengan efisien.
- **Pemilik Bisnis & Situs Web**: Meningkatkan visibilitas online dengan meta deskripsi yang lebih baik.
""")

st.markdown("---")

st.success("""
### Siap Mencoba?

- Klik halaman **Buat Meta Deskripsi SEO** di bilah sisi untuk mulai menggunakan alat ini.
- Kunjungi halaman **Panduan**, **Metodologi**, dan **Hasil** untuk mempelajari lebih lanjut tentang praktik terbaik SEO dan detail teknis penelitian di balik aplikasi ini.
""", icon="🚀")
