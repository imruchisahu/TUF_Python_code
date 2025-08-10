'''Given a sorted array of integers nums with 0-based indexing, find the index of a specified target integer. If the target is found in the array, return its index. If the target is not found, return -1.


Examples:
Input: nums = [-1,0,3,5,9,12], target = 9

Output: 4

Explanation: The target integer 9 exists in nums and its index is 4

Input: nums = [-1,0,3,5,9,12], target = 2

Output: -1

Explanation: The target integer 2 does not exist in nums so return -1

Input: nums = [-1,0,3,5,9,12], target = -1

Output:
0
Constraints:
  1 <= nums.length <= 105
  -105 < nums[i], target < 105
  nums is sorted in ascending order.
  Intuition:
Binary search is an efficient algorithm to find a target value within a sorted array. It works on the idea of repeatedly dividing the search space(the space in which the search of the target is taking place) in half until the target is found or it is concluded that the target is not present in the array.

What is Search Space?
The target must be found in the array itself. This means that the space in which the target must be searched for is the array. Now, to mark the search space, two pointers will come in hand -

Low: A pointer pointing to the smallest index possible of the search space.
High: A pointer pointing to the greatest index possible of the search space.
Initially, the search space is the whole array, i.e., the low and high pointers will be initialized with the following values:
low = 0, high = n-1 (where n is the size of the array)
Understanding:
To find the target, the middle element of the current search space will be found. If it matches the target, the search ends. Otherwise
If the middle element is less than the target: All the elements to the left of the middle element will also be less than the target (because the array is sorted). Thus, the search space can be trimmed down to the right half discarding the left half.
If the middle element is greater than the target: All the elements to the right of the middle element will also be greater than the target (because the array is sorted). Thus, the search space can be trimmed down to the left half discarding the right half.

This way, the search space is divided in half with every search increasing the chances of finding the target.
Edge Case:
If the target is not present in the array, the search space will eventually reduce to zero with every search indicating the absence of target in the given array. In such cases, -1 can be returned.

Approach:
Two pointers are set up to define the search space — one pointing to the beginning of the array and the other to the end.
The middle element of the current search space is found and the search space is repeatedly divided in half:
If the middle element matches the target, the index is returned.
If the target is greater than the middle element, the search space is narrowed to the right half.
If the target is smaller, the search space is narrowed to the left half.
If the loop ends without finding the target, return -1 indicating that the target is not present in the array.

Complexity Analysis:
Time Complexity: O(log(N)) (where N is the size of the given array)
In each step, the search space is divided into two halves. In the worst case, this process will continue until the search space can no longer be divided and the number of divisions required to reduce the array size to one is log(N), making the overall time complexity O(log(N)).

Space Complexity: O(1)
Using only a couple of variables.

#iterative Approach
class Solution:
    # Function to find the given target in a sorted array
    def search(self, nums, target):
        n = len(nums) # Size of array 
        
        # Pointers to define the search space
        low, high = 0, n - 1

        # Until the search space is not empty
        while low <= high:
            # Find the middle element
            mid = (low + high) // 2

            # If it matches the target
            if nums[mid] == target:
                return mid
                
            # If the target is greater than middle element 
            elif target > nums[mid]:
                low = mid + 1
                
            # Otherwise
            else:
                high = mid - 1

        # If the target is not found
        return -1

# Creating an instance of Solution class
sol = Solution()

# Test the function
a = [-1, 0, 3, 5, 9, 12]
target = 9

# Function call to find the given target in a sorted array
ind = sol.search(a, target)

if ind == -1:
    print("The target is not present.")
else:
    print("The target is at index:", ind)

    
Recursive Approach
Intuition:
Binary search is an efficient algorithm to find a target value within a sorted array. It works on the idea of repeatedly dividing the search space(the space in which the search of the target is taking place) in half until the target is found or it is concluded that the target is not present in the array.

What is Search Space?
The target must be found in the array itself. This means that the space in which the target must be searched for is the array. Now, to mark the search space, two pointers will come in hand -

Low: A pointer pointing to the smallest index possible of the search space.
High: A pointer pointing to the greatest index possible of the search space.
Initially, the search space is the whole array, i.e., the low and high pointers will be initialized with the following values:
low = 0, high = n-1 (where n is the size of the array)
Understanding:
A recursive approach will be used this time. In the recursive function, the middle element of the current search space will be found. If it matches the target, the search ends. Otherwise
If the middle element is less than the target: All the elements to the left of the middle element will also be less than the target (because the array is sorted). Thus, the search space can be trimmed down to the right half discarding the left half.
If the middle element is greater than the target: All the elements to the right of the middle element will also be greater than the target (because the array is sorted). Thus, the search space can be trimmed down to the left half discarding the right half.

This way, the search space is divided in half with every search increasing the chances of finding the target.
Base Case:
If the target is not present in the array, the search space will eventually reduce to zero (when high and low) with every search indicating the absence of target in the given array. In such cases, -1 can be returned.

Approach:
Two pointers are set up to define the search space — one pointing to the beginning of the array and the other to the end.
The middle element of the current search space is found and the search space is repeatedly divided in half:
If the middle element matches the target, the index is returned.
If the target is greater than the middle element, the search space is narrowed to the right half.
If the target is smaller, the search space is narrowed to the left half.
If the base case hits, return -1 indicating that the target is not present in the array.
Dry Run:

Complexity Analysis:
Time Complexity: O(logN), where N is the size of the array
In each step, the search space is divided into two halves. In the worst case, this process will continue until the search space can no longer be divided and the number of divisions required to reduce the array size to one is log(N), making the overall time complexity O(logN).

Space Complexity: O(logN), due to the recursion stack space.
class Solution:
    # Helper function to find the target in the given range
    def func(self, nums, low, high, target):
        # base case
        if low > high:
            return -1

        # to store the index of target
        mid = low + (high - low)//2
        
        # If target is found, return the index 
        if nums[mid] == target:
            ind = mid
        
        # Else if nums[mid] > target, search is left space 
        elif nums[mid] > target:
            ind = self.func(nums, low, mid-1, target)
        
        # Else search in right space
        else:
            ind = self.func(nums, mid+1, high, target)

        return ind  # Return the index 

    # Function to find the given target in a sorted array
    def search(self, nums, target):
        n = len(nums)
        
        # Find the target in the whole array
        return self.func(nums, 0, n-1, target)

def main():
    a = [-1, 0, 3, 5, 9, 12] 
    target = 9 

    # Creating an instance of Solution class
    sol = Solution() 

    # Function call to find the given target in a sorted array
    ind = sol.search(a, target)
    
    if ind == -1:
        print("The target is not present.")
    else:
        print("The target is at index:", ind)

if __name__ == "__main__":
    main()

  '''
class Solution:
    def search(self, nums, target):
        n=len(nums)
        low, high = 0, n-1
        while low <= high:
            mid = (low + high)//2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                low = mid + 1
            else:
                high = mid - 1
        return -1

        

