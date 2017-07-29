class A():
    def bergerak(self):
        print('Im movin')

class jamur():
    def makanjamur(self):
        print('now im big')




class mariogede(A,jamur):
    pass


bm = mariogede()
bm.bergerak()
bm.makanjamur()