# Misalnya kita ingin mengecek apakah nilai di dalam fungsi adalah angka genap atau ganjil. Kalau genap akan ditambah 2 dan kalau ganjil akan dika

def ceknilai(nilai):
    if nilai % 2 == 0:
        nilai += 2
    else:
        nilai *= 2
    
    return nilai

angka = input("masukkan nilai = ")
hasil = ceknilai(int(angka))

print("hasilnya adalah {} ".format(hasil))

# Nilai diinput oleh user kemudian disimpan di variabel angka. Selanjutnya memanggil fungsi ceknilai() dengan memparsing variabel angka dan disimpan ke variabel hasil.
# Selanjutnya di dalam fungsi dicek apakah nilai tersebut genap atau ganjil dengan menggunakan operator artimatika. Jika genap ditambah 2 sedangkan jika ganjil dikali 2.
# Terakhir fungsi mengembalikan nilai ke variabel hasil dan dicetak dengan menggunakan metode format.