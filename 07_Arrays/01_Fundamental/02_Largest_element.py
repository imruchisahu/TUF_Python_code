'''Given an array of integers nums, return the value of the largest element in the array


Examples:
Input: nums = [3, 3, 6, 1]

Output: 6

Explanation: The largest element in array is 6

Input: nums = [3, 3, 0, 99, -40]

Output: 99

Explanation: The largest element in array is 99

Input: nums = [-4, -3, 0, 1, -8]

Output:
1
Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104
nums may contain duplicate elements.

Hint 1
Start by assuming the first element is the largest, then iterate through the array to compare each element with the current largest.

Hint 2
Intuition
Imagine being a teacher and having a list of marks obtained by your students in a recent test. The task is to find out which student scored the highest marks. One simple way to do this is by sorting the marks in ascending order and then taking the last element from the sorted list.

Approach 
Sort the array in ascending order using in-built methods.
Return the element at the last index of the array.

Complexity Analysis
Time Complexity: O(N * logN), as we are sorting the array, where N is the length of the array.

Space Complexity: O(log(n)) if we use c++ sort() method.

from typing import List

class Solution:
    def largestElement(self, nums):
        # Sort the list 
        nums.sort()

        # Largest element will be 
        # at the last index of the list
        largest = nums[-1]

        # Return the largest element
        return largest

# Main function
if __name__ == "__main__":
    nums = [3, 2, 1, 5, 2]

# Create an instance of the Solution class
    sol = Solution()
    
    largest = sol.largestElement(nums)

    # Print the largest element
    print(largest)

'''

class Solution:
    def largestElement(self, nums):
        nums.sort()
        largest=nums[-1]
        return largest
        