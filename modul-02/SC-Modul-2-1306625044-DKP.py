#identitas
print("Program Faktor Bilangan")
print("Nama : Dyahayu Khaila Putri")
print("NIM  : 1306625044")

while True:
    bilangan = int(input("Masukkan sembarang bilangan < 100 (masukkan 0 untuk selesai) = "))

#kondisi selesai
    if bilangan == 0:
        print("SELESAI")
        break

#proses mencari faktor
    faktor = []
    i = 1

    while i <= bilangan:
        if bilangan % i == 0:
            faktor.append(i)
        i = i + 1

    print(f"Bilangan {bilangan} -> Faktornya = {faktor}")
    print("selesai")
