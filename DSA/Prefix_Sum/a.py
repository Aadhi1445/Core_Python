# l = [1, 7, 3, 6, 5, 6]
# for i in range(len(l)):
#     ssum=sum(l[0:i])
#     esum=sum(l[i+1:len(l)])
#     if ssum==esum:
#         print(i)
#         break
# else:
#     print('not found')
l = [2,1,-1]
sl=[]
sum=0
for i in l:
    sum+=i
    sl.append(sum)
# print(sl) # [2, 3, 2]
for i in range(len(l)):
    if i==0:
        ss=0
    else:
        ss=sl[i]


    # print('*')
    es=sl[len(l)-1]-sl[i]
    # print('&')
    if ss==es:
        print(i)
        break
else:
    print('Not')