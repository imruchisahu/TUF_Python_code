'''
Given a 0-indexed n x m matrix mat where no two adjacent cells are equal, find any peak element mat[i][j] and return the array [i, j].A peak element in a 2D grid is an element that is strictly greater than all of its adjacent neighbours to the left, right, top, and bottom.



Assume that the entire matrix is surrounded by an outer perimeter with the value -1 in each cell.



Note: As there can be many peak values, 1 is given as output if the returned index is a peak number, otherwise 0.


Examples:
Input: mat=[[10, 20, 15], [21, 30, 14], [7, 16, 32]]

Output: [1, 1]

Explanation: The value at index [1, 1] is 30, which is a peak element because all its neighbours are smaller or equal to it. Similarly, {2, 2} can also be picked as a peak.

Input: mat=[[10, 7], [11, 17]]

Output : [1, 1]

Explanation:The value at index [1, 1] is 17, which is the only peak element because all its neighbours are smaller or equal to it.

Input: mat=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

Output:
[2, 2]
Constraints:
  n == mat.length
  m == mat[i].length
  1 <= m, n <= 500
  1 <= mat[i][j] <= 105
  No two adjacent cells are equal
  
  Intuition: 
The brute-force solution to this problem involves searching for the largest element in the matrix by iterating through all cells. Since the question suggests that no two adjacent elements are equal, the largest element will be the peak element. However, this approach has a time complexity of O(N*M), where N is the number of rows and M is the number of columns.
To optimize the previous solution, binary search can be employed. The intuition behind the peak element in 1-D array can be used here. For each element (mid), we check if it is greater than its previous and next elements. If so, mid is identified as a peak element. Alternatively, if mid is smaller than its previous element, a peak must exist on the left side, so the right half is eliminated. Similarly, if mid is less than the next element, a peak must exist on the right side, so the left half is eliminated. This approach trims down the search space in each iteration, thereby enhancing the time complexity.
Here, for a 2-D array, the search will start from range [0, col-1], where col is the total number of columns in each row. First, find the 'mid' and find out the largest element in column 'mid' and apply the same approach as a 1-D array. That is, if the element at mid is a peak, return it. Otherwise, if the left element is greater, eliminate the right half; otherwise, eliminate the left half.
Approach: 
Working of findPeakElement(matrix):
Use two pointers, low initialized to 0 and high initialized to m - 1, to define the search range across columns.
Execute a loop where low is less than or equal to high and compute mid as (low + high) / 2 to determine the middle column.
Utilize maxElement() function to find the row index where the middle column(mid) has the maximum element and let's call it 'row'.
If element at cell(row,mid) is greater than both neighbors, return {row, mid} as the peak element coordinates.
If the left neighbor is greater than the element at cell(row,mid), adjust high to mid - 1 to search in the left half. Otherwise, adjust low to mid + 1 to search in the right half.
If the loop exits without finding a peak (i.e., low > high), return {-1, -1} to indicate no peak element exists in the matrix.

Working of maxElement(matrix,col):
Start by initializing n to arr.length, which gives the number of rows in the 2D array arr. Initialize max to Integer.MIN_VALUE to store the maximum value found in the specified column col and also initialize index to -1, which will store the index of the row containing the maximum element in the specified column.
Iterate through each row of the 2D array, find the maximum element in the column 'col' of matrix and return its index.

class Solution:
    """Helper function to find the index of the row
    with the maximum element in a given column"""
    def maxElement(self, arr, col):
        n = len(arr)
        max_val = float('-inf')
        index = -1
        
        """Iterate through each row to find the
        maximum element in the specified column"""
        for i in range(n):
            if arr[i][col] > max_val:
                max_val = arr[i][col]
                index = i
                
        # Return the index
        return index
    
    """Function to find a peak element in 
    the 2D matrix using binary search """
    def findPeakGrid(self, arr):
        n = len(arr)    
        m = len(arr[0])  
        
        """Initialize the lower bound for 
        and upper bound for binary search"""
        low = 0           
        high = m - 1      
        
        # Perform binary search on columns
        while low <= high:
            mid = (low + high) // 2 
            
            """Find the index of the row with the 
            maximum element in the middle column"""
            row = self.maxElement(arr, mid)
            
            """ Determine the elements to left and 
            right of middle element in the found row """
            left = arr[row][mid - 1] if mid - 1 >= 0 else float('-inf')
            right = arr[row][mid + 1] if mid + 1 < m else float('-inf')
            
            """ Check if the middle element 
            is greater than its neighbors """
            if arr[row][mid] > left and arr[row][mid] > right:
                return [row, mid]  
            elif left > arr[row][mid]:
                high = mid - 1  
            else:
                low = mid + 1  
        
        # Return [-1, -1] if no peak element is found
        return [-1, -1]

mat = [
    [4, 2, 5, 1, 4, 5],
    [2, 9, 3, 2, 3, 2],
    [1, 7, 6, 0, 1, 3],
    [3, 6, 2, 3, 7, 2]
]

#Create an instance of Solution class
sol = Solution()

# Call findPeakGrid function and print the result
peak = sol.findPeakGrid(mat)
print(f"The row of peak element is {peak[0]} and column of the peak element is {peak[1]}")


Complexity Analysis: 
Time Complexity: O(N * logM), where N is the number of rows in the matrix, M is the number of columns in each row. The complexity arises because binary search is performed on the columns, and for each mid column, a linear search through the rows is executed to find the maximum element.

Space Complexity: As no additional space is used, so the Space Complexity is O(1).'''

class Solution:
    def maxElement(self, arr, col):
        n = len(arr)
        max_val = float('-inf')
        index = -1
        for i in range(n):
            if arr[i][col] > max_val:
                max_val = arr[i][col]
                index = i
        return index
    def findPeakGrid(self, arr):
        n = len(arr)    
        m = len(arr[0])  
        low = 0           
        high = m - 1      
        while low <= high:
            mid = (low + high) // 2 
            row = self.maxElement(arr, mid)
            left = arr[row][mid - 1] if mid - 1 >= 0 else float('-inf')
            right = arr[row][mid + 1] if mid + 1 < m else float('-inf')
    
            if arr[row][mid] > left and arr[row][mid] > right:
                return [row, mid]  
            elif left > arr[row][mid]:
                high = mid - 1  
            else:
                low = mid + 1  
        return [-1, -1]