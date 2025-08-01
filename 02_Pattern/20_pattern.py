'''Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *


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
Start by initializing spaces to 2*N - 2. This variable tracks the number of spaces between the two sets of stars in each row, where N is the number of rows.
Use an outer loop (for loop) to iterate from 1 to 2*N- 1. This loop controls the number of rows printed for both the upper and lower halves of the pattern.
Inside the loop, calculate stars: For the first half (when row number <= N), stars starts from 1 and increments with each row. For the second half (when row > N), stars decreases with each row.
Use nested loops to print stars, spaces, the second set of stars, mirroring the first set. After printing stars and spaces for each row, adjust spaces.
If row < N, decrease spaces by 2 to gradually reduce the space between stars as rows progress towards the middle, else, increase spaces by 2 to gradually increase the space as rows move away from the middle.
After completing a row give a line break, to make sure next row gets printed as well.


Complexity Analysis: 
Time Complexity : O(N2). The overall complexity will be O(N2), where N is the number of rows.

Space Complexity :O(1). As no extra space is being used to print the patterns.


class Solution:
    # Function to print pattern20
    def pattern20(self, n):
        # Initialising the spaces.
        spaces = 2 * n - 2
        
        # Outer loop to print the row.
        for i in range(1, 2 * n):
            # Stars for first half
            stars = i
            
            # Stars for the second half.
            if i > n:
                stars = 2 * n - i
            
            # For printing the stars
            print("*" * stars, end="")
            
            # For printing the spaces
            print(" " * spaces, end="")
            
            # For printing the stars
            print("*" * stars, end="")
            
            # Give a line break for new row.
            print()
            
            # Adjust spaces for the next row
            if i < n:
                spaces -= 2
            else:
                spaces += 2

# Main function
if __name__ == "__main__":
    N = 5
    
    # Create an instance of Solution class
    sol = Solution()
    
    sol.pattern20(N)

'''
class Solution:
    def pattern20(self, n):
        #upper part
        for i in range(n):
            for j in range(i+1):
                print("*", end="")
            for j in range(2*n-2-2*i):
                print(" ", end="")
            for j in range(i+1):
                print("*", end="")
            print()
        
        #lower part
        for i in range(1, n-1+1):
            for j in range(n-i):
                print("*", end="")
            for j in range(2*i):
                print(" ", end="")
            for j in range(n-i):
                print("*", end="")
            print()
s=Solution()
s.pattern20(4)