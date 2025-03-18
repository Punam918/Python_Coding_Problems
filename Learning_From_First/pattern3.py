'''#include <iostream>
using namespace std;

int main() {
    int n = 5; // Number of rows

    for (int i = 1; i <= n; i++) {  // Outer loop for rows
        for (int j = 1; j <= i; j++) {  // Inner loop for numbers
            cout << j;  // Print the current number
        }
        cout << endl;  // Move to the next line after each row
    }

    return 0;
}

1
12
123
1234
12345
'''

n = 5

for i in range(1, n + 1): 
    for j in range(1, i + 1):  
        print(j, end="") 
    print() 