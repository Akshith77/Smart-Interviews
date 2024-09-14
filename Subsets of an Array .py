Subsets of an Array 
Given an array of unique integer elements, print all the subsets of the given array in lexicographical order.



Input Format

The first line of input contains T - the number of test cases. It's followed by 2T lines, the first line contains N - the size of the array and the second line contains the elements of the array.



Output Format

For each test case, print the subsets of the given array in lexicographical order, separated by new line. Print an extra newline between output of different test cases.



Constraints

1 <= T <= 100

1 <= N <= 10

0 <= A[i] <= 100



Example

Input

3

3

5 15 3 

2

57 96 

4

3 15 8 23 



Output

3 

3 5 

3 5 15 

3 15 

5 

5 15 

15 



57 

57 96 

96 



3 

3 8 

3 8 15 

3 8 15 23 

3 8 23 

3 15 

3 15 23 

3 23 

8 

8 15 

8 15 23 

8 23 

15 

15 23 

23



Explanation



Self Explanatory



# Enter your code here. Read inp
def check(n,i):
    if (n>>i)&1:
        return 1
    else:
        return 0

for _ in range(int(input())):
    n=int(input())
    ar=list(map(int,input().split()))
    ar.sort()
    li=[]
    for i in range(1<<n):
        sub=[]
        for j in range(n):
            if check(i,j)==1:
                sub.append(ar[j])
        li.append(sub)
    li.sort()
    for i in range(1,len(li)):
        for j in li[i]:
            print(j,end=' ')
        print()
    print()