'''Given an integer array nums of size n, sorted in ascending order with distinct values. The array has been right rotated an unknown number of times, between 0 and n-1 (including). Determine the number of rotations performed on the array.


Examples:
Input : nums = [4, 5, 6, 7, 0, 1, 2, 3]

Output: 4

Explanation: The original array should be [0, 1, 2, 3, 4, 5, 6, 7]. So, we can notice that the array has been rotated 4 times.

Input: nums = [3, 4, 5, 1, 2]

Output: 3

Explanation: The original array should be [1, 2, 3, 4, 5]. So, we can notice that the array has been rotated 3 times.

Input: nums = [4, 5, 1, 2]

Output:
2
Constraints:
 n == nums.length
 1 <= n <= 104
 -104 <= nums[i] <= 104
 All the integers of nums are unique.
 
 #Brute Froce
 Intuition: 
The straightforward solution to this problem involves performing a simple linear search to find the minimum element of the array by comparing each element individually. The index at which the minimum element is found corresponds to the number of times the array has been rotated. Since the array was initially sorted, the smallest element would have been at the front. Therefore, the index of this smallest element gives the number of rotations because it indicates how many positions the array has been shifted.

Approach: 
First, declare an ans and an index variable initialized with a INT_MAX and -1 respectively.
Next, iterate through the array and compare each element with the variable called ‘ans’. Whenever an element is encountered such that it is smaller than ‘ans’, update ‘ans’ with that value and also update the 'index' variable with the current index.
Finally, we will return ‘index’ as our answer.

class Solution:
    """ Function to find the number of
        rotations in a rotated sorted array """
    def findKRotation(self, nums):
        # Get the size of the array
        n = len(nums)
        
        """ Initialize variables to store
            minimum value and its index """
        ans = float('inf')
        index = -1
        
        """ Iterate through the array to
            find the smallest element """
        for i in range(n):
            if nums[i] < ans:
                ans = nums[i] 
                index = i      
        # Return the index of smallest element
        return index

if __name__ == "__main__":
    nums = [4, 5, 6, 7, 0, 1, 2, 3]  
    
    #Create an instance of Solution class
    sol = Solution()
    
    ans = sol.findKRotation(nums)
    
    print(f"The array is rotated {ans} times.")

Complexity Analysis: 
Time Complexity:O(N), where N is size of the array. As the array is being traversed only once using a single loop.

Space Complexity: As no additional space is used, so the Space Complexity is O(1).

#optimal Approach
Intuition: 
The idea here is to use the binary search algorithm to determine the index at which the minimum element of the array is located. This index will indicate the number of times the array has been rotated. Observing this, it's analogous to finding the minimum element in a rotated sorted array. Here, the additional requirement is to return the index of the minimum element rather than the element itself.

Approach: 
First, initialize few variables: low to 0 (beginning of the array, high to (end of the array), ans to Integer.MAX_VALUE to track the minimum element found during the search, index to -1 to store the index of the minimum element.
Use a binary search strategy to efficiently find the minimum element in the rotated sorted array, which directly gives the number of rotations.While low is less than or equal to high, calculate the middle index mid.
If element at `low` is less than or equal to element at `high`, the search space is already sorted. In this case, element at `low` is the smallest element, representing the start of the rotation. Update ans and index accordingly and break out of the loop.
Determine whether the left part of the array is sorted or the right part of the array is sorted
If the left part is sorted (element at (low) <= element at (mid)):
Check if element at (low) is less than `ans`. If so, update `ans` and `index` to reflect the new minimum element found.
Adjust `low` to `mid + 1` to search the right half, as the rotation point (minimum element) must be on the right side.
If the right part is sorted (element at (low) > element at (mid)):
Check if element at (mid) is less than `ans`. If so, update ans and index accordingly.
Adjust high to mid - 1 to search the left half.
Once the loop completes, index will hold the index of the minimum element, which represents the number of rotations.Return index as the answer.

class Solution:
    """ Function to find the number of
        rotations in a rotated sorted array """
    def findKRotation(self, nums):
        low, high = 0, len(nums) - 1
        ans = float('inf')
        index = -1
        while low <= high:
            mid = (low + high) // 2
            
            """ Search space is already sorted
                then nums[low] will always be
                the minimum in that search space """
            if nums[low] <= nums[high]:
                if nums[low] < ans:
                    index = low
                    ans = nums[low]
                break
            
            # If left part is sorted update the ans
            if nums[low] <= nums[mid]:
                if nums[low] < ans:
                    index = low
                    ans = nums[low]
                # Eliminate left half
                low = mid + 1
            else:
                """ update the ans if it 
                    is less than nums[mid] """
                if nums[mid] < ans:
                    index = mid
                    ans = nums[mid]
                # Eliminate right half
                high = mid - 1
        
        # Return the index as answer
        return index

if __name__ == "__main__":
    nums = [4, 5, 6, 7, 0, 1, 2, 3]
    
    # Create an object of the Solution class
    sol = Solution()
    
    ans = sol.findKRotation(nums)
    
    # Print the result
    print(f"The array is rotated {ans} times.")


Complexity Analysis: 
Time Complexity:O(logN), where N is size of the array. As binary search algorithm is being applied to solve the problem.

Space Complexity: As no additional space is used, so the Space Complexity is O(1).


'''
class Solution:
    def findKRotation(self, nums):
        n=len(nums)
        ans = float('inf')
        index = -1
        for i in range(n):
            if nums[i] < ans:
                ans = nums[i]
                index = i
        return index