# '''Reversing
# 24 Write a program to reverse a string using a loop.'''
# s='asdfghj'
# # rev=''
# # # print(s[::-1])
# # for i in s:
# #     rev=i+rev
# # print(rev)
# rev=[]
# for i in range(len(s)-1,-1,-1):
#     rev.append(s[i])
# print("".join(rev))
# '''25 Write a program to check whether a string is a palindrome.'''
# s='asddsa'
# k=len(s)//2
# if k%2==0:
#     for i in range(k-1,-1,-1):
#         if s[i]!=s[k+1]:
#             print("Not a Palindrome")
#             break
#         k+=1
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
'''26 Write a program to reverse each word in a given sentence.'''
s='my  name is aditya, i '
'''27 Write a program to check whether one string is a rotation of another string.
Frequency
28 Write a program to print the frequency of each character in a string.
29 Write a program to find the second most frequent character in a string. 
30 Write a program to remove duplicate characters from a string. 
31 Write a program to check whether two strings are anagrams. 
SubStrings 
32 Write a program to print all the substrings of the given string 
33 Write a program to find the word with the maximum number of vowels. '''
