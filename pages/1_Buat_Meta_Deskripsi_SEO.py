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
    try:
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
        return tokenizer, model
    except Exception as e:
        st.error(f"Gagal memuat model. Error: {e}")
        return None, None

# Panggil fungsi untuk memuat model
tokenizer, model = load_model()

# --- FUNGSI LOGIKA UNTUK GENERASI TEKS ---
def run_generation():
    """Fungsi yang dijalankan saat tombol 'on_click' ditekan."""
    judul = st.session_state.judul_artikel_input
    konten = st.session_state.isi_konten_input
    
    if konten and judul:
        with st.spinner("AI sedang membuat ringkasan..."):
            input_text = f"Judul: {judul}\n\n{konten}"
            prefixed_text = "ringkas: " + input_text
            inputs = tokenizer(prefixed_text, return_tensors="pt", max_length=1024, truncation=True)

            summary_ids = model.generate(
                inputs.input_ids,
                max_length=60,
                min_length=15,
                num_beams=5,
                early_stopping=True
            )
            
            output_text = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
            
            # Simpan hasil ke session state
            st.session_state.deskripsi_seo_output = output_text
            st.session_state.judul_pratinjau_output = judul
    else:
        st.warning("Judul dan Isi Konten tidak boleh kosong.", icon="⚠️")

# Inisialisasi session_state jika belum ada
if 'deskripsi_seo_output' not in st.session_state:
    st.session_state.deskripsi_seo_output = "Deskripsi meta Anda akan muncul di sini..."
if 'judul_pratinjau_output' not in st.session_state:
    st.session_state.judul_pratinjau_output = "Contoh Judul Halaman"

# --- TAMPILAN APLIKASI ---
if model is not None:
    st.title("✍️ Buat Meta Deskripsi SEO")
    st.markdown("Masukkan judul dan isi konten artikel Anda di bawah ini untuk menghasilkan draf meta deskripsi secara otomatis.")

    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader("Masukkan Teks")
        st.text_input("Judul Artikel", placeholder="Tuliskan judul artikel Anda di sini...", key="judul_artikel_input")
        st.text_area("Isi Konten", placeholder="Tempelkan isi konten artikel Anda di sini...", height=300, key="isi_konten_input")
        
        # Tombol memanggil fungsi 'run_generation' saat diklik
        st.button("Buat Deskripsi Meta", type="primary", on_click=run_generation)

    with col2:
        st.subheader("Deskripsi Meta SEO")
        deskripsi = st.session_state.deskripsi_seo_output
        st.write(deskripsi)
        st.caption(f"Jumlah Karakter: {len(deskripsi)}")

        st.markdown("---")

        st.subheader("Pratinjau SEO")
        judul_pratinjau = st.session_state.judul_pratinjau_output
        st.markdown(f"""
        <div style="border: 1px solid #333; border-radius: 8px; padding: 15px; background-color: #262730;">
            <h5 style="color: #8ab4f8; margin: 0; font-weight: normal;">{judul_pratinjau}</h5>
            <p style="color: #bdc1c6; font-size: 14px; margin-top: 5px;">
                {deskripsi if len(deskripsi) > 0 and deskripsi != 'Deskripsi meta Anda akan muncul di sini...' else 'Di sinilah deskripsi meta Anda akan muncul...'}
            </p>
        </div>
        """, unsafe_allow_html=True)
else:
    st.error("Model tidak berhasil dimuat. Aplikasi tidak dapat berjalan.")
