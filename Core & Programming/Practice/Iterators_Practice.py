'''Iterators'''
# class CountDown:
#     def __init__(self,n):
#
#         self.n=n
#     def __iter__(self):
#         # print(1)
#         self.m=0
#         return self
#     def __next__(self):
#         # print('2:',2)
#         if self.n<=0:
#             raise StopIteration
#         value=self.n
#         self.n-=1
#         return value
# for i in CountDown(5):
#     print(i)

# class Even_numbers:
#     def __init__(self,n):
#         self.n=n
#     def __iter__(self):
#         self.m=2
#         return self
#     def __next__(self):
#         k=self.m
#         self.m+=2
#         if k<=self.n:
#             return k
#         else:
#             raise StopIteration
# for i in Even_numbers(30):
#     print(i)

# class My_string:
#     def __init__(self,s):
#         self.s=s
#     def __iter__(self):
#         self.i=0
#         return self
#     def __next__(self):
#         self.i+=1
#         if (self.i-1)<len(self.s):
#             return self.s[self.i-1]
#         else:
#             raise StopIteration
# o=My_string('AdityaGuttula')
# for i in o:
#     print(i)

# l=[10,20,30,40,50]
# it=iter(l)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

# class ReverseIterator:
#     def __init__(self,l):
#         self.l=l
#     def __iter__(self):
#         self.k=len(self.l)
#         return self
#     def __next__(self):
#         self.k-=1
#         if self.k>=0:
#             return self.l[self.k]
#         else:
#             raise StopIteration
# obj=ReverseIterator([10,20,30,40,50])
# for i in obj:
#     print(i)

# class StepIterator:
#     def __init__(self,s,e,st):
#         self.s=s
#         self.e=e
#         self.st=st
#     def __iter__(self):
#         return self
#     def __next__(self):
#         self.s+=self.st
#         if self.s-3<self.e:
#             return self.s
#         else:
#             raise StopIteration
# obj=StepIterator(2,20,3)
# for i in obj:
#     print(i)

# class Iterator:
#     def __init__(self,l):
#         self.l=l
#         self.k=0
#     def __iter__(self):
#         # self.k=0
#         return self
#     def __next__(self):
#         self.k+=1
#         if self.k<=len(self.l):
#             return self.l[self.k-1]
#         else:
#             raise StopIteration
# obj=Iterator([10,20,30,40,50])
# for i in obj:
#     print(i)
# print('2nd Second loop')
# for i in obj: # here second loop prints nothing because previous iterator is stoopped at self.k=6 so condition falis and it give nothing
#     print(i) # to overcome this create new iterator self.k whener iter() is called then it works multiple times or follow below one's
#
# class Iterator:
#     def __init__(self,l):
#         self.l=l
#         self.k=0
#     def __iter__(self):
#         current=0
#         while current<len(self.l):
#             yield self.l[current]
#             current+=1
# obj=Iterator([10,20,30,40,50])
# for i in obj:
#     print(i)
# print('2nd Second loop')
# for i in obj:
#     print(i)

