import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# --- KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="Buat Meta Deskripsi",
    page_icon="✍️",
    layout="wide"
)

# --- FUNGSI UNTUK MEMUAT MODEL ---
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

# Inisialisasi session_state untuk menyimpan hasil
if 'deskripsi_seo' not in st.session_state:
    st.session_state.deskripsi_seo = "Deskripsi meta Anda akan muncul di sini..."
if 'judul_pratinjau' not in st.session_state:
    st.session_state.judul_pratinjau = "Contoh Judul Halaman"

# --- STRUKTUR LAYOUT DENGAN 2 KOLOM ---
col1, col2 = st.columns([1, 1])

# --- KOLOM 1: INPUT PENGGUNA ---
with col1:
    st.subheader("Masukkan Teks")
    judul_artikel = st.text_input("Judul Artikel", placeholder="Tuliskan judul artikel Anda di sini...")
    isi_konten = st.text_area("Isi Konten", placeholder="Tempelkan isi konten artikel Anda di sini...", height=300)
    
    buat_tombol = st.button("Buat Deskripsi Meta", type="primary")

# --- KOLOM 2: OUTPUT DAN PRATINJAU ---
with col2:
    st.subheader("Deskripsi Meta SEO")
    
    # Logika proses dipindahkan ke sini, hanya berjalan jika tombol ditekan
    if buat_tombol:
        if isi_konten and judul_artikel:
            with st.spinner("AI sedang membuat ringkasan..."):
                input_text = f"Judul: {judul_artikel}\n\n{isi_konten}"
                prefixed_text = "ringkas: " + input_text
                inputs = tokenizer(prefixed_text, return_tensors="pt", max_length=1024, truncation=True) # Perpanjang input maks

                # --- PARAMETER GENERASI YANG LEBIH STABIL ---
                summary_ids = model.generate(
                    inputs.input_ids,
                    max_length=60,  # Target token (sekitar 150-180 karakter)
                    min_length=15,
                    num_beams=5,    # Nilai standar untuk beam search
                    early_stopping=True
                )
                
                output_text = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
                
                # Simpan hasil ke session state untuk ditampilkan
                st.session_state.deskripsi_seo = output_text
                st.session_state.judul_pratinjau = judul_artikel
        else:
            st.warning("Judul dan Isi Konten tidak boleh kosong.", icon="⚠️")

    # Tampilkan hasil dari session_state
    st.write(st.session_state.deskripsi_seo)
    st.caption(f"Jumlah Karakter: {len(st.session_state.deskripsi_seo)}")

    st.markdown("---")

    st.subheader("Pratinjau SEO")
    st.markdown(f"""
    <div style="border: 1px solid #333; border-radius: 8px; padding: 15px; background-color: #262730;">
        <h5 style="color: #8ab4f8; margin: 0; font-weight: normal;">{st.session_state.judul_pratinjau}</h5>
        <p style="color: #bdc1c6; font-size: 14px; margin-top: 5px;">
            {st.session_state.deskripsi_seo if len(st.session_state.deskripsi_seo) > 0 and st.session_state.deskripsi_seo != 'Deskripsi meta Anda akan muncul di sini...' else 'Di sinilah deskripsi meta Anda akan muncul...'}
        </p>
    </div>
    """, unsafe_allow_html=True)
