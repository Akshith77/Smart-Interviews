Bubble Sort 
Implement Bubble Sort and print the total number of swaps involved to sort the array.



Input Format

The first line of input contains T - the number of test cases. It's followed by 2T lines. The first line of each test case contains N - the size of the array. The next line contains N integers - the elements of the array.



Output Format

For each test case, print the total number of swaps, separated by a new line.



Constraints

1 <= T <= 100

1 <= N <= 100

-1000 <= ar[i] <= 1000



Example

Input

4

8

176 -272 -272 -45 269 -327 -945 176

2

-274 161

7

274 204 -161 481 -606 -767 -351

2

154 -109



Output

15

0

16

1



Explanation



Self Explanatory




# Enter your code here. Read input from STDIN. Print output to STDOUT
a=int(input())
while a>0:
    b=int(input())
    c=list(map(int,input().split()))
    co=0
    for i in range(0,b-1):
        for j in range(0,b-i-1):
            if c[j]>c[j+1]:
                t=c[j]
                c[j]=c[j+1]
                c[j+1]=t
                co+=1
    print(co)
    a-=1