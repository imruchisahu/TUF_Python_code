'''Given an integer array nums of size N, sorted in ascending order with distinct values, and then rotated an unknown number of times (between 1 and N), find the minimum element in the array.


Examples:
Input : nums = [4, 5, 6, 7, 0, 1, 2, 3]

Output: 0

Explanation: Here, the element 0 is the minimum element in the array.

Input : nums = [3, 4, 5, 1, 2]

Output: 1

Explanation:Here, the element 1 is the minimum element in the array.

Input : nums = [4, 5, 6, 7, -7, 1, 2, 3]

Output:
-7
Constraints:
n == nums.length
 1 <= n <= 104
 -104 <= nums[i] <= 104
 All the integers of nums are unique.
 nums is sorted and rotated between 1 and n times.
 
 #Linear Search Approach
 Intuition: 
The idea here is to use simple linear search to fnd out the minimum element among the array elements.

Approach: 
Begin by initializing mini to INT_MAX, which is the maximum possible value for integers. This ensures that any element in the array will be smaller than mini initially.
Use a for loop to iterate through each element in the array. For each element, update `mini` using the min function. This function compares the current value of mini with the current element and assigns the smaller value back to `mini`. This effectively finds the smallest element encountered so far in the array.
Continue iterating until all elements of the array have been processed. Each iteration ensures that `mini` retains the smallest value found among the elements seen so far. Return this value as the result of the function.
class Solution:
    # Function to find minimum element in a list
    def findMin(self, arr):
        
        # Initialize mini to maximum float value
        mini = float('inf') 
        for num in arr:
            
            """ Update mini with the
            smaller of mini and num"""
            mini = min(mini, num) 
        # Return the minimum element found
        return mini 

if __name__ == "__main__":
    arr = [4, 5, 6, 7, 0, 1, 2, 3]
    
     # Create an object of the Solution class
    sol = Solution()
    
    ans = sol.findMin(arr) 
    
    # Print the result
    print("The minimum element is:", ans) 


Complexity Analysis: 
Time Complexity:O(N), where N is size of the array. As the array is being traversed only once using a single loop.

Space Complexity:O(1), As no additiona

#Binary Search Approach
Intuition: 
As the given array is sorted and then rotated, we can optimize the brute-force solution by applying the binary search algorithm. In any sorted array, the minimum element is located at the very first index. This observation allows us to reduce the search space by half in each iteration. The task is to identify the sorted half of the array, store its minimum element (which is the first element of this half), and then eliminate this half from our search space.

Approach: 
First, initialize few variables: low to 0 and high to sizeOfArray - 1, which represent the indices of the array arr that define the current search range, ans to Integer.MAX_VALUE, which ensures that any element in the array will be smaller than ans initially.
Use a while loop to continue searching while low is less than or equal to high. This ensures that the search space is valid and non-empty. Compute the midpoint mid of the current search range using mid = (low + high) / 2 or mid = low + (high-low)/2.
Compare element at (low) with element at (mid). If element at (low) is less than or equal to element at (mid), then the left part from low to mid is sorted:
Update ans with the minimum of its current value and element at (low). This step ensures that ans always holds the smallest element encountered in the sorted part of the array.
Move the low pointer to mid + 1 to search in the right part of the array, as the minimum element cannot be in the left part (which is already sorted).
If the left part is not sorted (element at (low) is greater than element at (mid)), then the right part from mid to high is sorted:
Update ans with the minimum of its current value and element at (mid). This ensures ans contains the smallest element encountered in the sorted part of the array.
Move the high pointer to mid - 1 to search in the left part of the array, as the minimum element cannot be in the right part (which is already sorted).
Once the loop completes,` ans` will contain the smallest element found in the rotated sorted array. Return `ans` as the minimum element in the rotated sorted array.
class Solution:
    """ Function to find minimum element
        in a rotated sorted array """
    def findMin(self, arr):
        # Initialize low and high indices
        low, high = 0, len(arr) - 1
        
        # Initialize ans to maximum integer value
        ans = float('inf')
        while low <= high:
            mid = (low + high) // 2
            
            # Check if left part is sorted
            if arr[low] <= arr[mid]:
                """ Update ans with minimum 
                    of ans and arr[low] """
                ans = min(ans, arr[low])
                
                # Move to the right part
                low = mid + 1
            else:
                """ Update ans with minimum 
                    of ans and arr[mid] """
                ans = min(ans, arr[mid])
                
                # Move to the left part
                high = mid - 1
        
        # Return the minimum element found
        return ans

if __name__ == "__main__":
    arr = [4, 5, 6, 7, 0, 1, 2, 3]
    
    #Create an instance of the Solution class
    sol = Solution()
    
    ans = sol.findMin(arr)
    
    print("The minimum element is:", ans)


Complexity Analysis: 
Time Complexity:O(log(N)), where N is size of the array. Because binary search is being used.

Space Complexity:O(1) As no additional space is used.
 '''

class Solution:
    def findMin(self, arr):
        mini=float('inf')
        for num in arr:
            mini = min(mini, num)
        return mini