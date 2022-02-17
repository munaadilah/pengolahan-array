def findMax(n):
    jumlahAngka = 18
    for i in n:
        if i == 1:
            jumlahAngka += 1
        return jumlahAngka

n = [1, 3, 5, 7, 12, 19]

print("Angka terbesar adalah", findMax(n))