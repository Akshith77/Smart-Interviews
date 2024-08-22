Sort 0s and 1s 
You are given an array of 0's and 1's. Sort the array in ascending order and print it.



Note:

Solve using two-pointer technique.



Input Format
The first line of input contains T - the number of test cases. It's followed by 2T lines, the first line contains N - the size of the array. The second line contains the elements of the array.



Output Format

For each test case, sort the array in ascending order and print it in a new line.



Constraints

1 <= T <= 1000

1 <= N <= 1000

0 <= A[i] <= 1



Example

Input

2

5

0 1 1 0 1

6

1 1 1 1 1 0



Output

0 0 1 1 1

0 1 1 1 1 1



Explanation



Self Explanatory



# Enter your code here. Read input from STDIN. Print output to STDOUT
a=int(input())
while(a>0):
    b=int(input())
    c=list(map(int,input().split()))
    z=c.count(0)
    o=c.count(1)
    for i in range(z):
        print("0",end=" ")
    for i in range(o):
        print("1",end=" ")
    print()
    a-=1