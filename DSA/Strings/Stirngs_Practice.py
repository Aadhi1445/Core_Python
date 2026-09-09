# '''Reversing
# 24 Write a program to reverse a string using a loop.'''
# s='asdsa'
# rev=''
# # print(s[::-1])
# for i in s:
#     rev=i+rev
# if rev==s:
#     print('Palindrome')
# else:
#     print(' not Palindrome')

# rev=[]
# for i in range(len(s)-1,-1,-1):
#     rev.append(s[i])
#     print(rev)
# print("".join(rev))
# '''25 Write a program to check whether a string is a palindrome.'''
# s='asddsa'
# k=len(s)//2
# if k%2==0:
#     for i in range(k-1,-1,-1):
#         if s[i]!=s[k+1]:
#             print("Not a Palindrome")
#             break
#         k+=18
#     else:
#         print("Palindrome")
# else:
#     for i in range(k - 1, -1, -1):
#         if s[i] != s[k]:
#             print("Not a Palindrome")
#             break
#         k += 1
#     else:
#         print("Palindrome")
# # # s='23432'
# # s='23456'
# # rev=[]
# # for i in range(len(s)-1,-1,-1):
# #     rev.append(s[i])
# # rev="".join(rev)
# # # print(rev)
# # if rev==s:
# #     print("Palindrome")
# # else:
# #     print('Not a Palindrome')
# # # s='234432'
# # s='234431'
# # k=len(s)//2
# # for i in range(k-1,-1,-1):
# #     if s[i]!=s[k]:
# #         # print(s[i],s[k+i])
# #         print('Not a Palindrome')
# #         break
# #     k=k+1
# # else:
# #     print("Palindrome")
# # # s='12321'
# # s='16321'
# # k=len(s)//2
# # # print(k)
# # for i in range(k-1,-1,-1):
# #     if s[i]!=s[k+1]:
# #         # print(s[i],s[k+1])
# #         print('Not aPalindrome')
# #         break
# #     k+=1
# # else:
# #     print('Palindrome')
#
#
# # 234432--234--342
# # 23432--23--32
# '''26 Write a program to reverse each word in a given sentence.'''
# s='my name is aditya '
# s=s.split()
# l=[]
# for i in s:
#     b=''
#     # print(i)
#     for j in range(len(i)-1,-1,-1):
#         # print('j:',j)
#         b=b+i[j]
#         # print('b:',b)
#     l.append(b)
#     # print(l)
# print(l)
# '''27 Write a program to check whether one string is a rotation of another string.'''
# s='12345'
# # print(type(s))
# # print(type(s[0]))
# l=s
# rs='54123'
# # print(s)
# for i in range(len(s)):
#     ss = ''
#     k=s[len(s)-1]
#     ss=''
#     ss=ss+k
#     # print(k)
#     for j in range(1,len(l)):
#         # print(type(s[j]))
#         # print(s[j])
#         print(j)
#         ss=ss+ss[j]
#     print(ss)
#     l = ss
'''Frequency
28 Write a program to print the frequency of each character in a string.
29 Write a program to find the second most frequent character in a string. 
30 Write a program to remove duplicate characters from a string. 
31 Write a program to check whether two strings are anagrams. 
SubStrings 
32 Write a program to print all the substrings of the given string 
33 Write a program to find the word with the maximum number of vowels. '''
