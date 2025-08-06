''''Given two sorted arrays, nums1 and nums2, return an array containing the intersection of these two arrays. Each element in the result must appear as many times as it appears in both arrays.



The intersection of two arrays is an array where all values are present in both arrays.


Examples:
Input: nums1 = [1, 2, 2, 3, 5], nums2 = [1, 2, 7]

Output: [1, 2]

Explanation:

The elements 1, 2 are the only elements present in both nums1 and nums2

Input: nums1 = [1, 2, 2, 3, 3, 3], nums2 = [2, 3, 3, 4, 5, 7]

Output: [2, 3, 3]

Explanation:

The element 2 appears in both arrays only one time.

The element 3 appears in both arrays two times so we add element 3 equal to its number of occurrences.

Input: nums1 = [-45, -45, 0, 0, 2], nums2 = [-50, -45, 0, 0, 5, 7]

Output:
[-45, 0, 0]
Constraints:
1 <= nums1.length, nums2.length <= 1000
-104 <= nums1[i], nums2[i] <= 104
Both nums1 and nums2 are sorted in non-decreasing order.

Hint 1

Hint 2
Intuition
Imagine you are organizing two different guest lists for two separate events. Some guests are invited to both events, and you want to create a new list of guests who are attending both.

Here’s how you can figure it out:

Start by going through the first guest list. For each guest in the first list, check if they are also on the second guest list. If you find a guest who is on both lists, add them to your new list of common guests, but make sure not to add the same guest more than once.

Approach 
Create an array called visited of the same size as nums2 to keep track of elements that have already been checked in nums2.
Iterate through loop (let's call the loop variable i) to go through each element in nums1.
For each element in nums1, use another for loop (let's call the loop variable j) to iterate through nums2.
For each element nums1[i], check if it is equal to nums2[j] and also ensure visited[j] is 0 (meaning this element of nums2 has not been visited yet).
If both conditions are met, add nums1[i] to the result array ans and mark visited[j] as 1 to indicate that nums2[j] has been processed.
Repeat the above steps until all elements in nums1 have been compared with all elements in nums2.


Complexity Analysis 
Time Complexity: O(MxN), where M is the length of nums1 and N is the length of nums2.

Space Complexity: O(N), where N is size of nums2, extra space to store answer is not considered.
from typing import List

class Solution:
    #Function to find intersection of two sorted arrays
    def intersectionArray(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans_list = []
        visited = [0] * len(nums2)
        i, j = 0, 0

        while i < len(nums1):
            while j < len(nums2):

                """ If nums1[i] is equal to nums2[j] and nums2[j] is
                    not visited then add nums2[j] in ans. """
                if nums1[i] == nums2[j] and visited[j] == 0:
                    
                    ans_list.append(nums2[j])
                    # Mark as visited
                    visited[j] = 1
                    
                    break
                 #If nums2[j] is greater than nums1[i], break out of loop
                elif nums2[j] > nums1[i]:
                    break
                j += 1
            i += 1
       
       #Return the final ans
        return ans_list

    def main(self):
        nums1 = [1, 2, 3, 3, 4, 5, 6, 7]
        nums2 = [3, 3, 4, 4, 5, 8]

        # Create an instance of the Solution class
        finder = Solution()

        # Get intersection of nums1 and nums2 using class method
        ans = finder.intersectionArrays(nums1, nums2)

        print("Intersection of nums1 and nums2 is:")
        print(ans)

if __name__ == "__main__":
    Solution().main()

'''

class Solution:
    def intersectionArray(self, nums1, nums2):
        ans_list=[]
        visited = [0] * len(nums2)
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j] and visited[j] == 0:
                    ans_list.append(nums2[j])
                    visited[j] = 1
                    break
                elif nums2[j] > nums1[i]:
                    break
        return ans_list

        
        
        