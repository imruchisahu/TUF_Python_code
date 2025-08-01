'''Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



1

22

333

4444

55555



Print the pattern in the function given to you.


Examples:
Input: n = 4

Output:



Input: n = 2

Output:



Constraints:
1 <= n <= 100

Similar Problems

class Solution:
    
    # Function to print pattern4
    def pattern4(self, n):
        
        # Outer loop will run for rows.
        for i in range(1,n+1):
            
            # Inner loop will run for columns.
            for j in range(1,i+1):
                print(i, end="")
                
            """ As soon as n stars are printed, move
            to the next row and give a line break."""
            print()

    def main(self):
        N = 5

        # Create an instance of the Solution class
        sol = Solution()

        sol.pattern4(N)

if __name__ == "__main__":
    Solution().main()


'''
class Solution:
    def pattern4(self, n):
        for i in range(1, n+1):
            for j in range(1, i+1):
                print(i, end="")
            print()
