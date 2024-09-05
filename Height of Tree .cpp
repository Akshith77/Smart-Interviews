Height of Tree 
Given an array of unique elements, construct a Binary Search Tree and find the height of the tree.



Input Format

The first line of input contains T - the number of test cases. It is followed by 2T lines. The first line of each test case contains N - the number of nodes in the BST. The next line contains N unique integers - value of the nodes.



Output Format

For each test case, print the height of the Binary Search Tree, separated by a newline.



Constraints

1 <= T <= 1000

1 <= N <= 1000

0 <= ar[i] <= 10000



Example

Input

3

5

1 2 3 4 5

5

3 2 4 1 5

7

4 5 15 0 1 7 17



Output

4

2

3



Explanation



Self Explanatory


#include <bits/stdc++.h>
using namespace std;
struct Node{
    int val;
    struct Node *left;
    struct Node *right;
};
struct Node *newNode(int val){
    struct Node * obj=(struct Node *)malloc(sizeof(struct Node));
    obj->val=val;
    obj->left=NULL;
    obj->right=NULL;
    return obj;
}
struct Node * insert(struct Node * node,int val){
    struct Node *obj=newNode(val);
    if(node==NULL){
        return obj;
    }
    struct Node *temp=node;
    struct Node *prev=node;
    while(temp!=NULL){
        prev=temp;
        if(val>temp->val){
            temp=temp->right;
        }
        else{
            temp=temp->left;
        }
    }
    if(val>prev->val){
        prev->right=obj;
    }
    else prev->left=obj;
    return node;
}
int geth(struct Node * root){
    if(root==NULL){
        return 0;
    }
    int left=1+geth(root->left);
    int right=1+geth(root->right);
    return (left>right)? left:right;
}
int main() {
    int t;
    cin>>t;
    for(int i=0;i<t;i++){
        int n;
        cin>>n;
        int *arr=(int *)malloc(sizeof(int)*n);
        int j=0;
        struct Node *node=NULL;
        for(j=0;j<n;j++){
            cin>>arr[j];
            node=insert(node,arr[j]);
        }
        cout<<geth(node)-1<<endl;
    }
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    return 0;
}