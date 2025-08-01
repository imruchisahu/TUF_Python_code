
'''
//Pattern1
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



*****
*****
*****
*****
*****



Print the pattern in the function given to you.


Examples:
Input: n = 4

Output:





Input: n = 2

Output:





Constraints:
1 <= n <= 100

Approach: 
Use a for loop to iterate from 0 to (N-1), where N is the number of rows. This loop will ensure to print each row of the pattern.
Inner loops makes sure that N stars are printed in every line, eventually since the inner loop will run for N times, it will make sure that N stars are printed in N lines, resulting in a square of size N x N, which is the desired pattern
Now, print the asterisks for each column of a row, inside the inner loop.
Move to a new line after printing each row to maintain the right-angled triangle shape of the pattern.




Complexity Analysis: 
Time Complexity:O(N2) As two for loops are being used to print the patterns and both of them runs for N time.

Space Complexity: As no additional space is used, so the Space Complexity is O(1)
class Solution:
    
    # Function to print pattern1
    def pattern1(self, n):
        
        # Outer loop will run for rows.
        for i in range(n):
            
            # Inner loop will run for columns.
            for j in range(n):
                print("*", end="")
                
            """ As soon as N stars are printed, move
            to the next row and give a line break."""
            print()

    def main(self):
        N = 4

        # Create an instance of the Solution class
        sol = Solution()

        sol.pattern1(N)

if __name__ == "__main__":
    Solution().main()

'''
class Solution:
    def pattern1(self, n):
        for i in range(n):
            for j in range(n):
                print("*", end="")
            print() # nextline
s=Solution()
s.pattern1(5)