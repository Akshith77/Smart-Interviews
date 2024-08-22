Spiral Traversal of Matrix 
Given a 2D square matrix, print the matrix in a spiral order. Refer to examples for more details. From an interview's point of view, after you scan the matrix in a 2D array, try to print the matrix in a spiral order without using any extra space.



Input Format

The first line of input contains T - the number of test cases. The first line of each test case contains N - the size of the matrix [NxN]. It is followed by N lines each containing N integers - matrix elements.



Output Format

For each test case, print the matrix in a spiral order, separated by newline.



Constraints

1 <= T <= 100

1 <= N <= 100

-100 <= ar[i][j] <= 100



Example

Input

4

1

1

2

1 2

4 3

3

1 2 3

8 9 4

7 6 5

5

-44 25 -52 69 -5

17 22 51 27 -44

-79 28 -78 1 -47

65 -77 -14 -21 -6

-96 43 -21 -20 90



Output

1

1 2 3 4

1 2 3 4 5 6 7 8 9

-44 25 -52 69 -5 -44 -47 -6 90 -20 -21 43 -96 65 -79 17 22 51 27 1 -21 -14 -77 28 -78



Explanation



Self Explanatory

#include <bits/stdc++.h>
using namespace std;
void printspiral(int **arr,int n,int x,int y){
    if(x>=n || y>=n) return;
    for(int i=x;i<n;i++){
        cout<<arr[x][i]<<" ";
    }
    for(int i=x+1;i<n;i++){
        cout<<arr[i][n-1]<<" ";
    }
    if ((n-1)!=x){
        for(int i=n-2;i>=y;i--){
            cout<<arr[n-1][i]<<" ";
        }
    }
    if((n-1)!=y){
        for(int i=n-2;i>x;i--){
            cout<<arr[i][y]<<" ";
        }
    }
    printspiral(arr,n-1,x+1,y+1);
}

int main() {
    int q;
    cin>>q;
    while(q--){
        int n;
        cin>>n;
        int **arr=new int*[n];
        for(int i=0;i<n;i++){
            arr[i]=new int[n];
        }
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                cin>>arr[i][j];
            }
        }
        printspiral(arr,n,0,0);
        cout<<endl;
    }
    return 0;
}