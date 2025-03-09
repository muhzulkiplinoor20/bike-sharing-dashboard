
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset cleaned
day_df = pd.read_csv("cleaned_day.csv")
hour_df = pd.read_csv("cleaned_hour.csv")

# Streamlit Dashboard
st.title("🚲 Bike Sharing Dashboard")
st.write("Analisis data penyewaan sepeda berdasarkan musim, hari kerja, dan kondisi cuaca.")

# Statistik dasar
st.header("📊 Statistik Data")
st.write(day_df.describe())

# Visualisasi jumlah penyewaan berdasarkan musim
st.header("🌦️ Penyewaan Sepeda Berdasarkan Musim")
fig, ax = plt.subplots()
sns.barplot(x='season', y='cnt', data=day_df, palette='viridis', ax=ax)
ax.set_xlabel('Musim')
ax.set_ylabel('Total Penyewaan')
ax.set_xticklabels(['Spring', 'Summer', 'Fall', 'Winter'])
st.pyplot(fig)

# Visualisasi perbandingan penyewaan hari kerja vs akhir pekan
st.header("📅 Penyewaan Sepeda: Hari Kerja vs Akhir Pekan")
fig, ax = plt.subplots()
sns.barplot(x='workingday', y='cnt', data=day_df, palette='coolwarm', ax=ax)
ax.set_xlabel('Hari Kerja (1 = Ya, 0 = Tidak)')
ax.set_ylabel('Total Penyewaan')
ax.set_xticklabels(['Akhir Pekan/Hari Libur', 'Hari Kerja'])
st.pyplot(fig)

# Analisis pengaruh cuaca terhadap penyewaan sepeda
st.header("☁️ Pengaruh Cuaca terhadap Penyewaan Sepeda")
fig, ax = plt.subplots()
sns.barplot(x='weathersit', y='cnt', data=day_df, palette='magma', ax=ax)
ax.set_xlabel('Kondisi Cuaca')
ax.set_ylabel('Total Penyewaan')
ax.set_xticklabels(['Cerah', 'Berkabut', 'Hujan Ringan', 'Hujan Lebat'])
st.pyplot(fig)

# Kesimpulan
st.header("📝 Kesimpulan")
st.write("1. Penyewaan sepeda lebih tinggi pada musim panas dan gugur.")
st.write("2. Hari kerja memiliki jumlah penyewaan lebih tinggi dibandingkan akhir pekan, menunjukkan sepeda banyak digunakan untuk keperluan komuter.")
st.write("3. Cuaca yang buruk (hujan lebat/salju) mengurangi jumlah penyewaan secara signifikan.")
