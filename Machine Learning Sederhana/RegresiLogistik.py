# Impor pustaka yang diperlukan
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Buat dataset contoh (misalnya, prediksi keberhasilan penerimaan pekerjaan berdasarkan pengalaman kerja)
data = {'Pengalaman_Kerja': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'Keberhasilan_Penerimaan': [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]}

df = pd.DataFrame(data)

# Pisahkan variabel prediktor (X) dan target (y)
X = df[['Pengalaman_Kerja']]
y = df['Keberhasilan_Penerimaan']

# Bagi data menjadi data pelatihan dan data pengujian
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Inisialisasi model Regresi Logistik
model = LogisticRegression()

# Latih model pada data pelatihan
model.fit(X_train, y_train)

# Lakukan prediksi pada data pengujian
y_pred = model.predict(X_test)

# Evaluasi kinerja model
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f'Akurasi: {accuracy}')
print('Laporan Klasifikasi:')
print(report)
