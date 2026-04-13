import streamlit as st

st.set_page_config(page_title="Teori Darwin", layout="wide")

st.title("🧬 Teori Evolusi Charles Darwin")

menu = st.sidebar.radio(
    "📚 Menu:",
    ["Beranda", "Teori", "Seleksi Alam", "Pertentangan", "Kuis"]
)

if menu == "Beranda":
    st.write("Selamat datang di website teori Darwin!")

elif menu == "Teori":
    st.write("Makhluk hidup berevolusi melalui seleksi alam.")

elif menu == "Seleksi Alam":
    pilihan = st.selectbox("Pilih kondisi:", ["Dingin", "Panas"])
    
    if pilihan == "Dingin":
        st.success("Makhluk berbulu tebal bertahan")
    else:
        st.success("Makhluk berbulu tipis bertahan")

elif menu == "Pertentangan":
    st.write("Teori Darwin sempat ditentang karena bertentangan dengan kepercayaan.")

elif menu == "Kuis":
    jawaban = st.radio(
        "Apa inti seleksi alam?",
        ["Acak", "Yang kuat", "Yang beradaptasi"]
    )

    if st.button("Cek"):
        if jawaban == "Yang beradaptasi":
            st.success("Benar!")
        else:
            st.error("Salah!")
