
# Beranda.py

import streamlit as st

# Konfigurasi halaman utama
st.set_page_config(
    page_title="Peringkas Meta SEO",
    page_icon="🔎",
    layout="wide"
)

# Judul Utama
st.title("Selamat Datang di Aplikasi Peringkas Meta SEO 🔎")
st.markdown("---")

# Penjelasan Masalah
st.header("Masalah: Inefisiensi Pembuatan Meta Deskripsi SEO")
st.markdown(
    """
    Di era digital yang sangat kompetitif, visibilitas di mesin pencari adalah kunci keberhasilan. Salah satu faktor penting dalam **Search Engine Optimization (SEO)** adalah **meta deskripsi**—ringkasan singkat yang muncul di hasil pencarian Google dan menentukan apakah pengguna akan mengklik tautan Anda.

    Namun, proses pembuatan meta deskripsi yang relevan dan menarik sering kali **dilakukan secara manual**. Proses ini terbukti **tidak efisien, memakan waktu, dan sulit untuk menjaga konsistensi kualitas**, terutama untuk situs web dengan ratusan atau ribuan halaman konten.
    """
)

# Penjelasan Solusi
st.header("Solusi: Otomatisasi dengan Kecerdasan Buatan (AI)")
st.markdown(
    """
    Aplikasi ini hadir untuk menjembatani celah tersebut. Dengan memanfaatkan kekuatan model *Natural Language Processing* (NLP) canggih, yaitu **Transformer T5-small**, aplikasi ini dapat secara otomatis menganalisis konten artikel Anda dan menghasilkan draf meta deskripsi yang koheren dan kontekstual.

    Tujuan kami adalah menyediakan alat bantu praktis bagi para **pemilik website, penulis konten, dan praktisi pemasaran digital** untuk meningkatkan efisiensi kerja dan kualitas konten SEO mereka.
    """
)
st.markdown("---")

# Ajakan untuk Bertindak (Call to Action)
st.info("Silakan pilih halaman **'Generator Meta Deskripsi'** dari menu navigasi di sebelah kiri untuk mulai.")
