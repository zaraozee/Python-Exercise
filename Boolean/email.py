def is_valid_email(email):
    return "@" in email and "." in email

email = input("Masukkan alamat email: ")
if is_valid_email(email):
    print("Alamat email valid.")
else:
    print("Alamat email tidak valid.")
