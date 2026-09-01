# k=lambda a, b: a + b
# print(k(2,6))


# def my_decorator(func):
#     def wrapper():
#         print("--- Before the function runs ---")
#         func()  # call the original function
#         print("--- After the function runs ---")
#
#     return wrapper  # return wrapper, not wrapper()
#
#
# def say_hello():
#     print("Hello, World!")
#
#
# say_hello = my_decorator(say_hello)  # manual decoration
# say_hello()  # manual decoration
l=[0,1,2,3,4,5,6,7,8]
print(l[-5:1:-1])
print(l[-5:7:-1])
print(l[-5:6:-1])
print(l[-5:5:-1])
print(l[-5:4:-1])
print(l[-5:4:1])
print("--")
print(l[-5:5:1])
print(l[-5:6:1])
print(l[-5:7:1])
print('--')
print(l[5:-7:1])
print(l[5:-7:-1])


'''CONSTRAINTS
print Valid Password or Not a Valid Password.
Constraints:
Password Must be consists of 8 Characters
Password Must be Starts with Capital Character
Password Must be consists of atleast one small Character
Password Must be consists of atleast one Special Character
Password Must be consists of atleast one Numerical Value
Password Must not be consists of Given Name (Either Small or Capital Characters)
If Above constraints is not Satisfy then print Not a Valid Password or 
else if satisfies print Valid Password.'''
p='Aditya@1445'
n='aditya'
u=l=sp=d=False
if len(p)>=8 and p[0].isupper() and n.lower() not in p.lower():
    for i in p:
        if i.isupper():
            u=True
        elif i.islower():
            l=True
        elif i.isdigit():
            d=True
        else:
            sp=True
    if u and l and sp and d:
        print("valid password")
    else:
        print("not valid")
else:
    print("not valid")