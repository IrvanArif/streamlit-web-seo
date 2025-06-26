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

# --- LOGIKA UTAMA: GABUNGAN SEMUA PERBAIKAN ---
if submit_button and tokenizer and model:
    if not article_text or len(article_text) < 150:
        st.warning("Masukkan setidaknya 150 karakter artikel untuk hasil terbaik.")
    else:
        with st.spinner("Sedang membuat ringkasan..."):
            try:
                # 1. Siapkan input dengan prefix
                input_text = "summarize: " + article_text
                
                # 2. Tokenisasi
                device = "cuda" if torch.cuda.is_available() else "cpu"
                inputs = tokenizer(input_text, return_tensors="pt", max_length=512, truncation=True).to(device)
                model.to(device)
                
                # 3. Generate dengan parameter yang terbukti menghasilkan ringkasan bagus
                summary_ids = model.generate(
                    inputs['input_ids'],
                    max_length=40,
                    min_length=20,
                    num_beams=5,
                    repetition_penalty=2.5,
                    length_penalty=1.5,
                    early_stopping=True,
                    no_repeat_ngram_size=2
                )
                
                # 4. Decode
                raw_summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
                
                # 5. Logika pemotongan karakter yang sudah final dan teruji
                target_length = 150
                final_text = raw_summary

                if len(final_text) > target_length:
                    truncated_text = final_text[:target_length]
                    last_space_index = truncated_text.rfind(' ')
                    
                    if last_space_index != -1:
                        final_text = truncated_text[:last_space_index] + "..."
                    else:
                        final_text = truncated_text + "..."

                # 6. Simpan hasil ke state dan refresh
                st.session_state.summary_result = final_text
                st.rerun()

            except Exception as e:
                st.error(f"Terjadi kesalahan saat proses peringkasan: {e}")
