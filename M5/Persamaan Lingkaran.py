import numpy as np  # Mengimpor pustaka numpy untuk perhitungan numerik
import matplotlib.pyplot as plt  # Mengimpor pustaka matplotlib untuk plotting grafik

# Parameter lingkaran
jari_jari = 4  # Menentukan jari-jari lingkaran
pusat_x, pusat_y = 12, 4  # Koordinat pusat lingkaran

# Menghitung titik-titik lingkaran
theta = np.linspace(0, 2 * np.pi, 100)  # Membuat array sudut dari 0 hingga 2π
x = pusat_x + jari_jari * np.cos(theta)  # Menghitung koordinat x titik lingkaran
y = pusat_y + jari_jari * np.sin(theta)  # Menghitung koordinat y titik lingkaran

# Plot lingkaran
plt.figure(figsize=(6, 6))  # Mengatur ukuran figure
plt.plot(x, y, label=f'Lingkaran dengan jari-jari {jari_jari}')  # Menggambar lingkaran
plt.scatter(pusat_x, pusat_y, color='red', label='Pusat Lingkaran')  # Menandai pusat lingkaran
plt.axhline(0, color='grey', lw=0.5)  # Menambahkan garis horizontal di y=0
plt.axvline(0, color='grey', lw=0.5)  # Menambahkan garis vertikal di x=0

# Memberi label
plt.xlabel("X")  # Menambahkan label sumbu x
plt.ylabel("Y")  # Menambahkan label sumbu y
plt.title("Persamaan Lingkaran")  # Menambahkan judul grafik
plt.legend()  # Menampilkan legenda
plt.grid(True)  # Menampilkan grid
plt.axis("equal")  # Mengatur skala sumbu agar sama
plt.show()  # Menampilkan grafik
