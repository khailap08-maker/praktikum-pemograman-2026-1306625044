# Modul [03] - [Trigonometri]

**Nama:** [Dyahayu Khaila Putri]  
**NIM:** [1306625044]  
**Kelas:** [Fisika C]  

---

## 1. Problem Statement
> Membuat program untuk menghitung nilai sin dari cos dengan pendekatan deret Mc Laurin

## 2. Mathematical Equation
   a. Deret Mclaurin untuk sinus :
   $$\sin(x)=\sum_{n=0}^{\infty}\frac{(-1)^n x^{2n+1}}{(2n+1)!}=x-\frac{x^3}{3!}+\frac{x^5}{5!}-\frac{x^7}{7!}+\cdots$$
   
   b. Deret Mclaurin untuk cos :
   $$\cos(x)=\sum_{n=0}^{\infty}\frac{(-1)^n x^{2n}}{(2n)!}=1-\frac{x^2}{2!}+\frac{x^4}{4!}-\frac{x^6}{6!}+\cdots$$
   
   c. Rumus Relativ Error (Er)
   $$\text{Relative Error} = \left|\frac{AV-TV}{TV}\right|\times 100\text{\%}$$
   
## 3. Algorithm
> 1. Mulai
> 2. print program "Trigonometric With Function
> 3. print Nama " Dyahayu Khaila Putri"
> 4. print NIM "1306625044
> 5. input besar sudut dalam derajat.
> 6. Hitung True Value sinus dan cosinus menggunakan kalkulator.
> 7. Konversikan sudut dari derajat ke radian.
> 8. Gunakan Def Function untuk menghitung pendekatan sinus dan cosinus dengan deret Maclaurin.
> 9. Inisialisasi jumlah suku deret.
> 10. Gunakan while untuk menambahkan suku deret sinus hingga Relative Error < 5%.
> 11. Gunakan while untuk menambahkan suku deret cosinus hingga Relative Error < 5%.
> 12. print nilai True Value, AV, dan ER untuk sinus dan cosinus.
> 13. input pilihan untuk menghitung kembali (y/t).
> 14. Jika memilih y, kembali ke langkah 3. Jika memilih t, program berakhir.
> 15. Selesai.
> 
