'''Given a binary array nums, return the maximum number of consecutive 1s in the array.



A binary array is an array that contains only 0s and 1s.


Examples:
Input: nums = [1, 1, 0, 0, 1, 1, 1, 0]

Output: 3

Explanation: The maximum consecutive 1s are present from index 4 to index 6, amounting to 3 1s

Input: nums = [0, 0, 0, 0, 0, 0, 0, 0]

Output: 0

Explanation: No 1s are present in nums, thus we return 0

Input: nums = [1, 0, 1, 1, 1, 0, 1, 1, 1]

Output:
3
Constraints:
1 <= nums.length <= 105
nums[i] is either 0 or 1.

Similar Problems

Hint 1

Hint 2
Intuition
To find the number of maximum consecutive 1s, the idea is to count the number of 1s each time we encounter them and update the maximum number of 1s. On encountering any 0, reset the count to 0 again so as to count the next consecutive 1s.

Approach 
Initialize two variables, count and max_count to 0. Traverse the array and if the current element is 1, increment the count by 1.
Update max_count if count is greater than max_count.
If the current element is 0, reset the count variable to 0 and at last return max_count.

Complexity Analysis 
Time Complexity: O(N), as there is single traversal of the array .Here N is the number of elements in the array.
Space Complexity: O(1), as no additional space is used .
from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        #Initialize count and max_count to track current and maximum consecutive 1s 
        cnt = 0
        maxi = 0

        # Traverse the array
        for num in nums:
            # If the current element is 1, increment the count
            if num == 1:
                cnt += 1

                # Update maxi if current count is greater than maxi
                maxi = max(maxi, cnt)

            else:
                # If the current element is 0, reset the count
                cnt = 0

        # Return the maximum count of consecutive 1s
        return maxi

# Main function
if __name__ == "__main__":
   
    nums = [1, 1, 0, 1, 1, 1]

    # Create an instance of the Solution class
    sol = Solution()

    # Find and print the maximum consecutive 1s
    ans = sol.findMaxConsecutiveOnes(nums)
    print("The maximum consecutive 1's are", ans)



'''
class Solution:
    def findMaxConsecutiveOnes(self, nums):
        max_count = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 0
        return max_count
        