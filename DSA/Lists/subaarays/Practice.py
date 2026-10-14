# # l=[2,3,4,5,1,2,6,9,3]
# # k=6
# # for i in range(len(l)):
# #     for j in range(i+1,len(l)):
# #         if l[i]+l[j]==k:
# #             print(l[i],l[j])
#
#
#
# # l=[1,2,3,4,5,6,7,8,9,10,1,2,3,1,5,6]
# # e=0
# # key=6
# # for i in range(len(l)):
# #     for j in range(i,len(l)):
# #         sum=0
# #         c=0
# #         l1=[]
# #         for h in range(i,j+1):
# #             l1.append(l[h])
# #             sum+=l[h]
# #             c+=1
# #         # if sum==key:
# #         #     print(l1)
# #         if sum==key and c>e:
# #             # print(l1)
# #             k2=l1
# #             e=c
# # print(k2)
#
#
#
# # s='adityaguttula'
# # ss='yag'
# # sl=len(s)
# # ssl=len(ss)
# # for i in range(sl-ssl+1):
# #     k=s[i:i+ssl]
# #     # print(k)
# #     if k==ss:
# #         print('Found')
# #         break
# # else:
# #     print('Not Found')
#
#
# # for i in range(10):
# #     if i==7:
# #         break
# #     print('i: ',i)
# #     for j in range(5):
# #         if j==3:
# #             break
# #         print('j: ',j)
#
# s='adityaguttula'
# for i in range(len(s)):
#     for j in range(i,len(s)):
#         for k in range(i,j+1):
#             print(s[k],end="")
#         print()
#
# print('-'*50)
# s='adityaguttula'
# for i in range(len(s)):
#     for j in range(i,len(s)):
#         d={}
#         for k in range(i,j+1):
#             if s[k] in d:
#                 break
#             else:
#                 d[s[k]]=1
#         else:
#             # # print(d.keys())
#             # k=d.keys()
#             # print(k)
#         # print()

# l=[9,6,3,12,4,5]
# k1=3
# maxs=0
# for i in range(len(l)):
#     for j in range(i,len(l)):
#         # s=0
#         # s=sum(l[i:j+1])
#         # print(l[i:j+1],'-->',s)
#         l1=[]
#         s=0
#         c=0
#         for k in range(i,j+1):
#             l1.append(l[k])
#             # sum+=l[k]
#         #     c+=1
#         #  sum>maxs:
#         #     maxs=sum
#         #     print('-->',maxs)
#         #     # print(l[k],end=" ")
#         # # print('-->',sum)
#         if len(l1)==k1:
#             sum+=sum(l1)
#         if sum>c:
#             c=sum
# prinmt(c)

l=[9,6,3,12,4,5,7]
k=3
max=0

# for i in range(len(l)-k+1):
#     sl=l[i:i+k]
#     print(sl)

# for i in range(len(l)-k+1):
#     sl=l[i:i+k]
#     s=sum(sl)
#     print(sl,'-->',s)
#     if s>max:
#         sl1=sl
#         max=s
# print(sl1,max)

l=[1,2,3,4,5,6,7]
le=r=max=sum=0
k=3
while r<len(l):
    sum+=l[r]
    if (r-le+1)==k:
        if sum>max:
            max=sum
            # print(sum)
            # sum=0
        sum-=l[le]
        le+=1
    r+=1
print(max)

















