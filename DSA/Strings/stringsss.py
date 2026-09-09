# '''1 Write a program to find the length of a string using the len() function.'''
# s='sdfgh'
# print('Length of s: ',len(s))
# '''2 Write a program to display the ASCII value of each character in the given string.'''
# s='dfghj'
# for i in s:
#     print(f'Asscii value of {i} = {ord(i)}')
# '''3 Write a program to convert a string to uppercase using string methods.'''
# s='asdfghj'
# print(s.upper())
# s='SDFGH'
# print(s.upper())
# s='ASdfgh2345'
# print(s.upper())
# '''4 Write a program to convert a string to lowercase using string methods.'''
# s='ASDFGH567asd'
# print(s.lower())
# print(s)
# ''' 5 Write a program to check whether the given string contains only alphabets '''
# s='sdfghjkSDFGHJ'
# print(s.isalpha())
# s='sdfgh34jkSDFGHJ'
# print(s.isalpha())
# '''6 Write a program to check whether the given string contains only digits '''
# s='234567'
# print(s.isdigit())
# s='2345dfg67'
# print(s.isdigit())
# '''7 Write a program to check whether the given string contains only alphabets and numeric characters '''
# s='dfg23456DFGH'
# print(s.isalnum())
# s='dfg2345@#6DFGH'
# print(s.isalnum())
# '''8 Write a program to replace all spaces in a string with hyphens (-) using string methods. '''
# s='df asdf sdfg'
# k=s.replace('','-')
# print(k)
# s='df asdf sdfg'
# k=s.replace(' ','-')
# print(k)
# s=''
# k=s.replace('','-')
# print(k)
# 17 Write a program to check whether a given substring exists in a string.'''
# s='GuttulaAditya'
# ss='tu'
# # print(ss.)
# for i in range(0,(len(s)-len(ss))+1):
#     w=s[i:i+(len(ss))]
#     # print('w:',w)
#     if w==ss:
#         print('Found')
#         break
# else:
#     print("Not Found")
# '''18 Write a program to find the index of a given character in a string. '''
# s='AdityaGuttula'
# ch='G'
# for i in range(0,len(s)):
#     if ch==s[i]:
#         print('Found',s[i],'->',i)
#         break
# else:
#     print("Not Found")
# '''19 Write a program to count the occurrences of a specific character in a string. '''
# s='AdityaGuttula'
# sp='a'
# c=0
# for i in s:
#     if i==sp:
#         c+=1
# print(c)
# '''20 Write a program to search for a word in a sentence and display whether it is present. '''
# s='I am Learning Python. I Love Python'
# w='Python'
# s=s.split()
# print(s)
# for i in s:
#     if i==w:
#         print('Found:',w)
#         break
# else:
#     print('Not Found',w)
# '''21 Write a program to extract all digits from a given string'''
# s='aditya324nbsf68uu0'
# for i in s:
#     if i >='0' and i<='9':
#         print(i,end=" ")
# '''Case Conversions
# 22 Write a program to count the number of uppercase and lowercase letters in a string. '''
# s='ASgh34SDFcvbWERfgh9876'
# up=lc=0
# for i in s:
#     if i >='A' and i <='Z':
#         up+=1
#     elif i>='a' and i<='z':
#         lc+=1
# print('up:',up, 'lc:',lc)
# '''23 Write a program to separate alphabets, digits, and special characters from a string.'''
# s='ASDsdfg345@*^%$'
# a=d=spc=''
# for i in s:
#     if i.lower()>='a' and i.lower()<='z':
#         a+=i
#     elif i>='0' and i<='9':
#         d+=i
#     else:
#         spc+=i
# print('alphabets:',a, '   Digits:',d, '   spc:',spc)

