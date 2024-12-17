def kado():
    nama_penerima = input("Masukkan nama penerima kado: ")
    jenis_kado = input("Masukkan kado: ")
    pesan = input("Masukkan pesan : ")

    print("\n--- Informasi Kado ---")
    print(f"Nama Penerima: {nama_penerima}")
    print(f"Jenis Kado: {jenis_kado}")
    print(f"Pesan Khusus: {pesan}")

    # memberi saran kado berdasarkan jenis kado yang dimasukkan
    if jenis_kado.lower() == "buku":
        saran = "Buku 'Laut Bercerita' karya Tere Liye /bere ieu we meh ceurik TwT"
    elif jenis_kado.lower() == "mainan":
        saran = "Boneka ambalabu"
    elif jenis_kado.lower() == "pakaian":
        saran = "Sweater rajut"
    else:
        saran = "kasih mingyu aja aww"

    print(f"Saran Kado: {saran}")

kado()
