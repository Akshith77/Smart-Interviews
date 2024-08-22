Triple Trouble 
Given an array of size 3X+1, where every element occurs three times, except one element, which occurs only once. Find the element that occurs only once.



Input Format

The first line of input contains T - the number of test cases. It's followed by 2T lines, the first line contains N - the size of the array (of the form 3X + 1) and second line contains the elements of the array.



Output Format

For each test case, print the number which occurs only once, separated by new line.



Constraints

30 points

1 <= T <= 100

1 <= N <= 103



70 points

1 <= T <= 100

1 <= N <= 106



Example

Input

2

10

5 7 8 7 7 9 5 9 5 9

7

10 20 20 30 20 30 30



Output

8

10



Explanation



Self Explanatory



a=int(input())
while a>0:
    b=int(input())
    c=list(map(int,input().split()))
    d=sum(c)
    e=set(c)
    f=0
    for i in e:
        f+=i*3
    print((f-d)//2)
    a-=1