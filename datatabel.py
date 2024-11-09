# Buatlah data tabel dengan total 10, Keluarkan data 5 teratas dan 5 terbawah

import pandas as pd

# Membuat DataFrame dengan total 10 beris data
data = {
    'Nama':['Ara', 'Tina', 'Lala', 'Lisna', 'Veve', 'Laras', 'Hanifa', 'Jara', 'Sandra', 'Nur'],
    'Alamat':['Bandung', 'Lampung', 'Pontianak', 'Bogor', 'Bangka', 'Jember', 'Surabaya', 'Jakarta', 'Garut', 'Depok']
}

df = pd.DataFrame(data)

# Menampilkan 5 data teratas
data_teratas = df.head(5)
print("5 Data Teratas:\n", data_teratas)

# Menampilkan 5 data terbawah
data_terbawah = df.tail(5)
print("\n5 Data Terbawah:\n", data_terbawah)