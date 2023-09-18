def fibonacci(n):
    if n <= 0:
        return "Masukkan jumlah langkah yang valid (bilangan bulat positif)."
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        a, b = 1, 2
        for _ in range(n - 2):
            a, b = b, a + b
        return b

def jumlah_kubus_tangga(n):
    if n <= 0:
        return "Masukkan jumlah langkah yang valid (bilangan bulat positif)."
    return fibonacci(n)  # Jumlah kubus yang diperlukan adalah bilangan Fibonacci ke-n+1

n = int(input("Masukkan jumlah langkah tangga yang ingin Anda bangun: "))
jumlah_kubus = jumlah_kubus_tangga(n)

if isinstance(jumlah_kubus, str):
    print(jumlah_kubus)
else:
    print("Untuk membangun tangga dengan", n, "langkah, Anda memerlukan sejumlah", jumlah_kubus, "kubus kayu.")
