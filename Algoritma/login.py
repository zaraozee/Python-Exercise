print("\tlogin")
print("="*20)

username = "kiko"
password = "12345"

input_username = input("masukan username: ")
input_password = input("masukan password: ")

if input_username == username and input_password == password:
    print("Login berhasil")
else:
    print("Login gagal")
