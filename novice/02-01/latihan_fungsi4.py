# function yang ketika di panggil akan langsung menampilkan teks

# def hitung_luas_segitiga(alas, tinggi):
 # luas = (alas * tinggi) / 2
 # print("Luas segitiga adalah: ",luas)
    
# hitung_luas_segitiga(5, 7)

# Dalam banyak situasi, hasil sebuah function perlu disimpan ke dalam variabel terlebih dahulu, untuk kemudian di proses lebih lanjut.
# Untuk keperluan inilah perlu menambah perintah return ke dalam function. Tujuannya, agar sebuah function bisa mengembalikan nilai.
# Langsung saja kita lihat modifikasi dari function hitung_luas_segitiga() dengan penambahan perintah return:

def hitung_luas_segitiga(alas, tinggi):
  luas = (alas * tinggi) / 2
  return luas
    
var1 = hitung_luas_segitiga(5, 7)
print("Luas segitiga adalah:",var1)

# Hasil kode program:
#Luas segitiga adalah: 17.5

#Perintah return ada di baris 3, yakni return luas. Artinya, kembalikan nilai yang tersimpan di dalam variabel luas kepada kode yang akan memanggil function tersebut.

#Di baris 5 saya membuat variabel var1 dan mengisinya dari hasil function hitung_luas_segitiga(5, 7). Dengan perintah ini, variabel var1 akan berisi angka 17.5 yang kemudian ditampilkan dengan perintah print.

#Seperti inilah cara penggunaan perintah return dalam mengembalikan nilai function.