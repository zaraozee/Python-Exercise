nilai_belanja = int(input("masukan nilai belanja :"))
pecahan_terendah = 25

sisa = nilai_belanja % pecahan_terendah
nilai_terbulatkan = nilai_belanja - sisa

print("nilai belanja setelah dibulatkan :", nilai_terbulatkan)