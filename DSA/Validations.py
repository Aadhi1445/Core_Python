'''Validations'''
# ''' 13 Write a program to validate an Aadhaar number based on its length and digit rules. '''
# s='703639835623'
# if len(s)==12 and s.isdigit():
#     print("Valid Aadhaar Number")
# else:
#     print("Invalid Aadhaar Number")
# # l=input("Enter the Aadhar Number in xxxx xxxx xxxx format:")
# # if len(l)==14 and l[4]==' ' and l[9]==" " and l[:4].isdigit() and l[5:9].isdigit() and l[10:14].isdigit():
# #     print("Valid Aadhaar Number")
# # else:
# #     print("Invalid Aadhaar Number")
# '''14 Write a program to validate a PAN card number using its format rules. '''
# # '''Total length = 10 characters 0123456789
# # First 5 characters must be uppercase English letters (A-Z)
# # Next 4 characters must be digits (0-9)
# # Last character must be an uppercase English letter (A-Z)
# # No spaces or special characters in the standard PAN representation.'''
# # l=input('Enter the Pan Number:')
# l='asdfg1234h'
# l=l.upper()
# c=0
# if len(l)!=10:
#     print("Invalid Length")
# else:
#     for i in range(len(l)):
#         if i in (0,1,2,4,(len(l)-1)) and l[i]>='A' and l[i]<='Z':
#             c+=1
#         elif i==3 and l[i] in ('P','C','H','F','A','T','B','L','J','G'):
#             c+=1
#         elif i in (5,6,7,8) and l[i]>='0' and l[i]<='9':
#             c+=1
#         elif l[i]!=' ':
#             print("Invalid PanCard")
#             break
#     if c==10:
#         print("Valid Pan card")
#     else:
#         print("Invalid Pan Card")

# if len(l)==10 and (l[:5].isupper() and l[:5].isalpha()) and (l[5:9].isalnum()) and l[-1].isalpha()and l[-1].isupper():
#     print("Valid pan Number")
# else:
#     print("Invalid pan Number")
# '''15 Write a program to validate a Gmail ID using string conditions.
# . Username constraints:
# Can contain letters (a-z)
# Can contain digits (0-9)
# Can contain periods (.)
# Must be 1–30 characters for Gmail usernames.
# Cannot contain spaces.
# Cannot contain characters such as #, $, %, &, etc.
# It cannot begin or end with a period.
# It cannot contain consecutive periods such as:
# abc..def@gmail.com'''
# # l='aditya965258@gmail.com'
# # l.lower()
# # n,m=l.split('@')
# # if n.isalnum() and m=='gmail.com':
# #     print("Valid Gmail Address")
# # else:
# #     print("Invalid Gmail Address")
# l=list(map(lambda x:x.lower(),input().split('@')))
# if l[0].isalnum() and l[1]=='gmail.com':
#     print("Valid Gmail Address")
# else:
#     print("Invalid Gmail Address")


'''
Constraints:
    ID@Domain.Extension
    Email id Must starts with Alphabet, 
    ld Consists of Capital Letters, Small Letters, Digits, dot(.) and Underscore( _) Only
    Id Doesn't Starts with dot(, ) or Underscore( _) and Doesn't Ends with dot(.) or Underscore(_)
    After ld @ Symbol Must
    Domain May consists of Alphabets and Digits Ony
    After Domain Dot( , ) Symbol Must
    Extension May Consists of only Alphabets
    Email Id Must Consists of 15 to 25 Characters Ony1n5 <- Length <=25)'''

n='aditYa965258@gmailcom'
a=n.find('@')
print(a)
b=n.find('.',a)
print(b)
a1=n[0:a]
print(a1)
b1=n[a+1:b]
print(b1)
c1=n[b+1:len(n)]
print(c1)
g=True
if a!=-1 and b!=-1:
    if 15<=len(n)<=25 and (n[0]>='A' and n[0]<='Z') or (n[0]>='a' and n[0]<='z'):
        print(1)
        # a=b=c=d=e=True
        if g and(a1[len(a1)-1]!='.' and a1[len(a1)-1!='_']):
            print(2)
            for i in a1:
        #         ld Consists of Capital Letters, Small Letters, Digits, dot(.) and Underscore( _) Only
                if i>='A' and i<='Z':
                    pass
                elif i>='a' and i<='z':
                    pass
                elif  i>='0' and i<='9':
                    pass
                elif i=='.' :
                    pass
                elif i=='_':
                    pass
                else:
                    print('Invalid 2')
                    g=False
                    break
            print('g:',g, 'n[a]:',n[a])
        if  g and n[a]=='@':
            print(3)
            b1.lower()
            for i in b1:
                if i>='a' and i<='z':
                    pass
                elif i>='0' and i<='9':
                    pass
                else:
                    print('Invalid 3')
                    g = False
                    break
        if g and n[b]=='.' :
            print(4)
            c1.lower()
            for i in c1:
                if i>='a' and i<='z':
                    pass
                else:
                    print('Invalid 4')
                    g = False
                    break
        if  g:
            print(5)
            print('valid')
        else:
            print(6)
            print('Invalid 6')
    else:
        print(7)
        print('Invalid 7')
else:
    print('Invalid')

























# '''6 Write a program to validate a password based on length, uppercase, lowercase, digit, and special character rules.
# lenght:10'''
# l='mouni'
# a=b=c=d=e=0
# if len(l)>=8 and len(l)<=16:
#     for i in l:
#         if i.isdigit():
#             a+=1
#         elif i.isupper():
#             b+=1
#         elif i.islower():
#             c+=1
#         elif i in "!@#$%^&*()-_=+[]{};:'\",.<>?/\\|`~":
#             d+=1
#         elif i.isspace():
#             e+=1
#     if a>0 and b>0 and c>0 and d>0 and e==0:
#         print("Valid Password")
#     elif a>0 and b>0 and c>0 and d>0 and e!=0:
#         print("Password Shouldn't contain Spaces")
#     elif a>0 and b>0 and c>0:
#         print('Password Should contain atleast one special Character and No Spaces')
#     elif a>0 and b>0:
#         print("Password Should contain atleast one Lower case Letter,No Spaces and one special Character")
#     elif a>0:
#         print("Password Should contain atleast one Upper case Letter,one Lower case Letter,No Spaces and one special Character")
# else:
#     print("Password Length Should be in between 8 &1 6")
#
# print('-'*50)
# check(())
# check(())
# '''CONSTRAINTS
# print Valid Password or Not a Valid Password.
# Constraints:
# Password Must be consists of 8 Characters
# Password Must be Starts with Capital Character
# Password Must be consists of atleast one small Character
# Password Must be consists of atleast one Special Character
# Password Must be consists of atleast one Numerical Value
# Password Must not be consists of Given Name (Either Small or Capital Characters)
# If Above constraints is not Satisfy then print Not a Valid Password or
# else if satisfies print Valid Password.'''
# p='Aditya@1445'
# n='dfghm'
# if len(p)>=8 and p[0].isupper() and n.lower() not in p.lower() :
#     a=b=c=d=False
#     for i in p:
#         if i.islower():
#             a=True
#         elif i.isdigit():
#             c=True
#         elif  not (i.isalnum() and i.isspace()):
#             b=True
#     if a and b and c:
#         print('Valid Password')
#     else:
#         print("Invalid Password ")
# else:
#     print('Invalid Password')


# a='a2'
# print(a.isalnum())