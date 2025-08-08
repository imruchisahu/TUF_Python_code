'''
Given an N * N 2D integer matrix, rotate the matrix by 90 degrees clockwise.



The rotation must be done in place, meaning the input 2D matrix must be modified directly.


Examples:
Input: matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]



Output: matrix = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]



Input: matrix = [[0, 1, 1, 2], [2, 0, 3, 1], [4, 5, 0, 5], [5, 6, 7, 0]]



Output: matrix = [[5, 4, 2, 0], [6, 5, 0, 1], [7, 0, 3, 1], [0, 5, 1, 2]]



Input: matrix = [[1, 1, 2], [5, 3, 1], [5, 3, 5]]

Output:
[[5, 5, 1], [3, 3, 1], [5, 1, 2]]
Constraints:
n == matrix.length.
n == matrix[i].length.
1 <= n <= 100.
-104 <= matrix[i][j] <= 104

Hint 1

Hint 2
Intuition
The naive way is to take another dummy matrix of row and column same as original matrix. Then, take the first row of the original matrix and place it in the last column of the dummy matrix. Next, take the second row of the original matrix and place it in the second last column of the dummy matrix, continuing this process until the last row of the original matrix is placed in the first column of the dummy matrix.

Finally, copy the elements of the dummy matrix back to the original matrix. This procedure ensures that the original matrix is rotated by 90 degrees clockwise.

Approach 
initialize a dummy matrix to store the elemens in rotated order.
Iterate in the array using nested for loops say (i) for row and (j) for columns and take the elements of the first row of matrix, put it in last column of the dummy matrix. Repeat this process until index i crosses sizeOfArray
Again, copy the elements of the dummy matrix to the original matrix and finally, return the original matrix.


Complexity Analysis 
Time Complexity: O(N2) +O(N2), to linearly iterate and put elements into dummy matrix and another O(N2) to copy elements of dummy matrix back to original matrix.

Space Complexity: O(N2), to store the elements in the dummy matrix.
from typing import List

class Solution:
    #Function to rotate the given matrix by 90 degrees clockwise
    
    def rotateMatrix(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        
        # Initialize new matrix to store rotated values
        rotated = [[0] * n for _ in range(n)]
        
        # Perform rotation logic
        for i in range(n):
            for j in range(n):
                rotated[j][n - i - 1] = matrix[i][j]
        
        # Copy rotated elements back to original matrix
        for i in range(n):
            matrix[i] = rotated[i]

if __name__ == "__main__":
    arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    
    # Create an instance of the Solution class
    sol = Solution()
    
    # Rotate the matrix
    sol.rotate(arr)
    
    # Print the rotated matrix
    print("Rotated Image:")
    for row in arr:
        print(" ".join(map(str, row)))


'''

class Solution:
    def rotateMatrix(self, matrix):
        n=len(matrix)
        rotated = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                rotated[j][n-i-1] = matrix[i][j]
        for i in range(n):
            matrix[i] = rotated[i]