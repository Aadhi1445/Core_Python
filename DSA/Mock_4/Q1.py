'''
A Tournament is happening in CvCorp So here C No of Players is Playing Cricket Match and R No of Matches played So take the Scores in 2D Array And
        Print the Highest Scorer in Every Match and Print the Highest Scorer in All Matches?

Input     : First Line of The Input Consists of One Integer Value Which Represents No of Matches

                        And Next Line Consists of Match -1 Scores of All Players and in Next Line Consists of Match -2 Scores of All Players
                            and so on for All R No of Matches

                        Each line of input represents Player one score and player two score and player three score and sooo on

Output         : Print the Highest Scorer Name And Score In Each and Every Match Separately after that Print the Highest Individual Scorer in All Matches.
Public examples
Sample 1
Input
3
3 5 6
7 8 9
12 15 12
Output
Player3 - 6
Player3 - 9
Player2 - 15
Player2 - 28
Sample 2
Input
5
2 15 12 13
8 5 0 19
18 17 4 7
9 18 4 19
15 14 13 2
Output
Player2 - 15
Player4 - 19
Player1 - 18
Player4 - 19
Player1 - 15
Player2 - 69
Sample 3
Input
2
10 20 30
40 50 60
Output
Player3 - 30
Player3 - 60
Player3 - 90
'''
n=int(input())
nl=[]
sum1=0
for i in range(n):
    nl.append(list(map(int,input().split())))
for i in range(len(nl)):
    m=float("-inf")
    sum=0
    for j in range(len(nl[i])):
        if nl[i][j]> m:
            m=nl[i][j]
            sum+=nl[i][j]
            k=j
    print(f'Player{k+1} - {m}')
for i in range(len(nl[0])):
    sum=0
    for j in range(len(nl)):
        # print(j,i)
        # print('i :',i)
        # if
        sum+=nl[j][i]
    if sum1<sum:
        sum1=sum
        k1=i+1
print(f"Player{k1} - {sum1}")


