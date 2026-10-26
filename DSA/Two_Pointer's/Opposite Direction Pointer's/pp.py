# ''' Reversing an Array'''
# l = [10, 20, 30, 40, 50,60]
# lf=0
# rt=len(l)-1
# while lf<rt:
#     l[lf],l[rt]=l[rt],l[lf]
#     lf+=1
#     rt-=1
# print(l)
#
#
# ''' String is Palindrome or not'''
# s = "madam"
# l=0
# r=len(s)-1
# while l<r:
#     if s[l]!=s[r]:
#         print('Not a Palindrome')
#         break
#     l+=1
#     r-=1
# else:
#     print('Palindrome')
#

''' target sum of two numbers'''
l=[1,2,3,4,5,6,7,8,9]
k=8
lf=0
r=len(l)-1
while lf<r:
    sum=l[lf]+l[r]
    if sum==k:
        print(lf,r)
        print('Found')
        break
    elif sum<l[r]:
        lf+=1
    else:
        r-=1
else:
    print('Not Found')
