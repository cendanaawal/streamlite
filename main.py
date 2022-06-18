import streamlit as st

st.write("""
# Aplikasi Luas Segi Tiga
Ini aplikasi menggunakan streamli """)

a = st.number_input("Masukkan luas alas a: ", 0)
t = st.number_input("Masukkan masukkan tinggi : ", 0)
hitung = st.button("Hitung")

if hitung:
    luas = a*t/2
    st.success(f"Luas segitiga adalah :  {luas}")
    st.balloons()
