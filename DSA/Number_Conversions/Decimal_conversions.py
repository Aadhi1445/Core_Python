def binary(n):
    l=[]
    n=int(n)
    while n>0:
        r=n%2
        l.insert(0,str(r))
        n=n//2
    l=''.join(l)
    return  l
def octal(n):
    l = []
    n = int(n)
    while n > 0:
        r = n % 8
        l.insert(0, str(r))
        n = n // 8
    l = ''.join(l)
    return l
def hexadecimal(n):
    l = []
    n = int(n)
    while n > 0:
        r = n % 16
        if r > 9:
            r = r + 55
        l.insert(0, str(r))
        n = n // 16
    l = ''.join(l)
    return l
dec='19'
print(binary(dec))
print(octal(dec))
print(hexadecimal(19))
