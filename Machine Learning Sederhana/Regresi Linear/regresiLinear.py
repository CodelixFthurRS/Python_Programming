import numpy as np
import matplotlib.pyplot as plt

# Data contoh
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 3, 5, 4, 6])

# Menghitung jumlah data
n = len(x)

# Menghitung rata-rata x dan y
mean_x = np.mean(x)
mean_y = np.mean(y)

# Menghitung slope (kemiringan) dan intercept (konstanta) dari persamaan garis
slope = np.sum((x - mean_x) * (y - mean_y)) / np.sum((x - mean_x) ** 2)
intercept = mean_y - slope * mean_x

# Membuat model regresi linier
def linear_regression(x):
    return slope * x + intercept

# Memprediksi nilai y untuk setiap x
predicted_y = linear_regression(x)

# Mencetak koefisien regresi linier
print("Slope (Kemiringan):", slope)
print("Intercept (Konstanta):", intercept)

# Plot data asli dan garis regresi
plt.scatter(x, y, label='Data Asli')
plt.plot(x, predicted_y, color='red', label='Regresi Linier')
plt.xlabel('Variabel Independen (X)')
plt.ylabel('Variabel Dependan (Y)')
plt.legend()
plt.show()
