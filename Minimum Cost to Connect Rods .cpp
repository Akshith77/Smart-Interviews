Minimum Cost to Connect Rods 
You are given the lengths of N rods. You want to connect all the rods to form a single rod. The cost of connecting 2 rods of lengths: L1 and L2 is L1+L2. The resultant rod will also be of size L1+L2. Your task is to find the minimum cost to connect all the rods.



Input Format

The first line of input contains T - the number of test cases. It's followed by 2T lines, the first line of each test case contains N - the number of rods. The next line contains N integers - the lengths of the rods.



Output Format

For each test case, print the minimum cost to connect all the rods, separated by a newline.



Constraints

30 points

1 <= T <= 100

1 <= N <= 1000

1 <= L[i] <= 1000



70 points

1 <= T <= 500

1 <= N <= 10000

1 <= L[i] <= 1000



Example

Input

3

3

3 1 4

2

1 2

4

4 3 2 6



Output

12

3

29



Explanation



Self Explanatory



#include <bits/stdc++.h>
using namespace std;
int connect(vector <int> &arr,int n){
    priority_queue <int, vector<int>, greater<int>> h;
    for(int i=0;i<n;i++){
        h.push(arr[i]);
    }
        int res=0;
        while(!h.empty()){
            int temp=h.top();
            h.pop();
            if(h.empty()){
                return res;
            }
            temp+=h.top();
            h.pop();
            res+=temp;
            h.push(temp);
        }
    return res;
}
int main() {
    int t;
    cin>>t;
    for(int i=0;i<t;i++)
    {
        int n;
        cin>>n;
        vector <int> arr;
        for(int j=0;j<n;j++){
            int x;
            cin>>x;
            arr.push_back(x);
        }
        cout<<connect(arr,n)<<endl;
    }
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    return 0;
}