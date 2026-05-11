#include <iostream>
using namespace std;

int lin_sear(int arr[], int n, int target) {
    for (int i = 0; i < n; i++) {
        if (arr[i] == target) {
            return i; // return index
        }
    }
    return -1;
}

int main() {
    int n, target;

    cout << "Enter your array size: ";
    cin >> n;

    int arr[n];

    cout << "Enter " << n << " elements:\n";
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    cout << "Enter the target element: ";
    cin >> target;

    int result = lin_sear(arr, n, target);

    if (result != -1)
        cout << "Element found at index no: " << result;
    else
        cout << "Element not found";

    return 0;
}
