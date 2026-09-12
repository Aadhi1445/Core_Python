#
# Generators: A special type of function which doesn't return everything at once and which uses "yield" keyword'
'''1. Write a generator that yields digits from an integer one by one. '''
def fun(n):
    while n>0:
        r=n%10
        yield r
        n=n//10
    # else:
    #     raise StopIteration
    #     in the above ,generator doesn't raise error explicitly.
k=fun(456)
print(next(k))
print(next(k))
print(next(k))
for i in k:
    print(i)
print()

g=fun(456)
for i in g:
    print(i)
print('-'*50)
'''2. Create a generator that yields cumulative sum of numbers in a list. Example: [1,2,3] → 1, 3, 6 '''
def fun(l):
    i=0
    sum=0
    while i<len(l):
        sum+=l[i]
        yield sum
        i+=1
k=fun([1,2,3,4,5])
for i in k:
    print(i)
print('-'*50)
'''3. Implement a generator that yields vowels from a string.'''
def fun(l):
    i=0
    while i<len(l):
        i+=1
        # k=['a','e','i','o','u']
        k='aeiou'
        if l[i-1].lower() in k:
            yield l[i-1]
            # i+=1
k=fun('asdfgeihjk')
for j in k:
    print(j)
print('-'*50)
'''4. Implement a generator that yields running maximum from a list 
Example: [3,1,4,2] → 3, 3, 4, 4'''
def fun(l):
    i=0
    s=min(l)
    while i<len(l):
        # print(i)
        i += 1
        if l[i-1]>s:
            s=l[i-1]
            yield s
        else:
            yield s

    # else:
    #     raise StopIteration
d=fun([2,1,4,7,1,9])
for i in d:
    print(i)
print('-'*50)
'''5.	Write a generator that yields numbers from 1 to N.'''
def fun(k):
    i=0
    while i<k:
        i+=1
        yield i

a=fun(10)
for i in a:
    print(i)
print('-'*50)
'''6.	Write a generator that yields even numbers from 1 to N'''
def even(k):
    i=2
    while i<=k:
        if i%2==0:
            yield i
        i+=1
a=even(10)
for i in a:
    print(i)
print('-'*50)
def even(k):
    i=2
    while i<=k:
        if i%2==0:
            print(i)
        i+=1
a=even(10)
print('-'*50)
'''7.	Write a generator that yields each character of a string.'''
def string(s):
    i=0
    while i<len(s):
        yield s[i]
        i+=1
s1=string('asdfghjklqsdcv')
for i in s1:
    print(i)
print('-'*50)
'''4.	Write a generator that yields characters of a string in reverse order.'''
def reverse(s):
    i=-1
    while i>=(-len(s)):
        yield s[i]
        i=i-1
r1=reverse('asdfghjkl')
for i in r1:
    print(i)
print('-'*50)
'''6.	Write a generator that yields only digits present in a string.'''
def digits(k):
    i=0
    while i<len(k):
        if k[i] in '1234567890':
            yield k[i]
        i+=1
a=digits('as345hgfd34')
for i in a:
    print(i)
print('-'*50)
'''7.	Write a generator that yields the square of each element in a list.'''
def square(l):
    i=0
    while i<len(l):
        yield l[i]*l[i]
        i+=1
s1=square([1,2,3,4,5,6,7,8,9])
for i in s1:
    print(i)