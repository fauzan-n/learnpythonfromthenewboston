list_inti = [2,4,6,39,29]
import modul

print ("ini adalah nomor yang masih tersedia")

for nomorpunggung in range(30):
    if  nomorpunggung in list_inti:
        continue
    print(nomorpunggung)

modul.ikan()

import random

x = random.randrange(1,1000)
print(x)