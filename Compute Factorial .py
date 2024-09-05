Compute Factorial 
Given a number N, print N!.



Input Format

The first line of input contains T - number of test cases. It's followed by T lines, each containing a single number N.



Output Format

For each test case, print N!. Since the result can be very large, print N! % 1000000007 [1e9+7].



Constraints

1 <= T <= 106

0 <= N <= 106



Example

Input

3

5

20

50



Output

120

146326063

318608048



Explanation



Self Explanatory


# Enter your code here. Read 
dp=[0]*(1000000+1)
def fact(n):
    if n>=0:
        dp[0]=1
        for i in range(1,n+1):
            dp[i]=(i*dp[i-1])%1000000007
fact(1000000)
for _ in range(int(input())):
    n=int(input())
    print(str(dp[n]))