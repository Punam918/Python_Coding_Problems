'''
#include <iostream>
using namespace std;

int main() {
    int n = 5; // Number of rows

    for (int i = 1; i <= n; i++) {  // Outer loop for rows
        for (int j = 1; j <= i; j++) {  // Inner loop for repetition
            cout << i;  // Print the current row number
        }
        cout << endl;  // Move to the next line after each row
    }

    return 0;
}

1
22
333
4444
55555

'''
# Number of rows
n = 5

for i in range(1, n + 1):  
    for j in range(i):  
        print(i, end="") 
    print()  