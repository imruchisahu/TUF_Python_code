'''
Given an integer k and a string s, any character in the string can be selected and changed to any other uppercase English character. This operation can be performed up to k times. After completing these steps, return the length of the longest substring that contains the same letter.


Examples:
Input : s = "BAABAABBBAAA" , k = 2

Output : 6

Explanation : we can change the B present at index 0 , 3 (0 base indexing) to A.

The new string is "AAAAAABBBAAA".

The substring "AAAAAA" is the longest substring having same letter with length 6.

Input : s = "AABABBA" , k = 1

Output : 4

Explanation : The underlined characters are changed in the new string obtained.

The new string is "AABBBBA". The substring "BBBB" is the answer.

There are other ways to achieve this answer.

Input : s = "ABCDEF" k = 1

Output:
2
Constraints:
1 <= s.length <= 105
0 <= k <= s.length
s contains only English uppercase letters.


#Brute
Intuition:
The thought process is very straightforward, first find out each and every substring and while doing so, keep a track of characters and their frequencies. Further, calculate the number of characters that needs to be changed, if it is greater than the given limit then no need to consider that substring, else calculate the maximum length of the substring encountred so far.

Approach:
First, initialize few variables: maxLen as 0 to track the maximum length found and maxFreq as 0 to track the highest frequency of any single character in the current window.
Iterate through the array, which will basically be the starting point of the substring. For each starting index, initialize a frequency array hash to count occurrences of characters.
Update max frequency encountered and store it in maxFreq variable. Calculate the number of changes needed to make.
If changes is less than or equal to k, update maxLen with the size of the current valid window. If changes exceeds k, break out of the inner loop since further expanding the window won't help in achieving a valid substring. Finally return the maxLen as a answer.

class Solution:
    """
    Function to find the longest substring
    with at most k characters replaced.
    """
    def characterReplacement(self, s: str, k: int) -> int:
        
        """ Variable to store the maximum
        length of substring found"""
        maxLen = 0
        
        """ Variable to track the maximum frequency of
        any single character in the current window"""
        maxFreq = 0

        # Iterate through each starting point of the substring
        for i in range(len(s)):
            
            # Initialize hash array for character frequencies
            hash = [0] * 26

            for j in range(i, len(s)):
                
                """ Update frequency of current
                character in the hash array"""
                hash[ord(s[j]) - ord('A')] += 1

                # Update max frequency encountered
                maxFreq = max(maxFreq, hash[ord(s[j]) - ord('A')])

                # Calculate the number of changes needed to make
                changes = (j - i + 1) - maxFreq

                """ If the number of changes is less than or 
                equal to k, the current window is valid"""
                if changes <= k:
                    maxLen = max(maxLen, j - i + 1)
                else:
                    break

        """ Return the maximum length of substring
        with at most k characters replaced"""
        return maxLen

if __name__ == "__main__":
    s = "AABABBA"
    k = 2
    
    # Create an instance of Solution class
    sol = Solution()
    
    length = sol.characterReplacement(s, k)
    
    # Print the result
    print(f"Maximum length of substring with at most {k} characters replaced: {length}")

Complexity Analysis: 
Time Complexity:O(N2), where N is the size of the array. Iterating the array twice using two for loops.

Space Complexity: O(26) . Hash array to store the frequencies of the capital letters.

#Better
Intuition:
The idea here is to use the sliding window technique to solve this problem optimally. This method efficiently finds the longest substring with frequency counting and dynamic adjustments to ensure validity of the window. First expand the window and add those substring that validates the cndition and when it crosses the limit, again shrink the window by moving the left pointer. This process ensures to provide a linear time complexity.

Approach:
First initialize few variables: l (left) and r (right) as 0 to define the current window in the string, maxLen as 0 to track the maximum length of valid substrings, maxFreq as 0 to monitor the highest frequency of any single character within the current window. Also, maintain a frequency array hash to count occurrences of characters.
Incrementally expand the window by moving the r pointer to the right. Update the frequency of the current character in hash and adjust maxFreq if this frequency exceeds the current maxFreq.
Check if the number of characters that need replacement exceeds k. If so, slide the l pointer to the right until the window becomes valid again. Adjust the frequencies in hash and update maxFreq accordingly.
After ensuring the window is valid, update maxLen with the length of the current window. Finally, return maxLen, which holds the length of the longest substring.

class Solution:
    """
    Function to find the longest substring 
    with at most k characters replaced
    """
    def characterReplacement(self, s: str, k: int) -> int:
        
        """ Variable to store the maximum
        length of substring found"""
        maxLen = 0
        
        """ Variable to track the maximum frequency
        of any single character in the current window"""
        maxFreq = 0
        
        # Pointers to maintain the current window [l, r]
        l = 0
        r = 0
        
        # Hash array to count frequencies of characters
        hash = [0] * 26

        # Iterate through each starting point of substring
        while r < len(s):
            
            """ Update frequency of current
            character in the hash array"""
            hash[ord(s[r]) - ord('A')] += 1
            
            # Update max frequency encountered
            maxFreq = max(maxFreq, hash[ord(s[r]) - ord('A')])
            
            # Check if current window is invalid
            while (r - l + 1) - maxFreq > k:
                
                """ Slide the left pointer to
                make the window valid again"""
                hash[ord(s[l]) - ord('A')] -= 1
                
                # Recalculate maxFreq for current window
                maxFreq = 0
                for i in range(26):
                    maxFreq = max(maxFreq, hash[i])
                
                # Move left pointer forward
                l += 1
            
            """ Update maxLen with the length
            of the current valid substring"""
            maxLen = max(maxLen, r - l + 1)
            
            # Move right pointer forward to expand window
            r += 1

        """ Return the maximum length of substring
        with at most k characters replaced"""
        return maxLen

if __name__ == "__main__":
    s = "AABABBA"
    k = 2

    # Create an instance of Solution class
    sol = Solution()

    length = sol.characterReplacement(s, k)

    # Print the result
    print(f"Maximum length of substring with at most {k} characters replaced: {length}")

Complexity Analysis: 
Time Complexity:O((N+N) * 26), where N is the size of the array. The right pointer runs for N times and the left pointer runs for N times throughout. The for loop takes extra O(26) to claculate the maximum frequency.

Space Complexity: O(26) . Hash array to store all the characters.


#Optimal
Intuition:
The idea here is to use the sliding window approach by avoiding the additional O(N) time complexity incurred when shifting the window entirely in the Better solution, to ensure that no more than k characters gets replaced in the current substring. Instead of moving the left pointer (l) completely till the distinct character comes under given limit, shift the window by one position at a time. This way the extra while loop used in Optimal I approach can be eliminated.

Approach:
First, initialize few variables: l(left) and r (right) as 0 to define the current window in the string, maxLen as 0 to track the maximum length of valid substrings. Also, maintain a frequency array hash to count occurrences of characters.
Incrementally expand the window by moving the r pointer to the right. Update the frequency count of current character. Track the maximum frequency encountered (maxFreq) within the current window.
If the length of the current window minus maxFreq exceeds k, the window becomes invalid. Slide the l pointer to the right to shrink the window by one position by decrementing the frequency count of character at the left pointer.
After ensuring the window is valid, update maxLen with the length of the current window. Continue this process until the r pointer reaches the end of the string and finally, return maxLen as an answer.

class Solution:
    """
    Function to find the longest substring 
    with at most k characters replaced
    """
    def characterReplacement(self, s: str, k: int) -> int:
        
        """ Variable to store the maximum
        length of substring found"""
        maxLen = 0
        
        """ Variable to track the maximum frequency
        of any single character in the current window"""
        maxFreq = 0
        
        # Pointers to maintain the current window [l, r]
        l = 0
        r = 0
        
        # Hash array to count frequencies of characters
        hash = [0] * 26

        # Iterate through each starting point of substring
        while r < len(s):
            
            """ Update frequency of current
            character in the hash array"""
            hash[ord(s[r]) - ord('A')] += 1
            
            # Update max frequency encountered
            maxFreq = max(maxFreq, hash[ord(s[r]) - ord('A')])
            
            # Check if current window is invalid
            if (r - l + 1) - maxFreq > k:
                
                """ Slide the left pointer to
                make the window valid again"""
                hash[ord(s[l]) - ord('A')] -= 1
                
                # Move left pointer forward
                l += 1
            
            """ Update maxLen with the length
            of the current valid substring"""
            maxLen = max(maxLen, r - l + 1)
            
            # Move right pointer forward to expand window
            r += 1

        """ Return the maximum length of substring
        with at most k characters replaced"""
        return maxLen

if __name__ == "__main__":
    s = "AABABBA"
    k = 2

    # Create an instance of Solution class
    sol = Solution()

    length = sol.characterReplacement(s, k)

    # Print the result
    print(f"Maximum length of substring with at most {k} characters replaced: {length}")

Complexity Analysis: 
Time Complexity:O(N), where N is the size of the array. The right pointer runs for N times.

Space Complexity: O(26) . Hash array to store all the characters.

'''
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLen = 0
        maxFreq = 0
        l = 0
        r = 0
        hash = [0] * 26
        while r < len(s):
            hash[ord(s[r]) - ord('A')] += 1
            maxFreq = max(maxFreq, hash[ord(s[r]) - ord('A')])
            if (r - l + 1) - maxFreq > k:
                hash[ord(s[l]) - ord('A')] -= 1
                l += 1
            maxLen = max(maxLen, r - l + 1)
            r += 1
        return maxLen