# '''Octal to Decimal'''
def decimal(n):
    if n[0]=='-':
        n=int(n)
        n=abs(n)
        n=str(n)
    val=c=0
    for i in range(len(n)-1,-1,-1):
        ch=n[i]
        if  ch>='0' and ch<='7':
            ch=int(ch)
            val+=ch*(8**c)
            c+=1
        else:
            b=False
            return b
    else:
        return val
def binary(n):
    l=[]
    while n>0:
        r=n%2
        l.insert(0,str(r))
        n=n//2
    l1=''.join(l)
    return l1
n='347'
b=True
k=decimal(n)
k1=binary(k)
if b:
    print(k1)
else:
    print('Invalid')
n='-347'
if n[0]=='-':
    n=int(n)
    n=abs(n)
    n=str(n)
# print(type(n))
val=c=0
for i in range(len(n)-1,-1,-1):
    ch=n[i]
    if ch>='0' and ch<='7':
        ch=int(ch)
        val+=ch*(8**c)
        c+=1
    else:
        print('Invalid')
        break
else:
    print(val)
'''Octal to Binary'''
n='347'
# n='-347'
if n[0]=='-':
    n=int(n)
    n=abs(n)
    n=str(n)
# print(type(n))
val=c=0
b=True
for i in range(len(n)-1,-1,-1):
    ch=n[i]
    if ch>='0' and ch<='7':
        ch=int(ch)
        val+=ch*(8**c)
        c+=1
    else:
        print('Invalid')
        b=False
        break
# else:
#     print(val)
if b:
    b=[]
    while val>0:
        r=val%2
        b.insert(0,str(r))
        val=val//2
    print(''.join(b))
'''Octal to  Hexadecimal'''
n='347'
# n='-347'
if n[0]=='-':
    n=int(n)
    n=abs(n)
    n=str(n)
# print(type(n))
val=c=0
b=True
for i in range(len(n)-1,-1,-1):
    ch=n[i]
    if ch>='0' and ch<='7':
        ch=int(ch)
        val+=ch*(8**c)
        c+=1
    else:
        print('Invalid')
        b=False
        break
# else:
#     print(val)
if b:
    b=[]
    while val>0:
        r=val%16
        if r>9:
            r=chr(r+55)
            b.insert(0,r)
        else:
            b.insert(0,str(r))
        val=val//16
    print(''.join(b))










