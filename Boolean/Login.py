def login(username, password):
    return username == "admin" and password == "1234"

username = input("Masukkan username: ")
password = input("Masukkan password: ")
if login(username, password):
    print("Login berhasil")
else:
    print("Login gagal")
