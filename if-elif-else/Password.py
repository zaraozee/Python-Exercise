def is_strong_password(password):
    return len(password) >= 8 and any(c.isdigit() for c in password) and any(c.isalpha() for c in password)

password = input("Masukkan password: ")
if is_strong_password(password):
    print("Password Anda kuat.")
else:
    print("Password Anda lemah.")
