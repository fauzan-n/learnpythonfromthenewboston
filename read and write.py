fw = open('contoh.txt','w')

fw.write('tes nulis di file\n cool')
fw.write('saya suka bakon\n\n\n\n1')
fw.close()

fr = open('contoh.txt','r')
text = fr.read()
print(text)
fr.close()