import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# --- KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="Buat Meta Deskripsi",
    page_icon="✍️",
    layout="wide"
)

# --- FUNGSI UNTUK MEMUAT MODEL (dengan cache agar tidak loading berulang) ---
@st.cache_resource
def load_model():
    """Memuat tokenizer dan model dari Hugging Face Hub."""
    model_name = "Irvan14/t5-small-indonesian-summarization"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    return tokenizer, model

# Panggil fungsi untuk memuat model
tokenizer, model = load_model()

# --- TAMPILAN APLIKASI ---

st.title("✍️ Buat Meta Deskripsi SEO")
st.markdown("Masukkan judul dan isi konten artikel Anda di bawah ini untuk menghasilkan draf meta deskripsi secara otomatis.")

# Layout kolom
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Masukkan Teks")
    judul_artikel = st.text_input("Judul Artikel", placeholder="Tuliskan judul artikel Anda di sini...")
    isi_konten = st.text_area("Isi Konten", placeholder="Tempelkan isi konten artikel Anda di sini...", height=300)
    
    # Tombol untuk memicu proses
    buat_tombol = st.button("Buat Deskripsi Meta", type="primary")

# --- PROSES GENERASI ---

# Inisialisasi state untuk menyimpan hasil
if 'deskripsi_seo' not in st.session_state:
    st.session_state.deskripsi_seo = "Deskripsi meta Anda akan muncul di sini..."
if 'jumlah_karakter' not in st.session_state:
    st.session_state.jumlah_karakter = 0

if buat_tombol:
    if isi_konten and judul_artikel:
        with st.spinner("AI sedang membuat ringkasan..."):
            # Gabungkan judul dan konten sebagai input
            input_text = f"Judul: {judul_artikel}\n\n{isi_konten}"
            
            # Tambahkan prefix tugas sesuai fine-tuning
            prefixed_text = "ringkas: " + input_text
            
            # Tokenisasi input
            inputs = tokenizer(prefixed_text, return_tensors="pt", max_length=512, truncation=True)

            # --- INI BAGIAN PENTING: GENERASI DENGAN PARAMETER OPTIMAL ---
            summary_ids = model.generate(
                inputs.input_ids,
                max_length=50,          # Batasi panjang maksimal meta deskripsi (sekitar 150-160 karakter)
                min_length=15,          # Batasi panjang minimal agar tidak terlalu pendek
                num_beams=4,            # Menggunakan beam search
                repetition_penalty=2.5, # Menghukum pengulangan
                length_penalty=1.0,     # Netral terhadap panjang
                early_stopping=True,    # Berhenti lebih awal jika sudah menemukan hasil baik
                no_repeat_ngram_size=2  # Mencegah pengulangan frasa 2 kata
            )
            
            # Decode hasil
            output_text = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
            
            # Simpan hasil ke session state
            st.session_state.deskripsi_seo = output_text
            st.session_state.jumlah_karakter = len(output_text)
    else:
        st.warning("Judul dan Isi Konten tidak boleh kosong.", icon="⚠️")

with col2:
    st.subheader("Deskripsi Meta SEO")
    st.write(st.session_state.deskripsi_seo)
    st.caption(f"Jumlah Karakter: {st.session_state.jumlah_karakter}")

    st.markdown("---")

    st.subheader("Pratinjau SEO")
    # Tampilkan pratinjau seperti di hasil pencarian Google
    st.markdown(f"""
    <div style="border: 1px solid #333; border-radius: 8px; padding: 15px; background-color: #262730;">
        <h5 style="color: #8ab4f8; margin: 0; font-weight: normal;">{judul_artikel if judul_artikel else 'Contoh Judul Halaman'}</h5>
        <p style="color: #bdc1c6; font-size: 14px; margin-top: 5px;">
            {st.session_state.deskripsi_seo if st.session_state.jumlah_karakter > 0 else 'Di sinilah deskripsi meta Anda akan muncul...'}
        </p>
    </div>
    """, unsafe_allow_html=True)
