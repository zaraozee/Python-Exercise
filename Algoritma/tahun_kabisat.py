def is_leap_year(year):
    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0):
                return True  # Tahun habis dibagi 400, maka tahun kabisat
            else:
                return False  # Tahun habis dibagi 100 tetapi tidak habis dibagi 400, maka bukan tahun kabisat
        else:
            return True  # Tahun habis dibagi 4 tetapi tidak habis dibagi 100, maka tahun kabisat
    else:
        return False  # Tahun tidak habis dibagi 4, maka bukan tahun kabisat


tahun = 2024
if is_leap_year(tahun):
    print(f"{tahun} adalah tahun kabisat.")
else:
    print(f"{tahun} bukan tahun kabisat.")
