import streamlit as st
import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration
import re

# --- KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="Peringkas Meta SEO",
    page_icon="✍️",
    layout="wide"
)

# --- FUNGSI PEMBANTU & KOMPONEN UTAMA ---
@st.cache_resource
def load_components():
    """Memuat model dan tokenizer dari Hugging Face Hub."""
    repo_id = "Irvan14/t5-small-indonesian-summarization"
    try:
        tokenizer = T5Tokenizer.from_pretrained(repo_id)
        model = T5ForConditionalGeneration.from_pretrained(repo_id)
        return tokenizer, model
    except Exception as e:
        st.error(f"Gagal memuat komponen dari Hub. Kesalahan: {e}")
        return None, None

def smart_truncate(text, target_length=155):
    """Memotong teks secara cerdas di akhir kalimat terakhir sebelum target_length."""
    if len(text) <= target_length:
        return text
    
    truncated_text = text[:target_length]
    last_period_index = truncated_text.rfind('.')
    
    if last_period_index != -1:
        return truncated_text[:last_period_index + 1]
    else:
        last_space_index = truncated_text.rfind(' ')
        if last_space_index != -1:
            return truncated_text[:last_space_index] + "."
        else:
            return truncated_text

# --- Memuat Komponen ---
tokenizer, model = load_components()

# --- Inisialisasi State ---
if 'summary_result' not in st.session_state:
    st.session_state.summary_result = ""

# --- ANTARMUKA PENGGUNA ---
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
    st.caption(f"{char_count} karakter. Ideal: 130-155.")
    
    st.subheader("Pratinjau SEO")
    with st.container(border=True):
        preview_title = article_title or st.session_state.get('prev_title', 'Contoh Judul Halaman')
        st.markdown(f"<h5 style='color: #4A90E2;'>{preview_title}</h5>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #4B5563;'>{output_text_value or 'Di sinilah deskripsi meta Anda akan muncul...'}</p>", unsafe_allow_html=True)

# --- BLOK LOGIKA SETELAH TOMBOL DITEKAN ---
if submit_button and tokenizer and model:
    if not article_text or len(article_text) < 150:
        st.warning("Masukkan setidaknya 150 karakter artikel untuk hasil terbaik.")
    else:
        with st.spinner("Membuat ringkasan dengan mode kreatif..."):
            try:
                # Menggunakan prompt yang sederhana dan alami
                source_text_for_summary = f"{article_title}\n\n{article_text}"
                input_text = "ringkas: " + source_text_for_summary
                
                device = "cuda" if torch.cuda.is_available() else "cpu"
                inputs = tokenizer(input_text, return_tensors="pt", max_length=1024, truncation=True).to(device)
                model.to(device)

                # --- PERUBAHAN UTAMA: Menggunakan teknik Sampling ---
                summary_ids = model.generate(
                    inputs['input_ids'],
                    max_length=80,
                    min_length=30,
                    do_sample=True,
                    top_k=50,
                    top_p=0.95,
                    repetition_penalty=2.5,
                    num_beams=1 # Matikan beam search agar sampling bisa bekerja
                )
                
                raw_summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
                
                # Gunakan fungsi smart_truncate untuk memastikan panjangnya pas
                final_summary = smart_truncate(raw_summary)
                
                # Menyimpan hasil ke state dan memuat ulang tampilan
                st.session_state.summary_result = final_summary
                st.session_state.prev_title = article_title
                st.rerun()

            except Exception as e:
                st.error(f"Terjadi kesalahan saat proses peringkasan: {e}")
