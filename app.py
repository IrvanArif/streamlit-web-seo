import streamlit as st
import torch
from transformers import pipeline

#KONFIGURASI HALAMAN
st.set_page_config(
    page_title="Peringkas Meta SEO",
    page_icon="🔎",
    layout="wide"
)

#MEMUAT MODEL
@st.cache_resource
def load_summarizer():
    """
    Memuat pipeline summarization dari Hugging Face Hub.
    Fungsi ini akan di-cache, jadi model hanya diunduh sekali.
    """
    repo_id = "Irvan14/t5-small-indonesian-summarization" 
    
    print(f"--- Mengunduh dan memuat model dari Hub: {repo_id}... ---")
    try:
        device = 0 if torch.cuda.is_available() else -1
        summarizer = pipeline(
            "summarization",
            model=repo_id,
            tokenizer=repo_id,
            device=device
        )
        print(f"--- Model berhasil dimuat di device: {'GPU' if device == 0 else 'CPU'} ---")
        return summarizer
    except Exception as e:
        st.error(f"Gagal memuat model dari Hub. Error: {e}")
        return None

#untuk memuat model
summarizer = load_summarizer()

# Inisialisasi State di Awal
if 'summary_result' not in st.session_state:
    st.session_state.summary_result = ""

#TAMPILAN
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

#LOGIKAnya
if submit_button and summarizer:
    if not article_text or len(article_text) < 200:
        st.warning("Silakan masukkan setidaknya 200 karakter artikel untuk hasil terbaik.")
    else:
        with st.spinner("Sedang membuat ringkasan..."):
            try:
                context_to_summarize = article_text[:2000]
                prompt_text = f"Berdasarkan teks berikut, apakah inti sari utamanya yang dapat diringkas menjadi satu paragraf singkat untuk meta deskripsi SEO? Teks: {context_to_summarize}"

                result = summarizer(
                    prompt_text,
                    max_new_tokens=60,
                    min_new_tokens=25,
                    do_sample=False
                )
                raw_summary = result[0]['summary_text']

                target_length = 150
                final_text = raw_summary
                if len(raw_summary) > target_length:
                    truncated_summary = raw_summary[:target_length]
                    last_space = truncated_summary.rfind(' ')
                    if last_space != -1:
                        final_text = truncated_summary[:last_space] + "."
                
                st.session_state.summary_result = final_text
                st.rerun()

            except Exception as e:
                st.error(f"Terjadi kesalahan saat proses peringkasan: {e}")
