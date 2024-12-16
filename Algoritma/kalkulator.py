operand1 = float(input("Masukkan operand pertama: "))
operator = input("Masukkan operator (+, -, *, /): ")
operand2 = float(input("Masukkan operand kedua: "))

# Melakukan operasi aritmatika berdasarkan operator yang diinput
if operator == '+':
    hasil = operand1 + operand2
elif operator == '-':
    hasil = operand1 - operand2
elif operator == '*':
    hasil = operand1 * operand2
elif operator == '/':
    if operand2 != 0:
        hasil = operand1 / operand2
    else:
        hasil = "Error: Pembagian dengan nol tidak diperbolehkan"
else:
    hasil = "Operator tidak valid"

print(f"Hasil: {hasil}")