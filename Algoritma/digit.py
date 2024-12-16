# (A) 
digit_char = input("masukan karakter digit:")
#konversi karakter ke integer
integer_value = ord(digit_char) - ord('0')

print("nilai integer:",integer_value)

# (B)
digit_char = input("masukan karakter:")
#memeriksa apakah karakter merupakan digit
if '0' <= digit_char <= '9':
    integer_value = ord(digit_char) - ord('0')
else:
    integer_value = -99

print("nilai integer:",integer_value)