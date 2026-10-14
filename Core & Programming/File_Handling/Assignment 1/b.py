# with open('Transction.txt','w') as t:
#     t.write('user_id,amount,category\n')
#     t.write('U1,100,food\n')
#     t.write('U2,-50,shopping\n')
#     t.write('U3,200,travel\n')
#     t.write('U4,abc,food\n')
#     t.write('U5,300,shopping\n')
#     t.write('U6,120,food\n')
#     t.write('U7,,travel\n')
#     t.write('U8,450,electronics\n')
with open('Transction.txt','r') as t,open('clean.txt','w') as c,open('error.txt','w') as er:
    t.readline()
    total_lines=0
    clean_lines=0
    error_lines=0
    total_amount=0
    cat_amount={}
    for line in t:
        total_lines+=1
        # print(line)
        line = line.replace('\n', '')
        # print(line)
        u, a, cat = line.split(',')
        # print(u,a,cat)
        try:
            if u=='' or a=='' or cat=='':
                raise ValueError('Cannot have empty or null values')
            a=int(a)
            if a<0:
                raise  ValueError('Amount cannot be Negative')
            clean_lines+=1
            total_amount+=a
            cat_amount[cat]=cat_amount.get(cat,0)+a
            # with open('clean.txt','w') as c:
            c.write(f"{line}\n")
            c.flush()
        except ValueError as e:
            # print(e)
            # with open('error.txt','w') as er:
            error_lines+=1
            er.write(f"{line}\n      --> {e}\n")
            er.flush()
with open('report.txt','w') as r:
    r.write(f"{total_lines} lines Processed \n")
    r.flush()
    r.write(f'{clean_lines} clean lines\n')
    r.flush()
    r.write(f'{error_lines} error lines\n')
    r.flush()
    for k,v in cat_amount.items():
        r.write(f'{k} -- {v}\n')
        r.flush()






