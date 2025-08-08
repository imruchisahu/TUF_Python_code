'''Given an integer array nums and an integer target. Return all quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

·      a, b, c, d are all distinct valid indices of nums.

·      nums[a] + nums[b] + nums[c] + nums[d] == target.



Notice that the solution set must not contain duplicate quadruplets. One element can be a part of multiple quadruplets. The output and the quadruplets can be returned in any order.


Examples:
Input: nums = [1, -2, 3, 5, 7, 9], target = 7

Output: [[-2, 1, 3, 5]]

Explanation: nums[1] + nums[0] + nums[2] + nums[3] = 7

Input: nums = [7, -7, 1, 2, 14, 3], target = 9

Output: []

Explanation: No quadruplets are present which add upto 9

Input: nums = [1, 1, 3, 4, -3], target = 5

(Give answer with the output and quadruplets sorted in ascending order)

Output:
[[-3, 1, 3, 4]]
Constraints:
1 <= nums.length <= 200
-104 <= nums[i] <= 104
-104 <= target <= 104

Similar Problems

Hint 1

Hint 2
Intuition
The idea is to check all possible quadruplets and among them, consider the ones whose sum is equal to the given target. And before considering them as our answer, sort the quadruplets in ascending order.

Approach 
For getting quadruplets, 4 nested loops will be used.
The first loop(say i) will run from 0 to n-1. Inside which, there will be the second loop(say j) that will run from i+1 to n-1. The third loop(say k) that runs from j+1 to n-1. Inside loop k, the fourth loop(say l) will run from k+1 to n-1, yielding 4 elements from array for considering a quadruplet.
Now, inside these four nested loops, check the sum of arr[i], arr[j], arr[k] and arr[l], and if it is equal to the target, sort this quadruplet and insert it in the set data structure declared to store ans. Finally, return a list of stored quadruplets.


Complexity Analysis 
Time Complexity: O(N4) for using 4 nested loops, where N is size of the array.

Space Complexity: O(2 x no. of the quadruplets), for using a set data structure and a list to store the quads.
from typing import List

class Solution:
    #function to find quadruplets having sum equal to target
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        #size of array
        n = len(nums)
        
        #Set to store unique quadruplets
        ans = set()
        
        # Checking all possible quadruplets
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    for l in range(k + 1, n):
                        # Calculate the sum of the current quadruplet
                        sum_val = nums[i] + nums[j] + nums[k] + nums[l]
                        
                        # Check if the sum matches the target
                        if sum_val == target:
                            temp = [nums[i], nums[j], nums[k], nums[l]]
                            # Sort the quadruplet to ensure uniqueness
                            temp.sort()
                            ans.add(tuple(temp))
        
        return list(ans)

if __name__ == "__main__":
    nums = [4, 3, 3, 4, 4, 2, 1, 2, 1, 1]
    target = 9
    
    #Create an instance of Solution class
    sol = Solution()
    
    ans = sol.fourSum(nums, target)
    
    # Print the result
    print("The quadruplets are: ")
    for quad in ans:
        print(f"[{', '.join(map(str, quad))}]")
'''

class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        n = len(nums)
        result = []

        for i in range(n - 3):
            # Skip duplicate elements for i
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n - 2):
                # Skip duplicate elements for j
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                left = j + 1
                right = n - 1

                while left < right:
                    sum_val = nums[i] + nums[j] + nums[left] + nums[right]

                    if sum_val == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1

                        # Skip duplicates
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1

                    elif sum_val < target:
                        left += 1
                    else:
                        right -= 1

        return result


        