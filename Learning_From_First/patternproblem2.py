
'''#include <iostream>
using namespace std;

int main() {
    int n = 5; // Number of rows

    for (int i = 0; i <= n; i++) {  // Outer loop for rows
        for (int j = 0; j < i; j++) {  // Inner loop for columns
            cout << "*";
        }
        cout << endl;  // Move to the next line after each row
    }

    return 0;
}

*
**
***
****
*****

'''

n = 5

for i in range(1, n + 1):  
    for j in range(i):  
        print("*", end="") 
    print()  
    


n = 5

for i in range(n, 0, -1):  
    for j in range(i):  
        print("*", end="")  
    print()  

