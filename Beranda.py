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
Aplikasi ini adalah alat bantu yang dirancang untuk **mempercepat dan mempermudah proses pembuatan meta deskripsi SEO**. Dengan memanfaatkan model kecerdasan buatan (AI) **T5-small**.

Tujuannya adalah untuk membantu Anda menghemat waktu dan membuat konten SEO tanpa perlu membuat deskripsi dari nol.
""")
st.markdown("---")

st.success("""
### Siap Mencoba?

- Klik halaman **Buat Meta Deskripsi SEO** di bilah sisi untuk mulai menggunakan alat ini.
- Kunjungi halaman **Panduan**, **Metodologi**, dan **Hasil** untuk mempelajari lebih lanjut tentang praktik terbaik SEO dan detail teknis penelitian di balik aplikasi ini.
""", icon="🚀")
