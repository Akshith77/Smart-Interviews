Compute nCr 
Given n and r, compute nCr.



Note:

Do not use BigInteger class, it defeats the purpose of the problem statement.



Input Format
The first line of input contains T - number of test cases. It is followed by T lines, each line contains 2 integers - N and R.



Output Format

For each test case, print the value of nCr, separated by new line. Since the number can be very large, print result % 1000000007.



Constraints

20 points

1 <= T <= 100

0 <= N, R <= 30



80 points

1 <= T <= 500000

0 <= N, R <= 2000



Example

Input

5

4 2

3 1

25 12

30 14

6 4



Output

6

3

5200300

145422675

15



Explanation



Self Explanatory



# Enter your code here. Read input from S
def ncr(n,r):
    dp=[[0 for i in range(r+1)] for i in range(n+1)]
    for i in range(n+1):
        for j in range(min(i,r)+1):
            if j==0 or j==i:
                dp[i][j]=1
            else:
                dp[i][j]=dp[i-1][j-1]+dp[i-1][j]%1000000007
    return dp
s=ncr(2000,2000)
for _ in range(int(input())):
    n,r=map(int,input().split())
    print(s[n][r]%1000000007)