'''Given an integer array nums, return a list of all the leaders in the array.



A leader in an array is an element whose value is strictly greater than all elements to its right in the given array. The rightmost element is always a leader. The elements in the leader array must appear in the order they appear in the nums array.


Examples:
Input: nums = [1, 2, 5, 3, 1, 2]

Output: [5, 3, 2]

Explanation: 2 is the rightmost element, 3 is the largest element in the index range [3, 5], 5 is the largest element in the index range [2, 5]

Input: nums = [-3, 4, 5, 1, -4, -5]

Output: [5, 1, -4, -5]

Explanation: -5 is the rightmost element, -4 is the largest element in the index range [4, 5], 1 is the largest element in the index range [3, 5] and 5 is the largest element in the range [2, 5]

Input: nums = [-3, 4, 5, 1, -30, -10]

Output:
[5, 1, -10]
Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104

Hint 1
Traverse the array from right to left, as the rightmost element is always a leader and gives a starting point for comparison. Maintain a variable to keep track of the maximum value encountered so far during the traversal. An element is a leader if it is greater than this maximum.

Hint 2
Intuition
The most naive thing that comes to mind is if at all any element on right is greater than the current element, then the current element can never be a leader.

Approach 
Iterate through each element of the array with the variable let's say i and take a boolean variable leader set at true initially which will tell if nums[i] is a leader or not.
For each i, iterate through the elements to the right (from i+1 to the end of the array) with the variable j & check if nums[j] is greater than nums[i], if so, reinitialize the variable leader as false and break.
After exiting from the inner loop, check if leader equals true, if so add nums[i] to ans vector. Finally return the answer vector.


Complexity Analysis  
Time Complexity: O(N2), where N is the length of that array, as 2 nested for loops are used to traverse the array.

Space Complexity: O(1), as extra space to store answer is not considered.

class Solution:
    # Function to find leaders in an array.
    def leaders(self, nums):
        ans = []

        # Iterate through each element in nums
        for i in range(len(nums)):
            leader = True

        #Check whether nums[i] is greater than all elements to its right
            for j in range(i + 1, len(nums)):
                if nums[j] >= nums[i]:
        #If any element to the right is greater or equal, nums[i] is not a leader
                    leader = False
                    break

            # If nums[i] is a leader, add it to the ans list
            if leader:
                ans.append(nums[i])

        # Return the leaders
        return ans


# Main method
nums = [1, 2, 5, 3, 1, 2]

# Create an instance of the Solution class
finder = Solution()

# Get leaders using class method
ans = finder.leaders(nums)

print("Leaders in the array are: ", end="")
for leader in ans:
    print(leader, end=" ")
print()
'''

class Solution:
    def leaders(self, nums):
        ans = []
        for i in range(len(nums)):
            leader = True
            for j in range(i+1, len(nums)):
                if nums[j] >= nums[i]:
                    leader = False
                    break
            if leader == True:
                ans.append(nums[i])       
        return ans 
