def fibonacci(n):
    if n <= 0:
        return "Masukkan jumlah bulan yang valid (bilangan bulat positif)."
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

def optimalkan_penjadwalan_pekerja(bulan):
    if bulan <= 0:
        return "Masukkan jumlah bulan yang valid (bilangan bulat positif)."
    
    fib_list = fibonacci(bulan)
    
    # Simulasikan penjadwalan pekerja berdasarkan urutan Fibonacci
    jadwal_pekerja = [fib_list[0]]
    for i in range(1, bulan):
        jadwal_pekerja.append(jadwal_pekerja[i-1] + fib_list[i])
    
    return jadwal_pekerja

bulan = int(input("Masukkan jumlah bulan untuk penjadwalan pekerja: "))
jadwal_pekerja = optimalkan_penjadwalan_pekerja(bulan)

if isinstance(jadwal_pekerja, str):
    print(jadwal_pekerja)
else:
    print("Penjadwalan pekerja selama", bulan, "bulan:")
    for i in range(bulan):
        print(f"Bulan {i+1}: Jumlah Pekerja = {jadwal_pekerja[i]}")
