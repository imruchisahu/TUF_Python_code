'''Given a sorted array of nums and an integer x, write a program to find the lower bound of x.



The lower bound algorithm finds the first and smallest index in a sorted array where the value at that index is greater than or equal to a given key i.e. x.



If no such index is found, return the size of the array.


Examples:
Input : nums= [1,2,2,3], x = 2

Output:1

Explanation:

Index 1 is the smallest index such that arr[1] >= x.

Input : nums= [3,5,8,15,19], x = 9

Output: 3

Explanation:

Index 3 is the smallest index such that arr[3] >= x.

Input : nums= [3,5,8,15,19], x = 3

Output:
0
Constraints:
  1 <= nums.length <= 105
  -105 < nums[i], x < 105
  nums is sorted in ascending order.
  
  #Brute Approrach
  Intuition: 
The brute force approach is to traverse the array linearly to find the lower bound of the given integer 𝑥.

The lower bound is defined as the first element in the array that is greater than or equal to 𝑥. By iterating through the array and comparing each value with 𝑥, we can efficiently identify this position using linear search.

Approach: 
Iterate through the array and compare each element with the target value, x. Continue this comparison until an element is found that is greater than or equal to the target.
The first index, where the element at that index is greater than or equal to target, that will be the lower bound.
After the complete iteration of the array, if no such index is found, return the length of the array.

Complexity Analysis: 
Time Complexity: O(N), where N is the size of the given array. In the worst case, we have to traverse the entire array. This is the time complexity of the linear search algorithm.

Space Complexity: O(1), no extra space is used to solve this problem.
class Solution:
    # Function to find the lower bound
    def lowerBound(self, nums, x):
        n = len(nums)
        for i in range(n):
            # Check the condition for 
            # the current element
            if nums[i] >= x:
                # If lower bound is found
                return i
        # If lower bound of 
        # target is not found
        return n

if __name__ == "__main__":
    arr = [1, 2, 2, 3]
    x = 2

    # Create an instance of the Solution class
    sol = Solution()

    # Function call to find the lower bound
    ind = sol.lowerBound(arr,  x)

    print("The lower bound is the index:", ind)


#optimal Approach
Intuition: 
Since the array is sorted there is a possibility to implement Binary Search algo. The goal is to find the smallest index where the element is greater than or equal to the target value, hence by dividing the search space in half and adjusting the pointers based on the comparison results, it is easily possible to get the position of the lower bound.

Lets understand the search space for the problem:
The answer can never lie beyond the array element, if at any case the lower bound is not present and no such element is found in the array, simply return -1. Hence if possible answer are the array elements the search space will be same too. Therefore the low pointer in binary search will point to first index 0, and high that is second pointer will point to last array index that is n-1, where n is length of array.

Approach: 
Start with two pointers: low at the start and high at the end of the array. Initialize ans to the size of the array.
Calculate the middle index, mid, using mid = (low + high) / 2. If arr[mid] is greater than or equal to x, update ans with mid as this could be the the required result and trim down the search space by eliminating the right half, as the smallest possible index is needed for lower bound, so start searching in the left half of the array. Otherwise, search the right half.
Repeat until the high pointer crosses the low pointer. The ans will hold the index of the lower bound if found, or the size of the array if no such index exists.

Complexity Analysis: 
Time Complexity: O(log N), where N is the size of the given array. For using the Binary Search algorithm, the search space is divided in half each time, resulting in a logarithmic time complexity.

Space Complexity: O(1), not using any extra space to solve this problem.

class Solution:
    # Function to find the lower bound
    def lowerBound(self, nums, x):
        low, high = 0, len(nums) - 1
        ans = len(nums)

        while low <= high:
            mid = (low + high) // 2

            # Check if mid element 
            # is a potential answer
            if nums[mid] >= x:
                ans = mid
                # Search left half
                high = mid - 1
            else:
                # Search right half
                low = mid + 1

        return ans

if __name__ == "__main__":
    nums = [1, 2, 2, 3]
    x = 2

    # Create an instance of the Solution class
    sol = Solution()

    # Function call to find the lower bound
    ind = sol.lowerBound(nums, x)

    print("The lower bound is the index:", ind)
  '''
class Solution:
    def lowerBound(self, nums, x):
        low, high = 0, len(nums) - 1
        ans= len(nums)
        while low <= high:
            mid=(low + high) // 2
            if nums[mid] >= x:
                ans= mid
                high = mid - 1
            else:
                low= mid + 1

        return ans
       


