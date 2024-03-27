def print_alphabet_pyramid(n):
    for i in range(n):
        print(" " * (n - i - 1), end="")
        for j in range(i + 1):
            print(chr(65 + j), end="")
        for j in range(i, 0, -1):
            print(chr(65 + j - 1), end="")
        print()
jumlah_huruf = int(input("Masukkan jumlah huruf pada piramida: "))
print_alphabet_pyramid(jumlah_huruf)
