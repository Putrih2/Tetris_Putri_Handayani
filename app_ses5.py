import streamlit as st

st.set_page_config(
    page_title = 'Belajar Streamlit'
    ,layout='wide'
)

# Menulis teks
st.title("5 Negara Paling Bahagia di Dunia Tahun 2024. Ada Hubungannya dengan Populasi Penduduk?")
st.text("By: Putri Handayani")

custom_container = st.container(border=True)
with custom_container:st.write("Negara-negara di seluruh dunia memiliki tingkat kebahagiaan yang berbeda-beda, dan setiap tahun, sebuah indeks global diterbitkan untuk menentukan negara-negara yang paling bahagia. Berdasarkan World Happiness Report 2024, negara-negara di Skandinavia, seperti Finlandia, Denmark, dan Iceland sering kali menduduki peringkat teratas sebagai negara paling bahagia di dunia. Berikut 5 negara yang menduduki tingkat teratas sebagai negara paling bahagia di dunia.")

st.write("5 Negara Paling Bahagia di Dunia")

import pandas as pd

df = pd.DataFrame({
"Negara": ["1. Finland","2. Denmark","3. Iceland","4. Switzerland","5. Netherlands"],
"Tingkat Kebahagiaan": [7.821,7.636,7.557,7.512,7.415]
})

df_sorted = df.sort_values(by='Tingkat Kebahagiaan', ascending=False)

st.bar_chart(data=df, x="Negara", y="Tingkat Kebahagiaan")

custom_container = st.container(border=True)

with custom_container:st.write("Pada dasarnya, kebahagiaan adalah hasil dari pembangunan manusia yang holistik, mencakup aspek-aspek seperti umur panjang dan sehat, pengetahuan, dan standar hidup yang layak. Indeks Kebahagiaan Dunia sering kali mencerminkan pencapaian-pencapaian ini dalam negara-negara di seluruh dunia. Berdasarkan Indeks Pembangunan Manusia (IPM) PBB, beberapa negara telah berhasil mencapai tingkat kebahagiaan yang tinggi berkat pencapaian rata-rata dalam tiga dimensi dasar pembangunan manusia.")

with custom_container:st.write("1. Umur Panjang dan Sehat")

with custom_container:st.write("Negara-negara dengan tingkat kebahagiaan tinggi sering kali memiliki harapan hidup yang tinggi dan sistem kesehatan yang efisien. Mereka menginvestasikan dalam layanan kesehatan universal dan promosi kesehatan masyarakat untuk memastikan bahwa penduduk mereka hidup lebih lama dan lebih sehat.")

with custom_container:st.write("2. Pengetahuan")

with custom_container:st.write("Pendidikan adalah kunci untuk mencapai kebahagiaan yang berkelanjutan. Negara-negara yang paling bahagia cenderung memiliki tingkat pendidikan yang tinggi dan akses yang mudah ke pengetahuan. Mereka menginvestasikan dalam pendidikan yang berkualitas untuk semua warga agar memiliki pengetahuan dan keterampilan yang diperlukan untuk mencapai potensi penuh mereka.")

with custom_container:st.write("3. Standar Hidup yang Layak")

with custom_container:st.write("Standar hidup yang layak mencakup akses terhadap kebutuhan dasar seperti makanan, air bersih, perumahan yang layak, dan pekerjaan yang layak. Negara-negara yang paling bahagia sering kali memiliki tingkat kemiskinan yang rendah dan tingkat pengangguran yang rendah, serta sistem perlindungan sosial yang kuat untuk melindungi warganya dari ketidakpastian ekonomi.")

st.write("Lalu Apakah Populasi Mempengaruhi Tingkat Kebahagiaan Negara?")

df = pd.DataFrame({
"Benua": ["Africa","Asia","Europe","North America","Oceania","South America"],
"Populasi Penduduk (Milyar)": [1.28,4.60,0.75,0.60,0.030,0.41]
})

st.bar_chart(data=df, x="Benua", y="Populasi Penduduk (Milyar)")

custom_container = st.container(border=True)

with custom_container:st.write("Data di atas menunjukkan populasi penduduk di setiap benua. Urutan populasi dari yang tertinggi hingga terendah adalah Benua Asia, Afrika, Eropa, Amerika Utara, Amerika Selatan, dan Ocania. Benua Asia menempati peringkat 1 sebagai benua dengan populasi terbanyak di dunia dan posisi terakhir ditempati oleh Benua Oceania. Dengan melihat data bahwa 5 negara paling bahagia di dunia semuanya berada di Benua Eropa. Sedangkan Benua Eropa bukan merupakan benua dengan populasi terbanyak atau tersedikit di dunia, maka dapat dibuktikan bahwa populasi penduduk tidak berhubungan dengan tingkat kebahagiaan suatu negara")

st.text("Sumber: World Happiness Report 2024")

# Selesai, tekan control+C pada terminal untuk mengakhiri app
# Lalu exit untuk turn off virtual environment
