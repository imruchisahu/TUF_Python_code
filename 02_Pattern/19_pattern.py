'''Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



**********
****  ****
***    ***
**      **
*        *
*        *
**      **
***    ***
****  ****
**********


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
This pattern can be broken down into lower half and upper half. Both the halves follow the same logic, first print the asterisks then the spaces and at last the asterisks again.
Upper half pattern: Start by initializing iniS to 0. This variable will keep track of the number of spaces between the two sets of stars in each row of the upper half pattern.
Use an outer loop to iterate from 0 to N-1 (where N is the input parameter), representing each row of the upper half pattern.
Print stars (*) starting from N - (the current row index) and decrementing until 1. Print spaces using another loop (for loop) that runs iniS times. iniS starts at 0 and increases by 2 with each new row. Print stars again, mirroring the first set but in reverse order.
After completing a row give a line break, to make sure next row gets printed as well.
Lower half pattern: Follow the same above steps to print the lower half pattern.


Complexity Analysis: 
Time Complexity : O(N2). The overall complexity will be O(N2), where N is the number of rows.

Space Complexity :O(1). As no extra space is being used to print the patterns.

class Solution:
    # Function to print pattern19
    def pattern19(self, n):
        # Print the upper half pattern
        
        # Store the initial spaces.
        iniS = 0
        
        for i in range(n):
            # Printing the stars in the row.
            print("*" * (n - i), end="")
            
            # Printing the spaces in the row.
            print(" " * iniS, end="")
            
            # Printing the stars in the row.
            print("*" * (n - i))
            
            """ The spaces increase by 2 
            every time we hit a new row."""
            iniS += 2
        
        # Print the lower half pattern
        
        # Store the initial spaces.
        iniS = 2 * n - 2
        
        for i in range(1, n + 1):
            # Printing the stars in the row.
            print("*" * i, end="")
            
            # Printing the spaces in the row.
            print(" " * iniS, end="")
            
            # Printing the stars in the row.
            print("*" * i)
            
            """ The spaces decrease by 2 
            every time we hit a new row."""
            iniS -= 2

if __name__ == "__main__":
    N = 5
    
    # Create an instance of Solution class
    sol = Solution()
    
    sol.pattern19(N)



'''
class Solution:
    def pattern19(self, n):
        for i in range(n):
            for j in range(n-i):
                print("*", end="")
            for j in range(2*i):
                print(" ", end="")
            for j in range(n-i):
                print("*", end="")
            print()

        for i in range(n):
            for j in range(i+1):
                print("*", end="")
            for j in range(2*n-2-2*i):
                print(" ", end="")
            for j in range(i+1):
                print("*", end="")
            print()

