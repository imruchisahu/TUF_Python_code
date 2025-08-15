'''
Given an integer array nums, which can have duplicate entries, provide the power set. Duplicate subsets cannot exist in the solution set. Return the answer in any sequence.


Examples:
Input : nums = [1, 2, 2]

Output : [ [ ] , [1] , [1, 2] , [1, 2, 2] , [2] , [2, 2] ]

Input : nums = [1, 2]

Output : [ [ ], [1] , [2] , [1, 2] ]

Input : nums = [1, 3, 3]

Output:
[ [ ], [1] , [1, 3] , [1, 3, 3] , [3] , [3, 3] ]
Constraints:
1 <= nums.length <= 10
-10 <= nums[i] <= 10

Intuition
Imagine a task to create all possible groups of items from a list that might have repeated items, ensuring no group is duplicated. The goal is to include each item or skip it, but if an item is skipped, all identical items must also be skipped to avoid duplicate groups. This mirrors the recursive process by methodically including or excluding each item while traversing the list. If an item is included, the process continues with the next item. If an item is excluded, the process skips all its duplicates to maintain unique groups. This step-by-step approach ensures all potential combinations are explored while preventing duplicates.

Approach
Sort the input list to group identical items together, simplifying the process of skipping duplicates.
Use a helper function to explore subsets recursively, starting from the first item and tracking the current subset.
For each item, choose to include it in the current subset and recurse to the next item. Then, backtrack and exclude the item, skipping any subsequent duplicates, and recurse again.
Upon reaching the end of the list, add the current subset to the result list. This ensures all possible subsets are captured while avoiding duplicates.


class Solution:
    def func(self, ind, arr, nums, ans):
        # If index reaches the end of nums
        if ind == len(nums):
            # Add the current subset (arr) to the result
            ans.append(arr.copy())
            return
        
        # Include the current element in the subset
        arr.append(nums[ind])
        # Recur for the next index
        self.func(ind + 1, arr, nums, ans)
        # Backtrack: remove the current element from the subset
        arr.pop()
        
        # Skip duplicates and recur for the next unique element
        for j in range(ind + 1, len(nums)):
            if nums[j] != nums[ind]:
                self.func(j, arr, nums, ans)
                return
        
        # Ensure the function finishes when no more unique elements are left
        self.func(len(nums), arr, nums, ans)
    
    def subsetsWithDup(self, nums):
        ans = []  # Resulting list of subsets
        arr = []  # Current subset
        nums.sort()  # Sort the array to handle duplicates
        self.func(0, arr, nums, ans)  # Start recursion
        return ans

if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 2]  # Example input
    result = sol.subsetsWithDup(nums)
    
    # Print the resulting subsets
    for subset in result:
        print(subset)
Complexity Analysis
Time Complexity: O(2^N * N) - Each element is either included or excluded, leading to an exponential number of subsets.

Space Complexity: O(N) - The space complexity is dominated by the recursion stack, which can go as deep as the number of elements in the input list.
'''
class Solution:
    def func(self, ind, arr, nums, ans):
        if ind == len(nums):
            ans.append(arr.copy())
            return
        arr.append(nums[ind])
        self.func(ind + 1, arr, nums, ans)
        arr.pop()

        for j in range(ind + 1, len(nums)):
            if nums[j] != nums[ind]:
                self.func(j, arr, nums, ans)
                return
        self.func(len(nums), arr, nums, ans)
    
    def subsetsWithDup(self, nums):
        ans = []  
        arr = [] 
        nums.sort() 
        self.func(0, arr, nums, ans)  
        return ans