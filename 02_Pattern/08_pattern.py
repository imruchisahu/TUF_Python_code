'''Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



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
Approach:
Iterate from 0 to N-1 using a loop, where N is the number of rows. This loop will ensure to print each row of the pattern.
Now, run another loop from 0 to the current value of outer loop variable. It will basically print the spaces before asterisks as required in every row.
Again, run a loop, print the asterisk, all in one line, to complete the current row.
Move to a new line after printing each row to maintain the right-angled triangle shape of the pattern.


Complexity Analysis: 
Time Complexity : O(N2). As the outer loop runs for N times and the first inner loop runs for(0 + 1 + 2 + .. + N-1), the second inner loop runs in decreasing manner in each iteration((2*N -1) + (2*N - 3) + ... + 1) . So, overall it is O(N2).

Space Complexity :O(1). As no extra space is being used to print the patterns.

class Solution:
    
    # Function to print pattern8
    def pattern8(self, n):
        
        # Outer loop will run for rows.
        for i in range(0,n):
            
            #This loop will print the spaces
            for j in range(0, i):
                print(" ", end="")
            
            
            # This loop will print asterisk.
            for j in range(0, 2*n-(2*i+1)):
                print("*", end="")
                
            """ As soon as n stars are printed, move
            to the next row and give a line break."""
            print()

    def main(self):
        N = 5

        # Create an instance of the Solution class
        sol = Solution()

        sol.pattern8(N)

if __name__ == "__main__":
    Solution().main()



'''
class Solution:
    def pattern8(self, n):
        for i in range(n):
            for j in range(i):
                print(' ', end="")
            for j in range((2*n-1)-(2*i)):
                print("*", end="")
            print()
s=Solution()
s.pattern8(4)