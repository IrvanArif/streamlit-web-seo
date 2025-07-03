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

# Inisialisasi session_state di awal untuk menyimpan hasil
if 'deskripsi_seo' not in st.session_state:
    st.session_state.deskripsi_seo = "Deskripsi meta Anda akan muncul di sini..."
if 'jumlah_karakter' not in st.session_state:
    st.session_state.jumlah_karakter = 0

# --- STRUKTUR LAYOUT DENGAN 2 KOLOM ---
col1, col2 = st.columns([1, 1])

# --- KOLOM 1: INPUT PENGGUNA ---
with col1:
    st.subheader("Masukkan Teks")
    judul_artikel = st.text_input("Judul Artikel", placeholder="Tuliskan judul artikel Anda di sini...")
    isi_konten = st.text_area("Isi Konten", placeholder="Tempelkan isi konten artikel Anda di sini...", height=300)
    
    buat_tombol = st.button("Buat Deskripsi Meta", type="primary")

    # Logika proses hanya berjalan jika tombol ditekan
    if buat_tombol:
        if isi_konten and judul_artikel:
            with st.spinner("AI sedang membuat ringkasan..."):
                input_text = f"Judul: {judul_artikel}\n\n{isi_konten}"
                prefixed_text = "ringkas: " + input_text
                inputs = tokenizer(prefixed_text, return_tensors="pt", max_length=512, truncation=True)

                # --- PARAMETER GENERASI YANG DIPERBAIKI ---
                summary_ids = model.generate(
                    inputs.input_ids,
                    max_length=40,          # DIUBAH: Mengurangi jumlah token agar karakter tidak lebih dari 160
                    min_length=12,
                    num_beams=4,
                    repetition_penalty=2.5,
                    length_penalty=1.0,
                    early_stopping=True,
                    no_repeat_ngram_size=2
                )
                
                output_text = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
                
                # Simpan hasil ke session state untuk ditampilkan di kolom 2
                st.session_state.deskripsi_seo = output_text
                st.session_state.jumlah_karakter = len(output_text)
                
                # Memaksa re-run agar tampilan di kolom kanan langsung update (best practice)
                st.rerun() 
                
        else:
            st.warning("Judul dan Isi Konten tidak boleh kosong.", icon="⚠️")

# --- KOLOM 2: OUTPUT DAN PRATINJAU (Selalu ditampilkan) ---
with col2:
    st.subheader("Deskripsi Meta SEO")
    st.write(st.session_state.deskripsi_seo)
    st.caption(f"Jumlah Karakter: {st.session_state.jumlah_karakter}")

    st.markdown("---")

    st.subheader("Pratinjau SEO")
    st.markdown(f"""
    <div style="border: 1px solid #333; border-radius: 8px; padding: 15px; background-color: #262730;">
        <h5 style="color: #8ab4f8; margin: 0; font-weight: normal;">{judul_artikel if judul_artikel else 'Contoh Judul Halaman'}</h5>
        <p style="color: #bdc1c6; font-size: 14px; margin-top: 5px;">
            {st.session_state.deskripsi_seo if st.session_state.jumlah_karakter > 0 else 'Di sinilah deskripsi meta Anda akan muncul...'}
        </p>
    </div>
    """, unsafe_allow_html=True)
