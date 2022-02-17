def findMin(n):
    jumlahAngka = 0
    for i in n:
        if i == 1:
            jumlahAngka += 1
        return jumlahAngka

n = [1, 3, 5, 7, 12, 19]

print("Angka terkecil adalah", findMin(n))