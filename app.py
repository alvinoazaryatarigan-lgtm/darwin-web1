import streamlit as st

st.set_page_config(page_title="Teori Darwin", layout="wide")

st.title("🧬 Teori Evolusi Charles Darwin")
st.subheader("Website Pembelajaran Interaktif")

menu = st.sidebar.radio(
    "📚 Pilih Menu:",
    ["Beranda", "Biografi Darwin", "Teori Evolusi", "Seleksi Alam", "Bukti Evolusi", "Pertentangan", "Kuis"]
)

# ================= BERANDA =================
if menu == "Beranda":
    st.image("https://upload.wikimedia.org/wikipedia/commons/3/3e/Charles_Darwin_by_Julia_Margaret_Cameron_2.jpg", width=250)

    st.write("""
    Selamat datang di website pembelajaran tentang **Teori Evolusi Charles Darwin**.
    
    🔍 Kamu akan belajar:
    - Biografi Darwin
    - Teori evolusi
    - Seleksi alam
    - Bukti evolusi
    - Pertentangan teori
    """)

# ================= BIOGRAFI =================
elif menu == "Biografi Darwin":
    st.header("👨‍🔬 Biografi Charles Darwin")

    st.image("https://upload.wikimedia.org/wikipedia/commons/3/3e/Charles_Darwin_by_Julia_Margaret_Cameron_2.jpg", width=250)

    st.write("""
    Charles Darwin adalah ilmuwan asal Inggris (1809–1882).
    
    Ia mengembangkan teori evolusi melalui seleksi alam setelah melakukan perjalanan panjang.
    """)

    st.image("https://upload.wikimedia.org/wikipedia/commons/6/6b/HMS_Beagle_by_Conrad_Martens.jpg")

# ================= TEORI =================
elif menu == "Teori Evolusi":
    st.header("📖 Teori Evolusi")

    st.image("https://upload.wikimedia.org/wikipedia/commons/9/9a/Evolution_diagram.png")

    st.write("""
    Teori evolusi menjelaskan bahwa makhluk hidup berubah dari waktu ke waktu.
    
    🌱 Intinya:
    - Semua makhluk hidup punya nenek moyang yang sama
    - Perubahan terjadi secara bertahap
    - Lingkungan mempengaruhi evolusi
    """)

# ================= SELEKSI ALAM =================
elif menu == "Seleksi Alam":
    st.header("🌿 Seleksi Alam")

    st.image("https://upload.wikimedia.org/wikipedia/commons/1/1e/Natural_selection.svg")

    st.write("""
    Seleksi alam adalah proses dimana makhluk hidup yang paling mampu beradaptasi akan bertahan hidup.
    """)

    pilihan = st.selectbox(
        "Pilih kondisi lingkungan:",
        ["Lingkungan dingin", "Lingkungan panas", "Banyak predator"]
    )

    if pilihan == "Lingkungan dingin":
        st.success("Makhluk berbulu tebal bertahan ❄️")
    elif pilihan == "Lingkungan panas":
        st.success("Makhluk berbulu tipis bertahan ☀️")
    else:
        st.success("Makhluk cepat atau kamuflase bertahan 🐆")

# ================= BUKTI =================
elif menu == "Bukti Evolusi":
    st.header("🔬 Bukti Evolusi")

    st.image("https://upload.wikimedia.org/wikipedia/commons/3/3c/Fossil_examples.jpg")

    st.write("""
    Bukti evolusi meliputi:
    """)

    st.markdown("""
    - **Fosil**
    - **Struktur tubuh (anatomi)**
    - **Embrio**
    - **DNA**
    """)

    st.image("https://upload.wikimedia.org/wikipedia/commons/5/5b/Darwin%27s_finches.jpeg")

# ================= PERTENTANGAN =================
elif menu == "Pertentangan":
    st.header("⚖️ Pertentangan")

    st.image("https://upload.wikimedia.org/wikipedia/commons/0/0c/Darwin_vs_creationism.png")

    st.write("""
    Teori Darwin sempat ditentang karena:
    """)

    st.error("""
    - Bertentangan dengan agama
    - Bukti awal kurang
    - Kontroversi asal manusia
    """)

# ================= KUIS =================
elif menu == "Kuis":
    st.header("🧠 Kuis")

    st.image("https://upload.wikimedia.org/wikipedia/commons/3/3f/Quiz_time.png", width=200)

    soal1 = st.radio(
        "Apa inti seleksi alam?",
        [
            "Acak",
            "Yang kuat",
            "Yang beradaptasi"
        ]
    )

    soal2 = st.radio(
        "Siapa pencetus teori evolusi?",
        [
            "Newton",
            "Darwin",
            "Einstein"
        ]
    )

    if st.button("Cek Jawaban"):
        skor = 0

        if soal1 == "Yang beradaptasi":
            skor += 1
        if soal2 == "Darwin":
            skor += 1

        st.success(f"Skor kamu: {skor}/2")

# Footer
st.sidebar.markdown("---")
st.sidebar.write("Dibuat dengan ❤️ menggunakan Streamlit")
