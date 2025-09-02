'''
Given a binary array nums and an integer k, flip at most k 0's.

Return the maximum number of consecutive 1's after performing the flipping operation.


Examples:
Input : nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0] , k = 3

Output : 10

Explanation : The maximum number of consecutive 1's are obtained only if we flip the 0's present at position 3, 4, 5 (0 base indexing).

The array after flipping becomes [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0].

The number of consecutive 1's is 10.

Input : nums = [0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1] , k = 3

Output : 9

Explanation : The underlines 1's are obtained by flipping 0's in the new array.

[1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1].

The number of consecutive 1's is 9.

Input : nums = [1, 1, 0, 0, 1] , k = 3

Output:
5
Constraints:
1 <= nums.length <= 105
0 <= nums[i] <= 1
0 <= k <= nums.length


#BRute
# Intuition: 
The idea here is to generate all possible substrings of the given array and while doing so, keep a track of all the zeros encountered so far in the substring. If the number of zeros exceeds k then no need to consider that substring, else calculate the length of the current substring and update the maximum length of substring.

Approach: 
Iterate the array using for loop which runs from 0 to sizeOfArray - 1, which indicates the starting point of a substring. Now, initialize a variable zero to 0 to keep track number of zeros found so far in the substring.
Use another for loop, which basically indicates the ending point of the substring, if the current element is 0, then increase the the variable zero by.
If number of 0 in the current substring exceeds k then break out of the inner loop, no need to consider such string. Else, calculate the length of current substring and update the maximum length of substring encountered so far. Finally, return the maximum length of the substring.
package main import ( "fmt" "math" ) // Function to find the length of the longest substring with at most k zeros func longestOnes(nums []int, k int) int { // Length of the input array n := len(nums) // Maximum length of the substring maxLen := 0 // Variable to count the number of zeros in the current window zeros := 0 // Iterate through all possible starting points of the substring for i := 0; i < n; i++ { zeros = 0 // Expand the window from starting point i to the end of the array for j := i; j < n; j++ { if nums[j] == 0 { // Increment zeros count when encountering a zero zeros++ } // If zeros count is within the allowed limit (k), update maxLen if zeros <= k { // Calculate the length of substring len := j - i + 1 maxLen = int(math.Max(float64(maxLen), float64(len))) } else { break } } } // Return the maximum length return maxLen } func main() { input := []int{1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0} k := 2 // Function call to get the result length := longestOnes(input, k) // Print the result fmt.Printf("Length of longest substring with at most %d zeros: %d\n", k, length) }
Complexity Analysis: 
Time Complexity:O(N2), where N is the size of the array. As for every element of the array the inner loop runs for N times.

Space Complexity: O(1) as no extra space is being used.


#Better
Intuition: 
The idea here is to use sliding window technique to solve this problem in linear time. The sliding window technique is chosen because it efficiently manages a window within the input array that meets specific criteria. It dynamically adjusts the size and position of the window based on the number of zeros encountered to ensure the that the number of zeros are less than and equal to k.

Approach: 
First, initialize few variables as : l and r as pointers to the left and right ends of the window respectively, both starting at the beginning of the array nums, zeros to keep track of the number of zeros encountered within the current window, maxLen to store the maximum length of the substring found so far.
Use a sliding window approach where r moves from the start to the end of the array nums. Check if current element in the array is 0. If yes, increment the zeros count.
While zeros exceeds k, adjust the window by moving l to the right until zeros is less than or equal to k. This ensures that the window contains at most k zeros.
If number of zero is less than or equal to k then calculate the length of the substring. Update maximum length of sustring to keep track of the maximum length encountered during the iteration and finally, return it.

class Solution:
    """ Function to find the length of the
    longest substring with at most k zeros """
    def longestOnes(self, nums, k):
        
        # Length of the input array
        n = len(nums)
        
        # Pointers for sliding window approach
        l, r = 0, 0
        
        """ Variables to count zeros
        and store maximum length """
        zeros, maxLen = 0, 0
        
        """ Iterate through the array 
        using sliding window approach """
        while r < n:
            if nums[r] == 0:
                
                """ Increment zeros count 
                when encountering a zero """
                zeros += 1  
            while zeros > k:
                if nums[l] == 0:
                    
                    """ Decrement zeros count
                    when moving left pointer """
                    zeros -= 1 
                
                """ Move left pointer to the
                right to shrink the window """
                l += 1  
            
            """ Calculate the length 
            of current substring """
            length = r - l + 1
            
            """ Update maxLen if the current
            substring length is greater """
            maxLen = max(maxLen, length)
            
            """ Move right pointer 
            to expand the window """
            r += 1  
        
        # Return the maximum length
        return maxLen

if __name__ == "__main__":
    
    input_arr = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    k = 2  
    
    # Create an instance of Solution class
    sol = Solution()
    
    length = sol.longestOnes(input_arr, k)
    
    # Print the result
    print(f"Length of longest substring with at most {k} zeros: {length}")

Complexity Analysis: 
Time Complexity:O(2N), where N is the size of the array. The outer and the inner loop is running for N times each.

Space Complexity: O(1) as no extra space is being used.

#Optimal
Intuition: 
The idea here is to employ the sliding window approach efficiently by avoiding the additional O(N) time complexity incurred when shifting the window entirely in the better solution, to ensure that the total number of zeros does not exceed k. Instead of moving the left pointer (l) to eliminate excess zeros completely, shift the window by one position at a time. This method ensures that the problem can be solved in O(N) time complexity only.

Approach: 
First, initialize few variables as: l and r as pointers, where l marks the left boundary and r marks the right boundary of the sliding window, zeros to count the number of zeros encountered within the current window, maxLen to store the maximum length of valid substrings found.
Use the r pointer to traverse through the array. For each element, check if it is 0. If so, increment the zeros count because we are adding one more zero to the current window.
After incrementing zeros, check if zeros exceeds the allowed limit k. If so, adjust the window by moving the l pointer to the right until the window contains at most k zeros (zeros <= k). Decrement the zeros count accordingly when the element pointed by l is 0 and increment l.
Whenever zeros is less than or equal to k, calculate the length of the current substring. Update maxLen to store the maximum length encountered so far among all valid substrings. Move r pointer by 1. Finally, return maxLen variable.
class Solution:
    """ Function to find the length of the
    longest substring with at most k zeros """
    def longestOnes(self, nums, k):
        
        # Length of the input array
        n = len(nums)
        
        # Pointers for sliding window approach
        l, r = 0, 0
        
        """ Variables to count zeros
        and store maximum length """
        zeros, maxLen = 0, 0
               
        """ Iterate through the array 
        using sliding window approach """
        while r < n:
            
            if nums[r] == 0:
                zeros += 1
            
            if zeros > k:
                if nums[l] == 0:
                    
                    """ Decrement zeros count
                    when moving left pointer """
                    zeros -= 1 
                l += 1
            
            if zeros <= k:
                """ Calculate the length 
                of current substring """
                length = r - l + 1
            
                """ Update maxLen if the current
                substring length is greater """
                maxLen = max(maxLen, length)
            
            r += 1  
        
        # Return the maximum length
        return maxLen

if __name__ == "__main__":
    input_nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    k = 2  
    
    # Create an instance of Solution class
    sol = Solution()
    
    length = sol.longestOnes(input_nums, k)
    
    # Print the result
    print(f"Length of longest substring with at most {k} zeros: {length}")
    
Complexity Analysis: 
Time Complexity:O(N), where N is the size of the array. As for every element , the loop run N times.

Space Complexity: O(1) as no extra space is being used.

'''

class Solution:
    def longestOnes(self, nums, k):
        n = len(nums)
        l, r = 0, 0
        zeros, maxLen = 0, 0
        while r < n:
            
            if nums[r] == 0:
                zeros += 1
            
            if zeros > k:
                if nums[l] == 0:
                    zeros -= 1 
                l += 1
            
            if zeros <= k:
                length = r - l + 1
                maxLen = max(maxLen, length)
            
            r += 1  
        return maxLen