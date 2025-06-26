import streamlit as st
import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration
import re # Diperlukan untuk membersihkan teks dari tanda baca

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

# --- FUNGSI BARU: EKSTRAKSI KATA KUNCI ---
def extract_keywords(title, text, num_keywords=4):
    """Mengekstrak kata kunci dari judul berdasarkan frekuensinya di dalam teks."""
    # Daftar singkat kata umum (stop words) Bahasa Indonesia untuk diabaikan
    stop_words = set([
        'di', 'dan', 'atau', 'yang', 'ini', 'itu', 'ke', 'dari', 'dengan', 'seorang',
        'adalah', 'ialah', 'merupakan', 'untuk', 'pada', 'sebagai', 'sebuah', 
        'karena', 'namun', 'saat', 'setelah', 'sebelum', 'juga', 'tak', 'bisa',
        'profil', 'lengkap', 'mantan', 'member', 'perjalanan', 'karier', 'kontroversi'
    ])

    # Fungsi untuk membersihkan dan memecah teks menjadi kata
    def preprocess(s):
        s = s.lower()
        s = re.sub(r'[^\w\s]', '', s) # Menghapus tanda baca
        return [word for word in s.split() if word not in stop_words and len(word) > 3]

    # Proses judul untuk mendapatkan kandidat kata kunci
    title_words = set(preprocess(title))
    # Proses isi artikel
    body_words = preprocess(text)

    # Hitung frekuensi setiap kata kunci dari judul di dalam isi artikel
    word_freq = {word: body_words.count(word) for word in title_words}

    # Urutkan kata kunci berdasarkan frekuensi (dari tertinggi ke terendah)
    sorted_keywords = sorted(word_freq.items(), key=lambda item: item[1], reverse=True)

    # Ambil 'num_keywords' teratas
    top_keywords = [keyword for keyword, freq in sorted_keywords if freq > 0][:num_keywords]
    
    return top_keywords

# --- MEMUAT KOMPONEN ---
tokenizer, model = load_components()

# --- INISIALISASI STATE ---
if 'summary_result' not in st.session_state:
    st.session_state.summary_result = ""
if 'suggested_keywords' not in st.session_state:
    st.session_state.suggested_keywords = []

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

    # TAMPILAN BARU: UNTUK KATA KUNCI
    st.subheader("Saran Kata Kunci")
    if st.session_state.suggested_keywords:
        keywords_html = " ".join([f"<span style='background-color: #e0e0e0; color: #333; padding: 4px 8px; border-radius: 12px; margin-right: 5px;'>{kw}</span>" for kw in st.session_state.suggested_keywords])
        st.markdown(keywords_html, unsafe_allow_html=True)
    else:
        st.caption("Kata kunci yang relevan akan muncul di sini...")

    st.subheader("Pratinjau SEO")
    with st.container(border=True):
        st.markdown(f"<h5>{article_title or 'Contoh Judul Halaman'}</h5>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #4B5563;'>{output_text_value or 'Di sinilah deskripsi meta Anda akan muncul...'}</p>", unsafe_allow_html=True)

# --- LOGIKA UTAMA ---
if submit_button and tokenizer and model:
    if not article_text or len(article_text) < 150:
        st.warning("Masukkan setidaknya 150 karakter artikel untuk hasil terbaik.")
    else:
        with st.spinner("Membuat ringkasan dan mengekstrak kata kunci..."):
            try:
                # --- PROSES RINGKASAN (TETAP SAMA) ---
                input_text = "summarize: " + article_text
                device = "cuda" if torch.cuda.is_available() else "cpu"
                inputs = tokenizer(input_text, return_tensors="pt", max_length=512, truncation=True).to(device)
                model.to(device)
                summary_ids = model.generate(
                    inputs['input_ids'], max_length=60, min_length=25, num_beams=5,
                    repetition_penalty=2.5, length_penalty=1.5, early_stopping=True, no_repeat_ngram_size=2
                )
                raw_summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
                
                target_length = 150
                final_text = raw_summary
                if len(final_text) > target_length:
                    truncated_text = final_text[:target_length]
                    last_space_index = truncated_text.rfind(' ')
                    if last_space_index != -1:
                        final_text = truncated_text[:last_space_index] + "..."
                    else:
                        final_text = truncated_text + "..."
                st.session_state.summary_result = final_text
                
                # --- INTEGRASI FITUR BARU: PANGGIL FUNGSI EKSTRAKSI ---
                keywords = extract_keywords(article_title, article_text)
                st.session_state.suggested_keywords = keywords
                
                st.rerun()

            except Exception as e:
                st.error(f"Terjadi kesalahan saat proses peringkasan: {e}")
