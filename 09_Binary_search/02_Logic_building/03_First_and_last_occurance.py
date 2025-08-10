'''Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value. If the target is not found in the array, return [-1, -1].


Examples:
Input: nums = [5, 7, 7, 8, 8, 10], target = 8

Output: [3, 4]

Explanation:The target is 8, and it appears in the array at indices 3 and 4, so the output is [3,4]

Input: nums = [5, 7, 7, 8, 8, 10], target = 6

Output: [-1, -1]

Expalantion: The target is 6, which is not present in the array. Therefore, the output is [-1, -1].

Input: nums = [5, 7, 7, 8, 8, 10], target = 5

Output:
[0, 0]
Constraints:
  0 <= nums.length <= 105
  -109 <= nums[i] <= 109
  nums is a non-decreasing array.
  -109 <= target <= 109
  
#Linear Search Approach
Intuition
The naive approach to solve this problem would be a linear traversal of the given array. We traverse the array and store the index where the target appears the first time, in both the first and last occurrence variables. We update the last variable when we again encounter an index where value is equal to the target.

Approach
Declare two variables, first and last, initialized to -1 to store the first and last occurrences of the target value.
Traverse the array, when the target value is first encountered in the array, store the index in both first and last.
For subsequent occurrences of the target value, update only the last variable with the current index.
Store the first and last occurrences in a vector and return that vector as a result.

Complexity Analysis: 
Time Complexity: O(N), where N is the size of the given array. This is because we are performing a linear search through the array to find the first and last occurrences of the target element.

Space Complexity: O(1), as we are not using any extra space that grows with the input size. We are only using a few additional variables to store indices and results.



class Solution:
    def searchRange(self, nums, target):
        # Initialize variables to store first and last occurrences
        first, last = -1, -1

        # Iterate through the array
        for i in range(len(nums)):
            # Check if current element is the target
            if nums[i] == target:
                if first == -1:
                    first = i  
                last = i  

        # Return the results as a list
        return [first, last]

# Example usage
if __name__ == "__main__":
    nums = [5, 7, 7, 8, 8, 10]
    target = 8

    # Create an instance of the Solution class
    sol = Solution()

    # Function call to find the first and last occurrences
    result = sol.searchRange(nums, target)

    print(f"The first and last occurrences are at indices: {result[0]} and {result[1]}")

#Using Bound Approach
Intuition
In this approach, we use the lower bound and upper bound values to get the first and last occurrences of the target element. Lower bound of the target element will provide us index of the first occurrence of the target element. And, upper bound will provide the index of the element just after the last appearance of the target. So, we could return the lower bound and the upper bound - 1, as the first and last occurrences of the target in the given array.

Approach
For Lower Bound:
To get the lower bound, use low and high pointers(Binary search approach) initialized with first and last indices.
Calculate the middle element and compare the values as mentioned in the below two points.
If the middle element is greater than or equal to target, update it as our possible answer and eliminate the right half by decreasing the high pointer.
If the middle element is lesser than the target, eliminate the left half.
Keep following these steps till the low pointer lesser than or equal to the high pointer.

For Upper Bound:
To get the upper bound, use low and high pointers(Binary search approach initialized with first and last indices.
Then calculate the middle element and compare the values as mentioned in the below two points.
If the middle element is greater than target, store it as our possible answer and eliminate the right half by decreasing the high pointer.
If the middle element is lesser than or equal to target, eliminate the left half.
Keep following these steps till the low pointer lesser than or equal to the high pointer.

Edge Case: In case the lower bound is equal to the size of the array or the value of array at index = lower bound is not equal to the target element, return both the first and last occurrence as -1. As it means that the target is not present in the array.
Now return the lower bound and (upper bound - 1) as the first and last occurrences of the target element in the given array.

class Solution:
    def lowerBound(self, nums, target):
        low, high = 0, len(nums) - 1
        ans = len(nums) 

        # Applying binary search algorithm
        while low <= high:
            mid = (low + high) // 2

            # If the middle element is greater than
            # or equal to the target element update 
            # the answer as mid and eliminate the right half
            if nums[mid] >= target:
                ans = mid  
                high = mid - 1  

            # If the middle element is smaller than
            # the target element then we eliminate 
            # the left half
            else:
                low = mid + 1 
                
        return ans

    def upperBound(self, nums, target):
        low, high = 0, len(nums) - 1
        ans = len(nums)

        # Applying binary search algorithm
        while low <= high:
            mid = (low + high) // 2

            # If the middle element is greater than
            # the target element update the answer 
            # as mid and eliminate the right half
            if nums[mid] > target:
                ans = mid
                high = mid - 1

            # If the middle element is greater than
            # or equal to the target element 
            # eliminate the right half
            else:
                low = mid + 1

        return ans

    def searchRange(self, nums, target):

        # Function call to find the first occurrence (lower bound)
        firstOcc = self.lowerBound(nums, target)

        # Check if the target is present in the array or not
        if firstOcc == len(nums) or nums[firstOcc] != target:
            return [-1, -1]

        # Function call to find the last occurrence (upper bound)
        lastOcc = self.upperBound(nums, target) - 1

        return [firstOcc, lastOcc]

if __name__ == "__main__":
    nums = [5, 7, 7, 8, 8, 10]
    target = 8

    # Create an instance of the Solution class
    sol = Solution()

    # Function call to find the first and last occurrences
    result = sol.searchRange(nums, target)

    print("The first and last occurrences are at indices:", result[0], "and", result[1])

Complexity Analysis: 
Time Complexity: 2*O(log N), where N is the size of the given array. Both the lowerBound and upperBound functions perform a binary search, which operates in logarithmic time. Thus, the overall time complexity is O(log N).

Space Complexity: O(1), as we are using a constant amount of extra space regardless of the input size. The space used by the variables low, high, mid, and ans does not depend on the size of the input array.
# Binary Search Approach
# Intuition
The optimal solution of this problem uses binary search to look for the first and last occurrences of the target element. While calculating the first occurrence, keep in mind that every time we get an element equal to target, look for the target again in its left half. Similarly, for getting the last occurrence, keep in mind that when we get an element equal to target, we look for the target again in its right half, so we get the last index where the target appears.

Approach
For firstOccurrence():
Start with taking low and high pointers initialized with the first index, and last index as that would be the search space.
Calculate the middle element and compare the values as mentioned in the below three points.
If the middle element of array is equal to target, update it as an possible answer and eliminate the right half by decreasing the high pointer. Then, search in the left half for more smaller index that satisfies the same condition.
If the middle element is lesser than the target, eliminate the left half.
If the middle element is greater than the target, eliminate the right half.
Keep following these steps till the low pointer lesser than or equal to the high pointer.



For lastOccurrence():
Start with taking low and high pointers initialized with the first index, and last index.
Calculate the middle element and compare the values as mentioned in the below three points.
If the middle element of the array is equal to target, update it as a possible answer and eliminate the right half by decreasing the high pointer. Then, search in the right half for more greater index that satisfies the same condition.
If the middle element is lesser than the target, eliminate the left half.
If the middle element is greater than the target, eliminate the right half.
Keep following these steps till the low pointer lesser than or equal to the high pointer.

I

Edge Case: In case the function firstOccurrence() returns -1, it'll indicate that the target element is not found in the array. If this happens we can directly return {-1,-1} as the answer. There would be no further need to calculate the last occurrence of the target element.
Now return the lower bound and (upper bound - 1) as the first and last occurrences of the target element in the given array.

Complexity Analysis: 
Time Complexity: O(log N), where N is the size of the given array. Both the firstOccurrence and lastOccurrence functions perform a binary search, which operates in logarithmic time. Thus, the overall time complexity is O(log N).

Space Complexity: O(1), as we are using a constant amount of extra space regardless of the input size. The space used by the variables low, high, mid, first, and last does not depend on the size of the input array.


class Solution:
    # Function to find the first occurrence of the target
    def firstOccurrence(self, nums, target):
        low, high = 0, len(nums) - 1
        first = -1

        # Applying Binary Search Algorithm
        while low <= high:
            mid = low + (high - low) // 2

            # If the target element is found, we 
            # update the first variable to mid and
            # eliminate the right half to look for 
            # more smaller index where target is present
            if nums[mid] == target:
                first = mid
                high = mid - 1

            # If middle element is smaller,
            # we eliminate the left half
            elif nums[mid] < target:
                low = mid + 1

            # If middle element is greater,
            # we eliminate the right half
            else:
                high = mid - 1

        return first

    # Function to find the last occurrence of the target
    def lastOccurrence(self, nums, target):
        low, high = 0, len(nums) - 1
        last = -1

        # Applying Binary Search Algorithm
        while low <= high:
            mid = low + (high - low) // 2

            # If the target element is found, we 
            # update the last variable to mid and
            # eliminate the left half to look for 
            # more greater index where target is present
            if nums[mid] == target:
                last = mid
                low = mid + 1

            # If middle element is smaller,
            # we eliminate the left half
            elif nums[mid] < target:
                low = mid + 1

            # If middle element is greater,
            # we eliminate the right half
            else:
                high = mid - 1

        return last

    # Function to find the first and last occurrences of the target
    def searchRange(self, nums, target):

        # Function call to find the first occurence of target
        first = self.firstOccurrence(nums, target)

        # If the target is not present in the array
        if first == -1:
            return [-1, -1]

        # Function call to find the last occurence of target
        last = self.lastOccurrence(nums, target)

        return [first, last]

if __name__ == "__main__":
    nums = [5, 7, 7, 8, 8, 10]
    target = 8

    # Create an instance of the Solution class
    sol = Solution()

    # Function call to find the first and last occurrences
    result = sol.searchRange(nums, target)

    print("The first and last occurrences are at indices:", result[0], "and", result[1])

# '''
class Solution:
    def searchRange(self, nums, target):
        first, last = -1, -1
        for i in range(len(nums)):
            if nums[i] == target:
                if first == -1:
                    first= i
                last= i
        return [first, last]