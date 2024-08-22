Insertion Sort 
Implement Insertion Sort and print the index at which the ith element gets inserted [i>=1].



Input Format

The first line of input contains T - the number of test cases. It's followed by 2T lines. The first line of each test case contains N - the size of the array. The next line contains N integers - elements of the array.



Output Format

For each test case, print the index at which the ith element gets inserted [i>=1], separated by space. Separate the output of different tests by a new line.



Constraints

1 <= T <= 100

2 <= N <= 100

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

0 1 2 4 0 0 6

1

0 0 3 0 0 2

0



Explanation



Self Explanatory




# Enter your code here. Read input from STDIN. Print output to STDOUT
a=int(input())
while a>0:
    b=int(input())
    c=list(map(int,input().split()))
    for i in range(1,b):
        x=c[i]
        idx=i-1
        while idx>=0 and c[idx]>x:
            c[idx+1]=c[idx]
            idx-=1
        c[idx+1]=x
        print(idx+1,end=" ")
    print()
    a-=1
