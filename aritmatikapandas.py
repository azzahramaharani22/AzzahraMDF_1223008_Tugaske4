# Membuat aritmatika menggunakan pandas

import pandas as pd

# Membuat data frame
data = {
        'A':[18, 26, 34],
        'B':[8, 13, 23]
}

df = pd.DataFrame(data)

# Operasi Aritmatika
penjumlahan = df['A'] + df['B']
pengurangan = df['A'] - df['B']
perkalian = df['A'] * df['B']
pembagian = df['A'] / df['B']

print("Penjumlahan:\n", penjumlahan)
print("Pengurangan:\n", pengurangan)
print("Perkalian:\n", perkalian)
print("Pembagian:\n", pembagian)