'''
Write a program to check whether the Given Number is Fascinating Number or not?

Fascinating Number: When a number( 3 digits or more ) is multiplied by 2 and 3, and when both these products are concatenated with the original number, then it results in all digits from 1 to 9 present exactly once. There could be any no of zeros and are ignored.


Input :                    First line consists of one integer value

Output :                 Print Fascinating Number or Not a Fascinating Number
Constraints
Given input must not equal to zero or else print "Invalid Input".

Given Input is less than 100 then print "Invalid Input".

If the given input is negative then convert it into positive.
Public examples
Sample 1
Input

192
Output

Fascinating Number
Explanation: 192 * 2 = 384 and 192 * 3 = 576 after concatinating the values we get 192384576 which contain all the digits from 1-9 exactly once. So it is a Fascinating Number.

Sample 2
Input

2019
Output

Fascinating Number
Explanation: 2019 * 2 = 4038 and 2019 * 3 = 6057 after concatinating the values we get 201940386057 which contain all the digits from 1-9 exactly once. So it is a Fascinating Number. Here zeros are ignored.
'''

n=int(input())
n1=str(n)
if n<0:
    n1=n1[1:len(n1)]
if n==0 or len(n1)<3:
    print('Invalid Input')
else:
    n=abs(n)
    t= str(n*2)
    th=str(n*3)
    k=n1+t+th
    d={}
    for i in k:
        if i in d and i!='0':
            print("Not a Fascinating Number")
            break
        else:
            d[i]=1
    else:
        print('Fascinating Number')