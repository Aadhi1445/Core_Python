# ''' Same-direction pointers'''
# l=[1,2,2,3,4,4,5]
# w=0
# for i in range(1,len(l)):
#     if l[i]!=l[w]:
#         w+=1
#         l[w]=l[i]
#     # print(l)
# print(l[:w+1])
#
#
#
#
# numbers = [0, 1, 0, 3, 12]
# write = 0
# for read in range(len(numbers)):
#     if numbers[read] != 0:
#         numbers[write], numbers[read] = numbers[read], numbers[write]
#         write += 1
# print(numbers)



''' Moving Even elements to Starting of List  and Odd Numbers To Ending Of List'''

l=[1,2,3,2,5,8,5,9,2]
left=0
right=len(l)-1
while left<right:
    while left <right and l[left]%2==0:
        left+=1
    while left<right and l[right]%2==1:
        right-=1
    if left<right:
        l[left],l[right]=l[right],l[left]
        left+=1
        right-=1
print(l)
