#include<iostream>
using namespace std;

int bin_sear(int arr[ ],int n,int terget){
    int left = 0;
    int right =n - 1;
    
    while(left<=right){
        int mid = (left + right)/2;

        if(arr[mid]==terget){
           return mid;
        }
        else if(arr[mid]<terget){
            left= mid + 1;
        }
        else{
            right= mid-1;
        }
    }
    return -1;

}

int main(){
    int n, terget;

    cout<<"Enter your arr size: ";
    cin>>n;


    int arr[n];
    cout<<"Enter a sorted Array: \n";
    for(int i=0;i<n;i++){
        cin>> arr[i];
    }

    cout<<"Enter your terget value: ";
    cin>>terget;

    int result = bin_sear(arr,n,terget);

    if(result != -1)
        cout<<terget<<" is found at index: " << result;

    else
        cout<<"Element is not found.";
        return 0;


}
