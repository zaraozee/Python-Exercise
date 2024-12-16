detik_ke_menit = 60
detik_ke_jam = 60 * 60 
detik_ke_hari = 60 * 60 * 24
 
detik = int(input('masukan detik: '))
# konversi ke hari
hari = int(detik / detik_ke_hari)
detik = detik % detik_ke_hari

# konversi sisa ke jam
jam = int(detik / detik_ke_jam)
detik = detik % detik_ke_jam

# konversi sisa ke menit 
menit = int(detik / detik_ke_menit)
detik = detik % detik_ke_menit

print(hari, 'hari', jam, 'jam', menit, 'menit',detik, 'detik')

