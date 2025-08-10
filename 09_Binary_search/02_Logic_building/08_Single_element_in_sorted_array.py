'''
Given an array nums sorted in non-decreasing order. Every number in the array except one appears twice. Find the single number in the array.


Examples:
Input :nums = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]

Output:4

Explanation: Only the number 4 appears once in the array.

Input : nums = [1, 1, 3, 5, 5]

Output:3

Explanation: Only the number 3 appears once in the array.

Input :nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7]

Output:
7
Constraints:
  n == nums.length
  1 <= n <= 104
  -104 <= nums[i] <= 104

#Brute 1
Intuition: 
The idea here is to perform simple comparisons between elements in the array. During iteration, for each element, check if it is equal to either its previous or next element. If it is, then it is not the single element; otherwise, it is the single element.

Approach: 
Edge case: If size of array equals 1, immediately return the only element in the array since it can't have a duplicate.
Handle the boundary cases(index `0` and index `sizeOfArray - 1`): Check if element at current index is not equal to its adjacent element (nums[1] for the element at 0th index and nums[sizeOfArray - 2] for the last element). If true, current element is the single non-duplicate element, and return it immediately.
For any other index i in between:Traverse through the array using a loop to examine each element in the array. Check if the current element is not equal to either of its adjacent elements (previous one and the next one). If so, current element is the single non-duplicate element, and return it immediately. If none of the above conditions match return of -1.

class Solution:
    """ Function to find the single non
        duplicate element in a sorted array """
    def singleNonDuplicate(self, nums):
        n = len(nums)  # Size of the array.
        
        """ If array has only one element
            return it immediately."""
        if n == 1:
            return nums[0]

        """ Traverse through the array to find 
            the single non-duplicate element."""
        for i in range(n):
            # Check for the first index.
            if i == 0:
                if nums[i] != nums[i + 1]:
                    return nums[i]
            # Check for the last index.
            elif i == n - 1:
                if nums[i] != nums[i - 1]:
                    return nums[i]
            # Check for any other index.
            else:
                if nums[i] != nums[i - 1] and nums[i] != nums[i + 1]:
                    return nums[i]

        """ Dummy return statement,
            should never reach here."""
        return -1

if __name__ == "__main__":
    nums = [1, 1, 2, 2, 3, 3, 4]
    
    # Create an object of the Solution class.
    sol = Solution()
    
    ans = sol.singleNonDuplicate(nums)
    
    # Print the result.
    print("The single element is:", ans)

Complexity Analysis: 
Time Complexity:O(N), where N is size of the array. As the array is being traversed only once using a single loop.

Space Complexity: As no additional space is used, so the Space Complexity is O(1).

#Brute 2
Intuition: 
Here, the concept of XOR operation will be used to solve this problem. When XOR is applied to two identical numbers, it results in 0 (a XOR a = 0), and XOR of a number with 0 gives the number itself (a XOR 0 = a). Therefore, iterate through the array and perform XOR on each element. Numbers that appear twice will cancel out to zero, leaving only the single number as the answer.

Approach: 
Edge case: If size of array equals 1, immediately return the only element in the array since it can't have a duplicate.
Start by initializing ans to 0. This variable will eventually hold the XOR result of all elements in the array.
Use a loop to iterate through all elements of the array nums. Perform XOR operation (^) between ans and each element of the array. XOR of an element with itself cancels out (resulting in 0), so the operation effectively pairs up and cancels out duplicate elements. Finally, return the ans variable.

class Solution:
    """ Function to find the single non
        duplicate element in a sorted array """
    def singleNonDuplicate(self, nums):
        n = len(nums)  # Size of the array.
        
        """ XOR all the elements to find 
            the single non-duplicate element. """
        ans = 0
        for num in nums:
            ans ^= num
        
        """ Return the single non 
            duplicate element found. """
        return ans

if __name__ == "__main__":
    nums = [1, 1, 2, 2, 3, 3, 4]
    
    # Create an object of the Solution class.
    sol = Solution()
    
    ans = sol.singleNonDuplicate(nums)
    
    # Print the result.
    print("The single element is:", ans)

Complexity Analysis: 
Time Complexity:O(N), where N is size of the array. As the array is being traversed only once using a loop.

Space Complexity: As no additional space is used, so the Space Complexity is O(1).


#Optimal Approach
Intuition: 
The idea is to use the binary search algorithm to optimize the solution, especially when it is given that the array is sorted. Binary search is well-suited for efficiently finding elements in sorted arrays.
Since each element in the array appears twice and forms pair(even, odd), that is the first element occurs at even index and the second one occurs at odd index, till a single unpaired element has appeared in the array, after that the index of occurrence of pairs would be(odd, even). This observation can be used to adjust the search space dynamically, hence enhancing the overall time complexity.
Approach: 
Edge case: If size of array equals 1, immediately return the only element in the array since it can't have a duplicate.
Handle the boundary cases(index `0` and index `sizeOfArray - 1`): Check if element at current index is not equal to its adjacent element (nums[1] for the element at 0th index and nums[sizeOfArray - 2] for the last element). If true, current element is the single non-duplicate element, and return it immediately.
Use a binary search algorithm to efficiently locate the single non-duplicate element. Initialize `low` as 1 and `high` as element just before the last element to search within the range of potential candidates.
While `low` is less than or equal to `high`, calculate the middle index `mid`. Check if element at `mid` is the unique element by checking its previous and next element in the array, if so, then it is the single non-duplicate element and return it.
If element at `mid` is not the unique element and mid is odd (mid % 2 == 1) and element at `mid` equals element at `[mid - 1]`, or if mid is even (mid % 2 == 0) and element at `mid` equals element at `[mid + 1]`, then adjust the search range:
If in the left part (mid is odd and element at `mid` equals element at `[mid-1]`), move low to mid + 1 to eliminate the left half.
Otherwise, move high to mid - 1 to eliminate the right half.
The loop continues adjusting low and high until the unique element is found. If the loop completes without finding the element, return -1 as a dummy return statement.

class Solution:
    """ Function to find the single non 
        duplicate element in a sorted array """
    def singleNonDuplicate(self, nums):
        n = len(nums) # Size of the array.

        # Edge cases:
        if n == 1:
            return nums[0]
        if nums[0] != nums[1]:
            return nums[0]
        if nums[n - 1] != nums[n - 2]:
            return nums[n - 1]

        low, high = 1, n - 2
        while low <= high:
            mid = (low + high) // 2

            # If nums[mid] is the single element:
            if nums[mid] != nums[mid + 1] and nums[mid] != nums[mid - 1]:
                return nums[mid]

            # We are in the left part:
            if (mid % 2 == 1 and nums[mid] == nums[mid - 1]) or (mid % 2 == 0 and nums[mid] == nums[mid + 1]):
                # Eliminate the left half:
                low = mid + 1
            # We are in the right part:
            else:
                # Eliminate the right half:
                high = mid - 1

        # Dummy return statement:
        return -1

nums = [1, 1, 2, 2, 3, 3, 4]

# Create an instance of the Solution class.
sol = Solution()

ans = sol.singleNonDuplicate(nums)

# Print the result.
print(f"The single element is: {ans}")


Complexity Analysis: 
Time Complexity:O(logN), N is size of the given array. We are basically using the Binary Search algorithm.

Space Complexity: As no additional space is used, so the Space Complexity is O(1)



'''
class Solution:
    def singleNonDuplicate(self, nums):
        ans=0
        for num in nums:
            ans ^= num
        return ans
       