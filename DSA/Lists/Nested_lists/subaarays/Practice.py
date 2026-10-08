l=[1,2,3,4,5,6,7,8,9,10]
key=9
for i in range(len(l)):
    for j in range(i,len(l)):
        sum=0
        for k in range(i,j+1):
            sum+=l[k]
        if key==sum:
            print(l[i:j+1])

