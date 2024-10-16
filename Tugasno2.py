num1 = float(input("Masukkan angka pertama : "))
num2 = float(input("Masukkan angka kedua : "))
num3 = float(input("Masukkan angka ketiga : "))
# Membuat input untuk memasukkan tiga angka

if num1 >= num2 and num1 >= num3:
    largest = num1
     # Jika num1 lebih besar atau sama dengan num2 dan num1 juga lebih besar atau sama dengan num3, maka num1 adalah yang terbesar
elif num2 >= num1 and num2 >= num3:
    largest = num2
    # Jika num2 lebih besar atau sama dengan num1 dan num2 juga lebih besar atau sama dengan num3, maka num2 adalah yang terbesar
else:
    largest = num3 # Jika kedua kondisi di atas tidak terpenuhi, maka num3 adalah yang terbesar

print("Angka terbesar adalah : ", largest) # Mencetak hasil angka terbesar