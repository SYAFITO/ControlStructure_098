# Meminta input dari pengguna untuk menentukan jumlah elemen deret Fibonacci
n = int(input("Masukkan nilai n:"))

# Inisialisasi dua elemen pertama deret Fibonacci: a = 0 dan b = 1
a, b = 0,1
# Membuat list kosong untuk menyimpan hasil deret Fibonacci
hasil = []
9
# Perulangan untuk menghitung dan menambahkan elemen Fibonacci ke dalam list 'hasil'
for i in range(n) :
    hasil.append(a) # Menambahkan nilai a ke list hasil
    a,b = b,a + b # Memperbarui nilai a dan b untuk iterasi berikutnya

# Menampilkan hasil deret Fibonacci hingga elemen ke-n
print("Deret Fibonacci hingga",n,":",hasil)