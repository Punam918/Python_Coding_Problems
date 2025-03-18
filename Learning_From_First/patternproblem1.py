# https://www.youtube.com/watch?v=tNm_NNSB3_w&list=PLgUwDviBIf0oF6QL8m22w1hIDC1vJ_BHz&index=4
'''
#include <iostream>
using namespace std;

int main() {
    int n = 4; // Number of rows and columns

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cout << "*";
        }
        cout << endl;
    }

    return 0;
}

'''

n = 4

for i in range(n):  
    for j in range(n):  
        print("*", end="") 
    print() 