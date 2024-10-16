# Fungsi untuk mencetak angka ganjil hingga n
def print_odd_numbers(n):
    odd_numbers = []
    for num in range(1, n + 1):  # Iterasi dari 1 hingga n
        if num % 2 != 0:  # Memeriksa apakah angka tersebut ganjil
            odd_numbers.append(num)  # Menambahkan angka ganjil ke dalam list
    return odd_numbers

# Main program
try:
    # Input: Meminta pengguna untuk memasukkan nilai n
    number = int(input("Enter a positive integer to print odd numbers up to: "))
    if number < 1:
        print("Please enter a positive integer greater than 0.")
    else:
        # Menghasilkan dan mencetak angka ganjil
        odd_numbers = print_odd_numbers(number)
        print(f"Odd numbers up to {number}: {odd_numbers}")
except ValueError:
    print("Please enter a valid integer.")
