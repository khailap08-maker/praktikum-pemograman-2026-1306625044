import os
import pandas as pd


def hitung_grade(na):
    if na >= 86:
        return "A"
    elif na >= 81:
        return "A-"
    elif na >= 76:
        return "B+"
    elif na >= 71:
        return "B"
    elif na >= 66:
        return "B-"
    elif na >= 61:
        return "C+"
    elif na >= 56:
        return "C"
    else:
        return "TL"


def cari_file():
    """Cari file Excel di folder yang sama dengan script (bukan folder terminal)."""
    folder_script = os.path.dirname(os.path.abspath(__file__))
    kandidat = ["DataNilai.xlsx", "DataNilai (1).xlsx"]

    for nama in kandidat:
        path = os.path.join(folder_script, nama)
        if os.path.exists(path):
            return path
    return None


def main():
    print("Program Grading")
    print("Nama : Dyahayu Khaila Putri")
    print("NRM  : 1306625044")
    print("\nLAPORAN GRADING MAHASISWA")

    path_file = cari_file()
    if path_file is None:
        print("File 'DataNilai.xlsx' tidak ditemukan.")
        print("Pastikan file Excel berada di folder yang sama dengan file .py ini:")
        print(os.path.dirname(os.path.abspath(__file__)))
        return

    try:
        df = pd.read_excel(path_file)
    except ImportError:
        print("Library 'openpyxl' belum terinstall. Jalankan: pip install openpyxl")
        return

    col_nama = df.columns[0]
    col_lain = df.columns[2]
    col_uts = df.columns[3]
    col_uas = df.columns[4]

    rekap = {
        "A": 0,
        "A-": 0,
        "B+": 0,
        "B": 0,
        "B-": 0,
        "C+": 0,
        "C": 0,
        "TL": 0
    }
    print("-" * 45)
    print(f"{'No':<4}| {'Nama Mahasiswa':<15}| {'Nilai Akhir':<11}| {'Grade':<5}|")
    print("-" * 45)

    i = 0
    total_mahasiswa = len(df)

    while i < total_mahasiswa:
        row = df.iloc[i]
        nama_mhs = str(row[col_nama])
        n_lain2 = float(row[col_lain])
        n_uts = float(row[col_uts])
        n_uas = float(row[col_uas])

        nilai_akhir = (0.30 * n_lain2) + (0.35 * n_uts) + (0.35 * n_uas)

        grade = hitung_grade(nilai_akhir)

        if grade in rekap:
            rekap[grade] += 1

        print(f"{i + 1:<4} | {nama_mhs:<15} | {nilai_akhir:<11.2f} | {grade:<5}|")

        i += 1

    print("-" * 45)
    print("\nRekapitulasi :")
    print(f"Grade A      = {rekap['A']}")
    print(f"Grade A-     = {rekap['A-']}")
    print(f"Grade B+     = {rekap['B+']}")
    print(f"Grade B      = {rekap['B']}")
    print(f"Grade B-     = {rekap['B-']}")
    print(f"Grade C+     = {rekap['C+']}")
    print(f"Grade C      = {rekap['C']}")
    print(f"Tidak Lulus (TL) = {rekap['TL']}")
    print(f"Total Mahasiswa = {total_mahasiswa}")
    print("\nselesai")


if __name__ == "__main__":
    main()
    