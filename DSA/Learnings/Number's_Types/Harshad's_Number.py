'''Write a program to print given number is Harshad Number or not
Harshad number is a number which exactly divisible by the sum of its digits
Constraints
Input :           First line of input contains Integer Value
Output :        Harshad Number or not
Constraints :If  the given Input is Zero Then Print "Zero".
                      If the input is negative then convert into Positive
Example
Input1   :     18
Output1  :   9
                   Harshad number
Input2   :     -144
Output2  :   9
                   Harshad number
Input3   :     113
Output3  :   5
                   not a Harshad number
Explanation
Input1 :          18
Output1 :       9
                       Harshad number
Explanation : 1+8=9, then 18 is divisible by 9 so 18 is Harshad number
Input2 :           -144
Output2 :        9
                        Harshad number
Explanation : 1+4+4=9, then 144 is divisible by 9 so 144 is Harshad number
Input3 :           113
Output3 :        5
                        not a Harshad number
Explanation : 1+1+3=5, then 113 is  not divisible by 5 so 113 is not a Harshad number'''
n=int(input())
m=0
if n==0:
    print("Zero")
else:
    if n<0:
        n*=-1
    k=n
    while n>0:
        r=n%10
        m=m+r
        n=n//10
    # print(m)
    n=k
    if n%m==0:
        print(m)
        print("Harshad number")
    else:
        print(m)
        print("not a Harshad number")