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
Meta deskripsi adalah tag HTML yang berisi deskripsi singkat mengenai topik sebuah halaman web [202]. Meskipun bukan satu-satunya faktor, meta deskripsi diidentifikasi sebagai salah satu faktor peringkat yang penting dalam literatur SEO [201]. Deskripsi ini merupakan elemen kedua setelah judul yang dilihat pengguna di hasil pencarian, sehingga menjadi cara terbaik untuk menarik perhatian pengunjung [202].
""")

# Praktik Terbaik
st.header("Praktik Terbaik (Best Practices)")

with st.expander("1. Jaga Panjang Karakter Tetap Optimal"):
    st.markdown("""
    Panjang optimal untuk teks meta deskripsi adalah sekitar **150 karakter**. Hal ini penting karena teks yang lebih panjang akan dipotong oleh mesin pencari, sehingga informasi atau pesan ajakan tidak tersampaikan sepenuhnya [203].
    """)

with st.expander("2. Gunakan Kata Kunci yang Relevan"):
    st.markdown("""
    Meta deskripsi harus dirancang untuk mencerminkan konten halaman dan wajib mengandung kata kunci yang relevan [26]. Penempatan kata kunci pada 150 karakter pertama akan membantu mesin pencari dan pengguna untuk cepat memahami relevansi halaman Anda [25].
    """)

with st.expander("3. Sertakan Ajakan untuk Bertindak (Call-to-Action)"):
    st.markdown("""
    Selain deskriptif, meta deskripsi yang baik harus menyertakan kalimat ajakan untuk bertindak (*call-to-action*). Ini akan mendorong pengguna untuk melakukan klik setelah membaca ringkasan Anda di hasil pencarian [203].
    """)

with st.expander("4. Pastikan Deskripsi Akurat dan Unik"):
    st.markdown("""
    Pastikan deskripsi secara akurat mewakili konten yang ada di halaman. Deskripsi yang menyesatkan dapat meningkatkan *bounce rate*. Setiap halaman di situs Anda harus memiliki meta deskripsi yang unik untuk menghindari kebingungan di mesin pencari dan memberikan pengalaman terbaik bagi pengguna.
    """)

st.markdown("---")

st.header("Referensi")
st.markdown("""
Berikut adalah daftar pustaka yang relevan dari penelitian yang mendasari aplikasi ini, sesuai dengan nomor sitasi yang digunakan.
""")

st.text("""
[8] U. Primakara, “IMPLEMENTASI PERINGKAS DOKUMEN BERBAHASA INDONESIA MENGGUNAKAN METODE TEXT TO TEXT TRANSFER TRANSFORMER (T5) I Nyoman Purnama 1) , Ni Nengah Widya Utami 2) Program Studi Sistem Informasi 1) , Sistem Informasi Akutansi 2).”

[17] G. Matošević, “Text summarization techniques for meta description generation in process of search engine optimization,” in Advances in Intelligent Systems and Computing, Springer Verlag, 2019, pp. 165–173.

[22] E. Woncharso, A. Muawwal, S. Informasi, and S. KHARISMA Makassar, “Penerapan Search Engine Optimization (SEO) untuk meningkatkan pengunjung pada website SCLEAN.” [Online]. Available: https://tech.kharisma.ac.id

[25] P. Septiani dan H. Kurniawan, “Analisa Penggunaan Keyword Untuk Implementasi Search Engine Optimization (SEO),” Jurnal Teknologi Informasi, vol. XV, no. 3, pp. 83–91, Nov. 2020.

[26] A. Zahra Maulaa Habiibah, A. Hermawan, and R. Gelar Guntara, “Implementasi Teknik Seo Dengan Metode On Page dan Off Page Dalam Meningkatkan Peringkat Website Canopybandung.Com”.

[63] Merujuk pada bagian Tujuan Penelitian dalam dokumen skripsi Anda, di mana disebutkan bahwa model diharapkan meningkatkan efisiensi kerja.

[173] Merujuk pada bagian Tinjauan Pustaka dalam skripsi Anda, yang menyatakan bahwa T5 adalah algoritma abstraktif.

[201-203] Merujuk pada bagian Meta Deskripsi SEO dalam Tinjauan Pustaka skripsi Anda.

[262-267] Merujuk pada bagian Identifikasi Masalah dalam skripsi Anda.
""")
