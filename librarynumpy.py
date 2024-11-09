# Membuat penjumlahan menggunakan library numpy

import numpy as np

array1 = np.array([1, 4, 3])
array2 = np.array([1, 2, 7])

# Penjumlahan menggunakan numpy.add
hasil_add = np.add(array1, array2)

# Penjumlahan menggunakan operator
hasil_operator = array1 + array2

print("Hasil penjumlahan menggunakan numpy.add: " , hasil_add)
print("Hasil penjumlahan menggunakan operator +:", hasil_operator)