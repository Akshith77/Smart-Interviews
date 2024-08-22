Selection Sort 
Implement Selection Sort and print the index which gets swapped at each step.



Input Format

The first line of input contains T - the number of test cases. It's followed by 2T lines. The first line of each test case contains N - the size of the array. The next line contains N integers - elements of the array.



Output Format

For each test case, print the index which gets swapped at each step, separated by space. Separate the output of different tests by a new line.



Constraints

1 <= T <= 100

2 <= N <= 100

-1000 <= ar[i] <= 1000



Example

Input

6

8

176 -272 -272 -45 269 -327 -945 176

2

-274 161

7

274 204 -161 481 -606 -767 -351

2

154 -109

4

5 3 1 5

4

40 10 20 40



Output

4 0 4 3 1 2 1

1

3 0 1 2 2 1

0

0 0 1

0 0 0



Explanation



Self Explanatory



# Enter your code here. Read input from STDIN. Print output to STDOUT
a=int(input())
while a>0:
    b=int(input())
    c=list(map(int,input().split()))
    for i in range(0,b-1):
        co=0
        for j in range(1,b-i):
            if c[j]>c[co]:
                co=j
        print(co,end=" ")
        t=c[co]
        c[co]=c[b-i-1]
        c[b-i-1]=t
    print()
    
    a-=1