Collect Apples 
You are given a maze containing cells. Each cell has certain number of apples. You have to start from the top-left position and traverse all the way to the bottom-right position, collecting apples on your way. You can move only in right and downward direction, i.e., from any cell (i,j) you can only move right: (i,j+1) or down: (i+1,j). Find the maximum number of apples you can collect.



Input Format

The first line of input contains T - number of test cases. First line of each test case contains N and M - the size of the maze. It is followed by N lines, each containing M integers indicating the number of apples in the cell.



Output Format

For each test case, print the maximum number of apples you can collect, separated by new line.



Constraints

1 <= T <= 100

1 <= N,M <= 300

0 <= Aij <= 100



Example

Input

2

3 4

1 5 1 4

10 11 0 13

4 15 1 12

4 2

4 5

1 3

10 5

1 0



Output

50

20



Explanation



Example 1:

The path using which you can collect maximum apples is highlighted below:

1 5 1 4

10 11 0 13

4 15 1 12

Total Apples = 1 + 10 + 11 + 15 + 1 + 12 = 50



Example 2:

The path using which you can collect maximum apples is highlighted below:

4 5

1 3

10 5

1 0

Total Apples = 4 + 1 + 10 + 5 + 0 = 20





# Enter your code here. Read inp
def find(ar):
    dp=[[0 for x in range(len(ar[0])+1)] for x in range(len(ar)+1)]
    dp[0][0]=ar[0][0]
    for i in range(1,len(ar[0])):
        dp[0][i]=dp[0][i-1]+ar[0][i]
    for i in range(1,len(ar)):
        dp[i][0]=dp[i-1][0]+ar[i][0]
    for r in range(len(ar)):
        for c in range(len(ar[0])):
            dp[r][c] = max(dp[r-1][c] , dp[r][c-1])+ar[r][c]
    return dp[len(ar)-1][len(ar[0])-1]

for _ in range(int(input())):
    r,c=list(map(int,input().split()))
    ar=[]
    for _ in range(r):
        ar.append(list(map(int,input().split())))
    print(find(ar))
