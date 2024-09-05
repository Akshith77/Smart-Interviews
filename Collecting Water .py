Collecting Water 
You are given the heights of N buildings. All the buildings are of width 1 and are adjacent to each other with no empty space in between. Assume that it is raining heavily, and as such water will be accumulated on top of certain buildings. Your task is to find the total amount of water accumulated.



Input Format

The first line of input contains T - the number of test cases. It's followed by 2T lines, the first line contains N - the number of buildings. The second line contains N elements denoting the height of the buildings.



Output Format

For each test case, print the units of water accumulated, separated by a new line.



Constraints

30 points

1 <= T <= 1000

1 <= N <= 1000

1 <= a[i] <= 1000



70 points

1 <= T <= 1000

1 <= N <= 100000

1 <= a[i] <= 1000



Example

Input

2

7

1 6 2 4 5 7 9 

5

3 2 7 4 7 



Output

7

4



Explanation



Test-Case 1

Water accumulated on top of Building-1 : 0

Water accumulated on top of Building-2 : 0

Water accumulated on top of Building-3 : 4

Water accumulated on top of Building-4 : 2

Water accumulated on top of Building-5 : 1

Water accumulated on top of Building-6 : 0

Water accumulated on top of Building-7 : 0

Total = 0 + 0 + 4 + 2 + 1 + 0 + 0 = 7



Test-Case 2

Water accumulated on top of Building-1 : 0

Water accumulated on top of Building-2 : 1

Water accumulated on top of Building-3 : 0

Water accumulated on top of Building-4 : 3

Water accumulated on top of Building-5 : 0

Total = 0 + 1 + 0 + 3 + 0 = 4



# Enter your code here. Read inpu
def getmax(ar,n,maxl,maxr):
    a=0
    for i in range(1,n-1):
        if min(maxl[i-1],maxr[i+1]) -ar[i]>0:
            a+=min(maxl[i-1],maxr[i+1])-ar[i]

    return a
for _ in range(int(input())):
    n=int(input())
    ar=list(map(int,input().split()))
    maxl=[ar[0]]
    maxr=[]
    m=ar[0]
    for i in range(1,n):
        m=max(ar[i],m)
        maxl.append(m)
    m=ar[-1]
    for i in range(n-1,-1,-1):
        m=max(ar[i],m)
        maxr.append(m)
    print(getmax(ar,n,maxl,list(reversed(maxr))))