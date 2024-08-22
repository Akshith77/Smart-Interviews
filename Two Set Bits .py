Two Set Bits 
Look at the following sequence:

3, 5, 6, 9, 10, 12, 17, 18, 20....

All the numbers in the series have exactly 2 bits set in their binary representation. Your task is simple, you have to find the Nth number of this sequence.



Input Format

The first line of input contains T - the number of test cases. It's followed by T lines, each containing a single number N.



Output Format

For each test case, print the Nth number of the sequence, separated by a newline. Since the number can be very large, print the number % 1000000007.



Constraints

30 points

1 <= T, N <= 200



70 points

1 <= T, N <= 105



100 points

1 <= T <= 105

1 <= N <= 1014



Example

Input

5

1

2

5

50

100



Output

3

5

10

1040

16640



Explanation



Self Explanatory




# Enter your code here. Read input from STDIN.
def apown(x,n):
    res=1
    mod=1000000007
    while n:
        if n&1:
            res=(res*x)%mod
        x=((x%mod)*(x%mod))%mod
        n>>=1
    return res 
for _ in range(int(input())):
    n=int(input())
    i=(int(pow((n<<3)-1,0.5))+1)>>1
    x=n-((i*(i-1))>>1)-1
    print(str((apown(2,i) + apown(2,x))%1000000007))