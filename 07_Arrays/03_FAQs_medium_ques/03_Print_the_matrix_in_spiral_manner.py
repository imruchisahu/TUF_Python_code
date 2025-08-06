'''Given an M * N matrix, print the elements in a clockwise spiral manner. Return an array with the elements in the order of their appearance when printed in a spiral manner.


Examples:
Input: matrix = [[1, 2, 3], [4 ,5 ,6], [7, 8, 9]]

Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]

Explanation: The elements in the spiral order are 1, 2, 3 -> 6, 9 -> 8, 7 -> 4, 5

Input: matrix = [[1, 2, 3, 4], [5, 6, 7, 8]]

Output: [1, 2, 3, 4, 8, 7, 6, 5]

Explanation: The elements in the spiral order are 1, 2, 3, 4 -> 8, 7, 6, 5

Input: matrix = [[1, 2], [3, 4], [5, 6], [7, 8]]

Output:
[1, 2, 4, 6, 8, 7, 5, 3]
Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-100 <= matrix[i][j] <= 100

Hint 1
Treat the matrix as a collection of concentric rectangular layers. Traverse each layer in four steps: top row (left to right), right column (top to bottom), bottom row (right to left), and left column (bottom to top).

Hint 2
Maintain four boundaries (top, bottom, left, right) to keep track of the limits of the matrix as you spiral inward.

Intuition
The idea is to use four separate loops to print the array elements in spiral. 1st loop will print the elements from left to right. 2nd loop will print the elements from top to bottom. 3rd loop will print the elements from right to left. 4th loop will print the elements from bottom to top.

Approach 
Initialize four variables top as 0, left as 0, bottom as TotalRow - 1, right as ToatalColumn - 1.
Iterate till top is less than or equal to bottom and left less than or equal to right
For moving left to right use a loop(say i) and add the elements. Increment top by 1.
For moving top to bottom use another loop and add the elements in answer. Decrement right by 1.
If top is less than or equal to bottom then for moving right to left use another loop and add the elements in answer. Decrement bottom by 1.
If left is less than or equal to right the for moving bottom to top take another loop and add the elements in answer. Increment left by 1. Lastly, return the answer.
Illustration 


Complexity Analysis 
Time Complexity: O(MxN) since all the elements are being traversed once and there are total N x M elements ( M elements in each row and total N rows) so the time complexity will be O(N x M).

Space Complexity: O(1) as extra space to store answer is not considered.

from typing import List

class Solution:
    # Function to print matrix in spiral manner
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        
        # Number of rows
        n = len(matrix)

         # Number of columns
        m = len(matrix[0])
        
        # Initialize pointers for traversal
        top, left = 0, 0
        bottom, right = n - 1, m - 1
        
        # Traverse the matrix in spiral order
        while top <= bottom and left <= right:
            # Traverse from left to right
            for i in range(left, right + 1):
                ans.append(matrix[top][i])
            top += 1
            
            # Traverse from top to bottom
            for i in range(top, bottom + 1):
                ans.append(matrix[i][right])
            right -= 1
            
            # Traverse from right to left
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    ans.append(matrix[bottom][i])
                bottom -= 1
            
            # Traverse from bottom to top
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    ans.append(matrix[i][left])
                left += 1
        
        #Return the ans
        return ans

# Test the solution
if __name__ == "__main__":
    mat = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    
    # Create an instance of the Solution class
    finder = Solution()
    
    # Get spiral order using class method
    ans = finder.spiralOrder(mat)

    print("Elements in spiral order are:", ans)

'''

class Solution:
    def spiralOrder(self, matrix):
        ans = []
        n=len(matrix)
        m=len(matrix[0])
        top, left = 0, 0
        bottom, right = n-1, m-1
        while top <= bottom and left <= right:
            #left to right
            for i in range(left, right +1):
                ans.append(matrix[top][i])
            top += 1

            #top to bottom
            for i in range(top, bottom + 1):
                ans.append(matrix[i][right])    
            right -= 1

            #right to left
            if top <= bottom:
                for i in range(right, left -1, -1):
                    ans.append(matrix[bottom][i])
                bottom -= 1

            #bottom to top
            if left <= right:
                for i in range(bottom, top-1, -1):
                    ans.append(matrix[i][left])
                left += 1
        return ans
