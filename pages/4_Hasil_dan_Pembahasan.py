import streamlit as st
import pandas as pd

# Konfigurasi Halaman
st.set_page_config(
    page_title="Hasil dan Pembahasan",
    page_icon="📊",
    layout="wide"
)

# Judul Halaman
st.title("📊 Hasil dan Pembahasan")
st.markdown("---")

st.markdown("""
Halaman ini menyajikan hasil kuantitatif dari proses *fine-tuning* model T5-small yang telah dijelaskan pada halaman Metodologi. Hasil ini menjadi dasar validasi bahwa model mampu menghasilkan ringkasan yang berkualitas untuk diimplementasikan dalam aplikasi ini.
""")

# Hasil Pelatihan
st.header("Hasil Pelatihan (Fine-Tuning)")
st.markdown("""
Tabel berikut menunjukkan progres pelatihan model selama 3 *epoch*. Penurunan nilai *Training Loss* dan *Validation Loss* di setiap tahap evaluasi (*step*) mengindikasikan bahwa model berhasil mempelajari pola dari data latihan secara efektif.
""")

# Data dari log training di notebook
training_data = {
    "Step": ["5,000", "10,000", "15,000", "20,000", "25,000", "30,000", "35,000"],
    "Training Loss": [2.0195, 1.9432, 1.9104, 1.8733, 1.8138, 1.8050, 1.8078],
    "Validation Loss": [2.6802, 2.6026, 2.5520, 2.5069, 2.4988, 2.4878, 2.4781]
}
df_training = pd.DataFrame(training_data)
st.table(df_training)

st.markdown("---")

# Hasil Evaluasi Final
st.header("Evaluasi Final pada Data Tes")
st.markdown("""
Setelah proses pelatihan selesai, model dievaluasi menggunakan data tes (*test set*) yang belum pernah dilihat sebelumnya. Hasil ini menunjukkan performa final model dalam menghasilkan ringkasan. Metrik yang digunakan adalah **ROUGE** (mengukur tumpang tindih kata/kalimat) dan **BLEU** (mengukur presisi).
""")

# Metrik dari hasil evaluasi final di notebook
col1, col2, col3, col4 = st.columns(4)
col1.metric("ROUGE-1", "34.09")
col2.metric("ROUGE-2", "18.68")
col3.metric("ROUGE-L", "29.38")
col4.metric("BLEU", "10.42")

st.info("""
**Interpretasi Singkat:**
- **ROUGE-1 (34.09)**: Menunjukkan adanya tumpang tindih kata tunggal sekitar 34% antara ringkasan yang dihasilkan model dengan ringkasan referensi (buatan manusia).
- **ROUGE-2 (18.68)**: Menunjukkan tumpang tindih pasangan kata sekitar 18%.
- Skor-skor ini dianggap cukup baik untuk tugas peringkasan abstraktif pada Bahasa Indonesia, yang memvalidasi bahwa model ini layak untuk digunakan.
""", icon="💡")

st.markdown("---")

# Tautan Sumber Daya
st.header("Sumber Daya & Tautan")
st.markdown("""
Berikut adalah tautan ke sumber daya utama yang digunakan dalam proses *fine-tuning* model pada penelitian ini.
- **Model Awal (Checkpoint)**: [panggi/t5-small-indonesian-summarization-cased](https://huggingface.co/panggi/t5-small-indonesian-summarization-cased)
- **Dataset**: [fajrikoto/id_liputan6](https://huggingface.co/datasets/fajrikoto/id_liputan6)
- **Repositori Asal Dataset**: [fajri91/sum_liputan6](https://github.com/fajri91/sum_liputan6/)
""")
