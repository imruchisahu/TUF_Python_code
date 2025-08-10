'''Given a sorted array of nums and an integer x, write a program to find the upper bound of x.



The upper bound algorithm finds the first and smallest index in a sorted array where the value at that index is greater than a given key i.e. x.



If no such index is found, return the size of the array.


Examples:
Input : n= 4, nums = [1,2,2,3], x = 2

Output:3

Explanation:

Index 3 is the smallest index such that arr[3] > x.

Input : n = 5, nums = [3,5,8,15,19], x = 9

Output: 3

Explanation:

Index 3 is the smallest index such that arr[3] > x.

Input : n = 5, nums = [3,5,8,15,19], x = 3

Output:
1
Constraints:
  1 <= nums.length <= 105
  -105 < nums[i], x < 105
  nums is sorted in ascending order.

#Brute Froce
  
Intuition: 
Imagine you're a concert organizer with a sorted list of ticket prices. A customer wants to know the first ticket price that is more expensive than a certain amount they can afford. This helps them see which tickets are out of their budget.

For example, have the following sorted list of ticket prices: [10, 20, 30, 40, 50, 60, 70, 80].

A customer can afford to pay up to Rs35. You want to find the first ticket price that exceeds Rs35.

Hence in order to find the first price greater than Rs35, you can go through the list one by one from the start until you find a price that's more than Rs35. This method is linear search approach to find the solution to this problem.

Approach: 
To find the upper bound of a given target value in an array, iterate through each element of the array.
Compare each element with the given target value. Continue this comparison until you find an element that is greater than the target.
The smallest index where the current element is greater than the target, will be the upper bound of the target element in the array.
If no such element is found, it means the target does not have an upper bound in the array, hence return the last index that is length of the array (considering 0 based indexing).


class Solution:
    # Function to find the upper bound
    def upperBound(self, nums, x):
        n = len(nums)
        # Iterate over each element
        for i in range(n):
            # Return the index if the 
            # element is greater than x
            if nums[i] > x:
                return i
        # If no element is greater 
        # than x, return n
        return n

if __name__ == "__main__":
    nums = [3, 5, 8, 9, 15, 19]
    x = 9

    # Create an instance of the Solution class
    solution = Solution()

    # Find the upper bound index for x
    ind = solution.upperBound(nums, x)

    print("The upper bound is the index:", ind)
Complexity Analysis: 
Time Complexity: O(N), where N is the size of the given array. In the worst case, we have to traverse the entire array, which is the time complexity of the linear search algorithm.

Space Complexity: O(1), as we are using no extra space to solve this problem.


#Optimal Approach
Intuition: 
Here, the idea is to use the fact that the given array is sorted. The linear search algorithm checks each element of the array to arrive at a conclusion. This can be optimized by using binary search, where the search space is halved based on the condition.

In binary search, the upper bound is determined by finding the smallest index for which the element is greater than the target. At each step, check if the element at the middle index (mid) is greater than the target. If it is, store this index as a potential answer and continue searching in the left half of the array, as the smallest possible index for the upper bound must be found.

Approach: 
Start with initializing 2 end points which mark the search range of the problem. Lets call them `low` and `high` where `low` pointer starts at the first index, and the `high` pointer points to the last index.
Along with this there shall be a need for `ans` variable initialized to the size of the array. This variable will store the index of the upper bound, or remain as the size of the array if no upper bound is found.
Calculate the middle index using simple formula of `mid=(low + high)/2` or `mid=(low+(high-low)/2)`. Compare if the middle index element is greater than the target. In that case update `ans` with `mid` (as that can be a potential answer) and search the left half for a smaller index that meets the condition.
If middle index element is less than or equal to the target, move to the right half to continue the search. This reduces the search space by half each time.
Repeat this process until the `low` pointer crosses the `high` pointer. At the end `ans` variable will then hold the index of the upper bound.



class Solution:
    # Function to find the upper bound
    def upperBound(self, nums, x):
        low, high = 0, len(nums) - 1
        ans = len(nums)

        # Binary search to find the upper bound
        while low <= high:
            # Calculate mid index
            mid = (low + high) // 2

            # Update ans if current
            #  element is greater than x
            if nums[mid] > x:
                ans = mid
                high = mid - 1
            else:
                # Otherwise, move to the right half
                low = mid + 1

        return ans

if __name__ == "__main__":
    nums = [1, 2, 2, 3]
    x = 2

    # Create an instance of the Solution class
    sol = Solution()

    # Function call to find the upper bound
    ind = sol.upperBound(nums, x)

    print("The upper bound is the index:", ind)
Complexity Analysis: 
Time Complexity: O(logN), where N is the size of the given array. We are using the Binary Search algorithm, which divides the search space in half each time, resulting in a logarithmic time complexity.

Space Complexity: O(1), as we are not using any extra space to solve this problem.

  '''
class Solution:
    def upperBound(self, nums, x):
        low, high = 0, len(nums) - 1
        ans= len(nums)
        while low <= high:
            mid=(low + high) // 2
            if nums[mid] > x:
                ans= mid
                high = mid - 1
            else:
                low= mid + 1
        return ans