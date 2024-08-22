Triplet with Sum K 
You are given an integer array and a positive integer K. You have to tell if there exists i,j,k in the given array such that ar[i]+ar[j]+ar[k]=K, i≠j≠k.



Input Format

The first line of input contains T - the number of test cases. Its followed by 2T lines, the first line contains N and K - the size of the array and the number K. The second line contains the elements of the array.



Output Format

For each test case, print "true" if the arrays contains such elements, false otherwise, separated by new line.



Constraints

30 points

1 <= T <= 100

3 <= N <= 100



70 points

1 <= T <= 100

3 <= N <= 1000



General Constraints

-100000 <= A[i] <= 100000

0 <= K <= 100000



Example

Input

3

5 60

1 20 40 100 80

12 54

12 45 52 65 21 645 234 -100 14 575 -80 112

3 15

5 5 5



Output

false

true

true



Explanation



Self Explanatory


#include <bits/stdc++.h>
using namespace std;
int main() {
    int a;
    cin>>a;
    while(a--){
        int b,c;
        cin>>b>>c;
        int ar[b];
        for(int i=0;i<b;i++){
            cin>>ar[i];
        }
        int f=0;
        sort(ar,ar+b);
        for(int i=0;i<b-1;i++){
            int p1=i+1,p2=b-1,an;
            an=c-ar[i];
            while(p1<p2){
            if(ar[p1]+ar[p2]==an){
                f=1;
                break;
            }
            else if(ar[p1]+ar[p2]<an){
                p1++;
            }
            else p2--;
            }
        }
        if(f==1){
            cout<<"true"<<endl;
        }
        else cout<<"false"<<endl;
    }
    return 0;
}