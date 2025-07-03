import streamlit as st

# Mengatur Konfigurasi Halaman
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
Meta deskripsi adalah elemen HTML yang memberikan ringkasan singkat tentang isi suatu halaman web. Meskipun tidak secara langsung menjadi faktor peringkat utama bagi Google [1], meta deskripsi yang efektif sangat krusial untuk meningkatkan *Click-Through Rate* (CTR) dari halaman hasil pencarian [2]. Deskripsi yang menarik akan memancing pengguna untuk mengklik tautan Anda, bukan milik kompetitor.
""")

# Praktik Terbaik
st.header("Praktik Terbaik (Best Practices)")

# Gunakan Expander untuk setiap poin agar lebih rapi
with st.expander("1. Jaga Panjang Karakter Tetap Optimal"):
    st.markdown("""
    - **Panjang ideal**: Usahakan panjang meta deskripsi antara **155-160 karakter**.
    - **Risiko terpotong**: Jika lebih dari itu, Google kemungkinan besar akan memotongnya, sehingga pesan Anda tidak tersampaikan sepenuhnya.
    - **Gunakan alat bantu**: Aplikasi ini sudah menyediakan penghitung karakter untuk memudahkan Anda.
    """)

with st.expander("2. Gunakan Kata Kunci Utama (Focus Keyword)"):
    st.markdown("""
    - **Relevansi**: Pastikan kata kunci utama yang Anda targetkan ada di dalam meta deskripsi.
    - **Penyorotan (Highlight)**: Google sering kali menebalkan kata kunci yang cocok dengan kueri pencarian pengguna, membuatnya lebih menonjol secara visual.
    """)

with st.expander("3. Tulis Kalimat yang Aktif dan Mengundang Aksi (Call-to-Action)"):
    st.markdown("""
    - **Gunakan kalimat aktif**: Buat deskripsi yang jelas dan langsung ke pokok permasalahan.
    - **Sertakan CTA**: Ajak pengguna untuk melakukan sesuatu. Contoh:
        - "Pelajari lebih lanjut tentang..."
        - "Temukan cara membuat..."
        - "Coba gratis sekarang."
        - "Belanja koleksi terbaru kami."
    """)

with st.expander("4. Hindari Deskripsi Duplikat"):
    st.markdown("""
    - **Keunikan itu penting**: Setiap halaman harus memiliki meta deskripsi yang unik, sama seperti tag judul (`title tag`).
    - **Dampak negatif**: Menggunakan deskripsi yang sama di banyak halaman dapat membingungkan mesin pencari dan menurunkan kualitas pengalaman pengguna.
    """)

with st.expander("5. Deskripsikan Isi Konten Secara Akurat"):
    st.markdown("""
    - **Jangan menipu (clickbait)**: Pastikan deskripsi Anda secara akurat mencerminkan apa yang akan pengguna temukan di halaman tersebut.
    - **Bounce rate**: Deskripsi yang tidak relevan dapat meningkatkan *bounce rate* (pengguna langsung kembali ke hasil pencarian), yang merupakan sinyal negatif bagi Google.
    """)

with st.expander("6. Anggap Deskripsi sebagai 'Iklan' untuk Halaman Anda"):
    st.markdown("""
    - **Tujuan utama**: Meta deskripsi adalah kesempatan Anda untuk "menjual" konten Anda kepada calon pengunjung di halaman hasil pencarian.
    - **Tonjolkan nilai lebih**: Apa yang membuat konten Anda lebih baik dari yang lain? Apakah lebih komprehensif, lebih mudah dipahami, atau menawarkan solusi unik? Sampaikan itu di sini.
    """)

st.markdown("---")

# Hal yang Perlu Dihindari
st.header("❌ Hal yang Perlu Dihindari")
st.error("""
* **Keyword Stuffing**: Jangan mengulang-ulang kata kunci secara tidak wajar. Ini terlihat seperti spam bagi pengguna dan mesin pencari.
* **Menggunakan Tanda Kutip Ganda**: Hindari penggunaan tanda kutip ganda ("...") dalam deskripsi. Google akan memotong teks pada tanda kutip tersebut saat menampilkannya di hasil pencarian.
* **Deskripsi Otomatis (Jika memungkinkan)**: Meskipun beberapa platform membuatnya secara otomatis, deskripsi yang ditulis manual hampir selalu lebih efektif.
""")

st.markdown("---")
st.markdown("""
**Referensi:**
<br>
[1] Google, "Google does not use the keywords meta tag in web ranking," *Google Search Central Blog*, 2009. [Online]. Available: https://developers.google.com/search/blog/2009/09/google-does-not-use-keywords-meta-tag
<br>
[2] A. M. T. Al-Saeed dan M. A. Wahdan, "The Impact of Meta Description on Click-Through Rate (CTR) in Search Engine Results Pages (SERPs)," *International Journal of Advanced Computer Science and Applications*, vol. 12, no. 5, hlm. 45-51, 2021.
""", unsafe_allow_html=True)import streamlit as st

# Mengatur Konfigurasi Halaman
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
Meta deskripsi adalah elemen HTML yang memberikan ringkasan singkat tentang isi suatu halaman web. Meskipun tidak secara langsung menjadi faktor peringkat utama bagi Google [1], meta deskripsi yang efektif sangat krusial untuk meningkatkan *Click-Through Rate* (CTR) dari halaman hasil pencarian [2]. Deskripsi yang menarik akan memancing pengguna untuk mengklik tautan Anda, bukan milik kompetitor.
""")

# Praktik Terbaik
st.header("Praktik Terbaik (Best Practices)")

# Gunakan Expander untuk setiap poin agar lebih rapi
with st.expander("1. Jaga Panjang Karakter Tetap Optimal"):
    st.markdown("""
    - **Panjang ideal**: Usahakan panjang meta deskripsi antara **155-160 karakter**.
    - **Risiko terpotong**: Jika lebih dari itu, Google kemungkinan besar akan memotongnya, sehingga pesan Anda tidak tersampaikan sepenuhnya.
    - **Gunakan alat bantu**: Aplikasi ini sudah menyediakan penghitung karakter untuk memudahkan Anda.
    """)

with st.expander("2. Gunakan Kata Kunci Utama (Focus Keyword)"):
    st.markdown("""
    - **Relevansi**: Pastikan kata kunci utama yang Anda targetkan ada di dalam meta deskripsi.
    - **Penyorotan (Highlight)**: Google sering kali menebalkan kata kunci yang cocok dengan kueri pencarian pengguna, membuatnya lebih menonjol secara visual.
    """)

with st.expander("3. Tulis Kalimat yang Aktif dan Mengundang Aksi (Call-to-Action)"):
    st.markdown("""
    - **Gunakan kalimat aktif**: Buat deskripsi yang jelas dan langsung ke pokok permasalahan.
    - **Sertakan CTA**: Ajak pengguna untuk melakukan sesuatu. Contoh:
        - "Pelajari lebih lanjut tentang..."
        - "Temukan cara membuat..."
        - "Coba gratis sekarang."
        - "Belanja koleksi terbaru kami."
    """)

with st.expander("4. Hindari Deskripsi Duplikat"):
    st.markdown("""
    - **Keunikan itu penting**: Setiap halaman harus memiliki meta deskripsi yang unik, sama seperti tag judul (`title tag`).
    - **Dampak negatif**: Menggunakan deskripsi yang sama di banyak halaman dapat membingungkan mesin pencari dan menurunkan kualitas pengalaman pengguna.
    """)

with st.expander("5. Deskripsikan Isi Konten Secara Akurat"):
    st.markdown("""
    - **Jangan menipu (clickbait)**: Pastikan deskripsi Anda secara akurat mencerminkan apa yang akan pengguna temukan di halaman tersebut.
    - **Bounce rate**: Deskripsi yang tidak relevan dapat meningkatkan *bounce rate* (pengguna langsung kembali ke hasil pencarian), yang merupakan sinyal negatif bagi Google.
    """)

with st.expander("6. Anggap Deskripsi sebagai 'Iklan' untuk Halaman Anda"):
    st.markdown("""
    - **Tujuan utama**: Meta deskripsi adalah kesempatan Anda untuk "menjual" konten Anda kepada calon pengunjung di halaman hasil pencarian.
    - **Tonjolkan nilai lebih**: Apa yang membuat konten Anda lebih baik dari yang lain? Apakah lebih komprehensif, lebih mudah dipahami, atau menawarkan solusi unik? Sampaikan itu di sini.
    """)

st.markdown("---")

# Hal yang Perlu Dihindari
st.header("❌ Hal yang Perlu Dihindari")
st.error("""
* **Keyword Stuffing**: Jangan mengulang-ulang kata kunci secara tidak wajar. Ini terlihat seperti spam bagi pengguna dan mesin pencari.
* **Menggunakan Tanda Kutip Ganda**: Hindari penggunaan tanda kutip ganda ("...") dalam deskripsi. Google akan memotong teks pada tanda kutip tersebut saat menampilkannya di hasil pencarian.
* **Deskripsi Otomatis (Jika memungkinkan)**: Meskipun beberapa platform membuatnya secara otomatis, deskripsi yang ditulis manual hampir selalu lebih efektif.
""")

st.markdown("---")
st.markdown("""
**Referensi:**
<br>
[1] Google, "Google does not use the keywords meta tag in web ranking," *Google Search Central Blog*, 2009. [Online]. Available: https://developers.google.com/search/blog/2009/09/google-does-not-use-keywords-meta-tag
<br>
[2] A. M. T. Al-Saeed dan M. A. Wahdan, "The Impact of Meta Description on Click-Through Rate (CTR) in Search Engine Results Pages (SERPs)," *International Journal of Advanced Computer Science and Applications*, vol. 12, no. 5, hlm. 45-51, 2021.
""", unsafe_allow_html=True)
