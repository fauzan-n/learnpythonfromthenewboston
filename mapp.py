pendapatan = [11, 22, 33]

def dikalidua(rupiah):
    return rupiah *2

map(dikalidua, pendapatan)

pendapatan_baru = list(map(dikalidua, pendapatan))
print(pendapatan_baru)