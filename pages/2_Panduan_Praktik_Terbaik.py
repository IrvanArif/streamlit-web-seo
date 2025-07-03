import streamlit as st

# Konfigurasi Halaman
st.set_page_config(
    page_title="Panduan Meta Deskripsi SEO",
    page_icon="📖",
    layout="wide"
)

# Judul Halaman
st.title("📖 Panduan & Praktik Terbaik Penulisan Meta Deskripsi")
st.markdown("---")

# Pengantar
st.markdown("""
Meta deskripsi adalah tag HTML yang berisi deskripsi singkat mengenai topik sebuah halaman web. Meskipun bukan satu-satunya faktor, meta deskripsi diidentifikasi sebagai salah satu faktor peringkat yang penting dalam literatur SEO. Deskripsi ini merupakan elemen kedua setelah judul yang dilihat pengguna di hasil pencarian, sehingga menjadi cara terbaik untuk menarik perhatian pengunjung.
""")

# Praktik Terbaik
st.header("Praktik Terbaik (Best Practices)")

with st.expander("1. Jaga Panjang Karakter Tetap Optimal"):
    st.markdown("""
    Panjang optimal untuk teks meta deskripsi adalah sekitar **150 karakter**. Hal ini penting karena teks yang lebih panjang akan dipotong oleh mesin pencari, sehingga informasi atau pesan ajakan tidak tersampaikan sepenuhnya.
    """)

with st.expander("2. Gunakan Kata Kunci yang Relevan"):
    st.markdown("""
    Meta deskripsi harus dirancang untuk mencerminkan konten halaman dan wajib mengandung kata kunci yang relevan. Penempatan kata kunci pada 150 karakter pertama akan membantu mesin pencari dan pengguna untuk cepat memahami relevansi halaman Anda.
    """)

with st.expander("3. Sertakan Ajakan untuk Bertindak (Call-to-Action)"):
    st.markdown("""
    Selain deskriptif, meta deskripsi yang baik harus menyertakan kalimat ajakan untuk bertindak (*call-to-action*). Ini akan mendorong pengguna untuk melakukan klik setelah membaca ringkasan Anda di hasil pencarian.
    """)

with st.expander("4. Pastikan Deskripsi Akurat dan Unik"):
    st.markdown("""
    Pastikan deskripsi secara akurat mewakili konten yang ada di halaman. Deskripsi yang menyesatkan dapat meningkatkan *bounce rate*. Setiap halaman di situs Anda harus memiliki meta deskripsi yang unik untuk menghindari kebingungan di mesin pencari dan memberikan pengalaman terbaik bagi pengguna.
    """)

st.markdown("---")

st.header("Referensi")
st.info("Informasi pada halaman ini disadur dari landasan teori dan tinjauan pustaka pada penelitian yang mendasari aplikasi ini.")

# Baris terakhir yang menyebabkan error telah dihapus.
