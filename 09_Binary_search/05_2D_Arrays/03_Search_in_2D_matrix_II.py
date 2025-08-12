'''Given a 2D array matrix where each row is sorted in ascending order from left to right and each column is sorted in ascending order from top to bottom, write an efficient algorithm to search for a specific integer target in the matrix.


Examples:
Input: matrix = [ [1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30] ], target = 5

Output: True

Explanation: The target 5 exists in the matrix in the index (1,1)

Input: matrix= [ [1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30] ], target = 20

Output: False

Explanation: The target 20 does not exist in the matrix.

Input: matrix= [ [1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30] ], target = 1

Output:
True
Constraints:
  n == matrix.length
  m == matrix[i].length
  1 <= n, m <= 300
  -109 <= matrix[i][j] <= 109
  All the integers in each row are sorted in ascending order.
  All the integers in each column are sorted in ascending order.
  -109 <= target <= 109
  
  
  #Better

  Intuition: 
Since the given matrix is sorted (both row-wise and column-wise), this information can be used to optimize the brute-force solution. The brute-force approach involves checking each cell of the matrix for the given target, similar to how it was done in the problem Search in 2D matrix. Here, to optimize the solution, use binary search in each row of the matrix to search for the target. If the target is found return true, else return false.

Approach: 
Working of searchMatrix(matrix, target):
Traverse each row of the matrix using a for loop.
Next, for every row, check if it contains the target using binary search.
After applying binary search on the row, if the target is found, return true. Otherwise, move on to the next row, as the target might be present there.
Finally, after completing all the row traversals, if no matching element is found, return false.

Working of binarySearch(arr, target):
First initialize low to 0 and and high to the last column index. This will define the search range of the binary search.
While low is less than or equal to high, calculate 'mid' and check if the element at mid is equal to target, if so, return true. Otherwise, if element at mid is greater than target, eliminate the right half, else eliminate the left half.
class Solution:
    # Helper function to perform binary search
    def binarySearch(self, nums, target):
        n = len(nums)
        low, high = 0, n - 1
        
        # Perform the steps:
        while low <= high:
            mid = (low + high) // 2
            
            # Return true if target is found
            if nums[mid] == target:
                return True
            elif target > nums[mid]:
                low = mid + 1
            else:
                high = mid - 1
        
        # Return false if target not found
        return False
    
    # Function to search for a given target in matrix
    def searchMatrix(self, matrix, target):
        n = len(matrix)
        m = len(matrix[0])
        
        # Traverse through each row
        for i in range(n):
            
            """ Check if target is 
            present in the current row"""
            flag = self.binarySearch(matrix[i], target)
            
            if flag:
                return True
        
        # Return false if target is not found
        return False

if __name__ == "__main__":
    matrix = [[1, 4, 7, 11, 15], 
              [2, 5, 8, 12, 19],
              [3, 6, 9, 16, 22],
              [10, 13, 14, 17, 24],
              [18, 21, 23, 26, 30]]
    target = 8
    
    # Create an instance of Solution class
    sol = Solution()
    
    result = sol.searchMatrix(matrix, target)
    
    # Output the result
    print("true" if result else "false")

Complexity Analysis: 
Time Complexity: O(N * logM), where N is the number of rows in the matrix, M is the number of columns in each row. All rows are traversed in O(N) time complexity, and binary search is applied to each row. Therefore, the total time complexity is O(N*logM).

Space Complexity: As no additional space is used, so the Space Complexity is O(1).


#optimal
# 
# Intuition: 
Here, the idea is to utilize the information that the matrix is sorted both row-wise (increasing from left to right) and column-wise (increasing from top to bottom). One corner of the matrix is chosen from (0, 0), (0, m-1), (n-1, 0), and (n-1, m-1). This selection ensures that moving in one direction (either vertically or horizontally) from this corner will lead only to smaller elements, while moving in the other direction will lead only to larger elements relative to the element at the chosen corner.
This strategy enhances traversal efficiency: if the element at the corner is smaller than the target, move in the direction where larger elements are present; if the element at the corner is greater than the target, move in the direction where smaller elements are present. If neither condition applies, it indicates that the corner element is the target, and true should be returned.

How to choose starting corners:
Assume n is the row number and m is the number of columns in each row.
Cell (0, 0): Assume traversal starts from (0, 0) and the search target is 14. Since both the row and column are sorted in increasing order, it cannot be determined whether to proceed row-wise or column-wise. Therefore, traversal cannot be started from (0, 0).
Cell (0, m-1): Assume traversal starts from (0, m-1) and the search target is 14. In this case, the row is in decreasing order and the column is in increasing order. Therefore, if traversal begins from (0, m-1), the direction of movement can be easily determined based on these conditions.
If matrix[0][m-1] is greater than target: Move row-wise.
If matrix[0][m-1] is smaller than target: Bigger elements are needed, so move column-wise.
Cell (n-1, m-1): Assume traversal starts from (n-1, m-1) and the search target is 14. Since both the row and column are sorted in decreasing order, it cannot be determined whether to proceed row-wise or column-wise. Therefore, traversal cannot be started from (n-1, m-1).>/li>
Cell (n-1, 0): Assume traversal starts from (n-1, 0) and the search target is 14. In this case, the row is in increasing order and the column is in decreasing order. Therefore, if traversal begins from (n-1, 0), the direction of movement can be easily determined based on these conditions.>/li>
If matrix[n-1][0] is smaller than target: Move row-wise.
If matrix[n-1][0] is greater than target: Smaller elements are needed, move column-wise.
From the above observations, it is quite clear that matrix traversal should be started from either the cell (0, m-1) or (n-1, 0).
Approach: 
Let us take starting cell as (0, m-1), the two variables i.e. ‘row’ and ‘col’ will point to 0 and m-1 respectively.
Initialize a while loop, which will run till 'row' is less than n(total rows in the matrix) and 'col' is greater than or equal to 0.
If the element at the cell (row, col) is equal to target, return true as the target has been found.
If the element at the cell (row, col) is geater than target, it means smaller elements are needed to reach the target. But the column is in increasing order and so it contains only greater elements. So, eliminate the column by decreasing the current column value by 1(i.e. col--) and thus, move row-wise.
If the element at the cell (row, col) is smaller than target, it suggests that bigger elements are needed to reach the target. But the row is in decreasing order and so it contains only smaller elements. So, eliminate the row by increasing the current row value by 1(i.e. row++) and thus move column-wise.
If the loop terminates without getting any matching element, return false.

class Solution:
    
    # Function to search for a given target in matrix
    def searchMatrix(self, matrix, target):
        n = len(matrix)
        m = len(matrix[0])
        
        # Initialize the row and col
        row, col = 0, m - 1

        # Traverse the matrix from (0, m-1):
        while row < n and col >= 0:
            
            # Return true if target is found
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                row += 1
            else:
                col -= 1
        
        # Return false if target not found
        return False

if __name__ == "__main__":
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    target = 8
    
    # Create an instance of Solution class
    sol = Solution()
    
    result = sol.searchMatrix(matrix, target)
    
    # Output the result
    print("true" if result else "false")

    
Complexity Analysis: 
Time Complexity: O(N + M), where N is the number of rows in the matrix, M is the number of columns in each row. Traversal starts from (0, M-1), and at most, it can end up in the cell (M-1, 0). Therefore, the total distance can be at most (N+M). Hence, the time complexity is O(N+M).

Space Complexity: As no additional space is used, so the Space Complexity is O(1).


'''
class Solution:
    def searchMatrix(self, matrix, target):
        n = len(matrix)
        m = len(matrix[0])
        row, col = 0, m - 1
        while row < n and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                row += 1
            else:
                col -= 1
        return False