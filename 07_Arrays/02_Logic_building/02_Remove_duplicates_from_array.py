'''Given an integer array nums sorted in non-decreasing order, remove all duplicates in-place so that each unique element appears only once. Return the number of unique elements in the array.



If the number of unique elements be k, then,

Change the array nums such that the first k elements of nums contain the unique values in the order that they were present originally.
The remaining elements, as well as the size of the array does not matter in terms of correctness.


An array sorted in non-decreasing order is an array where every element to the right of an element is either equal to or greater in value than that element.


Examples:
Input: nums = [0, 0, 3, 3, 5, 6]

Output: 4

Explanation: Resulting array = [0, 3, 5, 6, _, _]

There are 4 distinct elements in nums and the elements marked as _ can have any value.

Input: nums = [-2, 2, 4, 4, 4, 4, 5, 5]

Output: 4

Explanation: Resulting array = [-2, 2, 4, 5, _, _, _, _]

There are 4 distinct elements in nums and the elements marked as _ can have any value.

Input: nums = [-30, -30, 0, 0, 10, 20, 30, 30]

Select the possible resulting array.

Output:
[-30, 0, 10, 20, 30, _, _, _]
Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.

Hint 1
Since the array is sorted, duplicates will always be consecutive. Compare adjacent elements to identify duplicates and move unique elements forward.

Intuition
The naive way is to think of a data structure that does not store duplicate elements, that is HashSet. Keep track of unique elements in hashset, and at last copy all the elements from the HashSet to the original array.

Approach 
Declare a HashSet and traverse the array by putting every element of the array in the HashSet
Store size of the set in a variable K. Now put all elements of the set in the array from the starting of the array and finally return K


Complexity Analysis 
Time Complexity: O(N * log N) + O(N), for using hashset, it will take O(N * log N) and also to traverse the array once O(N). Here N is the size of the array.

Space Complexity: O(N) because in the worst case, all the elements of the array can be unique and it will take O(N) space. Here N represents the size of the array.

class Solution:
    # Function to remove duplicates from the array
    def removeDuplicates(self, nums):
        
        # Set data structure to store unique elements
        s = set()
        
        # Add all elements from array to the set
        for val in nums:
            s.add(val)
        
        # Get the sorted list of unique elements
        sorted_unique = sorted(s)
        
        # Copy unique elements from sorted list to array
        for j in range(len(sorted_unique)):
            nums[j] = sorted_unique[j]
        
        # Return the number of unique elements
        return len(sorted_unique)

# Helper function to print first n elements of the array
def printArray(nums, n):
    for i in range(n):
        print(nums[i], end=" ")
    print()

if __name__ == "__main__":
    nums = [1, 1, 2, 2, 2, 3, 3]
    
    print("Original Array: ", end="")
    printArray(nums, len(nums))
    
    # Create an instance of the Solution class
    sol = Solution()
    
    # Function call to remove duplicates from array
    k = sol.removeDuplicates(nums)
    
    print("Array after removing the duplicates: ", end="")
    printArray(nums, k)

'''
class Solution:
    def removeDuplicates(self, nums):
        s=set()
        for val in nums:
            s.add(val)
        sorted_unique = sorted(s)
        for j in range(len(sorted_unique)):
            nums[j] = sorted_unique[j]
        return len(sorted_unique)