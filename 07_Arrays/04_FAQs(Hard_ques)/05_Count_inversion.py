'''Given an integer array nums. Return the number of inversions in the array.



Two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.

It indicates how close an array is to being sorted.
A sorted array has an inversion count of 0.
An array sorted in descending order has maximum inversion.

Examples:
Input: nums = [2, 3, 7, 1, 3, 5]

Output: 5

Explanation: The responsible indexes are:

nums[0], nums[3], values: 2 > 1 & indexes: 0 < 3

nums[1], nums[3], values: 3 > 1 & indexes: 1 < 3

nums[2], nums[3], values: 7 > 1 & indexes: 2 < 3

nums[2], nums[4], values: 7 > 3 & indexes: 2 < 4

nums[2], nums[5], values: 7 > 5 & indexes: 2 < 5

Input: nums = [-10, -5, 6, 11, 15, 17]

Output: 0

Explanation: nums is sorted, hence no inversions present.

Input: nums = [9, 5, 4, 2]

Output:
6
Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104

Hint 1

Hint 2

Intuition 
The naive approach is pretty straightforward, which will use nested loops to solve this problem. The prerequisite is that the index i must be smaller than index j. So, fix i at one index, and with another loop say(j), which runs from i+1 to last index of the array, try to count the inversion pairs.

Approach 
Iterate in array from 0 to N-1 to select the first element in the pair. As index j should be greater than index i, inside loop i, run another loop i.e. j from i+1 to N-1. Inside this second loop, check if arr[i] is greater than arr[j] i.e. if arr[i] and arr[j] can be an inversion pair. If it satisfy the condition, increase the count by 1.
Finally, return the count i.e. the number of such pairs.


Complexity Analysis 
Time Complexity: O(N2), for using 2 nested loops, where N is the size of the array.

Space Complexity: O(1), no extra space is used.

from typing import List

class Solution:
    # Function to find number of inversions in an array
     def numberOfInversions(self, nums: List[int]) -> int:
        
        # Size of the array
        n = len(nums)

        # Count the number of pairs
        cnt = 0

        for i in range(n):
            for j in range(i + 1, n):
                
                """ If nums[i] is greater than 
                nums[j], increase count by 1"""
                if nums[i] > nums[j]:
                    cnt += 1

        # Return the count of inversions
        return cnt

# Main function
if __name__ == "__main__":
    nums = [5, 4, 3, 2, 1]
    
    # Create an instance of Solution class
    sol = Solution()

    result = sol.numberOfInversions(nums)
    
    # Print the number of inversions found
    print(f"The number of inversions is: {result}")

'''
class Solution:
    def numberOfInversions(self, nums):
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr, 0
            mid = len(arr) // 2
            left, inv_left = merge_sort(arr[:mid])
            right, inv_right = merge_sort(arr[mid:])
            merged, inv_merge = merge(left, right)
            return merged, inv_left + inv_right + inv_merge

        def merge(left, right):
            merged = []
            i = j = inv_count = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    inv_count += len(left) - i
                    j += 1
            merged.extend(left[i:])
            merged.extend(right[j:])
            return merged, inv_count

        _, total_inversions = merge_sort(nums)
        return total_inversions
#TC=O(N log N)
#SC= O(1)