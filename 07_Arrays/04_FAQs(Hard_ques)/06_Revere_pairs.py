'''Given an integer array nums. Return the number of reverse pairs in the array.



An index pair (i, j) is called a reverse pair if:



0 <= i < j < nums.length


nums[i] > 2 * nums[j]



Examples:
Input: nums = [6, 4, 1, 2, 7]

Output: 3

Explanation: The reverse pairs are:

(0, 2) : nums[0] = 6, nums[2] = 1, 6 > 2 * 1

(0, 3) : nums[0] = 6, nums[3] = 2, 6 > 2 * 2

(1, 2) : nums[1] = 4, nums[2] = 1, 4 > 2 * 1

Input: nums = [5, 4, 4, 3, 3]

Output: 0

Explanation: No pairs satisfy both the conditons.

Input: nums = [6, 4, 4, 2, 2]

Output:
2
Constraints:
1 <= nums.length <= 5 * 104
-231 <= nums[i] <= 231 - 1

Hint 1

Hint 2
Intuition
The straightforward approach to solve this problem is to iterate through each element in the array and run an inner loop say(j) to check all subsequent elements arr[j], if the condition arr[i] > 2 x arr[j] holds true, where i is the parent loop, then it is a reverse pair otherwise it's not a reverse pair.

Approach
iterate in the array from 0 to N-1 to select the arr[i]. As index j should be greater than index i, inside loop i, run another loop i.e. j from i+1 to N-1, and select the element arr[j].
Inside this second loop, check if arr[i] is greater than 2*arr[j] i.e. if arr[i] and arr[j] can be a pair. If they satisfy the condition, increase the count by 1. Finally, return the count as our answer.


Complexity Analysis 
Time Complexity: O(N2), where N is size of the given array. For using nested loops here and those two loops roughly run for N times.

Space Complexity: O(1), no extra space is used to solve this problem.

from typing import List

class Solution:
    """ Function to count reverse
    pairs where a[i] > 2 * a[j]"""
    def reversePairs(self, nums: List[int]) -> int:
        
        # Call countPairs with the list and its length
        return self.countPairs(nums, len(nums))
    
    """ Helper function to count pairs
    satisfying the condition a[i] > 2 * a[j]"""
    def countPairs(self, nums: List[int], n: int) -> int:
        
        # Initialize count of reverse pairs
        cnt = 0
        
        """ Nested loops to check each
        pair (i, j) where i < j"""
        for i in range(n):
            for j in range(i + 1, n):
                
                """ Check if the condition 
                a[i] > 2 * a[j] holds"""
                if nums[i] > 2 * nums[j]:
                    
                    """ Increment count if
                    condition is satisfied"""
                    cnt += 1
                    
        # Return the total count of reverse pairs
        return cnt

if __name__ == "__main__":
    nums = [6, 4, 1, 2, 7]
    
    # Create an instance of the Solution class
    sol = Solution()
    
    cnt = sol.reversePairs(nums)
    
    # Output the result
    print("The number of reverse pairs is:", cnt)


'''
class Solution:
    def reversePairs(self, nums):
        return self.merge_sort(nums, 0, len(nums) - 1)

    # Merge sort with reverse pair count
    def merge_sort(self, nums, low, high):
        if low >= high:
            return 0

        mid = (low + high) // 2
        cnt = 0
        cnt += self.merge_sort(nums, low, mid)
        cnt += self.merge_sort(nums, mid + 1, high)
        cnt += self.count_pairs(nums, low, mid, high)
        self.merge(nums, low, mid, high)

        return cnt

    # Count reverse pairs across two sorted halves
    def count_pairs(self, nums, low, mid, high):
        right = mid + 1
        cnt = 0

        for i in range(low, mid + 1):
            while right <= high and nums[i] > 2 * nums[right]:
                right += 1
            cnt += right - (mid + 1)

        return cnt

    # Merge function
    def merge(self, nums, low, mid, high):
        temp = []
        left, right = low, mid + 1

        while left <= mid and right <= high:
            if nums[left] <= nums[right]:
                temp.append(nums[left])
                left += 1
            else:
                temp.append(nums[right])
                right += 1

        while left <= mid:
            temp.append(nums[left])
            left += 1
        while right <= high:
            temp.append(nums[right])
            right += 1

        nums[low:high + 1] = temp
#TC=(2Nlog N)
#SC=O(N)