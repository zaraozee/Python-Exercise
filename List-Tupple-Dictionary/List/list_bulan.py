bulan = ['Januari', 'Februari', 'Maret', 'April' 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
print(bulan[2])
print(bulan[9])

bulan[7] = 'August'
bulan[0] = 'January'

bulan.append('Muharram')

for i,m in enumerate(bulan):
 print(f'Bulan ke-{i+1} yaitu {m}')