'''Given two sorted arrays nums1 and nums2, return an array that contains the union of these two arrays. The elements in the union must be in ascending order.



The union of two arrays is an array where all values are distinct and are present in either the first array, the second array, or both.


Examples:
Input: nums1 = [1, 2, 3, 4, 5], nums2 = [1, 2, 7]

Output: [1, 2, 3, 4, 5, 7]

Explanation: The elements 1, 2 are common to both, 3, 4, 5 are from nums1 and 7 is from nums2

Input: nums1 = [3, 4, 6, 7, 9, 9], nums2 = [1, 5, 7, 8, 8]

Output: [1, 3, 4, 5, 6, 7, 8, 9]

Explanation: The element 7 is common to both, 3, 4, 6, 9 are from nums1 and 1, 5, 8 is from nums2

Input: nums1 = [3, 4, 4, 4], nums2 = [6, 7, 7]

Output:
[3, 4, 6, 7]
Constraints:
1 <= nums1.length, nums2.length <= 1000
-104 <= nums1[i] , nums2[i] <= 104
Both nums1 and nums2 are sorted in non-decreasing order

Hint 1

Hint 2


Intuition
The union of two arrays will be all the unique elements of both of the arrays combined. So, using a set data structure will help & can find the distinct elements because the set does not hold any duplicates. As it is mandatory to preserve the order of the elements, use an ordered set.

Approach:
Declare a set s to store all the unique elements and a vector or list union to store the final answer.
Iterate through nums1 and nums 2 to store the elements in the set.
Now, iterate in the set and copy all the elements of the set to the answer vector and return it.

Complexity Analysis 
Time Complexity: O( (M+N)log(M+N) ), at max set can store M+N elements {when there are no common elements and elements in nums1 , nums2 are distntict}. So Inserting M+N th element takes log(M+N) time. Upon approximation across inserting all elements in worst, it would take O((M+N)log(M+N) time.

Space Complexity: O(M+N), considering space of Union Array.
from typing import List

class Solution:
    def unionArray(self, nums1, nums2):
        # Using set for storing unique elements
        s = set()
        Union = []

        # Insert all elements of nums1 into the set
        for num in nums1:
            s.add(num)

        # Insert all elements of nums2 into the set
        for num in nums2:
            s.add(num)

        # Convert the set to list to get the union
        for num in sorted(s):  # Sorting for union of sorted arrays
            Union.append(num)

        return Union
        
if __name__ == "__main__":
    # Initialize the arrays (lists in Python)
    nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    nums2 = [2, 3, 4, 4, 5, 11, 12]

    # Create an instance of the Solution class
    finder = Solution()

    """ Get the union of nums1 and 
    nums2 using the class method"""
    union = finder.unionArray(nums1, nums2)

    print("Union of nums1 and nums2 is:")
    print(" ".join(map(str, union)))

'''
class Solution:
    def unionArray(self, nums1, nums2):
        s=set()
        union=[]
        for num in nums1:
            s.add(num)
        for num in nums2:
            s.add(num)
        for num in sorted(s):
            union.append(num)
        return union