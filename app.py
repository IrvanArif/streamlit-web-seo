import streamlit as st
import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration

# --- KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="Peringkas Meta SEO",
    page_icon="🔎",
    layout="wide"
)

# --- FUNGSI UNTUK MEMUAT MODEL & TOKENIZER ANDA ---
@st.cache_resource
def load_components():
    """
    Memuat tokenizer dan model 'Irvan14/t5-small-indonesian-summarization'
    secara manual untuk kontrol penuh.
    """
    # Menggunakan model yang Anda tentukan
    repo_id = "Irvan14/t5-small-indonesian-summarization"
    try:
        print(f"--- Memuat Tokenizer dari Hub: {repo_id}... ---")
        tokenizer = T5Tokenizer.from_pretrained(repo_id)
        
        print(f"--- Memuat Model dari Hub: {repo_id}... ---")
        model = T5ForConditionalGeneration.from_pretrained(repo_id)
        
        print("--- Komponen berhasil dimuat. ---")
        return tokenizer, model
    except Exception as e:
        st.error(f"Gagal memuat komponen dari Hub. Kesalahan: {e}")
        return None, None

# --- MEMUAT KOMPONEN SAAT APLIKASI DIMULAI ---
tokenizer, model = load_components()

# --- INISIALISASI STATE UNTUK MENYIMPAN HASIL ---
if 'summary_result' not in st.session_state:
    st.session_state.summary_result = ""

# --- ANTARMUKA PENGGUNA (UI) ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("Masukkan Teks")
    article_title = st.text_input("Judul Artikel", placeholder="Masukkan judul artikel Anda di sini...")
    article_text = st.text_area("Isi Konten Artikel", height=300, placeholder="Tempelkan isi konten artikel Anda di sini...")
    
    submit_button = st.button("Buat Deskripsi Meta", type="primary")

with col2:
    st.subheader("Deskripsi Meta SEO")
    output_text_value = st.session_state.summary_result
    
    if output_text_value:
        st.info(output_text_value)
    else:
        st.info("Deskripsi meta Anda akan muncul di sini...")
    
    char_count = len(output_text_value)
    st.caption(f"{char_count}/150 karakter. Ideal: 130-150.")
    
    st.subheader("Pratinjau SEO")
    with st.container(border=True):
        st.markdown(f"<h5>{article_title or 'Contoh Judul Halaman'}</h5>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #4B5563;'>{output_text_value or 'Di sinilah deskripsi meta Anda akan muncul...'}</p>", unsafe_allow_html=True)

# --- LOGIKA UTAMA: PENDEKATAN MANUAL & EKSPLISIT ---
if submit_button and tokenizer and model:
    if not article_text or len(article_text) < 150:
        st.warning("Masukkan setidaknya 150 karakter artikel untuk hasil terbaik.")
    else:
        with st.spinner("Sedang membuat ringkasan..."):
            try:
                # 1. Siapkan input. Kita tetap menggunakan prefiks sebagai praktik terbaik.
                input_text = "summarize: " + article_text
                
                # 2. Tokenisasi: Ubah teks menjadi angka
                device = "cuda" if torch.cuda.is_available() else "cpu"
                inputs = tokenizer(input_text, return_tensors="pt", max_length=512, truncation=True).to(device)
                model.to(device)
                
                # 3. Generate: Gunakan parameter yang memaksa model lebih kreatif
                summary_ids = model.generate(
                    inputs['input_ids'],
                    max_length=80,
                    min_length=30,
                    num_beams=5,          # Meningkatkan pencarian menjadi 5
                    repetition_penalty=2.5, # Penalti kuat untuk kata yg berulang
                    length_penalty=1.5,   # Mendorong kalimat yg lebih panjang
                    early_stopping=True,
                    no_repeat_ngram_size=2 # Mencegah pengulangan frasa 2 kata
                )
                
                # 4. Decode: Ubah angka kembali menjadi teks
                raw_summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
                
                st.session_state.summary_result = raw_summary
                st.rerun()

            except Exception as e:
                st.error(f"Terjadi kesalahan saat proses peringkasan: {e}")
