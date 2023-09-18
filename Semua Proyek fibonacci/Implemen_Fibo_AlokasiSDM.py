def fibonacci(n):
    if n <= 0:
        return "Masukkan jumlah tahun yang valid (bilangan bulat positif)."
    elif n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    else:
        fib_list = [1, 1]
        a, b = 1, 1
        for _ in range(n - 2):
            a, b = b, a + b
            fib_list.append(b)
        return fib_list

def alokasi_sumber_daya_manufaktur(tahun):
    if tahun <= 0:
        return "Masukkan jumlah tahun yang valid (bilangan bulat positif)."
    
    fib_list = fibonacci(tahun)
    
    # Simulasikan alokasi sumber daya berdasarkan urutan Fibonacci
    hasil_alokasi = []
    total_sumber_daya = 1000  # Jumlah total sumber daya yang tersedia
    for i in range(tahun):
        alokasi = total_sumber_daya * (fib_list[i] / sum(fib_list))
        hasil_alokasi.append(alokasi)
    
    return hasil_alokasi

tahun = int(input("Masukkan jumlah tahun perencanaan alokasi sumber daya: "))
hasil_alokasi = alokasi_sumber_daya_manufaktur(tahun)

if isinstance(hasil_alokasi, str):
    print(hasil_alokasi)
else:
    print("Hasil alokasi sumber daya selama", tahun, "tahun:")
    for i in range(tahun):
        print(f"Tahun {i+1}: {hasil_alokasi[i]} sumber daya")
