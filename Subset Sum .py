Subset Sum 
Given a set of non-negative integers, and a value S, determine if there is a subset of the given set with sum equal to S.



Input Format

The first line of the input contains T - the number of test cases. It is followed by 2T lines - the first line of each test case contains N - number of elements in given array and S - the required sum. The second line contains elements of the array.



Output Format

For each test case, print "YES" if there is a subset of the given set with sum equal to given S, otherwise "NO", separated by new line .



Constraints

30 points

1 <= N <= 10

0 <= S <= 100



120 points

1 <= N <= 100

0 <= S <= 1000



General Constraints

1 <= T <= 100

0 <= A[i] <= 103



Example

Input

2

5 15

10 4 5 9 1

5 17

13 11 19 20 21



Output

YES

NO



Explanation



Example 1:

15 = 9 + 5 + 1



Example 2:

No such subset exists.




# Enter your code here. Read input
def subs(arr,k):
    dp=[[False for i in range(k+1)] for j in range(len(arr)+1)]
    for i in range(len(arr)+1):
        dp[i][0]=True
    for i in range(1,len(arr)+1):
        for j in range(1,k+1):
            if j<arr[i-1]:
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=dp[i-1][j] or dp[i-1][j-arr[i-1]]
    return dp[len(arr)][k]

for _ in range(int(input())):
    a,b=map(int,input().split())
    arr=list(map(int,input().split()))
    if subs(arr,b):
        print("YES")
    else:
        print("NO")