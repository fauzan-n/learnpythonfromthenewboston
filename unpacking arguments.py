def kalkulatorkesehatan(umur,apel,rokok):
    jawaban = (100-umur) + (apel*2 ) - (rokok*3)
    print(jawaban)

datagua = [1,2,3]

kalkulatorkesehatan(*datagua)