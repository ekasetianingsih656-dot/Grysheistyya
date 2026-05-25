import streamlt                      as st

#Mengatur judul tab browser
st.set_page_config(page_title="aplikasi pertamaku", page_icon="+")

# Menampilkan judul dan teks web
st.title("aplikasi streamlit pertamali!")
st.write("halo dunial jika kamu bisa melihat halaman ini, berarti kamu sudah *BERHASIL* meng upload dan mendeploy aplikasi streamlit dari Github.")

st.divider () # Garlis pembatas

#Input sederhana
nama = st.text_input("Siapa namau?")

# Tombol interaktif
if st.button("Klik saya!"):
    if nama :
        st.success(f"Halo, {nama}! Selamat belajar streamlt. Kamu hebat!")
        st.balloons() #Memunculkan animasi balon
    else:
        st.warning("isi namamu dulu di kotak atas ya!")