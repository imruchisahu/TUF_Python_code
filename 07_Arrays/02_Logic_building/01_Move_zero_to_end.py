'''Input: nums = [0, 1, 4, 0, 5, 2]

Output: [1, 4, 5, 2, 0, 0]

Explanation: Both the zeroes are moved to the end and the order of the other elements stay the same

Input: nums = [0, 0, 0, 1, 3, -2]

Output: [1, 3, -2, 0, 0, 0]

Explanation: All 3 zeroes are moved to the end and the order of the other elements stay the same

Input: nums = [0, 20, 0, -20, 0, 20]

Output:
[20, -20, 20, 0, 0, 0]
Constraints:
1 <= nums.length <= 105
-104 <=nums[i] <= 104

Hint 1
Use two pointers to iterate through the array. One pointer keeps track of the current position, and the other identifies where the next non-zero element should go.

Hint 2
Focus on swapping non-zero elements to the front while keeping track of the current index for placing zeros at the end. Avoid creating a new array by modifying the original array directly. Shift non-zero elements left and fill zeros at the end.
ntuition
To ideate a solution for the problem, store the non-zero numbers separately and then place those elements back into the original array. This ensures that all the non-zero numbers are kept at the front of the array. Lastly, fill the remaining positions in the array with zeros.

Approach 
Declare a temporary array to store all the non-zero elements. Traverse the original array and copy all non-zero elements to the temporary array.
Overwrite the original array's starting positions with the elements from the temporary array.
Fill the remaining positions in the original array with zeros.


Complexity Analysis 
Time Complexity: O(2*N), O(N) for copying non-zero elements from the original to the temporary array. O(X) for again copying it back from the temporary to the original array. O(N-X) for filling zeros in the original array. Here N is the size of the array and X is the number of non-zero elements.

Space Complexity: O(N), for using a temporary array to solve this problem and the maximum size of the array can be N in the worst case.

from typing import List

class Solution:
    # Function to move zeroes to the end
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)

        """Create a temporary array 
        to store non-zero elements"""
        temp = [0] * n
        count = 0

        # Copy non-zero elements to temp
        for i in range(n):
            if nums[i] != 0:
                temp[count] = nums[i]
                count += 1

        # Copy non-zero elements back to nums
        for i in range(count):
            nums[i] = temp[i]

        # Fill the rest with zeroes
        for i in range(count, n):
            nums[i] = 0

if __name__ == "__main__":
    nums = [1, 0, 2, 3, 2, 0, 0, 4, 5, 1]

    # Create an instance of Solution class
    sol = Solution()
    sol.moveZeroes(nums)

    print("Array after moving zeroes:", nums)

'''
class Solution:
    def moveZeroes(self, nums):
        n = len(nums)
        temp = [0] * n
        count= 0
        for i in range(n):
            if nums[i] != 0:
                temp[count] = nums[i]
                count += 1

        for i in range(count):
            nums[i] = temp[i]

        for i in range(count, n):
            nums[i] = 0

                