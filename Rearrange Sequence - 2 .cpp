Rearrange Sequence - 2 
You are given an array of size N containing integers which may not be unique. Find the size of the largest subarray that can be rearranged to form a strictly contiguous sequence.



Input Format

The first line of input contains T - number of test cases. Its followed by 2T lines, the first line contains N - the size of the array. The second line contains the elements of the array.



Output Format

For each test case, print the size of the largest subarray that can be rearranged to form a contiguous sequence, on a new line.



Constraints

30 points

1 <= T <= 100

4 <= N <= 100



70 points

1 <= T <= 100

4 <= N <= 1000



General Constraints

0 <= A[i] <= 105



Example

Input

2

5

4 3 3 1 1

9

8 8 6 7 3 5 7 1 1



Output

2

3



Explanation



Test-Case 1

The largest subarray which can be rearranged to form a contiguous sequence here, is {4, 3} which can be rearranged to form {3, 4}.



Test-Case 2

The largest subarray which can be rearranged to form a contiguous sequence here, is {8, 6, 7} which can be rearranged to form {6, 7, 8}.


#include <bits/stdc++.h>
using namespace std;
long int func(long int a[],long int n){
    long int ans=1;
    for(int i=0;i<n;i++){
        long int maxi=a[i],mini=a[i];
        unordered_set <int> hs;
        for(long int j=i;j<n;j++){
            mini=min(mini,a[j]);
            maxi=max(maxi,a[j]);
            hs.insert(a[j]);
            if(maxi-mini+1==hs.size() && j-i+1==hs.size()){
                ans=max(ans,j-i+1);
            }
        }
    }
    return ans;
}

int main() {
    int t;
    cin>>t;
    while(t--){
        long int n;
        cin>>n;
        long int a[n];
        for(int i=0;i<n;i++){
            cin>>a[i];
        }
        printf("%ld\n",func(a,n));
    }
    
     return 0;
}