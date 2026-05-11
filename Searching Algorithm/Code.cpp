#include<iostream>
using namespace std;

tern_sear(int arr[],int n, int target){
    int left= 0;
    int right= n-1;
    while(left<=right){
        int mid1= left+ (right-left)/3;
        int mid2= right - (right -left )/3;

        if(arr[mid1]==target){
            return mid1;
        }
        if(arr[mid2]==target){
            return mid2;
        }
        else if(arr[mid1]>target){
            right= mid1 - 1;
        }
        else if(arr[mid2]<target){
            left = mid2 + 1;
        }
        else{
           left = mid1+1;
           right = mid2-1;
        }
    }
    return -1;
}


int main(){
    int n, target;

    cout<<"Enter array size : ";
    cin>>n;

    int arr[n];
    cout<<"Enter Array element: \n";
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }

    cout<<"Enter Target Value: ";
    cin>>target;

    int result= tern_sear(arr,n,target);

    if(result != -1){
        cout<<"Target "<<target<<" found at index : "<<result;
    }
    else{
        cout<<"Not Found";
    }
}
