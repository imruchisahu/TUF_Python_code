'''Given an array of integers nums, return the second-largest element in the array. If the second-largest element does not exist, return -1.


Examples:
Input: nums = [8, 8, 7, 6, 5]

Output: 7

Explanation: The largest value in nums is 8, the second largest is 7

Input: nums = [10, 10, 10, 10, 10]

Output: -1

Explanation: The only value in nums is 10, so there is no second largest value, thus -1 is returned

Input: nums = [7, 7, 2, 2, 10, 10, 10]

Output:
7
Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104
nums may contain duplicate elements.

Hint 1
Use two variables to track the largest and second-largest elements as you iterate through the array. Update the second-largest only if you find an element smaller than the largest but larger than the current second-largest.

Hint 2
Intuition
To find the second largest element in an array, one simple way is to use sorting. By sorting the array in ascending order, the largest element will be surely at the last index, and the second largest element will be at the second-to-last index.
What if there are fewer than 2 elements in an array ?
There would not be any second largest element for this case, so returned value will be -1.

What if last and second last element turn out as same ?
If the second-to-last element is equal to the last element, continue checking the preceding elements until a different value is found. This approach guarantees that correct identification of the second largest element is made.
Approach 
Initialize 2 variables largest, and secondLargest. Initialize secondLargest to -1 as initially there shall be no second largest element.
Sort the array and update largest with last element of array.
Now iterate the array from second to last index and if the element is not equal to the largest , update secondLargest to that element and break out once secondLargest is updated. Return the value stored in secondLargest


Complexity Analysis 
Time Complexity: O(N * log N) for sorting the array, where N is the length of the array.

Space Complexity: O(1) as no additional space is used.

class Solution:
    
    # Function to find the second largest element
    def secondLargestElement(self, nums):
        n = len(nums)
        
        # Check if the array has less than 2 elements
        if n < 2:
            # Indicating no second largest element is possible
            return -1
        
        # Sort the list in ascending order
        nums.sort()

        # Largest element will be at last index
        largest = nums[-1]

        secondLargest = -1

        # Traverse the sorted list from right to left
        for i in range(n-2, -1, -1):

            #If the current element is not equal to the largest element
            if nums[i] != largest:

                #assign the current element as the second largest and break
                secondLargest = nums[i]
                break

        # Return the second largest element
        return secondLargest


# Example usage
nums = [1, 2, 4, 6, 7, 5]

# Create an instance of the Solution class
sol = Solution()

#Call the method to find the second largest element
ans = sol.secondLargestElement(nums)

print("The second largest element is:", ans)

'''
class Solution:
    def secondLargestElement(self, nums):
        unique = list(set(nums))  # Remove duplicates
        if len(unique) < 2:
            return -1
        unique.sort()
        return unique[-2]
#TC= o(N + k log k) 
#in worst case : k= n if all eelement unique
#TC= O(N log N)
#SC=O(N)