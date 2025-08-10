'''Given an array nums of n integers.



Return the length of the longest sequence of consecutive integers. The integers in this sequence can appear in any order.


Examples:
Input: nums = [100, 4, 200, 1, 3, 2]

Output: 4

Explanation:

The longest sequence of consecutive elements in the array is [1, 2, 3, 4], which has a length of 4. This sequence can be formed regardless of the initial order of the elements in the array.

Input: nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]

Output: 9

Explanation:

The longest sequence of consecutive elements in the array is [0, 1, 2, 3, 4, 5, 6, 7, 8], which has a length of 9. 

Input: nums = [1, 9, 3, 10, 4, 20, 2]

Output:
4
Constraints:
     1 <= nums.length <= 105
     -109 <= nums[i] <= 109
Intuition
One simple approach is to look for sequences of consecutive numbers by utilising linear search in the array. For each number 𝑥 in the array, we'll check if the next numbers like 𝑥+1, 𝑥+2, 𝑥+3, and so on, are also in the array. This is like checking if we can build a chain of numbers that follow each other directly. By doing this for every number in the array, we can find the longest chain of consecutive numbers. Finally, we'll find the length of the longest chain among all the numbers in the array.

Approach
As you iterate through each number in the array, begin by checking if consecutive numbers like ( x+1, x+2, x+3 ), and so on, exist in the array. The occurrence of the next consecutive number can be checked by using linear search.
When you find consecutive numbers, start counting them using a counter. Increment this counter each time you find the next consecutive number in the sequence.
This counter effectively keeps track of how long the current consecutive sequence is as you move through the array and find more consecutive numbers.
Dry Run:-Please refer to the video for the dry-run.

Complexity Analysis:
Time Complexity: O(N3), where N is the size of the array.
In the worst case, all N elements form a single consecutive sequence. Each element in nums is checked in the outer loop O(N) times. The inner while loop could also run O(N) times for one outer iteration. Since linearSearch() is called inside the conditional statement of the while loop and itself runs in O(N), this results in a cubic time complexity.

Space Complexity: O(1), as we are not using any extra space to solve this problem.

#Brute Force Solution
class Solution:
    # Helper function to perform linear search
    def linearSearch(self, nums, num):
        n = len(nums)
        # Traverse through the array
        for i in range(n):
            if nums[i] == num:
                return True
        return False

    def longestConsecutive(self, nums):
        # If the array is empty
        if len(nums) == 0:
            return 0
        n = len(nums)
        # Initialize the longest sequence length
        longest = 1

        # Iterate through each element in the array
        for i in range(n):
            # Current element
            x = nums[i]
            # Count of the current sequence
            cnt = 1

            # Search for consecutive numbers
            while self.linearSearch(nums, x + 1):
                # Move to the next number in the sequence
                x += 1
                # Increment the count of the sequence
                cnt += 1

            # Update the longest sequence length found so far
            longest = max(longest, cnt)
        return longest

if __name__ == "__main__":
    a = [100, 4, 200, 1, 3, 2]

    # Create an instance of the Solution class
    solution = Solution()

    # Function call for longest consecutive sequence
    ans = solution.longestConsecutive(a)
    print("The longest consecutive sequence is", ans)

#Better Approach

class Solution:
    def longestConsecutive(self, nums):
        n = len(nums)

        # Return 0 if array is empty
        if n == 0:
            return 0 

        nums.sort()

        # Track last smaller element
        lastSmaller = float('-inf') 
        # Count current sequence length
        cnt = 0 
        # Track longest sequence length
        longest = 1 

        for i in range(n):
            # If consecutive number exists
            if nums[i] - 1 == lastSmaller:
                # Increment sequence count
                cnt += 1 
                # Update last smaller element
                lastSmaller = nums[i] 
            # If consecutive number doesn't exist
            elif nums[i] != lastSmaller:
                # Reset count for new sequence
                cnt = 1 
                # Update last smaller element
                lastSmaller = nums[i] 
            # Update longest if needed
            longest = max(longest, cnt) 
        return longest

# Sample array
a = [100, 4, 200, 1, 3, 2]

# Create an instance of solution class
solution = Solution() 
# Function call for finding longest consecutive sequence
ans = solution.longestConsecutive(a) 
print("The longest consecutive sequence is", ans)

    

'''
class Solution:
    def longestConsecutive(self, nums):
        n = len(nums)
        # If the array is empty
        if n == 0:
            return 0 

        # Initialize the longest sequence length
        longest = 1 
        st = set()

        # Put all the array elements into the set
        for i in range(n):
            st.add(nums[i])

        # Traverse the set to find the longest sequence
        for it in st:
            # Check if 'it' is a starting number of a sequence
            if it - 1 not in st:
                # Initialize the count of the current sequence
                cnt = 1 
                # Starting element of the sequence
                x = it 

                # Find consecutive numbers in the set
                while x + 1 in st:
                    # Move to the next element in the sequence
                    x = x + 1 
                    # Increment the count of the sequence
                    cnt = cnt + 1 
                # Update the longest sequence length
                longest = max(longest, cnt)
        return longest

if __name__ == "__main__":
    a = [100, 4, 200, 1, 3, 2] 
    # Create an instance of the solution class
    solution = Solution() 
    # Function call to find the longest consecutive sequence
    ans = solution.longestConsecutive(a) 
    print("The longest consecutive sequence is", ans)
