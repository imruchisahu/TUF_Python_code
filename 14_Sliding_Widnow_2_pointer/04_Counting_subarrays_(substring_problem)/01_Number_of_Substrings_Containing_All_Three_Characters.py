'''
Given a string s , consisting only of characters 'a' , 'b' , 'c'.Find the number of substrings that contain at least one occurrence of all these characters 'a' , 'b' , 'c'.


Examples:
Input : s = "abcba"

Output : 5

Explanation : The substrings containing at least one occurrence of the characters 'a' , 'b' , 'c' are "abc" , "abcb" , "abcba" , "bcba" , "cba".

Input : s = "ccabcc"

Output : 8

Explanation : The substrings containing at least one occurrence of the characters 'a' , 'b' , 'c' are "ccab" , "ccabc" , "ccabcc" , "cab" , "cabc" , "cabcc" , "abc" , "abcc".

Input : s = "abccba"

Output:
7
Constraints:
1 <= s.length <= 5*104
s consist only of characters 'a' , 'b' , 'c'.

#Brute
Intuition:
Here, the idea is to find all possible substrings of the given string and while doing so, mark the presence of each character in the hash array. If 'a', 'b', 'c' are present in the current subarray increment the count and finally return it.

Approach:
Initialize count to 0 to keep track of the number of valid substrings found.
Iterate through the array using a loop, to reach every staring point of the substring. Use an array hash of size 3 to track the presence of characters 'a', 'b', 'c'. Initialize it to {0} at the beginning of each iteration of the outer for loop.
Now, initialize another for loop from starting point of the substring till the end of the array. Mark the presence of the current character in the hash array.
After marking the current character in hash, check if all characters 'a', 'b', 'c' are present by summing up hash[0] + hash[1] + hash[2]. If the sum equals 3, increment the count as it indicates that the substring from index i to j contains all required characters. After completing the loops, finally return the count variable.

class Solution:
    """ Function to find the number of substrings 
    containing all characters 'a', 'b', 'c' in string s. """
    def numberOfSubstrings(self, s: str) -> int:
        count = 0
        
        # Iterate through each starting point of substring
        for i in range(len(s)):
            
            # Array to track presence of 'a', 'b', 'c'
            hash = [0, 0, 0]
            
            # Iterate through each ending point of substring
            for j in range(i, len(s)):
                
                # Mark current character in hash
                hash[ord(s[j]) - ord('a')] = 1
                
                # Check if all characters 'a', 'b', 'c' are present
                if sum(hash) == 3:
                    
                    # Increment count for valid substring
                    count += 1
        
        # Return the total count of substrings
        return count

if __name__ == "__main__":
    s = "bbacba"
    
    # Create an instance of Solution class
    sol = Solution()
    
    ans = sol.numberOfSubstrings(s)
    
    # Print the result
    print(f"Number of substrings containing 'a', 'b', 'c' in \"{s}\" is: {ans}")


Complexity Analysis: 
Time Complexity:O(N2), where N is the size of the string. The outer loop runs for N time and for each character the inner loop also runs for N times.

Space Complexity: O(1) . As no significant amount of extra space is used.

#optimal
Intuition:
The idea here is to use a for loop to iterate through the array, as moving forward in the array update the last seen of 'a', 'b', 'c' in the hash array. Now, check if the current substring has atleast one of each 'a', 'b', 'c', if so, then the previous substrings must be having these characters too, so add all such substrings in the count varaible and return it.

Approach:
First, initialize few variables: An arraylastSeen of size 3 ({-1, -1, -1}) to store the last seen index of characters 'a', 'b', 'c' respectively, count to 0 to keep track of the number of valid substrings found.
Use a loop to iterate through each character in the string. Update the lastSeen array for the current character. After updating lastSeen, check if all characters 'a', 'b', 'c' have been seen at least once.
Add the calculated count to count. After iterating through all characters in string, return count.

class Solution:
    """ Function to find the number of substrings 
    containing all characters 'a', 'b', 'c' in string s. """
    def numberOfSubstrings(self, s: str) -> int:
        
        """Array to store the last seen 
        index of characters 'a', 'b', 'c'"""
        last_seen = [-1, -1, -1]
        
        count = 0
        
        # Iterate through each character in string s
        for i in range(len(s)):
            
            """ Update last_seen index
            for current character"""
            last_seen[ord(s[i]) - ord('a')] = i
            
            """ Check if all characters 'a',
            'b', 'c' have been seen"""
            if last_seen[0] != -1 and last_seen[1] != -1 and last_seen[2] != -1:
                
                """ Count valid substrings 
                ending at current index"""
                count += 1 + min(last_seen[0], last_seen[1], last_seen[2])
        
        # Return the total count of substrings
        return count

# Test the solution
if __name__ == "__main__":
    s = "bbacba"
    
    # Create an instance of Solution class
    sol = Solution()
    
    ans = sol.numberOfSubstrings(s)
    
    # Print the result
    print(f"Number of substrings containing 'a', 'b', 'c' in \"{s}\" is: {ans}")

Complexity Analysis: 
Time Complexity:O(N), where N is the size of the string. The outer loop runs for N time.

Space Complexity: O(1) . As no significant amount of extra space is used.

'''
class Solution:    
    def numberOfSubstrings(self, s: str) -> int:
        last_seen = [-1, -1, -1]
        count = 0
        for i in range(len(s)):
            last_seen[ord(s[i]) - ord('a')] = i
            if last_seen[0] != -1 and last_seen[1] != -1 and last_seen[2] != -1:
                count += 1 + min(last_seen[0], last_seen[1], last_seen[2])
        return count