#include<iostream>
using namespace std;

int fib_sear(int arr[], int n ,int target){
    int fibM2=0;
    int fibM1=1;
    int fibM = fibM2+fibM1;

    while(fibM < n){
        fibM2 = fibM1;
        fibM1 = fibM;
        fibM = fibM2 + fibM1;
    }

    int offset = 1;

    while(fibM > 1){
        int i = min(offset + fibM2,n-1);

        if (arr[i] < target){
            fibM = fibM1;
            fibM1 = fibM2;
            fibM2 = fibM - fibM1;

            offset = i;

        }
        else if(arr[i] > target){
            fibM = fibM2;
            fibM1 = fibM1 - fibM2;
            fibM2 = fibM - fibM1;
        }
        else{
            return i ;
        }
    }
    if(fibM1 && arr[offset+1] == target){
        return offset+1;
    }
    return -1;
}

int main()
{
    int arr[] = {10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100};
    int n = sizeof(arr) / sizeof(arr[0]);

    int target;

    cout << "Enter element to search: ";
    cin >> target;

    int result = fib_sear(arr, n, target);

    if (result != -1)
        cout << "Element found at index: " << result << endl;
    else
        cout << "Element not found." << endl;

    return 0;
}
