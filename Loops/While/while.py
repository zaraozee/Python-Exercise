kata = ""

while kata.lower() != "selesai":
    kata = input("Masukkan kata (ketik 'selesai' untuk berhenti): ")
    if kata.lower() != "selesai":
        print(f"Anda memasukkan: {kata}")

print("Program selesai.")
