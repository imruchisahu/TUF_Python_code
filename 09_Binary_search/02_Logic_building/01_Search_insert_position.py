'''Given a sorted array of nums consisting of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.


Examples:
Input: nums = [1, 3, 5, 6], target = 5

Output: 2

Explanation: The target value 5 is found at index 2 in the sorted array. Hence, the function returns 2.

Input: nums = [1, 3, 5, 6], target = 2

Output: 1

Explanation: The target value 2 is not found in the array. However, it should be inserted at index 1 to maintain the sorted order of the array.

Input: nums = [1, 3, 5, 6], target = 7

Output:
4
Constraints:
  1 <= nums.length <= 105
  -105 <= nums[i] <= 105
  nums contains distinct values sorted in ascending order.
  -105<= target <= 105
  
  #Brute Force
  Intuition: 
Let's start with the simplest way to solve this problem. Imagine you're reading a book, and you want to find a specific page. You start from the beginning and turn each page one by one until you find the page you're looking for. If you don't find it, you know exactly where it should be inserted based on the pages you've turned so far.

Approach: 
Begin with the first number in the list. If the number matches the target, return the current index.
If the number is greater than the target, return the current index as the position where the target should be inserted.
If you reach the end of the list without finding the target, return the length of the list, as the target should be inserted at the end.
Cpp
Java
Python
Javascript
C#
Go


class Solution:
    def searchInsert(self, nums, target):
        # Iterate through the list
        for i in range(len(nums)):
            # If current element is greater than
           # or equal to the target
            if nums[i] >= target:
                # Return the current index
                return i
        # If target is greater than all elements, 
        # return the length of the list
        return len(nums)

nums = [1, 3, 5, 6]
target = 5

# Create an instance of the Solution class
sol = Solution()

# Find the insertion index
index = sol.searchInsert(nums, target)
print(f"The index is: {index}")
Time Complexity: O(N), where N is the size of the given array. We are using the Linear Search algorithm, which iterates linearly resulting in N time complexity.

Space Complexity: O(1), as we are not using any extra space to solve this problem.



#optimal Approach
Intuition: 
Considering our example used in brute force approach, imagine you have a faster way to find the target, using a table of contents in a book where you can quickly skip to different sections instead of turning each page one by one. This is essentially what binary search accomplishes. It allows us to efficiently narrow down the search range by repeatedly dividing it in half.

In this specific problem, if the target itself is found, return its index. Otherwise, return the smallest index where the element is greater than the target. Upon observation, it becomes clear that the lower bound of the target serves this purpose. Therefore, for this problem, simply find the lower bound of the target. If no such element is found, return the size of the array.

Approach: 
Use two pointers to traverse the array, low and high, and an ans variable with the size of the array to store the answer. The low pointer starts at the first index, and the high pointer starts at the last index.
Calculate the middle index, and compare arr[mid] with the given element. If arr[mid] is greater than or equal to the given element then we the update the ans variable with mid and search in the left half for a smaller index that also satisfies the condition.
If arr[mid] is less than the given element, then we search in the right half by eliminating the left half. We do so by making the low pointer as mid+1.
Continue the process until the low pointer crosses the high pointer. At this point, the ans variable will hold the answer.
Dry Run: 
Image 1
Image 2
Image 3

1/3



Cpp
Java
Python
Javascript
C#
Go


class Solution:
    def searchInsert(self, nums, target):
        n = len(nums)
        low, high = 0, n - 1
        ans = n

        # Applying Binary Search Algorithm
        while low <= high:
            mid = (low + high) // 2

            # If mid element is greater than 
            # or equal to target, update ans 
            # and search the left half
            if nums[mid] >= target:
                ans = mid
                high = mid - 1
            else:
                # Otherwise, search the right half
                low = mid + 1

        return ans

if __name__ == "__main__":
    nums = [1, 3, 5, 6]
    target = 5

    # Create an instance of the Solution class
    sol = Solution()

    # Find the insertion index
    ind = sol.searchInsert(nums, target)

    print("The index is:", ind)
Complexity Analysis: 
Time Complexity: O(logN), where N is the size of the given array. We are using the Binary Search algorithm, which divides the search space in half each time, resulting in a logarithmic time complexity.

Space Complexity: O(1), as we are not using any extra space to solve this problem.
  
  '''
class Solution:
    def searchInsert(self, nums, target):
        n=len(nums)
        low, high = 0, n-1
        ans = n
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] >= target:
                ans= mid
                high = mid - 1
            else:
                low= mid + 1
        return ans