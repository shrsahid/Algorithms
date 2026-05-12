#include<iostream>
using namespace std;

int inter_sear(int arr[],int n, int target){
    int low= 0;
    int high = n-1;

    while(low<= high && arr[low]<=target && arr[high]>=target){
        if(arr[low]==arr[high]){
            if(arr[low]==target){
                return low;
            }
        return -1;
        }
        int pos= low +
               ((target-arr[low])*(high - low)) /
               (arr[high]- arr[low]);

        if (arr[pos]==target){
            return pos;
        }
        else if(arr[pos]<target){
            low= pos +1;
        }
        else{
            high=pos-1;
        }

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

    int result= inter_sear(arr,n,target);

    if(result != -1){
        cout<<target<<" is found at index "<<result;
    }
    else{
        cout<<"Not Found.";
    }
}
