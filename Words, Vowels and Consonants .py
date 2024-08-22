Words, Vowels and Consonants 
Given a sentence containing only uppercase/lowercase english alphabets and spaces, you have to count the number of words, vowels and consonants.



Input Format

The first line of input contains T - number of test cases. It's followed by T lines, each line contains a single sentence.



Output Format

For each test case, print the number of words, vowels and consonants, separated by newline.



Constraints

1 <= T <= 1000

1 <= len(sentence) <= 104



Example

Input

4

Hi

Hello World

  Exception  

Hi there



Output

1 1 1

2 3 7

1 4 5

2 3 4



Explanation



Self Explanatory

# Enter your code here. Read input from STDIN. Print output to STDOUT
a=int(input())
while a>0:
    b=input()
    wo=len(b.split())
    vo,co=0,0
    d=['a','e','i','o','u','A','E','I','O','U']
    for i in range(0,len(b)):
        if b[i] in d:
            vo+=1
        elif b[i]==" ":
            s=0
        else:
            co+=1
    print(wo,vo,co)
    a-=1