Largest Concatenated Number 
Given an array of integers, find the largest number that can be constructed by concatenating all the elements of the given array.



Input Format

The first line of input contains T - the number of test cases. It's followed by 2T lines. The first line of each test case contains N - the size of the array and the second line contains N integers - the elements of the array.



Output Format

For each test case, print the largest number that can be constructed by concatenating all the elements of the given array, separated by a new line.



Constraints

1 <= T <= 1000

1 <= N <= 1000

0 <= ar[i] <= 1000



Example

Input

3

8

49 73 58 30 72 44 78 23

4

69 9 57 60

2

40 4



Output

7873725849443023

9696057

440



Explanation



Self Explanatory



# Enter your code here. Read input from STDIN. Prin
def findl(arr):
    l=len(str(max(arr)))+1
    ans=''
    a=[]
    for i in arr:
        a.append(((str(i)*l)[:l],i))
    a.sort(reverse=True)
    for i in a:
        ans+=str(i[1])
    return ans

for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    print(findl(arr))