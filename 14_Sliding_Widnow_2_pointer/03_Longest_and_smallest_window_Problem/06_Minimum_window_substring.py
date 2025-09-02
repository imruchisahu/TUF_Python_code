'''
Given two strings s and t. Find the smallest window substring of s that includes all characters in t (including duplicates) , in the window. Return the empty string "" if no such substring exists.


Examples:
Input : s = "ADOBECODEBANC" , t = "ABC"

Output : "BANC"

Explanation : The minimum window substring of string s that contains the string t is "BANC".

Input : s = "a" , t = "a"

Output : "a"

Explanation : The complete string is the minimum window

Input : s = "aAbBDdcC" , t = "Bc"

Output:
"BDdc"
Constraints:
1 <= n , m <= 105
n = s.length
m = t.length
string s and t consist of uppercase and lowercase letters.

Similar Problems


#Brute
#Intuition:
The idea here is to use two for loops to find out all the substrings and while finding out, keep a track of the charaters present in the current substring using a hash array. If the current substring has all the charaters required then store its starting index and return the substring.

Approach:
First, initialize few variables: minLen to Integer.MAX_VALUE to store the minimum length of the substring found and sIndex to -1 to store the starting index of this substring. Use an array hash of size 256 (assuming ASCII characters) to count frequencies of characters in the reference string.
Traverse through each character in string, it will indicate the starting point of the substring, for each starting index, initialize count to 0 to track how many characters from t are found in the current substring.
Now, again iterate through the array using a for loop form the starting point of the substring till the end of array. Update the frequency count in hash for the character current character.
If this character is required, increment count. When count equals the length of the another string given this means all characters from the later string are found in the current substring.
Update minLen and sIndex if the length of this window (j - i + 1) is smaller than the current minimum length found. After iterating through all possible starting indices, return the substring starting at sIndex with length minLen. If sIndex remains -1, return an empty string indicating no valid substring was found.

class Solution:
    """
    Function to find the minimum length substring
    in string s that contains all characters from string t.
    """
    def minWindow(self, s: str, t: str) -> str:

        """ Variable to store the minimum
        length of substring found"""
        minLen = float('inf')
        
        """ Variable to store the starting index
        of the minimum length substring"""
        sIndex = -1
        
        # Iterate through string s
        for i in range(len(s)):
            """Reset list for counting current window. List to
            count frequencies of characters in string t"""
            hash = [0] * 256
            for c in t:
                hash[ord(c)] += 1
            
            count = 0;
            
            # Iterate through current window 
            for j in range(i, len(s)):
                if hash[ord(s[j])] > 0:
                    count += 1
                hash[ord(s[j])] -= 1
                
                """ If all characters from t 
                are found in current window"""
                if count == len(t):
                    
                    """ Update minLen and sIndex
                    if current window is smaller"""
                    if j - i + 1 < minLen:
                        minLen = j - i + 1
                        sIndex = i
                        
                    break  
        
        # Return the minimum length substring from s
        return s[sIndex:sIndex + minLen] if sIndex != -1 else ""

if __name__ == "__main__":
    s = "ddaaabbca"
    t = "abc"

    # Create an instance of Solution class
    sol = Solution()

    ans = sol.minWindow(s, t)

    # Print the result
    print(f"Minimum length substring containing all characters from \"{t}\" is: {ans}")

Complexity Analysis: 
Time Complexity:O(N2), where N is the size of the string. The outer loop runs for N time and for each character the inner loop also runs for N times.

Space Complexity: O(256) . Hash array to store frequency of all the characters.

#Optimal
Intuition:
The idea here is to use sliding window approach, which ensures to find the required result in linear time. So, basically first store the frequencies of characters of the reference string into hash array and every time while encountering the characters of the string, decrease its frequency. After doing so if the frequecy of any character is greater than 0 it means it is prefilled and the current character is needed. If the count is equal to length of reference string then update the minumum length of the substring and store its starting index.

Approach:
First, initialize few variables: minLen to Integer.MAX_VALUE to store the minimum length of the substring found and sIndex to -1 to store the starting index of this substring. Use an array hash of size 256 (assuming ASCII characters) to count frequencies of characters in the reference string, l (left) and r (right), both initially set to 0, to define the current window in the string.
Fill the hash array with frequencies of characters from string t using a loop iterating through each character in the reference string provided.
Expand the window by incrementing r and include the character at r pointer in the current window. Adjust the frequency count in hash for current character. If the character is required, increment count.
While count equals the length of reference string, attempt to shrink the window from the left (l) by incrementing l. Adjust the frequency count in hash for character at left pointer. If removing the character at left pointer reduces the count of required characters, decrement count.
Continue expanding and shrinking the window until r reaches the end of string. Return the substring sIndex with length minLen. If sIndex remains -1, return an empty string indicating no valid substring was found.

class Solution:
    """ Function to find the minimum length 
    substring in string s that contains
    all characters from string t. """
    def minWindow(self, s: str, t: str) -> str:
        
        """ Variable to store the minimum 
        length of substring found """
        minLen = float('inf')
        
        """ Variable to store the starting index
        of the minimum length substring """
        sIndex = -1
        
        """ Array to count frequencies
        of characters in string t"""
        hash = [0] * 256
        
        # Count the frequencies of characters in t
        for c in t:
            hash[ord(c)] += 1
            
        count = 0
        l, r = 0, 0
        
        # Iterate through current window 
        while r < len(s):
            # Include the current character in the window
            if hash[ord(s[r])] > 0:
                count += 1
            hash[ord(s[r])] -= 1
                
            """ If all characters from t 
            are found in current window """
            while count == len(t):
                    
                """ Update minLen and sIndex
                if current window is smaller """
                if r - l + 1 < minLen:
                    minLen = r - l + 1
                    sIndex = l
                
                # Remove leftmost character from window
                hash[ord(s[l])] += 1
                if hash[ord(s[l])] > 0:
                    count -= 1
                l += 1
            r += 1
        
        # Return minimum length substring from s
        return s[sIndex:sIndex + minLen] if sIndex != -1 else ""

if __name__ == "__main__":
    s = "ddaaabbca"
    t = "abc"

    # Create an instance of Solution class
    sol = Solution()

    ans = sol.minWindow(s, t)

    # Print the result
    print(f"Minimum length substring containing all characters from \"{t}\" is: {ans}")

Complexity Analysis: 
Time Complexity:O(2N + M ), where N is the size of the string s and M is the size of the string t.

Space Complexity: O(256) . Hash array to store frequency of all the characters.
'''
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        minLen = float('inf')
        sIndex = -1
        hash = [0] * 256
        for c in t:
            hash[ord(c)] += 1
            
        count = 0
        l, r = 0, 0
        while r < len(s):
            if hash[ord(s[r])] > 0:
                count += 1
            hash[ord(s[r])] -= 1
            while count == len(t):
                if r - l + 1 < minLen:
                    minLen = r - l + 1
                    sIndex = l
                hash[ord(s[l])] += 1
                if hash[ord(s[l])] > 0:
                    count -= 1
                l += 1
            r += 1
        return s[sIndex:sIndex + minLen] if sIndex != -1 else ""
