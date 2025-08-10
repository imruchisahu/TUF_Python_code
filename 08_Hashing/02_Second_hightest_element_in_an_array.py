'''Given an array of n integers, find the second most frequent element in it. If there are multiple elements that appear a maximum number of times, find the smallest of them. If second most frequent element does not exist return -1.


Examples:
Input: arr = [1, 2, 2, 3, 3, 3]

Output: 2

Explanation: The number 2 appears the second most (2 times) and number 3 appears the most(3 times). 

Input: arr = [4, 4, 5, 5, 6, 7]

Output: 6

Explanation: Both 6 and 7 appear second most times, but 6 is smaller.

Input: arr = [10, 9 ,7, 7]

Output:
9
Constraints:
1 <= n <= 105
1 <= arr[i] <= 104

Similar Problems

Intuition:
Imagine you have a bag full of marbles, each with a different number. Your task is to find the marble that appears the second most number of times in the bag. To solve this, we need to keep track of the number of times each marble appears. We should identify the marble with the highest occurrence first and then look for the marble that comes next in terms of frequency. This way, we ensure that we correctly find the second highest occurring marble in the bag.

Approach:
Create variables to store the highest and second highest frequencies. Also, create variables to store the corresponding elements. Use a visited array of boolean type to mark elements that have already been counted to avoid recounting them.
Loop through each element in the array. For each element, if it hasn't been counted yet, proceed to count its occurrences. For each element, count how many times it appears in the array. Mark these elements as counted.
Compare the frequency of the current element with the highest and second highest frequencies. Update the highest and second highest frequencies and their corresponding elements as needed.
If two elements have the same frequency, choose the smaller one. After processing all elements, return the element with the second highest frequency.

Complexity Analysis:
Time Complexity: O(N2) (where N is the size of the array given) – Using two nested loops.

Space Complexity: O(N) – Using a visited array of size N and a couple of variables.

class Solution:
    """Function to get the second highest 
    occurring element in array"""
    def secondMostFrequentElement(self, nums):
        
        # Variable to store the size of array
        n = len(nums)
        
        """Variable to store maximum frequency
        and second Max frequency"""
        maxFreq = 0
        secMaxFreq = 0
        
        """Variable to store elements with most 
        and second most frequency"""
        maxEle = -1
        secEle = -1
        
        # Visited array
        visited = [False] * n
        
        # First loop
        for i in range(n):
            # Skip second loop if already visited
            if visited[i]:
                continue
            
            """Variable to store frequency
            of current element"""
            freq = 0
            
            # Second loop
            for j in range(i, n):
                if nums[i] == nums[j]:
                    freq += 1
                    visited[j] = True
            
            """Update variables if new element  
            having highest frequency or second
            highest frequency is found"""
            if freq > maxFreq:
                secMaxFreq = maxFreq
                maxFreq = freq
                secEle = maxEle
                maxEle = nums[i]
            elif freq == maxFreq:
                maxEle = min(maxEle, nums[i])
            elif freq > secMaxFreq:
                secMaxFreq = freq
                secEle = nums[i]
            elif freq == secMaxFreq:
                secEle = min(secEle, nums[i])
        
        # Return the result
        return secEle

if __name__ == "__main__":
    nums = [4, 4, 5, 5, 6, 7]
    
    """Creating an instance of 
    Solution class"""
    sol = Solution()
    
    """Function call to get the second
    highest occurring element in array"""
    ans = sol.secondMostFrequentElement(nums)
    
    print(f"The second highest occurring element in the array is: {ans}")


'''
from collections import Counter

class Solution:
    def second_most_frequent(self, nums):
        freq = Counter(nums)  
        
        freq_list = sorted(freq.items(), key=lambda x: (-x[1], x[0]))  

        first_freq = freq_list[0][1]

        for value, count in freq_list:
            if count < first_freq:
                return value  

        return -1  
s=Solution()
print(s.second_most_frequent([1, 2, 2, 3, 3, 3]))

        