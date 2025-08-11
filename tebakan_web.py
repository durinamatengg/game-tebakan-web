import streamlit as st

st.title("🎯 Tebak Angka Rahasia!")
st.write("Aku punya angka rahasia antara 1 - 10. Coba tebak!")

# Simpan angka rahasia di session_state biar tidak reset tiap submit
if "angka_rahasia" not in st.session_state:
    import random
    st.session_state.angka_rahasia = random.randint(1, 10)
    st.session_state.selesai = False

# Input tebakan dari user
tebakan = st.number_input("Masukkan tebakanmu:", min_value=1, max_value=10, step=1)

if st.button("Tebak!"):
    if tebakan == st.session_state.angka_rahasia:
        st.success("🎉 Benar! Kamu menebak dengan tepat!")
        st.session_state.selesai = True
    elif tebakan < st.session_state.angka_rahasia:
        st.warning("📉 Angkanya lebih besar!")
    else:
        st.warning("📈 Angkanya lebih kecil!")

if st.session_state.selesai:
    if st.button("Main Lagi"):
        st.session_state.angka_rahasia = random.randint(1, 10)
        st.session_state.selesai = False
