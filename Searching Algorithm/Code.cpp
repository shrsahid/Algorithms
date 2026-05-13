#include<iostream>
using namespace std;

int bin_sear(int arr[],int left,int right,int target){
    while(left<=right ){
        int mid=left+ (right-left)/2;

        if(arr[mid]==target){
            return mid;
        }
        if(arr[mid]<target){
            left=mid+1;
        }
        else{
            right=mid-1;
        }
    }
    return -1;
}
int exp_sear(int arr[],int n,int target){
    if(arr[0]==target){
        return 0;
    }

    int i=1;
    while(i<n && arr[i]<=target){
        i=i*2;

    }
    return bin_sear(arr,i/2,min(i,n-1), target);
}
int main(){
    int arr[]={1,2,2,3,3,5};
    int n =sizeof(arr)/sizeof(arr[0]);

    int target;
    cout<<"Enter your target value: ";
    cin>>target;

    int result= exp_sear(arr,n,target);

    if(result != -1){
        cout<<target<< "Is in index: "<<result;
    }
    else{
        cout<<"Not Found";
    }
    return 0;
}
