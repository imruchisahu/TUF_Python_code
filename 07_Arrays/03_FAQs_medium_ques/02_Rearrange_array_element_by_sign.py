'''Given an integer array nums of even length consisting of an equal number of positive and negative integers.Return the answer array in such a way that the given conditions are met:



Every consecutive pair of integers have opposite signs.
For all integers with the same sign, the order in which they were present in nums is preserved.
The rearranged array begins with a positive integer.

Examples:
Input : nums = [2, 4, 5, -1, -3, -4]

Output : [2, -1, 4, -3, 5, -4]

Explanation: The positive number 2, 4, 5 maintain their relative positions and -1, -3, -4 maintain their relative positions

Input : nums = [1, -1, -3, -4, 2, 3]

Output : [1, -1, 2, -3, 3, -4]

Explanation: The positive number 1, 2, 3 maintain their relative positions and -1, -3, -4 maintain their relative positions

Input: nums = [-4, 4, -4, 4, -4, 4]

Output:
[4, -4, 4, -4, 4, -4]
Constraints:
2 <= nums.length <= 105
1 <= | nums[i] | <= 104
nums.length is an even number.
Number of positive and negative numbers are equal.

Hint 1
Extract positive and negative integers into two separate arrays while preserving their relative order. Iterate through the positive and negative arrays simultaneously, alternately adding elements from each to the result array.

Hint 2

Intuition:
As the array contains positive and negative elements, we can think of segregating the array elements into two parts. The first array will contain only positive elements and the second array will contain only negative elements. After this, we can just put the elements back in the original array alternatively. As the question states that positive elements should come first, so put positive element first and then negative one and so on. At the end of the process the original array will contain the desired result.

Approach:
Since the number of positive and negative elements are the same, we put positives into an array called “pos” and negatives into an array called “neg”.
After segregating each of the positive and negative elements, we start putting them alternatively back into the original array.
Initialize an array which will run from 0 till (sizeOfArray/2 - 1) because the number of positive and negative elements are equal, so the total count of any of them will be equal to (sizeOfArray/2).
Since the array must begin with a positive number and the start index is 0, so all the positive numbers would be placed at even indices (2*i) and negatives at the odd indices (2*i+1), where i is the index of the pos or neg array while traversing them simultaneously.

Complexity Analysis:
Time Complexity: O(N+N/2), where N is the size of the array. O(N) for traversing the array once for segregating positives and negatives and another O(N/2) for adding those elements alternatively to the array.

Space Complexity: O(N/2 + N/2) = O(N), N/2 space required to store each of the positive and negative elements in separate arrays.

class Solution:
    # Function to rearrange the given array by signs
    def rearrangeArray(self, nums):
        n = len(nums)
        
        """ Define 2 vectors, one for storing positive 
        and other for negative elements of the array."""
        pos = []
        neg = []
  
        # Segregate the array into positives and negatives.
        for num in nums:
            if num > 0:
                pos.append(num)
            else:
                neg.append(num)
  
        # Positives on even indices, negatives on odd.
        for i in range(n // 2):
            nums[2 * i] = pos[i]
            nums[2 * i + 1] = neg[i]
        
        # Return the result
        return nums

if __name__ == "__main__":
    A = [1, 2, -4, -5]
    
    # Create an instance of Solution class
    sol = Solution()
    
    ans = sol.rearrangeArray(A)
    
    # Print the result
    print(" ".join(map(str, ans)))

'''
class Solution:
    def rearrangeArray(self, nums):
        n=len(nums)
        pos = []
        neg = []
        for num in nums:
            if num > 0:
                pos.append(num)
            else:
                neg.append(num)
        for i in range(n//2):
            nums[2 * i] = pos[i]
            nums[2 * i + 1] = neg[i]
        return nums