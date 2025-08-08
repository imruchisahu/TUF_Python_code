'''Given an integer array nums. Return all triplets such that:

i != j, i != k, and j != k
nums[i] + nums[j] + nums[k] == 0.


Notice that the solution set must not contain duplicate triplets. One element can be a part of multiple triplets. The output and the triplets can be returned in any order.


Examples:
Input: nums = [2, -2, 0, 3, -3, 5]

Output: [[-2, 0, 2], [-3, -2, 5], [-3, 0, 3]]

Explanation: nums[1] + nums[2] + nums[0] = 0

nums[4] + nums[1] + nums[5] = 0

nums[4] + nums[2] + nums[3] = 0

Input: nums = [2, -1, -1, 3, -1]

Output: [[-1, -1, 2]]

Explanation: nums[1] + nums[2] + nums[0] = 0

Note that we have used two -1s as they are separate elements with different indexes

But we have not used the -1 at index 4 as that would create a duplicate triplet

Input: nums = [8, -6, 5, 4]

(Give answer with the output and triplets sorted in ascending order)

Output:
[]
Constraints:
1 <= nums.length <= 3000
-104 <= nums[i] <= 104

Similar Problems

Hint 1

Hint 2
Intuition
The most naive idea is to check all possible triplets using 3 loops and among them, consider the ones whose sum is equal to the given target 0.

Before taking them as the answer, sort the triplets in ascending order so as to consider only the unique triplets.

Approach 
Declare a set to store unique triplets that sum up to zero.
Use three nested loops to consider every possible triplet in the array:
Outer loop i runs from 0 to n-3.
Middle loop j runs from i+1 to n-2.
Inner loop k runs from j+1 to n-1.
For each triplet (nums[i], nums[j], nums[k]), check if their sum equals zero.
If yes, sort the triplet to maintain a consistent order and insert it into the set to avoid duplicates.
After processing all triplets, convert the set into a vector and return it as the final result.


Complexity Analyis
Time Complexity: O(N3 x log(no. of unique triplets)), where N is size of the array. Using 3 nested loops & inserting triplets into the set takes O(log(no. of unique triplets)) time complexity. But we are not considering the time complexity of sorting as we are just sorting 3 elements every time.

Space Complexity: O(2 x no. of the unique triplets) for using a set data structure and a list to store the triplets.
from typing import List

class Solution:
    #Function to find triplets having sum equals to target
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Set to store unique triplets
        triplet_set = set()

        n = len(nums)

        # Check all possible triplets
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        # Found a triplet that sums up to target
                        temp = [nums[i], nums[j], nums[k]]
                        
                        """ Sort the triplet to ensure 
                        uniqueness when storing in set"""
                        temp.sort()
                        triplet_set.add(tuple(temp))
        
        # Convert set to list of lists (unique triplets)
        ans = [list(triplet) for triplet in triplet_set]

        #Return the ans
        return ans

if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]

    # Create an instance of Solution class
    sol = Solution()


    ans = sol.threeSum(nums)

    # Print the result
    for triplet in ans:
        print(f"[{', '.join(map(str, triplet))}]")

'''
class Solution:
    def threeSum(self, nums):
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n - 2):
            # Skip duplicate elements for i
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, n - 1

            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                if curr_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # Skip duplicates for left and right
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif curr_sum < 0:
                    left += 1
                else:
                    right -= 1

        return result

