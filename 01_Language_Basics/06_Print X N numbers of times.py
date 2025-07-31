'''Given two integers X and N, print the value X on the screen N times. Move to the next line after printing, even if N = 0.


Examples:
Input: X = 7, N = 5

Output: 7 7 7 7 7

Input: X = 15, N = 1

Output: 15

Input: X = -5, N = 4

Output:
-5 -5 -5 -5
Constraints:
-100 <= X <= 100
0 <= N <= 100

Approach:
Receive Inputs: Capture the integers X and N from the user.
Check Validity: Ensure N is non-negative, as printing a value a negative number of times doesn't make sense.
Use a loop to print the value X exactly N times, ensuring a space separates each value.

//solution:
class Solution:
    # Function to print the value X on the screen N times
    def printX(self, X, N):
        # Check if N is non-negative
        if N < 0:
            print("Invalid number of times")
            return

        # Loop to print the value X, N times
        for i in range(N):
            # Print the value X
            print(X, end='')
            
            # Print a space between numbers,
            # but not after the last one
            if i < N - 1:
                print(" ", end='')
        
        # Move to the next line after printing
        print()

# Creating an instance of Solution class 
sol = Solution()
X = 7
N = 5

# Function call to print the value X, N times
sol.printX(X, N)


'''
class Solution:
    def printX(self, X, N):
        if N < 0:
            print("InValid Number")
            return
        for i in range(N):
            print(X, end='')

            if i < N - 1:
                print(" ", end='')
        print()
Solution() 

