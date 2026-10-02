# Program Konversi Suhu Celcius - Reamur - Fahrenheit #

# Header dan Input Identitas
print("Program Konversi Suhu")
print("Nama : Dyahayu Khaila Putri")
print("NIM : 1306625044")
print()

# Input Parameter Suhu
suhu_awal = float(input("Suhu awal="))
suhu_akhir = float(input("Suhu akhir="))
selang = float(input("selang ="))
print()

# Header Tabel
print("TABEL KONVERSI")
print(f"{'No.':<4} | {'Celcius':<10} | {'Reamur':<10} | {'Fahrenheit':<10}")
print("-" * 45)

# Inisialisasi Variabel Perulangan
c = suhu_awal
no = 1

# Perulangan while untuk Perhitungan dan Cetak Format Tabel
while c <= suhu_akhir:
    r = 0.8 * c
    f = (1.8 * c) + 32
    # Cetak baris tabel dengan format rapi
    print(f"{no:<4} | {c:<10.1f} | {r:<10.1f} | {f:<10.1f}")

    c += selang
    no += 1

# penutup tabel
print("-" * 60)
print("selesai")
