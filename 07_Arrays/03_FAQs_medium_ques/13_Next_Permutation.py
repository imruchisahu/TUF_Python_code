'''A permutation of an array of integers is an arrangement of its members into a sequence or linear order.



For example, for arr = [1,2,3], the following are all the permutations of arr:

[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1].



The next permutation of an array of integers is the next lexicographically greater permutation of its integers.

More formally, if all the permutations of the array are sorted in lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted order.



If such arrangement is not possible (i.e., the array is the last permutation), then rearrange it to the lowest possible order (i.e., sorted in ascending order).



You must rearrange the numbers in-place and use only constant extra memory.


Examples:
Input: nums = [1,2,3]

Output: [1,3,2]

Explanation: The next permutation of [1,2,3] is [1,3,2].

Input: nums = [3,2,1]

Output: [1,2,3]

Explanation: [3,2,1] is the last permutation. So we return the first: [1,2,3].

Input: nums = [1,1,5]

Output:

[1, 1, 5]

Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 100

Intuition
A straightforward but naive approach to solving this problem is to generate all possible permutations of the given array. Once all permutations are generated, we sort them in lexicographical order and perform a linear search to locate the current permutation. The next permutation in the sorted list is then returned. If the current permutation happens to be the last one, we simply return the first permutation from the sorted list.

To generate all permutations, we use backtracking, where we recursively swap each element with the current index and explore all possible configurations. After each recursive call, we backtrack by swapping the elements back to restore the original state. This ensures that we explore every unique arrangement without missing or repeating any permutations.

Approach
Generate all permutations of the given array using backtracking.
Store each permutation in a result list after exploring all positions by swapping elements recursively.
Sort the list of all permutations in lexicographical order.
Find the current permutation's index using linear search.
If the current permutation is the last in order, return the first permutation.
Otherwise, return the next permutation from the sorted list.
Solution

Complexity Analysis
Time Complexity: O(N × N!), where N is the size of the input array.
Generating all permutations involves exploring N! arrangements, and each permutation requires O(N) time to construct, resulting in O(N × N!). Although sorting the permutations and performing a linear search add to the total time, the dominant factor remains O(N × N!) due to the exponential nature of permutation generation.

Space Complexity: O(N × N!)
Recursion stack takes up to O(N) space, and storing all permutations requires O(N × N!) space.

Note
Note that for C++ users, there is an STL function available to find the next permutation of the given array.

The function next_permutation() from the <algorithm> header modifies the array in-place to the next lexicographical permutation. If the array is already the highest permutation, it rearranges it to the lowest possible order (i.e., sorted in ascending order). This function runs in O(N) time and is the most efficient way to solve this problem in C++.

from typing import List

class Solution:
    # Function to get the next permutation of given array
    def nextPermutation(self, nums: List[int]) -> None:
        # Get all the Permutations
        ans = self.getAllPermutations(nums)

        index = -1  # Current permutation index

        #Perform a linear search to get the permutation of current permutation 
        for i in range(len(ans)):
            if list(nums) == ans[i]:
                index = i
                break

        # Store the next permutation in-place
        next_perm = ans[0] if index == len(ans) - 1 else ans[index + 1]
        for i in range(len(nums)):
            nums[i] = next_perm[i]

        return

    #Function to generate all permutations of 
    the given array in sorted order 
    def getAllPermutations(self, nums: List[int]) -> List[List[int]]:
        ans = []  # To store the permutation

        # Recursive Helper function call 
        self.helperFunc(0, nums, ans)

        ans.sort()  # Sort the permutations
        return ans  # Return the result

    # Helper function to get all the permutations of the given array
    def helperFunc(self, ind: int, nums: List[int], ans: List[List[int]]) -> None:

        # Base case
        if ind == len(nums):
            # Add the permutation to the answer
            ans.append(nums[:])
            return

        # Traverse the array
        for i in range(ind, len(nums)):
            nums[ind], nums[i] = nums[i], nums[ind]  # Swap-In

            # Recursively call the helper function
            self.helperFunc(ind + 1, nums, ans)

            nums[ind], nums[i] = nums[i], nums[ind]  # Swap-Out

        return

if __name__ == "__main__":
    nums = [1, 2, 3]

    #Creating an instance of Solution class 
    sol = Solution()

    # Output
    print("Given array: ", end="")
    for x in nums:
        print(x, end=" ")

    # Function call to get the next permutation of given array
    sol.nextPermutation(nums)

    # Output
    print("\nNext Permutation: ", end="")
    for x in nums:
        print(x, end=" ")

'''
class Solution:
    def nextPermutation(self, nums):
        n = len(nums)
        
        # Step 1: Find the first decreasing element from the end
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        # Step 2: If found, find element just larger than nums[i] and swap
        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        
        # Step 3: Reverse the suffix starting from i + 1
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
