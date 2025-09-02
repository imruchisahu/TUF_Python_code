'''
Given a string, S. Find the length of the longest substring without repeating characters.


Examples:
Input : S = "abcddabac"

Output : 4

Explanation : The answer is "abcd" , with a length of 4.

Input : S = "aaabbbccc"

Output : 2

Explanation : The answers are "ab" , "bc". Both have maximum length 2.

Input : S = "aaaa"

Output:
1
Constraints:
1 <= S.length <= 5*104
S contains only English lowercase letters.

#BRute
# Intuition:
The idea here is very straightforward, first generate all the possible substrings of given array using two for loops. While finding the substrings check if the current character has occured previously with the help of a hash array. If so, no need to take this substring into consideration as characters are repeating, otherwise, calculate the length of current substring, update maximum length and finally mark the character as visited.

Approach:
Iterate through the array using a for loop from 0th index to sizeofArray - 1, to take all possible starting points of the substring into consideration.
Check if the current character is already in the hash array, if so, break out of the loop. Otherwise, as it is not visited yet, mark the character as 1 in the hash array, signifying that the current character is now visited.
Now, calculate the length of current substring and update the maximum length of the substrings found so far. Finally, return the maximum length.

class Solution:
    def longestNonRepeatingSubstring(self, s):
        # Length of the input string
        n = len(s)
        
        # Variable to store max length
        maxLen = 0
        
        """ Iterate through all possible 
            starting points of the substring """
        for i in range(n):
            
            """ Hash to track characters in 
                the current substring window """
            # Assuming extended ASCII characters
            hash_set = [0] * 256
            
            for j in range(i, n):
                
                """ If s[j] is already in the
                    current substring window """
                if hash_set[ord(s[j])] == 1:
                    break
                
                """ Update the hash_set to mark s[j]
                    as present in the current window """
                hash_set[ord(s[j])] = 1
                
                """ Calculate the length of
                    the current substring """
                current_len = j - i + 1
                
                """ Update maxLen if the current
                    substring length is greater """
                maxLen = max(maxLen, current_len)
        
        # Return the maximum length
        return maxLen

if __name__ == "__main__":
    
    input_str = "cadbzabcd"
    
    # Create an instance of Solution class
    sol = Solution()
    
    length = sol.longestNonRepeatingSubstring(input_str)
    
    # Print the result
    print("Length of longest substring without repeating characters:", length)

Complexity Analysis: 
Time Complexity:O(N2), where N is the size of the array. Iterating the array twice using two for loops.

Space Complexity: O(256) . Hash array to store all the characters.

#Optimal
Intuition:
The idea is to use two-pointers approach to solve this problem. The two-pointer technique involves employing two indices, l (left) and r (right), which basically indicates a window starting from l and ending at r. Use a HashSet called set to keep track of characters within the current window (l to r). This allows for efficient checks and ensures no duplicates are present. While checking every window, keep track of the maximum length of subarray encountered so far.

Approach:
Initialize few variables as: l and r pointers to 0. These pointers will define the current window [l, r] that contains characters without repetition, maxLen to 0 to store the maximum length of substring found without repeating character.
Use an array hash of size 256 (assuming ASCII characters) to store the last occurrence index of each character in the string. Initialize all elements of hash to -1, indicating that no characters have been encountered yet.
Now, while r pointer is less than sizeOfArray - 1, iterate in the array. While iterating, check if current character has occured before using hash array. If so, updadate the left pointer to index of current character plus 1. This ensures that l moves past the last occurrence of of repeated character, effectively removing the repeated character from the window.
Calculate the length of the current substring as len = r - l + 1. Update maximum length of the substring found so far.
Update hash array with the current index r, indicating the most recent occurrence of character at pointer r in the string. Finally, return maximum length of the substring.

class Solution:
    """ Function to find the longest substring
        without repeating characters """
    def longestNonRepeatingSubstring(self, s):
        n = len(s)
        
        # Assuming all ASCII characters
        HashLen = 256
        
        """ Hash table to store last
            occurrence of each character """
        hash = [-1] * HashLen
        
        """ Initialize hash table with
            -1 (indicating no occurrence) """
        for i in range(HashLen):
            hash[i] = -1

        l, r, maxLen = 0, 0, 0
        while r < n:
            """ If current character s[r] 
                is already in the substring """
            if hash[ord(s[r])] != -1:
                """ Move left pointer to the right
                    of the last occurrence of s[r] """
                l = max(hash[ord(s[r])] + 1, l)
            
            # Calculate the current substring length
            current_len = r - l + 1
            
            # Update maximum length found so far
            maxLen = max(current_len, maxLen)
            
            """ Store the index of the current
                character in the hash table """
            hash[ord(s[r])] = r
            
            # Move right pointer to next position
            r += 1
        
        # Return the maximum length found
        return maxLen

if __name__ == "__main__":
    s = "cadbzabcd"
    
    # Create an instance of the Solution class
    sol = Solution()

    result = sol.longestNonRepeatingSubstring(s)

    # Output the maximum length
    print("The maximum length is:")
    print(result)

Complexity Analysis: 
Time Complexity:O(N), where N is the size of the array. As the array runs for N times.

Space Complexity: O(256) . Hash array to store all the characters.

'''
class Solution:
    def longestNonRepeatingSubstring(self, s):
        n = len(s)
        HashLen = 256
        hash = [-1] * HashLen
        for i in range(HashLen):
            hash[i] = -1

        l, r, maxLen = 0, 0, 0
        while r < n:
            if hash[ord(s[r])] != -1:
                l = max(hash[ord(s[r])] + 1, l)
            current_len = r - l + 1
            maxLen = max(current_len, maxLen)
            hash[ord(s[r])] = r
            r += 1
        return maxLen