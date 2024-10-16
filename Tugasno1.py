# Fungsi untuk mengevaluasi performa berdasarkan nilai persentase yang diberikan
def evaluate_performance(percentage):
    # Jika nilai persentase >= 90, cetak "Excellent performance"
    if percentage >= 90:
        print("Excellent performance")
    # Jika nilai persentase >= 80 tapi kurang dari 90, cetak "Very Good performance"
    elif percentage >= 80:
        print("Very Good performance")
    # Jika nilai persentase >= 70 tapi kurang dari 80, cetak "Good performance"
    elif percentage >= 70:
        print("Good performance")
    # Jika nilai persentase >= 60 tapi kurang dari 70, cetak "Averange performance"
    elif percentage >= 60:
        print("Averange performance")
    # Jika nilai persentase kurang dari 60, cetak "Bellow Averange performance"
    else:
        print("Bellow Averange performance")

# Meminta input dari pengguna untuk memasukkan nilai persentase sebagai angka desimal
percentage = float(input("Enter the Student's percentage: "))

# Memanggil fungsi evaluate_performance untuk mengevaluasi nilai persentase yang diberikan
result = evaluate_performance(percentage)
print(result)
