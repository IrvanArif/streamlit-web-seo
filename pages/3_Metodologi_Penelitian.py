import streamlit as st

# Konfigurasi Halaman
st.set_page_config(
    page_title="Metodologi Penelitian",
    page_icon="🔬",
    layout="wide"
)

# Judul Halaman
st.title("🔬 Metodologi Penelitian")
st.markdown("---")

# Pengantar Metodologi
st.markdown("""
Penelitian yang mendasari aplikasi ini menggunakan pendekatan kuantitatif dalam kerangka penelitian terapan (*applied research*). Fokus utamanya adalah menerapkan teknologi *Natural Language Processing* (NLP) untuk menyelesaikan masalah praktis dalam optimasi mesin pencari (SEO), yaitu pembuatan meta deskripsi secara otomatis.

Berikut adalah tahapan penelitian yang dilaksanakan, dari identifikasi masalah hingga implementasi aplikasi.
""")

st.header("Tahapan Penelitian")

with st.expander("1. Identifikasi Masalah"):
    st.markdown("""
    - **Masalah Utama**: Proses pembuatan meta deskripsi untuk SEO yang sering dilakukan secara manual terbukti tidak efisien, memakan waktu, dan sulit menjaga konsistensi kualitas dalam skala besar.
    - **Dampak**: Kondisi ini menciptakan celah antara kebutuhan praktis optimasi konten dengan kapabilitas teknologi peringkasan teks modern yang belum dimanfaatkan secara optimal.
    """)

with st.expander("2. Studi Literatur dan Pemilihan Model"):
    st.markdown("""
    - **Studi Literatur**: Kajian literatur menunjukkan adanya peluang signifikan untuk menerapkan teknik NLP dalam optimasi SEO, khususnya penggunaan peringkasan teks otomatis untuk menghasilkan meta deskripsi.
    - **Pemilihan Arsitektur**: Model berbasis arsitektur Transformer dipilih karena kemampuannya yang unggul dalam memahami konteks teks. Secara spesifik, model T5 (*Text-to-Text Transfer Transformer*) dipilih karena kerangka kerjanya yang fleksibel.
    - **Pemilihan Varian**: Varian **T5-small** digunakan dengan pertimbangan efisiensi sumber daya komputasi tanpa mengorbankan kemampuan generalisasi model secara signifikan.
    - **Checkpoint Awal**: Model *checkpoint* `panggi/t5-small-indonesian-summarization-cased` dipilih sebagai titik awal karena telah dilatih untuk tugas peringkasan Bahasa Indonesia.
    """)

with st.expander("3. Pengumpulan dan Pra-pemrosesan Data"):
    st.markdown("""
    - **Dataset**: Dataset yang digunakan adalah `fajrikoto/id_liputan6`, yang berisi lebih dari 215.000 pasangan artikel berita berbahasa Indonesia dan ringkasannya yang ditulis secara profesional.
    - **Pra-pemrosesan Awal**: Dataset ini telah melalui tahap pembersihan oleh pembuatnya, meliputi normalisasi spasi dan penghapusan frasa promosi.
    - **Pra-pemrosesan untuk Model**: Dilakukan pra-pemrosesan tambahan yang spesifik untuk model T5, yaitu:
        - **Pemberian Awalan Tugas**: Setiap artikel diberi awalan `"ringkas: "` untuk menginstruksikan model agar melakukan tugas peringkasan.
        - **Pembatasan Token**: Teks input artikel dibatasi maksimal 512 token, sedangkan teks target ringkasan dibatasi maksimal 128 token.
    """)

with st.expander("4. Proses Fine-Tuning Model"):
    st.markdown("""
    - **Proses Inti**: Tahap *fine-tuning* merupakan proses adaptasi model T5-small yang sudah terlatih (*pre-trained*) untuk tugas spesifik peringkasan teks berbahasa Indonesia pada dataset yang telah disiapkan. Ini adalah bentuk dari *transfer learning*.
    - **Implementasi Teknis**: Proses ini diatur menggunakan kelas `Seq2SeqTrainingArguments` dan dieksekusi oleh `Seq2SeqTrainer` dari pustaka Hugging Face Transformers.
    - **Konfigurasi Hiperparameter**: Konfigurasi kunci yang digunakan dalam proses *fine-tuning* dirangkum dalam tabel berikut.
    """)
    
    # Menggunakan Markdown untuk membuat tabel, ini lebih aman dari SyntaxError
    st.markdown("""
    | Hiperparameter                  | Nilai                                       | Deskripsi                                                                    |
    |---------------------------------|---------------------------------------------|------------------------------------------------------------------------------|
    | `output_dir`                    | `Irvan14/t5-small-indonesian-summarization` | Direktori untuk menyimpan hasil model dan checkpoint.                        |
    | `learning_rate`                 | `2e-5`                                      | Nilai umum yang efektif untuk fine-tuning model Transformer.                 |
    | `per_device_train_batch_size`   | `8`                                         | Jumlah sampel data yang diproses per perangkat (GPU) dalam satu iterasi pelatihan. |
    | `per_device_eval_batch_size`    | `8`                                         | Jumlah sampel data yang diproses per perangkat (GPU) dalam satu iterasi evaluasi. |
    | `num_train_epochs`              | `3`                                         | Jumlah total putaran pelatihan pada keseluruhan dataset.                     |
    | `weight_decay`                  | `0.01`                                      | Teknik regularisasi untuk mencegah overfitting.                              |
    | `save_total_limit`              | `2`                                         | Membatasi jumlah checkpoint yang disimpan untuk menghemat ruang penyimpanan. |
    | `load_best_model_at_end`        | `True`                                      | Memastikan model dengan validation loss terendah yang disimpan di akhir.     |
    | `fp16`                          | `True`                                      | Mengaktifkan mixed-precision training untuk mempercepat pelatihan.           |
    | `push_to_hub`                   | `True`                                      | Mengunggah model final secara otomatis ke Hugging Face Hub.                  |
    """)

with st.expander("5. Evaluasi Kinerja Model"):
    st.markdown("""
    - **Tujuan Evaluasi**: Untuk memvalidasi kemampuan model dalam menghasilkan ringkasan yang berkualitas pada data yang belum pernah dilihat sebelumnya (*test set*).
    - **Metrik Kuantitatif**: Kualitas ringkasan dievaluasi menggunakan metrik standar berikut:
        - **ROUGE (1, 2, L)**: Mengukur tumpang tindih kata atau urutan kata antara ringkasan hasil model dengan ringkasan referensi. Metrik ini adalah standar dalam evaluasi peringkasan otomatis.
        - **BLEU**: Mengukur presisi n-gram dari ringkasan yang dihasilkan, yang umum digunakan dalam tugas generasi teks.
    """)

with st.expander("6. Deployment Aplikasi"):
    st.markdown("""
    - **Tujuan Deployment**: Sebagai tahap akhir, model yang telah dilatih diimplementasikan ke dalam sebuah aplikasi web fungsional untuk mendemonstrasikan penerapan praktis dari hasil penelitian.
    - **Framework**: Aplikasi ini dibangun menggunakan **Streamlit** untuk menyediakan antarmuka pengguna yang interaktif dan intuitif.
    - **Platform**: Untuk memastikan aksesibilitas, aplikasi ini di-*hosting* pada platform **Streamlit Community Cloud**, dengan kode sumber yang dikelola pada repositori GitHub.
    """)
