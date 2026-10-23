with open('data.txt', 'r') as file:
    k=0
    l=file.read()
    l=len(l)
    file.seek(0)
    while k<=l:
        f=file.read(5)
        print(f)
        print('Cursor Position : ',file.tell())
        k=k+5
        file.seek(k)



