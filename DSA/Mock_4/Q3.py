'''
Write a program to check whether the given number is Keith Number or not .

Constraints
Input :            First line input consists of one integer value.

output :         Print Keith Number or Not a Keith Number.
Constraints
Given Input must contain atleast two digits or else print "Invalid Input"
Public examples
Sample 1
Input

14
Output

Keith Number
Explanation: 1 + 4 =5 4 +5 = 9 5 + 9 = 14. which is equal to given number. So 14 is Keith Number.

Sample 2
Input

742
Output

Keith Number
Explanation: 7 + 4 + 2 =13 4 + 2 + 13 = 19 2 + 13 + 19 = 34 13 + 19 + 34 = 66 19 + 34 + 66 = 119 34 + 66 + 119 = 219 66 + 119 + 219 = 404 119 + 219 + 404 = 742. Which is equal to given number . So 742 is a Keith Number.

Sample 3
Input

25
Output

Not a Keith Number
Explanation: 2 + 5 =7 5 + 7 = 12 7 + 12 = 19 12 + 19 = 31.Which is not equal to given number . So 25 is not a Keith Number.
'''


n=int(input())
n1=str(n)
l=[]
for i in n1:
    l.append(i)
if len(n1)<2:
    print("Invalid Input")
else:
    s=0
    def fun(n1):
        sum=0
        for i in n1:
            sum+=int(i)
        return sum
    def repeat(l,s):
        l.append(str(s))
        l.pop(0)
        return l
    while s<=n:
        if s==n:
            print('Keith Number')
            break
        else:
            s=fun(l)
            l=repeat(l,s)
    else:
        print('Not a Keith Number')