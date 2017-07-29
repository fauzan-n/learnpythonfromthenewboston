class Musuh:

    def __init__(self, x):
        self.tenaga=x

    def cetak_tenaga(self):
        print(self.tenaga)

dono = Musuh(5)
adot = Musuh(20)

dono.cetak_tenaga()
adot.cetak_tenaga()