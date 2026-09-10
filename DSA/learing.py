'''Write a Program to check Whether the Given Number is a Pointer Prime Number or Not?
Constraints
Given Input must be Greater than zero or else print "Invalid Input."
Explanation
Find the product of digits of N.
Then, find the next prime number to N.
Now, if N is prime and N + product of digits of N equals the next prime to N. Then, N is a pointer prime number.

Input 1:     23
Output 1:  23 is a Pointer Prime Number
Explanation :
23 is Prime then,
Product of digits of 23 = 2 * 3 = 6.
Add that value with to the original number 23 + 6= 29.
The prime number which is next to the 23 number is 29.
As we notice here, both the calculated number and the next prime number are the same.
Hence, 23 is a pointer prime number.

Input 2:     149
Output 2:  149 is Not a Pointer Prime Number
Explanation :
149 is Prime then,
Product of digits of 149 = 1 * 4 * 9 = 36.
Add that value with the original number 149 + 36= 185.
The actual prime number which is next to the 149 number is 151.
As we notice here the calculated number is not a prime number.
Hence, 149 is not a pointer prime number.

Input 3:    1321
Output 3:   1321 is a Pointer Prime Number
Explanation :
1321 is Prime then,
Product of digits of 1321 = 1 * 3 * 2 * 1 = 6.
Add that value with the original number 1321 + 6= 1327.
The actual prime number which is next to the 1321 number is 1327.
As we notice here, both the calculated number and the next prime number are the same.
Hence, 1321 is a pointer prime number.'''
n=23
k=1
for i in str(n):
    k=k*int(i)
# print(k)
sum=n+k
# print(n1)
m=n
g=True
while g:
    m+=1
    # print('m:',m)
    for i in range(2,m):
        if m%i==0:
            # g=False
            break
    else:
        g=False
if sum==m:
    print('Pointer Prime')
else:
    print('Not Pointer prime')































# n=24
# g=True
# while g:
#     for i in range(2,n):
#         if n%i==0:
#             break
#     else:
#         g=False
#         print(n)
#     n=n+1