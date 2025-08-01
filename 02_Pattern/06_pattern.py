'''Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



12345

1234

123

12

1



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
Use a for loop to iterate from 0 to N-1, where N is the number of rows. This loop will ensure to print each row of the pattern.
Inside this loop, run another loop from 0 to (N - current value of the outer loop variable). It will ensure to decrease the number of columns as the row value increases.
Now, print the current value of inner loop + 1, it will print the column number strating from 1 to N.
Move to a new line after printing each row to maintain the right-angled triangle shape of the pattern.


Complexity Analysis: 
Time Complexity : O(N2). As the outer loop runs for N times and the inner loop runs in decreasing manner in each iteration(N + (N-1) + (N-2) + ... + 1), which is equal to (N*(N+1)/2). So, overall it is O(N2).

Space Complexity :O(1). As no extra space is being used to print the patterns.
class Solution:
    
    # Function to print pattern6
    def pattern6(self, n):
        
        # Outer loop will run for rows.
        for i in range(0,n):
            
            # Inner loop will run for columns.
            for j in range(0,n-i):
                print(j+1, end="")
                
            """ As soon as n stars are printed, move
            to the next row and give a line break."""
            print()

    def main(self):
        N = 5

        # Create an instance of the Solution class
        sol = Solution()

        sol.pattern6(N)

if __name__ == "__main__":
    Solution().main()




'''

class Solution:
    def pattern6(self, n):
        for i in range(n):
            for j in range(1, n-i+1):
                print(j, end="")
            print()