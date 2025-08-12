'''
Given a 2D array matrix that is row-wise sorted. The task is to find the median of the given matrix.


Examples:
Input: matrix=[ [1, 4, 9], [2, 5, 6], [3, 7, 8] ] 

Output: 5

Explanation: If we find the linear sorted array, the array becomes 1 2 3 4 5 6 7 8 9. So, median = 5

Input: matrix=[ [1, 3, 8], [2, 3, 4], [1, 2, 5] ] 

Output: 3

Explanation: If we find the linear sorted array, the array becomes 1 1 2 2 3 3 4 5 8. So, median = 3

Input: matrix=[ [1, 4, 15], [2, 5, 6], [3, 8, 11] ] 

Output:
5
Constraints:
  N==matrix.size
  M==matrix[0].size
  1 <= N, M <= 105
  1 <= N*M <= 106
  1 <= matrix[i] <= 109
 N*M is odd


 #Brute
 Intuition: 
The brute force approach is based on the most straightforward idea: if we can gather all elements from the matrix into a single list and sort them, the median will simply be the middle element of that sorted list.

This approach doesn't take advantage of the matrix being row-wise sorted, but it guarantees correctness and is simple to implement.

Approach: 
Flatten the Matrix:
Loop through each row of the matrix and append its elements to a new list.
This gives us a one-dimensional array containing all matrix elements.
Sort the Array:
Sort the flattened list using any efficient sorting algorithm (e.g., Timsort in Python).
This will arrange the elements in non-decreasing order.
Find the Median:
Since the total number of elements is n * m, the median will be at index (n * m) // 2 in the sorted list.

class Solution:
    def findMedian(self, matrix):
        # Step 1: Flatten the matrix into a single list
        flattened = []
        for row in matrix:
            flattened.extend(row)

        # Step 2: Sort the flattened list
        flattened.sort()

        # Step 3: Return the middle element
        n = len(flattened)
        return flattened[n // 2]

# Driver code
if __name__ == "__main__":
    matrix = [
        [1, 3, 5],
        [2, 6, 9],
        [3, 6, 9]
    ]
    sol = Solution()
    print(sol.findMedian(matrix))  # Output: 5

    
Complexity Analysis: 
Time Complexity: O(n * m * log(n * m)), as Flattening the matrix takes O(n * m) time and Sorting the flattened list takes O(n * m * log(n * m)) time.

Space Complexity: O(n * m), Extra space is required to store the flattened list of matrix elements.


#optimal
Intuition: 
In the naive approach, we can flatten the matrix into a 1D array and sort the array. After sorting, the median can be directly obtained by selecting the middle element of the sorted array.

For odd-length matrices, the median is simply the element at position (n * m) // 2 in the sorted array.
For even-length matrices, the median is the average of the two middle elements in the sorted array.
Approach: 
Flatten the Matrix: Convert the matrix into a single linear array by traversing each row and column.
Sort the Array: Sort the 1D array in ascending order.
Find the Median:
For an odd-length matrix, return the element at index (n * m) // 2.
For an even-length matrix, return the average of the two middle elements.

class Solution:
    # Function to find the upper bound of an element in a row
    def upperBound(self, arr, x, m):
        low, high = 0, m - 1
        ans = m

        # Apply binary search
        while low <= high:
            mid = (low + high) // 2

            # If arr[mid] > x, it can be a possible upper bound
            if arr[mid] > x:
                ans = mid
                # Look for smaller bound on the left
                high = mid - 1
            else:
                low = mid + 1

        return ans

    # Function to count how many elements in matrix are less than or equal to x
    def countSmallEqual(self, matrix, n, m, x):
        cnt = 0
        for i in range(n):
            cnt += self.upperBound(matrix[i], x, m)
        return cnt

    # Function to find the median in the matrix
    def findMedian(self, matrix):
        n, m = len(matrix), len(matrix[0])
        low, high = float('inf'), float('-inf')

        # Find the minimum and maximum values
        for i in range(n):
            low = min(low, matrix[i][0])
            high = max(high, matrix[i][m - 1])

        req = (n * m) // 2

        # Binary search to find the median
        while low <= high:
            mid = (low + high) // 2

            smallEqual = self.countSmallEqual(matrix, n, m, mid)

            if smallEqual <= req:
                low = mid + 1
            else:
                high = mid - 1

        return low

# Driver code
if __name__ == "__main__":
    matrix = [
        [1, 2, 3, 4, 5],
        [8, 9, 11, 12, 13],
        [21, 23, 25, 27, 29]
    ]

    sol = Solution()
    result = sol.findMedian(matrix)
    print("The median element is:", result)

    
Complexity Analysis: 
Time Complexity: O(log(max)) * O(N(logM)), where N is the number of rows in the matrix, M is the number of columns in each row. Our search space ranges from [min, max], where min is the minimum and max is the maximum element of the matrix. Binary search is applied within this search space, which operates with a time complexity of O(log(max)). Then, the countSmallEqual() function is called for each 'mid', which has a time complexity of O(N*log(M)).

Space Complexity: As no additional space is used, so the Space Complexity is O(1).

 '''
class Solution:
    def findMedian(self, matrix):
        flattened = []
        for row in matrix:
            flattened.extend(row)
        flattened.sort()
        n = len(flattened)
        return flattened[n // 2]