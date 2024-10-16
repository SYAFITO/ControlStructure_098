# Fungsi untuk mencetak pola angka berdasarkan nilai n
def cetak_pola(n):
    # Loop dari 1 hingga n (inklusif)
    for i in range(1, n + 1):
        # Mencetak angka i sebanyak i kali dengan spasi di antaranya
        print((str(i) + ' ') * i)  

try:
    # Input: Meminta pengguna memasukkan nilai n dalam bentuk integer
    n = int(input("Enter the value of n (positive integer): "))
    
    # Memastikan nilai n positif (lebih besar dari 0)
    if n < 1:
        print("Please enter a positive integer greater than 0.")  # Pesan kesalahan untuk input negatif atau 0
    else:
        cetak_pola(n)  # Memanggil fungsi cetak_pola untuk menampilkan pola angka

# Mengatasi kesalahan jika input bukan integer yang valid
except ValueError:
    print("Please enter a valid integer.")  # Pesan kesalahan jika input bukan angka
