diskon = 0.0
total_belanja = float(input("Masukkan nilai total belanja : "))

if total_belanja > 100000:
    diskon = 0.15 * total_belanja
    total_setelah_diskon = total_belanja - diskon

    print(f'''
      Anda mendapatkan diskon 15% sebesar Rp{diskon}
      Total belanja yang harus dibayar adalah Rp{total_setelah_diskon}\n
      ''')
else:
    diskon = 0.0
    print("\nkamu tidak mendapatkan diskon")