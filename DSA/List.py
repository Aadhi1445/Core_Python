# # '''Basics'''
# # # l=[10,20,30,40,50]
# # # # print(l)
# # # # print(*l)
# # # # for i in l:
# # # #     print(i)
# # # # l.append(100)
# # # # print(l)
# # # # l.extend([200,300])
# # # # print(l)
# # # # l.append([400,500])
# # # # print(l)
# # # # l1=[600,700,800]
# # # # l.append(l1)
# # # # print(l)
# # # # l.extend(l1)
# # # # print(l)
# # # # l.insert(1,200)
# # # # print(l)
# # # # l.insert(7,500)
# # # # print(l)
# # # # l.insert(9,900)
# # # # print(l)
# # # # l.remove(40)
# # # # print(l)
# # # # l.remove()
# # # # print(l)
# # # # l.remove(100)
# # # # print(l)
# # # l=[10,20,30,40,50,10,50]
# # # # l.pop()
# # # # print(l)
# # # # l.pop(2)
# # # # print(l)
# # # # l.clear()
# # # # print(l)
# # # # print(l.index(40))
# # # # k=l.index(20)
# # # # print(k)
# # # # print(l.count(10))
# # # # m=l.count(20)
# # # # print(m)
# # # l.sort()
# # # print(l)
# # # l.sort(reverse=True)
# # # print(l)11
# # print("-"*50)
# print('-'*50)
# '''Basic List Questions'''
# '''1. Write a program to create a list by taking input from the user and print the list
#     2. Write a program to insert an element at a specific index in a list.'''
# l=[1,2,3,4,5,5,6,7,7,9,8,9]
# # l=list(map(int,input().split()))
# # print(l.insert(9,10))
# l.insert(9,10)
# # print(l)
# print("-"*50)
# '''3. Write a program to merge two lists into a single list.'''
# l1=[11,12,13,14,15]
# # # l=l+l1
# # # print(l)
# # l.append(l1)
# # print(l)
# l.extend(l1)
# print("-"*50)
# '''4. Write a program to remove a specific element from a list.'''
# # print(l)
# # # l.remove(11)
# # # print(l)
# # print(l.remove(11))
# print("-"*50)
# '''5. Write a program to remove an element from a list using its index.'''
# # # # l.pop(10)
# # # # print(l)
# # print(l.pop(10))
# # print(l,"-",len(l))
# print("-"*50)
# '''6. Write a program to find the index of a given element in a list.'''
# l.index(1)
# # print(l.index(1))
# # print(l.index(8))
# print("-"*50)
# '''7. Write a program to count the number of occurrences of an element in a list.'''
# l.count(5)
# # print(l.count(5))
# # print(l.count(3))
# # print(l.count(0))
# # print(l.count(18))
# print("-"*50)
# '''8. Write a program to find the sum of the first and last elements of a list.'''
# k=l[0]+l[-1]
# print(k)
# print(l[0]+l[-1])
# # print(l[0]+l[(len(l)-1)])
# print("-"*50)
# '''9. Write a program to calculate the sum of list elements up to a given index.'''
# sum=0
# k=6
# l=[1,2,3,4,5,6,7,8,9,10]
# for i in range(k+1):
#     sum=sum+l[i]
# print(sum)
# print("-"*50)
# '''10. Write a program to calculate the average of odd numbers in a list.'''
# sum=c=0
# l=[1,2,3,4,5,6,7,8,9,10]
# # print(len(l))
# for i in l:
#     if i%2==1:
#         sum+=i
#         c=c+1
# print(sum," ",c)
# print(sum//c)
# print("-"*50)
# '''11. Write a program to print all prime numbers present in a list.'''
# l=[1,2,3,4,5,6,7,8,9,10]
# for i in l:
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         if i >1:
#             print(i,end=" ")
# print()
# print("-"*50)
# '''9. Write a program to calculate the sum of list elements up to a given index.'''
# l=[1,2,3,4,5]
# sum=0
# for i in range(3):
#     sum+=l[i]
# print(sum)
# print("-"*50)
# '''12. Write a program to print the next prime number for each element in the list'''
# m=[]
# for i in l:
#     d=0
#     k=i+1
#     while d<1:
#         for j in range(2,k):
#             if k%j==0:
#                 break
#         else:
#             # print(k,end=" ")
#             d=d+1
#             m.append(k)
#         k=k+1
# print(m,"-",len(m))
# # g=set(m)
# # print(g)
# l=[1,2,3,4,5,6,7,8,9,10]
# for i in l:
#     k=i+1
#     d=0
#     while d<1:
#         for j in range(2,k):
#             if k%j==0:
#                 break
#         else:
#             if k>1:
#                 print(k,end=" ")
#                 d=d+1
#         k=k+1
# print()
# print("-"*50)
# '''13. Write a program to print the list in reverse order.'''
# # for i in range(len(l)-1,-1,-1):
# #     print(l[i],end=" ")
# for i in range(1,len(l)+1):
#     print(i,end="--")
#     print(l[-i],end=" ")
# print()
# print("-"*50)
# '''14. Write a program to find sum of any two elements which is equal to key value'''
# l=tuple(map(int,input().split()))
# l=list(l)
# k=9
# for i in range(0,len(l)-2):
#     for j in range(i+1,len(l)):
#         if l[i]+l[j]==k:
#             print(l[i],l[j])
# print("-"*50)
# '''Maximum & Minimum'''
# '''15. Write a program to find the largest number in a list.'''
# l=tuple(map(int,input().split()))
# l=list(l)
# l=[1,2,3,4,5,6,7,8]
# s=float('-inf')
# for i in l:
#     if i >s:
#         s=i
# print(s)
# print("-"*50)
# '''16. Write a program to find the second largest number in a list. '''
# l=tuple(map(int,input().split()))
# l=list(l)
# n=2
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         # print(l[i],l[j],end="-")
#         if l[i]>l[j]:
#             l[i],l[j]=l[j],l[i]
            # print(l[i],l[j])
            # print(l)
# print(l)
# print(l[(len(l))-n])
# print("-"*50)
# '''17. Write a program to find the third largest number in a list.'''
# l=tuple(map(int,input().split()))
# l=list(l)
# n=3
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         # print(l[i],l[j],end="-")
#         if l[i]>l[j]:
#             l[i],l[j]=l[j],l[i]
#             # print(l[i],l[j])
#             # print(l)
# # print(l)
# print(l[(len(l))-n])
# print("-"*50)
# '''18. Write a program to sort a list without using any built-in sorting functions. '''
# l=list(map(int,input().split()))
# l=[2,3,6,4,9]
# for i in range(len(l)):
#     for j in range(len(l)):
#         if l[i]>l[j]:
#             l[i],l[j]=l[j],l[i]
# print(l)


# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]>l[j]:
#             l[i],l[j]=l[j],l[i]
# print(l)
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]<l[j]:
#             l[i],l[j]=l[j],l[i]
# print(l)
# print('-'*50)
# '''19. Write a program to find the Nth largest element in a list. '''
# l=tuple(map(int,input().split()))
# l=list(l)
# n=int(input())
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]>l[j]:
#             l[i],l[j]=l[j],l[i]
# print(l[(len(l)-n)])
# print("-"*50)
# '''20. Write a program to print the first four smallest missing elements from a list
# Searching'''
# l=list(map(int,input().split()))
# n=int(input())
# c=0
# s=min(l)
# while c<n:
#     if s not in l:
#         print(s,end=" ")
#         c+=1
#     s+=1
# print('-'*50)
# ''' 21. Write a program to perform linear search on a list.'''
# l=list(map(int,input().split()))
# n=int(input())
# for i in l:
#     if i==n:
#         print(l.index(n))
#         break
# print('-'*50)
# '''22. Write a program to perform binary search on a sorted list.'''
# l=[10,20,30,40,50,60]
# n=40
# l.sort()
# s,e=0,len(l)-1
# b=False
# while s<=e:
#     m=(s+e)//2
#     if l[m]==n:
#         b=True
#         break
#     elif n>l[m]:
#         s=m+1
#     else:
#         e=m-1
# if b:
#     print("Found")
# else:
#     print("Not Found")
# print('-'*50)
# '''23. Write a program to return all index positions of a searched element in a list. '''
# l=[1,3,2,4,5,2,7,8,2,10]
# n=2
# for i in range(0,len(l)):
#     if n==l[i]:
#         print(i,end=" ")
# print()
# print('-'*50)
# '''24. Write a program to check whether a list is sorted or not. '''
# l=[10,20,30,40,50,60]
# b=False
# for i in range(0,len(l)-1):
#     if l[i]>l[i+1]:
#         b=True
# if b:
#     print("Sorted")
# else:
#     print("Not Sorted")
# print('-'*50)
# ''' 25. Write a program to find the LCM of all numbers in the list. '''
# l=[2,8,4]
# h=max(l)
# k=h
# c=0
# while True:
#     for i in l:
#         if k%i==0:
#             c+=1
#     if c==len(l):
#         print(k)
#         break
#     k=k+h
# print('-'*50)
# '''26. Write a program to find the GCD of all numbers in the list. '''
# l=[2,4,6,8,14]
# s=min(l)
# for i in range(s,0,-1):
#     c=0
#     for j in l:
#         if j%i==0:
#             c+=1
#     if c==len(l):
#         print(i)
#         break
# print('-'*50)
# '''27. Write a program to find the factorial of each element in a list '''
# l=[1,2,3,4,5]
# for i in l:
#     k=1
#     for j in range(i,0,-1):
#         k=k*j
#     print(k,end=" ")
#
# print()
# print('-'*50)
# l=[1,2,3,5,3,7,2,9,9,2,9,9,4,6,1,6,4,7]
# for i in range(len(l)):
#     c=0
#     for j in range(i):
#         if l[i]==l[j]:
#             c+=1
#     if c==0:
#         print(l[i],'->',l.count(l[i]))
# print('-'*50)
# l=[1,2,3,2,4,2,4]
# k=3
# for i in range(len(l)):
#     c=0
#     for j in range(i):
#         if l[i]==l[j]:
#             c+=1
#     if c==0 and l.count(l[i])==k:
#         print('Element:',l[i],'->',l.count(l[i]))
# print('-'*50)
# '''Most Repeated Element'''
# l=[1,2,3,4,2,2,4,3,1,5,6,3,2,1]
# e=f=0
# for i in range(len(l)):
#     c=0
#     for j in range(i):
#         if l[i]==l[j]:
#             c+=1
#     if c==0:
#         c1=l.count(l[i])
#         if c1>f:
#             f=c1
#             e=l[i]
# print(e,'->',f)
# print('-'*50)
# ''' ListRotation'''
# '''35. Write a program to print all rotations of a list (clockwise) '''
# l=[0,1,2,3,4]
# for i in range(len(l)):
#     print(l)
#     l=[l[len(l)-1]]+l[0:(len(l)-1)]
# print('-'*50)
# l=[0,1,2,3,4]
# for i in range(len(l)):
#     print(l)
#     k=l[len(l)-1]
#     for j in range(len(l)-2,-1,-1):
#         l[j+1]=l[j]
#     l[0]=k
# print('-'*50)
# '''2. Write a program to print all rotations of a list (anticlockwise) '''
# l=[1,2,3,4,5]
# for i in range(len(l)):
#     print(l)
#     k=l[0]
#     for j in range(1,len(l)):
#         l[j-1]=l[j]
#     l[len(l)-1]=k
# print('-'*50)
# l=[1,2,3,4,5]
# for i in range(len(l)):
#     print(l)
#     l=l[1:len(l)]+[l[0]]
# print('-'*50)
# '''37. Write a program to rotate a list by k positions.(anticlockwise) '''
# l=[10,20,30,40,50]
# k=2
# for i in range(len(l)):
#     print(l)
#     l1=[]
#     for j in range(k):
#         l1.append(l[j])
#     for s in range(k):
#         l.pop(0)
#     l.extend(l1)
# print('-'*50)
# l=[10,20,30,40,50]
# k=2
# for i in range(len(l)):
#     print(l)
#     l=l[k:len(l)]+l[0:k]
#
#
