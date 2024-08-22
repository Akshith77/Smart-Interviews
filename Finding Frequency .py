Finding Frequency 
Given an array, you have to find the frequency of a number x.



Input Format

The first line of input contains N - size of the array. The next line contains N integers, the elements of the array. The next line contains Q - number of queries. Each of the next Q lines contains a single integer X, for which you have to find the frequency of X in the given array.



Output Format

For each query, print the frequency of X, separated by a new line.



Constraints

20 points

1 <= N <= 105

1 <= Q <= 102

-108 <= ar[i] <= 108



30 points

1 <= N <= 105

1 <= Q <= 105

-108 <= ar[i] <= 108



50 points

1 <= N <= 105

1 <= Q <= 105

-108 <= ar[i] <= 108



Example

Input

9

-6 10 -1 20 -1 15 5 -1 15

5

-1

10

8

15

20



Output

3

1

0

2

1



Explanation



Self Explanatory


# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
n=int(input())
arr=list(map(int,input().split()))
q=int(input())
di=dict(Counter(arr))
for _ in range(q):
    try:
        print(di[int(input())])
    except:
        print(0)
        