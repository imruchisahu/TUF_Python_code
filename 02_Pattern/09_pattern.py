'''Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



    * 
   ***
  *****
 *******
*********
*********
 *******
  *****
   ***
    *


Print the pattern in the function given to you.


Examples:
Input: n = 4

Output:



Input: n = 2

Output:



Constraints:
1 <= n <= 100

Similar Problems

Approach: 
This pattern is a combination of the pyramid and an inverted pyramid. First, print the pyramid and then the inverted one.
Use nested for loops to print the pyramid. First, print the spaces using a for loop, and then the required asterisks using a second for loop.
After this, give a line break to print the next row. Follow the same process to print the inverted pyramid.
Solution:

Complexity Analysis: 
Time Complexity : O(2*N2). As both functions take O(N2) each.

Space Complexity :O(1). As no extra space is being used to print the patterns.

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    // Function to print pattern9
    void pattern9(int n) {
        erect_pyramid(n);
        inverted_pyramid(n);
    }
private: 
    void erect_pyramid(int n) {
        // Outer loop which will loop for the rows.
        for (int i = 0; i < n; i++){
            // For printing the spaces before stars in each row
            for (int j = 0; j < n - i - 1; j++) {
                cout<< " ";
            }
            
            // For printing the stars in each row
            for (int j = 0; j < 2 * i + 1; j++) {
                cout<< "*";
            }

            /* As soon as the stars for each iteration are printed,
            we move to the next row and give a line break */
            cout << endl;
        }
    }
    void inverted_pyramid(int n){
        // Outer loop which will loop for the rows.
        for (int i = 0; i < n; i++){
            // For printing the spaces before stars in each row
            for (int j =0; j<i; j++){
                cout<< " ";
            }
       
            // For printing the stars in each row
            for(int j=0;j< 2*n -(2*i +1);j++){
                cout<< "*";
            }
       
            /* As soon as the stars for each iteration are printed,
            we move to the next row and give a line break */
            cout<< endl;
        }
    }
};

int main() {
    int N = 5;

    //Create an instance of Solution class
    Solution sol;

    sol.pattern9(N);

    return 0;
}


'''
class Solution:
    def pattern9(self, n):
        self.pattern7(n)
        self.pattern8(n)
    def pattern7(self, n):
        for i in range(n):
            #spaces
            for j in range(1, n-i):
                print(' ', end="")
            #stars
            for j in range(2*i+1):
                print("*", end="")
            print()
    def pattern8(self, n):
        for i in range(n):
            for j in range(i):
                print(' ', end="")
            for j in range((2*n-1)-(2*i)):
                print("*", end="")
            print()
        
            
            