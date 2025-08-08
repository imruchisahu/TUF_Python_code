'''Given two integer arrays nums1 and nums2. Both arrays are sorted in non-decreasing order.



Merge both the arrays into a single array sorted in non-decreasing order.

The final sorted array should be stored inside the array nums1 and it should be done in-place.
nums1 has a length of m + n, where the first m elements denote the elements of nums1 and rest are 0s.
nums2 has a length of n.

Examples:
Input: nums1 = [-5, -2, 4, 5], nums2 = [-3, 1, 8]

Output: [-5, -3, -2, 1, 4, 5, 8]

Explanation: The merged array is: [-5, -3, -2, 1, 4, 5, 8], where [-5, -2, 4, 5] are from nums1 and [-3, 1, 8] are from nums2

Input: nums1 = [0, 2, 7, 8], nums2 = [-7, -3, -1]

Output: [-7, -3, -1, 0, 2, 7, 8]

Explanation: The merged array is: [-7, -3, -1, 0, 2, 7, 8], where [0, 2, 7, 8] are from nums1 and [-7, -3, -1] are from nums2

Input: nums1 = [1, 3, 5], nums2 = [2, 4, 6, 7]

Output:
[1, 2, 3, 4, 5, 6, 7]
Constraints:
n == nums2.length.
m + n == nums1.length.
0 <= n, m <= 1000
-104 <= nums1[i], nums2[i] <= 104
Both nums1 and nums2 are sorted in non-decreasing order.

Similar Problems

Hint 1

Hint 2
Intuition
The naive idea is to use the sorted property of array. As the given arrays are sorted, use 2 pointer approach to get a third array by simply comparing the elements at both the pointers, the third array contains all the elements from the given two arrays in the sorted order. Now, from the sorted third array, again fill back the given two arrays.

Approach
Declare a third array, arr3[] of size n+m, and two pointers i.e. left and right, one pointing to the first index of arr1[] and the other pointing to the first index of arr2[].
Now, if arr1[left] is less than arr2[right], insert the element arr1[left] into the third array and increase the left pointer by 1.
If arr2[right] less than arr1[left], insert the element arr2[right] into the third array and increase the right pointer by 1.
If arr1[left] is equal to arr2[right], insert any of the elements and increase that particular pointer by 1.
If one of the pointers reaches the end, then only move the other pointer and insert the rest of the elements of that particular array into the third array i.e. arr3[].
If we move the pointer like the above, will get the third array in the sorted order. Now, from sorted array arr3[], copy all the elements back to arr1[].

Complexity Analysis 
Time Complexity: O(N+M) + O(N+M), where N and M are the sizes of the given arrays. O(N+M) is for copying the elements from nums1[] and nums2[] to the third array. And another O(N+M) is for filling back nums1[].

Space Complexity: O(N+M) for using an extra array of size N+M.

from typing import List

class Solution:
    # Function to merge two sorted arrays nums1 and nums2
   def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Declare a 3rd array and 2 pointers:
        merged = [0] * (m + n)
        left = 0
        right = 0
        index = 0

        """ Insert elements from nums1 and nums2 into
        merged array using left and right pointers """
        while left < m and right < n:
            if nums1[left] <= nums2[right]:
                merged[index] = nums1[left]
                left += 1
            else:
                merged[index] = nums2[right]
                right += 1
            index += 1

        # If right pointer reaches the end of nums2:
        while left < m:
            merged[index] = nums1[left]
            left += 1
            index += 1

        # If left pointer reaches the end of nums1:
        while right < n:
            merged[index] = nums2[right]
            right += 1
            index += 1

        """ Copy elements from merged array
        array back to nums1 """
        for i in range(m + n):
            nums1[i] = merged[i]
            

if __name__ == "__main__":
    nums1 = [-5, -2, 4, 5, 0, 0, 0]
    nums2 = [-3, 1, 8]
    m = 4
    n = 3

    # Create an instance of the Solution class
    sol = Solution()

    sol.merge(nums1, m, nums2, n)

    # Output the merged arrays
    print("The merged arrays is:")
    print("nums1[] =", nums1)
 

'''

# class Solution:
#     def merge(self, nums1, m, nums2, n):
#         nums1[:] = sorted(nums1[:m] + nums2) # O(n+m) SC= O(m+n)

#second approch
class Solution:
    def merge(self, nums1, m, nums2, n):
        i = m - 1        # Pointer for the end of valid nums1
        j = n - 1        # Pointer for nums2
        k = m + n - 1    # Pointer for the end of nums1 (total size)

        # Merge in reverse order
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # If there are remaining elements in nums2, copy them
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

        
#TC = O(M+N) and sc= O(1) no extra spce used
        
