'''
Given an array of integers nums, each element in the array represents the maximum jump length at that position. Initially starting at the first index of the array, determine if it is possible to reach the last index. Return true if the last index can be reached, otherwise return false.


Examples:
Input : [2, 3, 1, 1, 4]



Output : true



Explanation : We can simply take Jump of 1 step at each index to reach the last index.

Input : [3, 2, 1, 0, 4]



Output : false



Explanation : No matter how you make jumps you will always reach the third index (0 base) of the array.

The maximum jump of index three is 0, So you can never reach the last index of array.

Input : [5, 3, 2, 1, 0]

Output:
true
Constraints:
1 <= nums.length <= 104
0 <= nums[i] <= 105

Intuition
Keep track of the farthest position that can be reached at any point. If at an index where it's impossible to move to the next one because it's too far away, then it's impossible to get to the end, and the process must stop.
Otherwise, continue updating the farthest reachable index while moving forward. If the traversal manages to reach or pass the last index, then reaching the end is possible.
Approach
Start by setting a pointer to track the farthest point that can be reached from the beginning of the array.
Iterate through each position in the array, checking if the current position exceeds the farthest point reached so far.
If the current position is beyond the reachable point, it indicates that further progress is not possible, and reaching the end is infeasible.
If the current position is within the reachable point, update the pointer to reflect the farthest position that can be reached from the current spot.
If the entire array is traversed without finding an unreachable position, it confirms that the last index is reachable, thus making it possible to reach the end.

class Solution:
    # To determine if last index is reachable
    def canJump(self, nums):
        # Initialize maximum index
        max_index = 0

        # Iterate through each index of the array
        for i in range(len(nums)):
            # If the current index is greater than the 
            # maximum reachable index it means we cannot move 
            # forward and should return false
            if i > max_index:
                return False

            # Update the maximum index that can be 
            # reached by comparing the current maxIndex with the sum 
            # of the current index and the maximum jump from that index
            max_index = max(max_index, i + nums[i])

        # If we complete the loop, it means we can reach the last index
        return True

# Example usage
if __name__ == "__main__":
    nums = [4, 3, 7, 1, 2]

    print("Array representing maximum jump from each index: ", end="")
    for num in nums:
        print(num, end=" ")
    print()

    solution = Solution()
    ans = solution.canJump(nums)

    if ans:
        print("It is possible to reach the last index.")
    else:
        print("It is not possible to reach the last index.")

Complexity Analysis
Time Complexity: O(N) where N is the length of the array. We iterate through the input array exactly once and at each element perform constant time operations.
Space Complexity: O(1) no extra space used.

'''
class Solution:
    def canJump(self, nums):
        max_index = 0
        for i in range(len(nums)):
            if i > max_index:
                return False
            max_index = max(max_index, i + nums[i])
        return True