'''Given an integer array nums of size n containing values from [1, n] and each value appears exactly once in the array, except for A, which appears twice and B which is missing.

Return the values A and B, as an array of size 2, where A appears in the 0-th index and B in the 1st index.



Note: You are not allowed to modify the original array.


Examples:
Input: nums = [3, 5, 4, 1, 1]

Output: [1, 2]

Explanation: 1 appears two times in the array and 2 is missing from nums

Input: nums = [1, 2, 3, 6, 7, 5, 7]

Output: [7, 4]

Explanation: 7 appears two times in the array and 4 is missing from nums.

Input: nums = [6, 5, 7, 1, 8, 6, 4, 3, 2]

Output:
[6, 9]
[9, 6]
[10, 6]
[6, 8]

Submit
Constraints:
n == nums.length
1 <= n <= 105
n - 2 elements in nums appear exactly once and are valued between [1, n].
1 element in nums appears twice, and is valued between [1, n].

Hint 1

Hint 2
Intuition 
The naive way is to count the occurrence in the given array using linear search, for each number between 1 to N. The element which occurs twice will be the repeating number and the number with 0 occurrence will be the missing number.

Approach 
Iterate in array from 1 to N & for each integer, i, count its occurrence in the given array using linear search.
Store those two elements that have the occurrence of 2 and 0. Finally, return the elements.


Complexity Analysis 
Time Complexity: O(N2), where N is the size of the array. Since we are using nested loops to count occurrences of every element between 1 to N.

Space Complexity: O(1) as no extra space is used.

class Solution:
    # Function to find repeating and missing numbers
    def findMissingRepeatingNumbers(self, nums):
        
        # Size of the array
        n = len(nums) 
        repeating, missing = -1, -1

        # Find the repeating and missing number:
        for i in range(1, n + 1):
            # Count the occurrences:
            cnt = nums.count(i)

            # Check if i is repeating or missing
            if cnt == 2:
                repeating = i
            elif cnt == 0:
                missing = i

            """ If both repeating and missing
            are found, break out of loop"""
            if repeating != -1 and missing != -1:
                break

        # Return [repeating, missing]
        return [repeating, missing]

if __name__ == "__main__":
    nums = [3, 1, 2, 5, 4, 6, 7, 5]
    
    # Create an instance of Solution class
    sol = Solution()

    result = sol.findMissingRepeatingNumbers(nums)
    
    # Print the repeating and missing numbers found
    print(f"The repeating and missing numbers are: {{{result[0]}, {result[1]}}}")

'''
class Solution:
    def findMissingRepeatingNumbers(self, nums):
        n=len(nums)
        repeating, missing = -1, -1
        for i in range(1, n + 1):
            count = nums.count(i)
            if count == 2:
                repeating = i
            elif count == 0:
                missing = i
            
            if repeating != -1 and missing != -1:
                break
        return [repeating, missing]