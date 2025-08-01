'''Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



*
**
***
****
*****



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
First, run a loop for N times(0 to N-1). This loop will ensure to print each row of the pattern.
Inside the outer loop, run another loop for current value of the outer loop variable. It will basically ensure that the total columns is equal to the current row.
Within the inner loop, print an asterisk (*) without moving to a new line. This keeps all asterisks for a single row on the same line.
After the inner loop completes, move to a new line to start printing the next row.

Complexity Analysis: 
Time Complexity : O(N2). As the outer loop runs for N time and the inner loop runs incrementally in each iteration(1+2+3+...+N), which is equal to (N*(N+1)/2). So, overall it is O(N2).

Space Complexity :O(1). As no extra space is being used to print the patterns.
class Solution:
    
    # Function to print pattern2
    def pattern2(self, n):
        
        # Outer loop will run for rows.
        for i in range(n):
            
            # Inner loop will run for columns.
            for j in range(i+1):
                print("*", end="")
                
            """ As soon as n stars are printed, move
            to the next row and give a line break."""
            print()

    def main(self):
        N = 5

        # Create an instance of the Solution class
        sol = Solution()

        sol.pattern2(N)

if __name__ == "__main__":
    Solution().main()



'''

class Solution:
    def pattern2(self, n):
        for i in range(n):
            for j in range(i+1):
                print("*", end="")
            print()
s=Solution()
s.pattern2(5)