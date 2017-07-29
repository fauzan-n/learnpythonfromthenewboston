date, name, price = ['desember 1, 2011', 'bread gloovee', 5.23]

print(name)

def drop_first_last(grades):
    first, *middle, last = grades
    avg = sum(middle)/len(middle)
    print(avg)


drop_first_last([11,53,57,2,78,4,556])