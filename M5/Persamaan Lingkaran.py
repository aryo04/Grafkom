import numpy as np  # Mengimpor pustaka numpy untuk perhitungan numerik
import matplotlib.pyplot as plt  # Mengimpor pustaka matplotlib untuk plotting grafik

# Parameter lingkaran
jari_jari = 4  # Menentukan jari-jari lingkaran
a, b = 12, 4  # Koordinat pusat lingkaran

# Menghitung titik-titik lingkaran
theta = np.linspace(0, 2 * np.pi, 100)  # Membuat array sudut dari 0 hingga 2π
x = a + jari_jari * np.cos(theta)  # Menghitung koordinat x titik lingkaran
y = b + jari_jari * np.sin(theta)  # Menghitung koordinat y titik lingkaran

# Plot lingkaran
plt.figure(figsize=(6, 6))  # Mengatur ukuran figure
plt.plot(x, y, label=f'Lingkaran dengan jari-jari {jari_jari}')  # Menggambar lingkaran
plt.scatter(a, b, color='red', label='Pusat Lingkaran')  # Menandai pusat lingkaran
plt.axhline(0, color='grey', lw=0.5)  # Menambahkan garis horizontal di y=0
plt.axvline(0, color='grey', lw=0.5)  # Menambahkan garis vertikal di x=0

# Memberi label
plt.xlabel("X")  # Menambahkan label sumbu x
plt.ylabel("Y")  # Menambahkan label sumbu y
plt.title("Persamaan Lingkaran")  # Menambahkan judul grafik

# Menambahkan rumus lingkaran di tengah grafik
equation = f"(x - {a})² + (y - {b})² = {jari_jari**2}"  # Rumus lingkaran
plt.text(a - 4, b, equation, fontsize=12, color='blue', ha='center')  # Posisi teks disesuaikan

plt.legend()  # Menampilkan legenda
plt.grid(True)  # Menampilkan grid
plt.axis("equal")  # Mengatur skala sumbu agar sama
plt.show()  # Menampilkan grafik
