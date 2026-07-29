# '''Iterator= one should iterables '''
# # l='asdfgh'
# # for i in l:
# #     print(i)
# # i=iter(l)--i.__iter__(l)
# # print(next(i))--l.__next__(i)
# #
# l='asdfgh'
# k=iter(l)
# # k=__iter__(l)
# print(next(k))
# print(next(k))
# print(next(k))
# print()
# s=iter(l)
# print(next(s))
# print(next(s))
# print(next(s))
# print()
# print(next(k))
# print(next(k))
# print(next(k))
# print(next(k))

# l=[1,2,3,4]
# k=iter(l)
# print(k)
# print(next(k))
# print(next(k))
# print(next(k))
# print(next(k))
# print('-'*50)
# '''try & Catch'''
# l=[1,2,3,4]
# it=iter(l)
# a=0
# while True:
#     try:
#         print(next(it))
#         a+=1
#     except StopIteration:
#         print(a)
#         break
# print('-'*50)
# student={
#     'name':'aadhya',
#     'age':24,
#     'branch':'eee'
# }
# k=iter(student)
# print(next(k))
# print(next(k))
# print(next(k))
# k=iter(student.items())
# print(next(k))
# print(next(k))
# print(next(k))
# k=iter(student.values())
# print(next(k))
# print(next(k))
# print(next(k))
# print('-'*50)
# student={
#     'name':'aadhya',
#     'age':9,
#     'branch':'eee'
# }
# def fun(data):
#     k=iter(data.items())
#     while True:
#         try :
#             print(next(k))
#         except StopIteration:
#             break
# fun(student)
# print('-'*50)
# iterators  work on mainly  preloaded values.
# l=[1,2,3]
# print(l[0])
# class Playlist:
#     def __init__(self,l):
#         self.lst=l
#         self.index=0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         # k=self.lst[self.index]
#         # self.index+=1
#         # return k
#         #   p1.lst[0]
#
#         if self.index<len(self.lst):
#             song=self.lst[self.index]
#             self.index+=1
#             return song
#         else:
#             raise StopIteration
#
#         # raise stopiteration gives below error in console in print(next(p))
#         # if this raise stopiteration is in  for loop autmoactically stops ,due to for loop know how to handle the stopiteration error .
# p1=Playlist(['Irumudi','Fear','Saiyara','Sunflower','Aaya Shear'])
# p2=Playlist(['Soura','Hukum','Return of the OG','Vikram Ost','Oorum Blood'])
# for i in p1:
    # i=iter(p1)
    # print(i)
#     print(next(i))
# p=iter(p1)
# print(next(p))
# print(next(p))
# print(next(p))
# print(next(p))
# print(next(p))
# print(next(p))

# for i in p1:
#     if i is None:
#         break
#     print(i)


# for i in p1:
#     print(i)

# print(next(p))
# print(next(p))
# print(next(p))
# print(next(p))
# print(next(p))
# print(next(p))
# print(next(p))
# print("-"*50)
# class Attendance:
#     def __init__(self,st):
#         self.students=st
#         self.roll_no=0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.roll_no<len(self.students):
#             name=self.students[self.roll_no]
#             self.roll_no+=1
#             return name
#         else:
#             raise StopIteration
# st1=Attendance(['Aadhi','Shiva','Parul','Balu'])
# st2=Attendance(['Parvati','navya','Pooja','Ashritha','Chinni'])
# for i in st1:
#     print(f'{i} : Present')
# for j in st2:
#     print(f'{j} : Present')
# print("-"*50)
# class Even:
#     def __init__(self,l):
#         self.lst=l
#         self.index=0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         # if self.index<self.len(self.l):
#         #     k=self.l[self.index]%2
#         #     self.index+=1
#         #     if k==0:
#         #         return n
#         # here internally we have to run a loop ,due to some elements not even .so to avoid None use another loop inside it
#         while self.index<(len(self.lst)-1):
#             self.index+=1
#             n=self.lst[self.index]
#             if n%2==0:
#                 return n
#         else:
#             raise StopIteration
# e=Even([1,2,3,4,5,6,7,8,9,10])
# for i in e:
#     print(i)
# class A:
#     def __init__(self,l):
#         self.l=l
#         self.index=0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.index < len(self.l):
#             k=self.l[self.index]
#             self.index+=1
#             return k
#         else:
#             raise StopIteration
#
# a1=A([1,2,3,4,5])
# for i in a1:
#     print(i)

# ----------8-08-2026-----------
# create a custom iterator that   takes a  whole sentence and return non vowels only?
# class Sentence:
#     def __init__(self,s):
#         self.s=s
#         self.index=0
#         self.k=['a','e','i','o','u','A','E','O','U','I']
#     def __iter__(self):
#         return self
#     def __next__(self):
#         self.index+=1
#         if self.index-1<len(self.s):
#             m=self.s[self.index-1]
#             if m not in self.k:
#                 return m
#             else:
#                 pass
#         else:
#             raise StopIteration
# s1=Sentence('My Frnd is @parul @Belongs to 408')
# for i in s1:
#     print(i,end=" ")
# in the above program if vowel is exist none is returned so while loop we should use

# class Sen:
#     def __init__(self,s):
#         self.s=s
#         self.i=0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         while self.i<len(self.s):
#             self.i+=1
#             if self.s[self.i-1] not in 'AEIOUaeiou':
#                 return self.s[self.i-1]
#             else:
#                 pass
#         # else:
#         #     raise StopIteration
#         raise StopIteration
# s1=Sen('My Frnd "Parul" name @Belongs to 408')
# for j in s1:
#     print(j,end=" ")
#'''char to ord'''
# class Sen:
#     def __init__(self,l):
#         self.s=l
#         self.i=0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         self.i+=1
#         if self.i>len(self.s):
#             raise StopIteration
#         k=ord(self.s[self.i-1])
#         return k
# s1=Sen('abcdefg')
# sum=0
# for i in s1:
#     sum+=i
#     print(i)
# print(sum)
    # print(i,end=" ")
# print()
# '''Cumulative Sum'''
# class Sen1:
#     def __init__(self,l):
#         self.s=l
#         self.i=0
#         self.sum=0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         self.i+=1
#         if self.i>len(self.s):
#             raise StopIteration
#         self.sum+=ord(self.s[self.i-1])
#         return self.sum
# d=Sen1('abcdef')
# # 97 98 99 100 101 102 103
# for i in d:
#     print(i)
print('-'*50)
# '''1. Write a custom iterator that prints numbers from 1 to N.'''
class A:
    def __init__(self,n):
        self.n=n
        self.k=0
    def __iter__(self):
        return self
    def __next__(self):
        while self.k<=self.n:
            self.k+=1
            return self.k
        else:
            raise StopIteration
a1=A(int(input()))
for i in a1:
    print(i)
print('-'*50)
# '''2. Create an iterator that returns only even numbers from a given list.'''
class Even:
    def __init__(self,l):
        self.l=l
        self.i=0
    def __iter__(self):
        return self
    def __next__(self):
        self.i+=1
        if (self.i-1)<len(self.l):
            if self.l[self.i-1]%2==0:
                return self.l[self.i-1]
            else:
               return  self.__next__()
        else:
            raise StopIteration
l1=Even([1,2,3,4,5,6,7,8,9,10])
for i in l1:
    print(i)
print('-'*50)
# # '''3. Implement an iterator that iterates over a string character by character in reverse order. '''
class String:
    def __init__(self,l):
        self.l=l
        self.i=-1
    def __iter__(self):
        return self
    def __next__(self):
        while self.i<(-len(self.l)):
            k=self.l[self.i]
            self.i-=-1
            return k
        else:
            raise StopIteration
s1=String('Pushpa Ante Flower🌺 anukuntiva , Firuuu!🔥')
for i in s1:
    print(i)
print('-'*50)
# '''4. Write an iterator that yields elements of a list with their index (don’t use enumerate).'''
class Enum:
    def __init__(self,l):
        self.i=0
        self.l=l
    def __iter__(self):
        return self
    def __next__(self):
        while self.i<len(self.l):
            k=self.l[self.i]
            self.i+=1
            return  self.i-1 , k
        else:
            raise StopIteration
l=Enum(['a','b','c','d','e'])
for i,j in l:
    print(i,j)
print('-'*50)
# '''5. Create an iterator that yields words from a sentence one by one.'''
class Sen:
    def __init__(self,s):
        self.s=list(s.split())
        self.i=0
    def __iter__(self):
        return self
    def __next__(self):
        self.i+=1
        while self.i<=len(self.s):
            print(self.i)
            return self.s[self.i-1]
        else:
            raise StopIteration
s1=Sen('aditya parul shiva sathtik hemanth')
for i in s1:
    print(i)
    # if len(i)>5:
        # print(i)
print('-'*50)
# '''6. Write an iterator that returns characters at even indices of a string.'''
class Even:
    def __init__(self,s):
        self.s=s
        self.i=0
    def __iter__(self):
        return self
    def __next__(self):
        while self.i<=len(self.s):
            self.i+=1
            if (self.i-1)%2==0:
                return self.s[self.i-1]
        else:
            raise StopIteration
e1=Even('asdfghjkl')
for i in e1:
    print(i)

