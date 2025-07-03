import streamlit as st
import pandas as pd

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
[cite_start]Penelitian yang mendasari aplikasi ini menggunakan pendekatan kuantitatif dalam kerangka penelitian terapan (*applied research*)[cite: 219]. [cite_start]Fokus utamanya adalah menerapkan teknologi *Natural Language Processing* (NLP) untuk menyelesaikan masalah praktis dalam optimasi mesin pencari (SEO), yaitu pembuatan meta deskripsi secara otomatis[cite: 220].

Berikut adalah tahapan penelitian yang dilaksanakan, dari identifikasi masalah hingga implementasi aplikasi.
""")

st.header("Tahapan Penelitian")

with st.expander("1. Identifikasi Masalah"):
    st.markdown("""
    - [cite_start]**Masalah Utama**: Proses pembuatan meta deskripsi untuk SEO yang sering dilakukan secara manual terbukti tidak efisien, memakan waktu, dan sulit menjaga konsistensi kualitas dalam skala besar[cite: 229].
    - [cite_start]**Dampak**: Kondisi ini menciptakan celah antara kebutuhan praktis optimasi konten dengan kapabilitas teknologi peringkasan teks modern yang belum dimanfaatkan secara optimal[cite: 230].
    """)

with st.expander("2. Studi Literatur dan Pemilihan Model"):
    st.markdown("""
    - [cite_start]**Studi Literatur**: Kajian literatur menunjukkan adanya peluang signifikan untuk menerapkan teknik NLP dalam optimasi SEO [cite: 270][cite_start], khususnya penggunaan peringkasan teks otomatis untuk menghasilkan meta deskripsi[cite: 271].
    - [cite_start]**Pemilihan Arsitektur**: Model berbasis arsitektur Transformer dipilih karena kemampuannya yang unggul dalam memahami konteks teks[cite: 275]. [cite_start]Secara spesifik, model T5 (*Text-to-Text Transfer Transformer*) dipilih karena kerangka kerjanya yang fleksibel[cite: 276, 277].
    - [cite_start]**Pemilihan Varian**: Varian **T5-small** digunakan dengan pertimbangan efisiensi sumber daya komputasi tanpa mengorbankan kemampuan generalisasi model secara signifikan[cite: 234, 279].
    - [cite_start]**Checkpoint Awal**: Model *checkpoint* `panggi/t5-small-indonesian-summarization-cased` dipilih sebagai titik awal karena telah dilatih untuk tugas peringkasan Bahasa Indonesia[cite: 235, 284].
    """)

with st.expander("3. Pengumpulan dan Pra-pemrosesan Data"):
    st.markdown("""
    - [cite_start]**Dataset**: Dataset yang digunakan adalah `fajrikoto/id_liputan6`, yang berisi lebih dari 215.000 pasangan artikel berita berbahasa Indonesia dan ringkasannya yang ditulis secara profesional[cite: 237, 292].
    - [cite_start]**Pra-pemrosesan Awal**: Dataset ini telah melalui tahap pembersihan oleh pembuatnya, meliputi normalisasi spasi dan penghapusan frasa promosi[cite: 239, 241, 242].
    - [cite_start]**Pra-pemrosesan untuk Model**: Dilakukan pra-pemrosesan tambahan yang spesifik untuk model T5[cite: 243], yaitu:
        - [cite_start]**Pemberian Awalan Tugas**: Setiap artikel diberi awalan `"ringkas: "` untuk menginstruksikan model agar melakukan tugas peringkasan[cite: 244].
        - [cite_start]**Pembatasan Token**: Teks input artikel dibatasi maksimal 512 token, sedangkan teks target ringkasan dibatasi maksimal 128 token[cite: 245, 246].
    """)

with st.expander("4. Proses Fine-Tuning Model"):
    st.markdown("""
    - [cite_start]**Proses Inti**: Tahap *fine-tuning* merupakan proses adaptasi model T5-small yang sudah terlatih (*pre-trained*) untuk tugas spesifik peringkasan teks berbahasa Indonesia pada dataset yang telah disiapkan[cite: 308]. [cite_start]Ini adalah bentuk dari *transfer learning*[cite: 309].
    - [cite_start]**Implementasi Teknis**: Proses ini diatur menggunakan kelas `Seq2SeqTrainingArguments` dan dieksekusi oleh `Seq2SeqTrainer` dari pustaka Hugging Face Transformers[cite: 311, 312].
    - **Konfigurasi Hiperparameter**: Konfigurasi kunci yang digunakan dalam proses *fine-tuning* dirangkum dalam tabel berikut.
    """)
    
    # Membuat DataFrame untuk tabel hiperparameter
    hp_data = {
        "Hiperparameter": [
            "output_dir", "learning_rate", "per_device_train_batch_size",
            "per_device_eval_batch_size", "num_train_epochs", "weight_decay",
            "save_total_limit", "load_best_model_at_end", "fp16", "push_to_hub"
        ],
        "Nilai": [
            "Irvan14/t5-small-indonesian-summarization", "2e-5", "8", "8", "3", "0.01", "2", "True", "True", "True"
        ],
        "Deskripsi": [
            "Direktori untuk menyimpan hasil model dan checkpoint.",
            [cite_start]"Nilai umum yang efektif untuk fine-tuning model Transformer[cite: 316].",
            "Jumlah sampel data yang diproses per perangkat (GPU) dalam satu iterasi pelatihan.",
            "Jumlah sampel data yang diproses per perangkat (GPU) dalam satu iterasi evaluasi.",
            "Jumlah total putaran pelatihan pada keseluruhan dataset.",
            "Teknik regularisasi untuk mencegah overfitting.",
            "Membatasi jumlah checkpoint yang disimpan untuk menghemat ruang penyimpanan.",
            "Memastikan model dengan validation loss terendah yang disimpan di akhir.",
            [cite_start]"Mengaktifkan mixed-precision training untuk mempercepat pelatihan pada GPU[cite: 316].",
            "Mengunggah model final secara otomatis ke Hugging Face Hub."
        ]
    }
    df_hp = pd.DataFrame(hp_data)
    st.table(df_hp)


with st.expander("5. Evaluasi Kinerja Model"):
    st.markdown("""
    - [cite_start]**Tujuan Evaluasi**: Untuk memvalidasi kemampuan model dalam menghasilkan ringkasan yang berkualitas pada data yang belum pernah dilihat sebelumnya (*test set*)[cite: 321].
    - [cite_start]**Metrik Kuantitatif**: Kualitas ringkasan dievaluasi menggunakan metrik standar berikut[cite: 322]:
        - **ROUGE (1, 2, L)**: Mengukur tumpang tindih kata atau urutan kata antara ringkasan hasil model dengan ringkasan referensi. [cite_start]Metrik ini adalah standar dalam evaluasi peringkasan otomatis[cite: 254, 325].
        - [cite_start]**BLEU**: Mengukur presisi n-gram dari ringkasan yang dihasilkan, yang umum digunakan dalam tugas generasi teks[cite: 255, 327].
    """)

with st.expander("6. Deployment Aplikasi"):
    st.markdown("""
    - [cite_start]**Tujuan Deployment**: Sebagai tahap akhir, model yang telah dilatih diimplementasikan ke dalam sebuah aplikasi web fungsional untuk mendemonstrasikan penerapan praktis dari hasil penelitian[cite: 257, 332].
    - [cite_start]**Framework**: Aplikasi ini dibangun menggunakan **Streamlit** untuk menyediakan antarmuka pengguna yang interaktif dan intuitif[cite: 258].
    - [cite_start]**Platform**: Untuk memastikan aksesibilitas, aplikasi ini di-*hosting* pada platform **Streamlit Community Cloud**, dengan kode sumber yang dikelola pada repositori GitHub[cite: 258, 344].
    """)
