#include<iostream>
#include<cmath>
using namespace std;

int jump_sear(int arr[],int n,int target){
    int step= sqrt(n);
    int prev=0;

    while(arr[min(step,n)-1]<target){
          prev=step;
          step += sqrt(n);

          if(prev>=n){
            return -1;
          }
    }
    while(arr[prev]<target){
        prev++;

        if (prev == min(step,n)){
            return -1;
        }
    }
    if(arr[prev]==target){
            return prev;
        }
    return -1;
}

int main(){
    int n,target;

    cout<<"Enter your  array size: ";
    cin>>n;

    int arr[n];
    cout<<"Enter the array value: \n";
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }

    cout<<"Enter the target Value: ";
    cin>> target;

    int result= jump_sear(arr,n,target);

    if(result != -1){
        cout<<target<<" is found at index "<<result;
    }
    else{
        cout<<"Not Found.";
    }
}
