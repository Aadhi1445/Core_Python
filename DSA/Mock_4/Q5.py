'''
Write a Program to print the 'X' Percentage of 'Y' ?

Input:             First Line of the Input Consists of one Integer Value.

                       Second Line of the Input Consists of one Integer Value.

Output:          Print the Value of 'X' Percentage of 'Y'.
Constraints
• Both X and Y are positive integers.
Public examples
Sample 1
Input

20
250
Output

50.00
Sample 2
Input

15
500
Output

75.00
Sample 3
Input

25
81
Output

20.25
'''
x=int(input())
y=int(input())
print(f'{(x/100)*y:.2f}')