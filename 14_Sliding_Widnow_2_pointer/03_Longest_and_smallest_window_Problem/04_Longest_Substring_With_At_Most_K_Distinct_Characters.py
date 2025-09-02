'''
Given a string s and an integer k.Find the length of the longest substring with at most k distinct characters.


Examples:
Input : s = "aababbcaacc" , k = 2

Output : 6

Explanation : The longest substring with at most two distinct characters is "aababb".

The length of the string 6.

Input : s = "abcddefg" , k = 3

Output : 4

Explanation : The longest substring with at most three distinct characters is "bcdd".

The length of the string 4.

Input : s = "abccab" , k = 4

Output:
6
Constraints:
1 <= s.length <= 105
1 <= k <= 26


#Brute
Intuition: 
The idea here is to generate all possible substrings of the given array using two loops and while doing so, check if the number of distinct characters in the current substring is within the allowed limit, using a map data structure. If the number of distinct characters exceed limit, then no need to consider that substring, else calculate the length of the current substring and update the maximum length of substring.

Approach: 
First, initialize few variables as: maxLen as 0, which will store the maximum length of substrings with at most k distinct characters, mpp an unordered_map to track the count of each character in the current substring.
iterate through each possible starting point of the substring in the string using a loop. Before entering the inner loop for each new starting point, clear the map. This ensures that we start counting characters fresh for the new window.
Use another loop from strating point of the substring till sizeOfArray - 1, to expand the window and include more characters in the substring. Add each character to the map and increment its count.
Check if the number of distinct characters is within the limit k. If so, calculate the length of the current valid substring. Update maximum length of the substring. Else, break out of the loop. Finally, return the maxLen variable as an answer.

class Solution:
    """ Function to find the maximum length of 
    substring with at most k distinct characters """
    def kDistinctChar(self, s: str, k: int) -> int:
        
        """ Variable to store the 
        maximum length of substring"""
        maxLen = 0  
        
        """ Dictionary to track the count of each
        character in the current window"""
        mpp = {}
        
        """ Iterate through each starting
        point of the substring"""
        for i in range(len(s)):
            # Clear dictionary for a new starting point
            mpp.clear()
            
            for j in range(i, len(s)):
                
                # Add the current character to the dictionary
                if s[j] in mpp:
                    mpp[s[j]] += 1
                else:
                    mpp[s[j]] = 1
                
                """ Check if the number of distinct 
                characters is within the limit"""
                if len(mpp) <= k:
                    
                    """ Calculate the length of
                    the current valid substring"""
                    maxLen = max(maxLen, j - i + 1)
                else:
                    break
        
        # Return the maximum length found
        return maxLen

if __name__ == "__main__":
    s = "aaabbccd"  
    k = 2
    
    # Create an instance of Solution class
    sol = Solution()
    
    length = sol.kDistinctChar(s, k)
    
    # Print the result
    print(f"Maximum length of substring with at most {k} distinct characters: {length}")

Complexity Analysis: 
Time Complexity:O(N2), where N is the size of the array. As for every element of the array the inner loop runs for N times.

Space Complexity: O(k), as at most the map data structure is holding k elements.

#Better
Intuition: 
Here, the idea is to use sliding window approach with hashMap to solve this problem in optimal way. Which ensures that to find the longest substring with at most k distinct characters efficiently by maintaining a sliding window and using a hashmap to keep track of character frequencies within the window.

Approach: 
First, initialize few variables: l and r pointers to 0 which represent the left and right boundaries of the current window respectively, maxLen initialized to 0 to store the maximum length of substring with at most k distinct characters found so far, mpp a hashMap is used to track the frequency of characters within the current window.
Use r pointer to expand the window by iterating through each character of the string. Increment the frequency of the current character in the mpp HashMap.
Check if the number of distinct characters exceeds k. If so, maintain k distinct characters by decrementing the frequency of the character at l pointer. If the frequency becomes zero, remove that character from the map. Move l pointer to the right to shrink the window.
Continue expanding r until it reaches the end of the string. Return maxLen as an answer.

class Solution:
    """ Function to find the length of the longest 
    substring with at most k distinct characters """
    def kDistinctChar(self, s, k):
        
        """ Initialize left pointer, right pointer,
        and maximum length of substring"""
        l, r, maxLen = 0, 0, 0
        
        # Hash map to store character frequencies
        mpp = {}
        
        while r < len(s):
            
            # Increment frequency of current character
            if s[r] in mpp:
                mpp[s[r]] += 1
            else:
                mpp[s[r]] = 1
            
            """ If the number of distinct characters 
            exceeds k, shrink the window from the left"""
            while len(mpp) > k:
                
                # Decrement frequency of character at left pointer
                mpp[s[l]] -= 1
                if mpp[s[l]] == 0:
                    
                    """ Remove character from map 
                    if its frequency becomes zero"""
                    del mpp[s[l]]
                    
                # Move left pointer to the right
                l += 1
            
            """ Update maximum length of substring with
            at most k distinct characters found so far"""
            if len(mpp) <= k:
                maxLen = max(maxLen, r - l + 1)
            
            # Move right pointer
            r += 1
        
        # Return the maximum length found
        return maxLen

if __name__ == "__main__":
    s = "aaabbccd"
    
    #Create an instance of Solution class
    sol = Solution()
    
    res = sol.kDistinctChar(s, 2)
    
    # Output the result
    print(f"The maximum length of substring with at most 2 distinct characters is: {res}")

Complexity Analysis: 
Time Complexity:O(2N), where N is the size of the array. As the other while loop runs for N time and the inner while loop runs for N time in total throghto the program. Ignore the contribution of map data structure in the time complexity as size of the map is extremely small.

Space Complexity: O(k) , as at most the map data structure is holding k elements.


#Optimal
Intuition: 
The idea here is to use the sliding window approach by avoiding the additional O(N) time complexity incurred when shifting the window entirely in the Better solution, to ensure that no more than k distinct characters occurs in the current substring. Instead of moving the left pointer (l) completely till the distinct character comes under given limit, shift the window by one position at a time. This way the extra while loop used in Optimal I approach can be eliminated.

Approach: 
First, initialize few variables: l and r pointers to 0 to represent the left and right boundaries of the current window, maxLen is initialized to 0 to keep track of the maximum length of substring with at most k distinct characters and mpp (unordered_map) is used to track the count of each character in the current sliding window.
Iterate through the string using the r pointer to expand the window, increment the count of element at r pointer in the map. If the number of different characters exceeds k, shrink the window from the left (l++). Decrement the count of element at left pointer in the map.
If the count of element at left pointer becomes 0, remove it from the map. Increment l pointer to move the left boundary of the window to the right until size of map again becomes less than or equals to k.
Whenever size of map is less than or equal to k, calculate the length of the current valid substring. Update maxLen to store the maximum length found so far.
Continue expanding r pointer until it reaches the end of the string. After iterating through the entire string return maxLen.

class Solution:
    """ Function to find the maximum length of 
    substring with at most k distinct characters """
    def kDistinctChar(self, s, k):
        
        # Length of the input string
        n = len(s)
        
        # Variable to store the 
        # maximum length of substring
        maxLen = 0
        
        # Map to track the count of each
        # character in the current window
        mpp = {}
        
        # Pointers for the sliding window approach
        l, r = 0, 0
        
        while r < n:
            charR = s[r]
            mpp[charR] = mpp.get(charR, 0) + 1
            
            # If number of different characters exceeds
            # k, shrink the window from the left
            if len(mpp) > k:
                charL = s[l]
                mpp[charL] -= 1
                if mpp[charL] == 0:
                    del mpp[charL]
                l += 1
            
            # If number of different characters 
            # is at most k, update maxLen
            if len(mpp) <= k:
                maxLen = max(maxLen, r - l + 1)
            
            r += 1
        
        # Return the maximum length
        return maxLen

if __name__ == "__main__":
    s = "aaabbccd"  
    k = 2
    
    # Create an instance of Solution class
    sol = Solution()
    
    length = sol.kDistinctChar(s, k)
    
    # Print the result
    print(f"Maximum length of substring with at most {k} distinct characters: {length}")

Complexity Analysis: 
Time Complexity:O(N), where N is the size of the array. As the other while loop runs for N times only. Ignore the contribution of map data structure in the time complexity as size of the map is extremely small.

Space Complexity: O(k) , as at most the map data structure is holding k elements.

'''
class Solution:
    def kDistinctChar(self, s, k):
        n = len(s)
        maxLen = 0
        mpp = {}
        l, r = 0, 0
        
        while r < n:
            charR = s[r]
            mpp[charR] = mpp.get(charR, 0) + 1
            if len(mpp) > k:
                charL = s[l]
                mpp[charL] -= 1
                if mpp[charL] == 0:
                    del mpp[charL]
                l += 1
            if len(mpp) <= k:
                maxLen = max(maxLen, r - l + 1)
            
            r += 1
        return maxLen
        