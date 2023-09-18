def fibonacci(n):
    fib_list = []
    a, b = 0, 1
    while len(fib_list) < n:
        fib_list.append(a)
        a, b = b, a + b
    return fib_list

n = int(input("Masukkan jumlah bilangan Fibonacci yang ingin Anda hitung: "))

if n <= 0:
    print("Masukkan jumlah bilangan yang valid (bilangan bulat positif).")
else:
    result = fibonacci(n)
    print("Urutan bilangan Fibonacci pertama", n, "adalah:")
    print(result)
