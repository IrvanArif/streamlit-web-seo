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

# --- FUNGSI UNTUK MEMUAT MODEL & TOKENIZER ---
@st.cache_resource
def load_components():
    """Memuat komponen penting dari Hugging Face Hub."""
    repo_id = "Irvan14/t5-small-indonesian-summarization"
    try:
        tokenizer = T5Tokenizer.from_pretrained(repo_id)
        model = T5ForConditionalGeneration.from_pretrained(repo_id)
        return tokenizer, model
    except Exception as e:
        st.error(f"Gagal memuat komponen dari Hub. Kesalahan: {e}")
        return None, None

# --- FUNGSI UNTUK EKSTRAKSI KATA KUNCI ---
def extract_keywords(title, text, num_keywords=4):
    """Mengekstrak kata kunci dari judul yang juga sering muncul di teks."""
    stop_words = set([
        'di', 'dan', 'atau', 'yang', 'ini', 'itu', 'ke', 'dari', 'dengan', 'seorang',
        'adalah', 'ialah', 'merupakan', 'untuk', 'pada', 'sebagai', 'sebuah', 
        'karena', 'namun', 'saat', 'setelah', 'sebelum', 'juga', 'tak', 'bisa',
        'profil', 'lengkap', 'mantan', 'member', 'perjalanan', 'karier', 'kontroversi'
    ])
    
    def preprocess(s):
        s = s.lower()
        s = re.sub(r'[^\w\s]', '', s)
        return [word for word in s.split() if word not in stop_words and len(word) > 3]

    title_words = set(preprocess(title))
    body_words = preprocess(text)
    word_freq = {word: body_words.count(word) for word in title_words}
    sorted_keywords = sorted(word_freq.items(), key=lambda item: item[1], reverse=True)
    top_keywords = [keyword for keyword, freq in sorted_keywords if freq > 0][:num_keywords]
    return top_keywords

# --- Memuat Komponen ---
tokenizer, model = load_components()

# --- Inisialisasi State untuk Menyimpan Hasil ---
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
    st.caption(f"{char_count}/150 karakter. Ideal: 130-150.")
    
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
        with st.spinner("Menganalisis kata kunci dan membuat ringkasan alami..."):
            try:
                # 1. Ekstrak kata kunci (logika Anda tetap digunakan karena sudah bagus)
                keywords = extract_keywords(article_title, article_text)
                
                # --- PERUBAHAN LOGIKA UTAMA ADA DI SINI ---
                # Alih-alih memfilter kalimat, kita gunakan keywords sebagai petunjuk/prompt
                
                if keywords:
                    # Buat prompt dengan kata kunci sebagai panduan
                    keyword_prompt = ", ".join(keywords)
                    source_text_for_summary = f"topik: {keyword_prompt}\n\n{article_text}"
                else:
                    # Jika tidak ada kata kunci, gunakan artikel lengkap
                    source_text_for_summary = article_text

                # Gunakan prefix yang benar untuk model
                input_text = "ringkas: " + source_text_for_summary
                
                device = "cuda" if torch.cuda.is_available() else "cpu"
                inputs = tokenizer(input_text, return_tensors="pt", max_length=1024, truncation=True).to(device)
                model.to(device)

                # Parameter generate tetap sama sesuai keinginan Anda
                summary_ids = model.generate(
                    inputs['input_ids'],
                    max_length=22,          # TIDAK DIUBAH, sesuai permintaan Anda
                    min_length=20,
                    num_beams=5,
                    repetition_penalty=2.5,
                    length_penalty=1.2,
                    early_stopping=True,
                    no_repeat_ngram_size=2
                )
                
                final_summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
                
                # Menyimpan hasil ke state dan memuat ulang tampilan
                st.session_state.summary_result = final_summary
                st.session_state.prev_title = article_title # Simpan judul untuk pratinjau
                st.rerun()

            except Exception as e:
                st.error(f"Terjadi kesalahan saat proses peringkasan: {e}")
