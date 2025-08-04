'''Given an array arr of size n, the task is to check if the given array is sorted in (ascending / Increasing / Non-decreasing) order. If the array is sorted then return True, else return False.


Examples:
Input: n = 5, arr = [1,2,3,4,5]



Output: True



Explanation: The given array is sorted i.e Every element in the array is smaller than or equals to its next values, So the answer is True.

Input: n = 5, arr = [5,4,6,7,8]



Output: False



Explanation: The given array is Not sorted i.e Every element in the array is not smaller than or equal to its next values, So the answer is False. Here element 5 is not smaller than or equal to its future elements.

Input: n = 5, arr = [5,4,3,2,1]

Output:
False
Constraints:
1 ≤ n ≤ 106
- 109 ≤ arr[i] ≤ 109

Intuition:
The simplest method to verify if an array is sorted involves comparing each element with its subsequent neighbor. If any element is found to be greater than the one that follows it, the array is determined to be unsorted.

Approach:
Start by focusing on the element at the first index. Compare this element with every subsequent element in the array.
If this element is greater than any of the following elements, the array is not sorted.
If the element is smaller than or equal to all subsequent elements, proceed to the next element.
Continue this process for every element in the array. If all the elements are in proper order, the array can be said sorted.
Edge Cases:
If the array has zero or one element (N = 0 or N = 1), it's sorted. Return True.
Dry Run:
Image 1
Image 2
Image 3
Image 4
Image 5
Image 6
Image 7
Image 8

1/8


Solution:

Complexity Analysis:
Time Complexity: O(N²)
Compare each element with all the elements that come after it. This involves a nested loop: the outer loop runs N times (traversing every single element of the array with N elements) and the inner the loop runs up to N-1 times.

Space Complexity: O(1)
A constant amount of extra space is used because no additional data structures is needed.


class Solution:
    def arraySortedOrNot(self, arr, n):
        # Iterate through each element
        for i in range(n - 1):
            # Compare with every subsequent element
            for j in range(i + 1, n):
                # If any element is out of order, return False
                if arr[i] > arr[j]:
                    return False
        # All elements are in order
        return True

# Driver code

# Creating an instance of solution class
solution = Solution()
arr = [1, 2, 3, 4, 5]
n = len(arr)

# Function call to check if the array is sorted
sorted = solution.arraySortedOrNot(arr, n)
if sorted:
    print("Array is sorted.")
else:
    print("Array is not sorted.")

'''
class Solution:
    def arraySortedOrNot(self, arr, n):
        for i in range(n-1):
            for j in range(i+1, n):
                if arr[i]>arr[j]:
                    return False
                
        return True
        