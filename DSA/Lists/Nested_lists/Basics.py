# l=list(map(int,input().split()))
# print(l)

# nl=[]
# n=int(input('Enter No of Rows: '))
# for i in range(n):
#     nl.append(list(map(int,input().split())))
# print(nl)


# nl=[]
# r=int(input('Enter No of Rows : '))
# c=int(input('Enter No of Columns : '))
# for i in range(r):
#     l=[]
#     for j in range(c):
#         l.append(int(input()))
#     nl.append(l)
# print(nl)


# '1. Write a Program to print  all the EVEN Number in Nested List.'
# nl=[]
# n=int(input('Enter No of Rows: '))
# for i in range(n):
#     nl.append(list(map(int,input().split())))
# for i in range(len(nl)):
#     for j in range(len(nl[i])):
#         if nl[i][j]%2==0:
#             print(nl[i][j],end=" ")
#     print()

# '2. Write a Program to print all the Prime Number in nested lists'
# nl=[]
# def prime(x):
#     if x<=1:
#         return False
#     for i in range(2,x):
#         if x%i==0:
#             return False
#     else:
#          return True
# n=int(input('Enter No of Rows: '))
# for i in range(n):
#     nl.append(list(map(int,input().split())))
# for i in range(len(nl)):
#     for j in range(len(nl[i])):
#         k=nl[i][j]
#         if prime(k):
#             print(k,end=" ")
#     print()

# r=int(input())
# nl=[]
# for i in range(r):
#     l=input().split()
#     print('l: ',l)
#     l1=list(map(int,l))
#     print('l1: ',l1)
#     nl.append(l1)
#     print('nl: ',nl)

# r=int(input('Rows: '))
# c=int(input('columns: '))
# nl=[]
# for i in range(r):
#     l=[]
#     for j in range(c):
#         l.append(int(input()))
#         print(l)
#     print('l: ',l)
#     nl.append(l)
#     print('nl: ',nl)




