def decimal(n):
    val=c=0
    for i in range(len(n)-1,-1,-1):
        ch=int(n[i])
        val+=ch*(2**c)
        c+=1
    return val
def Octal(n):
    val = c = 0
    for i in range(len(n) - 1, -1, -1):
        ch = int(n[i])
        val += ch * (8 ** c)
        c += 1
    return val
def Hexadecimal(n):
    val = c = 0
    for i in range(len(n) - 1, -1, -1):
        ch = int(n[i])
        val += ch * (16 ** c)
        c += 1
    return val
b='1101'
print(decimal(b))
print(Octal(b))
print(Hexadecimal(b))





