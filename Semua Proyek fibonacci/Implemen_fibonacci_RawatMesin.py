def fibonacci(n):
    if n <= 0:
        return "Masukkan tahun yang valid (bilangan bulat positif)."
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        a, b = 1, 2
        for _ in range(n - 2):
            a, b = b, a + b
        return b

def biaya_pemeliharaan_mesin(tahun):
    if tahun <= 0:
        return "Masukkan tahun yang valid (bilangan bulat positif)."
    return fibonacci(tahun) * 1000  # Biaya pemeliharaan per tahun adalah bilangan Fibonacci ke-n+1 dikali 1000

tahun = int(input("Masukkan jumlah tahun pemeliharaan mesin: "))
biaya_total = biaya_pemeliharaan_mesin(tahun)

if isinstance(biaya_total, str):
    print(biaya_total)
else:
    print("Biaya total pemeliharaan mesin selama", tahun, "tahun adalah $", biaya_total)
