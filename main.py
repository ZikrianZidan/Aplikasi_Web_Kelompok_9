import streamlit as st

st.title('Aplikasi Perhitungan Kuat Tekan')

import streamlit as st

st.subheader('Perhitungan Luas Sampel')

Panjang = st.number_input('Masukkan Panjang Sampel (cm)')
Lebar = st.number_input('Masukkan Lebar Sampel (cm')

tombol = st.button('Hitung Luas Sampel')


if tombol:
    luas_sampel = (Panjang*Lebar)/10000
    st.success(f'Nilai Luas Sampel (m^2) adalah {luas_sampel}')


import streamlit as st

st.subheader('Perhitungan Gaya Tekan')

massa = st.number_input('Masukkan Massa Tekan (Kg)')
gravitasi = st.number_input('Masukkan Percepatan Gravitasi (m^2)')

tombol = st.button('Hitung Gaya Tekan')

if tombol:
    gaya_tekan = massa*gravitasi
    st.success(f'Nilai Gaya Tekan (N) adalah {gaya_tekan}')

import streamlit as st

st.subheader('Perhitungan Kuat Tekan')

gaya_tekan = st.number_input('Masukkan Gaya Tekan (N)')
luas_sampel = st.number_input('Masukkan Luas Sampel (m^2)')

tombol = st.button('Hitung Kuat Tekan')

if tombol:
    kuat_tekan = gaya_tekan/luas_sampel
    st.success(f'Nilai Kuat Tekan (N/m^2) adalah {kuat_tekan}')
