import math

def main():
    while True:
        print("program Sinus-Cosinus")
        print("Nama : Dyahayu Khaila Putri")
        print("NIM  : 1306625044")

        sudut_deg = float(input("\nBesar sudut (derajat) = "))
        x_rad = math.radians(sudut_deg)

        tv_sin = math.sin(x_rad)
        tv_cos = math.cos(x_rad)

        print(f"\nTrue value sin({sudut_deg : .0f}) = {tv_sin : .6f}")
        print(f"True value cos({sudut_deg : .0f}) = {tv_cos : .6f}")
        print("-" * 65)
        print(f"{'Jumlah':<11}{'AV sinus':<15}{'ER sinus (%)':<12}")
        print("-" * 65)

        suku = 1
        av_sin = 0
        av_cos = 0

        while True:
            term_sin = ((-1)**(suku-1) * x_rad**(2*suku-1)) / math.factorial(2*suku-1)
            term_cos = ((-1)**(suku-1) * x_rad**(2*suku-2)) / math.factorial(2*suku-2)

            av_sin += term_sin
            av_cos += term_cos

            er_sin = abs((av_sin - tv_sin) / tv_sin) * 100 if tv_sin != 0 else abs(av_sin - tv_sin) * 100
            er_cos = abs((av_cos - tv_cos) / tv_cos) * 100 if tv_cos != 0 else abs(av_cos - tv_cos) * 100

            print(f"{suku:^11} | {av_sin:^12.6f} | {er_sin:^9.2f} | {av_cos:^12.6f} | {er_cos:^9.2f}")
            if er_sin < 5 and er_cos < 5:
                break
            suku += 1

        print("-" * 65 + "\n")

        ulang = input("Mau menghitung lagi (y/t)? ").lower()
        if ulang != 'y':
            print("\n" + "=" * 65 + "\n")

if __name__ == "__main__":
    main()

print("Program Selesai")
