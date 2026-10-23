# Modul [05] - [Mengurutkan]

**Nama:** [Dyahayu Khaila Putri]  
**NIM:** [1306625044]  
**Kelas:** [Fisika C]  

---

## 1. Problem Statement
> Diberikan 100 data nilai ujian yang tersimpan dalam sebuah list dan belum terurut.

## 2. Mathematical Equation
> a. Himpunan data
> X = {x₁, x₂, x₃, …, xₙ}, dengan n = 100
> b. Tujuan pengurutan (ascending)
> Hasil akhir X’ = {x’₁, x’₂, …, x’ₙ} harus memenuhi:
> x’₁ ≤ x’₂ ≤ x’₃ ≤ … ≤ x’ₙ
> c. Jumlah perbandingan
> Σ (n − i) untuk i = 1 sampai n−1 = n(n − 1)/2 = 100 × 99 / 2 = 4950 perbandingan

## 3. Algorithm
1.  Mulai
2.  Cetak "Program Sorting"
3.  Cetak "Nama : Dyahayu Khaila Putri"
4.  Cetak "NIM  : 1306625044"
5.  Deklarasikan list nilai berisi 100 data
6.  n ← 100
7.  Cetak "Data nilai awal :" lalu seluruh isi nilai
8.  data ← salinan dari nilai
9.  i ← 1
10. Selama i ≤ n - 1 kerjakan:
11.     j ← 1
12.     Selama j ≤ n - i kerjakan:
13.         Jika data[j] > data[j+1] maka
14.             temp ← data[j]
15.             data[j] ← data[j+1]
16.             data[j+1] ← temp
17.         j ← j + 1
18.     i ← i + 1
19. Cetak "Data nilai terurut :"
20. k ← 1
21. Selama k ≤ n kerjakan:
22.     Cetak data[k]
23.     Jika k mod 10 = 0 maka pindah baris
24.     k ← k + 1
25. Cetak "*selesai*"
26. Selesai
