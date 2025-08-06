'''Given an integer array nums and a non-negative integer k, rotate the array to the left by k steps.


Examples:
Input: nums = [1, 2, 3, 4, 5, 6], k = 2

Output: nums = [3, 4, 5, 6, 1, 2]

Explanation: rotate 1 step to the left: [2, 3, 4, 5, 6, 1]

rotate 2 steps to the left: [3, 4, 5, 6, 1, 2]

Input: nums = [3, 4, 1, 5, 3, -5], k = 8

Output: nums = [1, 5, 3, -5, 3, 4]

Explanation: rotate 1 step to the left: [4, 1, 5, 3, -5, 3]

rotate 2 steps to the left: [1, 5, 3, -5, 3, 4]

rotate 3 steps to the left: [5, 3, -5, 3, 4, 1]

rotate 4 steps to the left: [3, -5, 3, 4, 1, 5]

rotate 5 steps to the left: [-5, 3, 4, 1, 5, 3]

rotate 6 steps to the left: [3, 4, 1, 5, 3, -5]

rotate 7 steps to the left: [4, 1, 5, 3, -5, 3]

rotate 8 steps to the left: [1, 5, 3, -5, 3, 4]

Input: nums = [1, 2, 3, 4, 5], k = 4

Output:
[
[5, 1, 2, 3, 4]

Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104
0 <= k <= 105

Similar Problems

Hint 1
Split the array into two parts at index k: the first k elements and the rest. Then rearrange the two parts to place the second part before the first part.

Hint 2
Intuition:
To rotate an array by K positions to the left, consider that the first K elements of the array will move to the end, while the remaining elements will shift K positions to the left.

The thought process involves first capturing the first K elements in a temporary array. Next, shift each of the remaining elements from position K to the beginning of the array. Finally, append the temporarily stored elements to the end of the array. This approach ensures that the array is rotated to the left by K positions effectively.

Approach:
First, calculate the effective number of rotations by taking the modulo of K with the array size to avoid unnecessary rotations.
Create a temporary array to store the first K elements of the array.
Shift the remaining (N - K) elements of the array to the front.
Copy the stored K elements from the temporary array to the end of the array.
The array is now rotated to the left by K places.
Solution

Complexity Analysis:
Time Complexity: O(N), where N is the length of the array.
Three loops are used taking K, N-K, and K iterations respectively contributing to O(N+K). However, K can be N-1 in the worst case boiling down the time complexity as O(N).

Space Complexity: O(K), due to the temporary list created to copy the K elements.

class Solution:
    # Function to rotate the array to the left by k positions
    def rotateArray(self, nums, k):
        n = len(nums)  # Size of array
        k = k % n  # To avoid unnecessary rotations

        temp = []

        # Store first k elements in a temporary array
        for i in range(k):
            temp.append(nums[i])

        # Shift n-k elements of given array to the front
        for i in range(k, n):
            nums[i - k] = nums[i]

        # Copy back the k elements at the end
        for i in range(k):
            nums[n - k + i] = temp[i]


# Helper function to print the array
def printArray(nums):
    for val in nums:
        print(val, end=" ")
    print()


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6]
    k = 2

    print("Initial array: ")
    printArray(nums)

    # Create an instance of the Solution class
    sol = Solution()

    # Function call to rotate the array to the left by k places
    sol.rotateArray(nums, k)

    print(f"Array after rotating elements by {k} places: ")
    printArray(nums)
'''

class Solution:
    def rotateArray(self, nums, k):
        n=len(nums)
        k = k %  n
        temp=[]
        for i in range(k):
            temp.append(nums[i])

        for i in range(k, n):
            nums[i-k] = nums[i]

        for i in range(k):
            nums[n-k+i] = temp[i]
        
        #for printitng array after rotatig
        for val in nums:
            print(val, end=" ")
        print()
s=Solution()
s.rotateArray([1,2,3,4,5,6], 2)