import numpy as np
import matplotlib.pyplot as plt

# Parameter lingkaran
jari_jari = 4
pusat_x, pusat_y = 12, 4  # Koordinat pusat lingkaran

# Menghitung titik-titik lingkaran
theta = np.linspace(0, 2 * np.pi, 100)
x = pusat_x + jari_jari * np.cos(theta)
y = pusat_y + jari_jari * np.sin(theta)

# Plot lingkaran
plt.figure(figsize=(6, 6))
plt.plot(x, y, label=f'Lingkaran dengan jari-jari {jari_jari}')
plt.scatter(pusat_x, pusat_y, color='red', label='Pusat Lingkaran')
plt.axhline(0, color='grey', lw=0.5)
plt.axvline(0, color='grey', lw=0.5)

# Memberi label
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Persamaan Lingkaran")
plt.legend()
plt.grid(True)
plt.axis("equal")
plt.show()
