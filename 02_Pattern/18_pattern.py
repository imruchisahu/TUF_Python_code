'''Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



E 

D E 

C D E 

B C D E 

A B C D E



Print the pattern in the function given to you.


Examples:
Input: n = 4

Output:



Input: n = 2

Output:



Constraints:
1 <= n <= 26

Similar Problems
Approach: 
Use a for loop to iterate from 0 to N-1, where N is the number of rows. This loop will ensure to print each row of the pattern.
The triangle has to be right-angled so, the inner loop will run for exactly current row number and the needed alphabet characters will get printed here.
After completing a row give a line break, to make sure next row gets printed as well.


Complexity Analysis: 
Time Complexity : O(N2). The overall complexity will be O(N2) due to the nested loops, where N is the number of rows.

Space Complexity :O(1). As no extra space is being used to print the patterns.

class Solution:
    # Function to print pattern18
    def pattern18(self, n):
        # Outer loop for the number of rows.
        for i in range(n):
            
            """ Inner loop for printing alphabets
            from 'A' + n - 1 - i to 'A' + n - 1."""
            for ch in range(ord('A') + n - 1 - i, ord('A') + n):
                print(chr(ch), end=" ")
            
            # Move to the next line for the next row.
            print()

if __name__ == "__main__":
    N = 5
    
    # Create an instance of Solution class
    sol = Solution()
    
    sol.pattern18(N)


'''
class Solution:
    def pattern18(self, n):
        for i in range(n):
            for ch in range(ord('A') + n-1-i, ord('A') + n):
                print(chr(ch), end=" ")
            print()