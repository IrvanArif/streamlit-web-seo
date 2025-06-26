import streamlit as st
import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration
import re

# --- KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="Peringkas Meta SEO",
    page_icon="🔎",
    layout="wide"
)

# --- FUNGSI UNTUK MEMUAT MODEL & TOKENIZER ---
@st.cache_resource
def load_components():
    repo_id = "Irvan14/t5-small-indonesian-summarization"
    try:
        tokenizer = T5Tokenizer.from_pretrained(repo_id)
        model = T5ForConditionalGeneration.from_pretrained(repo_id)
        return tokenizer, model
    except Exception as e:
        st.error(f"Gagal memuat komponen dari Hub. Kesalahan: {e}")
        return None, None

# --- FUNGSI EKSTRAKSI KATA KUNCI (TETAP DIGUNAKAN) ---
def extract_keywords(title, text, num_keywords=4):
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

# --- MEMUAT KOMPONEN ---
tokenizer, model = load_components()

# --- INISIALISASI STATE ---
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

    # Bagian 'Saran Kata Kunci' telah dihapus dari sini

    st.subheader("Pratinjau SEO")
    with st.container(border=True):
        st.markdown(f"<h5>{article_title or 'Contoh Judul Halaman'}</h5>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #4B5563;'>{output_text_value or 'Di sinilah deskripsi meta Anda akan muncul...'}</p>", unsafe_allow_html=True)

# --- LOGIKA UTAMA DENGAN INJEKSI KATA KUNCI ---
if submit_button and tokenizer and model:
    if not article_text or len(article_text) < 150:
        st.warning("Masukkan setidaknya 150 karakter artikel untuk hasil terbaik.")
    else:
        with st.spinner("Membuat ringkasan dan menyisipkan kata kunci..."):
            try:
                # --- Langkah 1: Buat ringkasan seperti biasa ---
                input_text = "summarize: " + article_text
                device = "cuda" if torch.cuda.is_available() else "cpu"
                inputs = tokenizer(input_text, return_tensors="pt", max_length=512, truncation=True).to(device)
                model.to(device)
                summary_ids = model.generate(
                    inputs['input_ids'], max_length=60, min_length=25, num_beams=5,
                    repetition_penalty=2.5, length_penalty=1.5, early_stopping=True, no_repeat_ngram_size=2
                )
                raw_summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
                
                # --- Langkah 2: Ekstrak kata kunci ---
                keywords = extract_keywords(article_title, article_text)
                
                # --- Langkah 3: Gabungkan (Inject) kata kunci ke awal ringkasan ---
                processed_summary = raw_summary
                if keywords:
                    keyword_prefix = ", ".join(keywords).capitalize()
                    processed_summary = f"{keyword_prefix}. {raw_summary}"

                # --- Langkah 4: Potong hasil gabungan agar sesuai batas karakter ---
                target_length = 150
                final_text = processed_summary
                if len(final_text) > target_length:
                    truncated_text = final_text[:target_length]
                    last_space_index = truncated_text.rfind(' ')
                    if last_space_index != -1:
                        final_text = truncated_text[:last_space_index] + "..."
                    else:
                        final_text = truncated_text + "..."
                
                st.session_state.summary_result = final_text
                st.rerun()

            except Exception as e:
                st.error(f"Terjadi kesalahan saat proses peringkasan: {e}")
