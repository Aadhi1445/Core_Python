# '''1.Write a function square(n) that returns the square of a number.
# Pass it as an argument to another function calculate() and display the result.'''
# def sq(n):
#     # print(1)
#     return n*n
# def cal(x):
#     # print(2)
#     return sq(x)
# print(cal(3))
# '''2.Create a function greet(name) and pass it as an argument to another function that calls it.'''
# def  greet(name):
#     print(1)
#     print(name)
# def fun(x):
#     print(2)
#     greet(x)
# fun('Aditya')
# '''3.Write a higher-order function that accepts a function and a number,
# then applies the function to the number.'''
# def sq(n):
#     return n*n
# def fun1(sq,n):
#      return sq(n)
# print(fun1(sq,4))
# '''4.Create a function operate(a, b, operation)
# where operation can be addition, subtraction, multiplication, or division.'''
# def op(a,b,operation):
#     if operation=='+':
#         return a+b
#     elif operation=='-':
#         return a-b
#     elif  operation=='*':
#         return a*b
#     else:
#         return a%b
# k=op(5,3,'*')
# print(k)
# '''5.Write a function that returns another function.
# The returned function should multiply a number by 10'''
# def fun():
#     def multiply(x):
#         return x*10
#     return multiply
# k=fun()
# print(k(5))
'''Map'''
# l=[1,2,3,4,5]
# def sq(x):
#     return x**2
# # k=list(map(lambda x:x**2,l))
# # print(k)
# l1=[]
# for i in l:
#     l1.append(sq(i))
# print(l1)
'''Filter'''
# num= [10, 15, 20, 25, 30, 35]
# # # print(list(filter(lambda x:x%2==0,num)))
# # num1=[]
# def even(x):
#     if x%2==0:
#         return x
# # for i in num:
# #     num1.append(even(i))
# # print(num1)
# k=list(filter(even,num))
# print(k)
# names = ["aditya", "satwik", "sai", "hemanth"]
# # k=list(map(lambda x:x.upper(),names))
# # print(k)
# def upp(x):
#     return x.upper()
# k=list(map(upp,names))
# print(k)
numbers = [20, 65, 40, 80, 35, 90]
# # k=list(filter(lambda  x:x>50,numbers))
# # print(k)
# def gt(x):
#     return x>50
# k=list(filter(gt,numbers))
# print(k)
'''Reduce'''
from functools import reduce
# numbers = [20, 65, 40, 80, 35, 90]
# # k=reduce(lambda x,y:x+y,numbers,20)
# # print(k)
# # k=reduce(lambda x,y:x+y,numbers)
# # print(k)
# def add(x,y):
#     # x=x+y
#     return x+y
# k=reduce(add,numbers)
# print(k)

# numbers = [15, 45, 12, 78, 34]
# k=reduce(lambda x,y:x if x>y else y, numbers)
# print(k)

'''Combinations'''
# words = ["Python", "Java", "SQL", "HTML"]
# k=list(map(lambda x:len(x),words))
# print(k)
# def ln(x):
#     return len(x)
# k=list(map(ln,words))
# print(k)
# names = ["Aditya", "Sai", "Hemanth", "Ravi", "Satwik"]
# def ln(x):
#     return len(x)>5
# k=list(filter(ln,names))
# print(k)

# numbers = [1, 2, 3, 4, 5, 6]
# k=list(map(lambda x:x**2,filter(lambda x:x%2==0,numbers)))
# print(k)

employees = [
    ("Aditya", 60000),
    ("Satwik", 45000),
    ("Sai", 30000),
    ("Hemanth", 25000)
]
# print(employees[0][1])
# def fun(x):
#     return x[1]+(x[1]*0.10)
# k=list(map(lambda x:x[1]+(x[1]*0.10),employees))
# print(k)
# k=list(map(fun,employees))
# print(k)
# def fun(x,y):
#     return x*y
# salaries=list(map(lambda x:x[1],employees))
# k=reduce(fun,salaries)
# print(k)
# '''Create your own higher-order function my_filter() that
# behaves similarly to Python's filter() without using the built-in filter().'''
# # ex: even numbers
# def my_filter(func,data):
#     result=[]
#     for i in data:
#         if func(i):
#             result.append(i)
#     return result
# def even(x):
#     return x%2==0
# l=[1,2,3,4,5,6,7]
# print(my_filter(even,l))
# '''Create a function create_multiplier(n) that returns a function. For example:
# double = create_multiplier(2)
# triple = create_multiplier(3)
# Then use them to double and triple numbers'''
# def create_multiplier(n):
#     def multiply(x):
#         return x*n
#     return multiply
# double=create_multiplier(10)
# tripple=create_multiplier(20)
# print(double(2))
# print(tripple(3))

# numbers = [10, 15, 20, 25, 30, 35, 40]
# k=list(map(lambda x:x*x,filter(lambda x:x%2==0,numbers)))
# print(k)

# from functools import reduce
# def employees(*z):
#     # k=reduce(lambda x,y:x if x>y else y,z) --- python comapres alphabets order
#     k=reduce(lambda x,y:x if x[1]>y[1] else y,z)
#     print(k)
# employees(('Aadhya',20000),('Paaru',30000),('Siva',40000),('Satwik',60000))





