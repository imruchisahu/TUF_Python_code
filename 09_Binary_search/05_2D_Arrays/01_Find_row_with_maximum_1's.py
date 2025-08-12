'''
Given a non-empty grid mat consisting of only 0s and 1s, where all the rows are sorted in ascending order, find the index of the row with the maximum number of ones.

If two rows have the same number of ones, consider the one with a smaller index. If no 1 exists in the matrix, return -1.


Examples:
Input : mat = [ [1, 1, 1], [0, 0, 1], [0, 0, 0] ]

Output: 0

Explanation: The row with the maximum number of ones is 0 (0 - indexed).

Input: mat = [ [0, 0], [0, 0] ]

Output: -1

Explanation: The matrix does not contain any 1. So, -1 is the answer.

Input : mat = [ [0, 0, 1], [0, 1, 1], [0, 1, 1] ]

Output:
-1
0
2
1

Submit
Constraints:
  n == mat.length 
  m == mat[i].length 
  1 <= n, m <= 100 
  mat[i][j] is either 0 or 1.
  
  #Linear Search
  
  Intuition: 
The extremely naive approach is to traverse the matrix as usual using nested loops and for every single row count the number of 1’s. Finally, return the row with the maximum no. of 1’s. If multiple rows contain the maximum no. of 1’s, return the row with the minimum index.

Approach: 
First, declare two variables: cnt_max initialized with 0 to store the maximum number of 1’s found and index initialized with -1 to store the row number.
Next, start traversing the matrix using nested loops to get each cell of the matrix. For each row count the number of 1's.
After that, compare it with cnt_max and if the current number of 1’s is greater, update cnt_max with the current no. of 1’s and ‘index’ with the current row index.
Finally, return the variable ‘index’. It will store the index of the row with the maximum no. of 1’s. And otherwise, it will store -1 if there is no 1's in the matrix at all.

class Solution:
    """ Function to find the row 
    with the maximum number of 1's"""
    def rowWithMax1s(self, mat):
        n = len(mat)
        m = len(mat[0])
        """ Variable to store the 
        maximum count of 1's found"""
        cnt_max = 0 
        
        """ Variable to store the index
        of the row with max 1's"""
        index = -1  

        # Traverse the matrix row by row
        for i in range(n):
            
            """ Counter for 1's 
            in the current row"""
            cnt_ones = 0 

            """ Count the number of 
            1's in the current row"""
            for j in range(m):
                cnt_ones += mat[i][j]

            """ Update cnt_max and index if current
            row has more 1's than previously found"""
            if cnt_ones > cnt_max:
                cnt_max = cnt_ones
                index = i

        """ Return the index of the row 
        with the maximum number of 1's"""
        return index

if __name__ == "__main__":
    matrix = [[1, 1, 1], [0, 0, 1], [0, 0, 0]]
    
    # Create an instance of the Solution class
    sol = Solution()
    
    # Print the answer
    print("The row with maximum number of 1's is:", sol.rowWithMax1s(matrix))

Complexity Analysis: 
Time Complexity: O(N X M), where N is the number of rows in the matrix, M is the number of columns in each row. As, nested loops are being used to traverse the matrix.

Space Complexity: As no additional space is used, so the Space Complexity is O(1).


#Binary search

Intuition: 
The idea here is to use Binary Search to optimize the brute-force solution where linear search was being used. Since, each row of the given matrix is sorted, Binary Search can be applied on each row to find the Lower Bound of 1, as lower bound gives the very first index such that element on that index is either equal to 1 or greater than 1. So, total number of 1's in each row can be calculated as: lower bound of 1 subtracted from total number of columns. Do the same of each row and return the index of row having maximum 1's or in case of multiple rows having maximum 1's, return the smallest index. Finally, if there is no 1 in the matrix return -1.

Approach: 
Working of rowWithMax1s(matrix):
First, declare two variables: cnt_max initialized with 0 to store the maximum number of 1’s found and index initialized with -1 to store the row number.
Next, start traversing the rows of the matrix using a for loop. For each row call the lowerBound() function to get the first occurrence of 1(0 based indexing). Calculate the total number of 1's in each row by subtraction the first occurrence of 1 from total columns.
After that, compare it with cnt_max and if the current number of 1’s is greater, update cnt_max with the current no. of 1’s and ‘index’ with the current row index.
Finally, return the variable ‘index’. It will store the index of the row with the maximum no. of 1’s. And otherwise, it will store -1 if there is no 1's in the matrix at all.

Working of lowerBound(arr, n, x):
Start with initializing low = 0 and high = n - 1, where n is the total columns of the matrix. Initialize 'ans' to n, which serves as the default answer assuming no element in the array is greater than or equal to x.
Initialize a while loop to perform binary search until low exceeds high. Calculate the 'mid' index as (low + high) / 2.
If arr[mid] greater than or equal to x. This means it's a potential candidate for being the lower bound (first element that is not less than x). Update ans to mid, indicating that we found a potential lower bound. Then adjust high to mid - 1 to search for a potentially smaller lower bound on the left side of mid. Otherwise, move low to mid + 1 to search for the lower bound on the right side of mid.
When the while loop terminates, return 'ans'.
class Solution:
    # Helper function to find the lower bound of 1.
    def lowerBound(self,arr, n, x):
        low, high = 0, n - 1
        ans = n

        while low <= high:
            mid = (low + high) // 2
                
            """If element at mid is greater than or equal 
            to x then it could be a possible answer."""
            if arr[mid] >= x:
                ans = mid
                    
                # Look for smaller index on the left
                high = mid - 1
            else:
                low = mid + 1
            
        # Return the answer
        return ans
        
    """ Function to find the row 
    with the maximum number of 1's"""
    def rowWithMax1s(self, mat):
        n = len(mat)
        m = len(mat[0])
        
        """ Variable to store the 
        maximum count of 1's found"""
        cnt_max = 0 
        
        """ Variable to store the index
        of the row with max 1's"""
        index = -1  

        # Traverse each row of the matrix
        for i in range(n):
            # Get the number of 1's
            cnt_ones = m - self.lowerBound(mat[i], m, 1)
            
            """ If the current count is greater than 
            maximum, store the index of current row
            and update the maximum count."""
            if cnt_ones > cnt_max:
                cnt_max = cnt_ones
                index = i
        
        """ Return the index of the row 
        with the maximum number of 1's"""
        return index

if __name__ == "__main__":
    matrix = [[1, 1, 1], [0, 0, 1], [0, 0, 0]]
    
    # Create an instance of the Solution class
    sol = Solution()
    
    # Print the answer
    print("The row with maximum number of 1's is:", sol.rowWithMax1s(matrix))


Complexity Analysis: 
Time Complexity:O(N * logM), where N is the number of rows in the matrix, M is the number of columns in each row. As, each row is being traversed once and then binary search is being applied for M columns of every row.

Space Complexity: As no additional space is used, so the Space Complexity is O(1).

'''
class Solution:
    def lowerBound(self, arr, n, x):
        low, high = 0, n-1
        ans = n
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] >= x:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
    def rowWithMax1s(self, mat):
        n=len(mat)
        m=len(mat[0])
        cnt_max = 0
        index = -1
        for i in range(n):
            cnt_ones = m - self.lowerBound(mat[i], m, 1)
            if cnt_ones > cnt_max:
                cnt_max = cnt_ones
                index = i
        return index
       