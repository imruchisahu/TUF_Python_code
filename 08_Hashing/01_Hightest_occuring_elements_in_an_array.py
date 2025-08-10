'''Given an array of n integers, find the most frequent element in it i.e., the element that occurs the maximum number of times. If there are multiple elements that appear a maximum number of times, find the smallest of them.



Please note that this section might seem a bit difficult without prior knowledge on what hashing is, we will soon try to add basics concepts for your ease! If you know the concepts already please go ahead to give a shot to the problem. Cheers!


Examples:
Input: arr = [1, 2, 2, 3, 3, 3]

Output: 3

Explanation: The number 3 appears the most (3 times). It is the most frequent element.

Input: arr = [4, 4, 5, 5, 6]

Output: 4

Explanation: Both 4 and 5 appear twice, but 4 is smaller. So, 4 is the most frequent element.

Input: arr = [10, 9 ,7]

Output:
7
Constraints:
1 <= n <= 105
1 <= arr[i] <= 104

Similar Problems

Intuition:
A brute-force way to solve this problem will be to use two loops:

First loop to iterate on the array, selecting an element.
Second loop to traverse the remaining array to find the occurrences of the selected element in the first loop.

Maintain a visited array to mark the elements to keep track of duplicate elements that were already taken into account.
Approach:
Initialize a visited array of boolean type having size n, where n is the size of the array with all elements set to false. Also, declare the following variables :
maxFreq - to store the frequency of the highest occurring element.
maxEle - to store the highest occurring element in the array.
In the first loop, start iterating on the elements of the array selecting one element at a time.
In the second loop, iterate on the rest portion of the array and count the frequency (number of occurrences) of the selected element. And every time, the same element is found, mark the corresponding index in the visited array as true.
If the frequency of the current element is found greater than maxFreq, update maxFreq and maxEle with the new frequency and new element respectively.
If the frequency of the current element is the same as maxFreq, store the smaller of maxEle and the current element in maxEle.
Before starting the second loop, check if the element is marked as unvisited. Skip the element if it is visited because its frequency has already been taken into consideration.
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



Complexity Analysis:
Time Complexity: O(N2) (where N is the size of the array given) – Using two nested loops.

Space Complexity: O(N) – Using a visited array of size N and a couple of variables.


class Solution:
    # Function to get the highest 
    # occurring element in array nums
    def mostFrequentElement(self, nums):
        
        # Variable to store the size of array
        n = len(nums)
        
        # Variable to store maximum frequency
        maxFreq = 0 
        
        # Variable to store element 
        # with maximum frequency
        maxEle = 0
        
        # Visited array
        visited = [False] * n
        
        # First loop
        for i in range(n):
            # Skip second loop if already visited
            if visited[i]:
                continue
            
            # Variable to store frequency
            # of current element 
            freq = 0
            
            # Second loop
            for j in range(i, n):
                if nums[i] == nums[j]:
                    freq += 1
                    visited[j] = True
            
            # Update variables if new element having 
            # highest frequency is found
            if freq > maxFreq:
                maxFreq = freq
                maxEle = nums[i]
            elif freq == maxFreq:
                maxEle = min(maxEle, nums[i])
        
        # Return the result
        return maxEle

if __name__ == "__main__":
    nums = [4, 4, 5, 5, 6]
    
    # Creating an instance of Solution class
    sol = Solution()
    
    # Function call to get the
    # highest occurring element in array nums
    ans = sol.mostFrequentElement(nums)
    
    print("The highest occurring element in the array is:", ans)

'''
from collections import Counter
class Solution:

    def mostFrequentElement(self, nums):
        
        freq = Counter(nums)
        
        max_freq = max(freq.values())
        
        most_freq_elements = [num for num, count in freq.items() if count == max_freq]
        
        return min(most_freq_elements)