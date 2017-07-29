def jeniskelamin(kelamin='tidak diketaui'):
    if kelamin is 'm':
        kelamin = "Laki-laki"
    elif kelamin is 'f':
        kelamin = "Perempuan"
    print(kelamin)


jeniskelamin('m')
jeniskelamin('f')
jeniskelamin()
