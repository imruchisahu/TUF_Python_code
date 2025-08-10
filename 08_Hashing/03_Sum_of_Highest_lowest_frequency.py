'''Given an array of n integers, find the sum of the frequencies of the highest occurring number and lowest occurring number.


Examples:
Input: arr = [1, 2, 2, 3, 3, 3]

Output: 4

Explanation: The highest frequency is 3 (element 3), and the lowest frequency is 1 (element 1). Their sum is 3 + 1 = 4.

Input: arr = [4, 4, 5, 5, 6]

Output: 3

Explanation: The highest frequency is 2 (elements 4 and 5), and the lowest frequency is 1 (element 6). Their sum is 2 + 1 = 3.

Input: arr = [10, 9, 7, 7, 8, 8, 8]

Output:
4
Constraints:
1 <= n <= 105
1 <= arr[i] <= 104

Similar Problems
Intuition:
The brute force way to solve this problem will be to count the frequency of each element in the array, and once found, this frequency can be compared with the highest and the lowest frequency. Accordingly, the highest and the lowest frequency can be set.

Approach:
Determine the size of the array. Initialize two variables: one to keep track of the highest frequency and another for the lowest frequency.
Initially, set the highest frequency to zero (to ensure any actual frequency found will be higher and update this value.) and the lowest to the size of the array (to ensure any actual frequency found will be lower and update this value).
Create a visited array to avoid counting the same number multiple times.
Loop through each element in the array. For each element:
If the element has already been counted (visited), skip it.
Otherwise, count how many times this element appears in the array by comparing it with every other element.
Update the highest and lowest frequency variables based on the count of the current element.
Mark all occurrences of this element as visited.
Finally, add the highest and lowest frequencies together and return the result.
Dry Run:
Image 1
Image 2
Image 3
Image 4
Image 5
Image 6
Image 7
Image 8
Image 9

1/9


Solution:
Cpp
Java
Python
Javascript
CSharp
Go


1234567891011121314151617181920212223
Complexity Analysis:
Time Complexity: O(N2) (where N is the size of the array given) – Using two nested loops.

Space Complexity: O(N) – Using a visited array of size N and a couple of variables.




class Solution:
    """ Function to get the sum of highest
    and lowest frequency in array """
    def sumHighestAndLowestFrequency(self, nums):
        
        # Variable to store the size of array
        n = len(nums)
        
        """ Variable to store maximum 
        and minimum frequency """
        max_freq = 0
        min_freq = n

        # Visited array
        visited = [False] * n
        
        # First loop
        for i in range(n):
            # Skip second loop if already visited
            if visited[i]:
                continue
            
            """ Variable to store frequency
            of current element """
            freq = 0
            
            # Second loop
            for j in range(i, n):
                if nums[i] == nums[j]:
                    freq += 1
                    visited[j] = True
            
            """ Update maximum and 
            minimum frequencies """
            max_freq = max(max_freq, freq)
            min_freq = min(min_freq, freq)
            
        # Return the required sum
        return max_freq + min_freq

# Example usage
nums = [1, 2, 2, 3, 3, 3]

""" Creating an instance of 
Solution class """
sol = Solution()

""" Function call to get the sum of highest
and lowest frequency in array """
ans = sol.sumHighestAndLowestFrequency(nums)

print("The sum of highest and lowest frequency in the array is:", ans)

'''
from collections import Counter
class Solution:
    def sumHighestAndLowestFrequency(self, nums):
        freq_map = Counter(nums)
        max_freq = max(freq_map.values())
        min_freq = min(freq_map.values())
        return max_freq + min_freq
        