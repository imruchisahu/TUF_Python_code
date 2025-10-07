'''
Given a string s, determine the number of distinct substrings (including the empty substring) of the given string.



A string B is a substring of a string A if B can be obtained by deleting several characters (possibly none) from the start of A and several characters (possibly none) from the end of A.



Two strings X and Y are considered different if there is at least one index i such that the character of X at index i is different from the character of Y at index i (X[i] != Y[i]).


Examples:
Input : s = "aba"

Output : 6

Explanation :

The distinct substrings are "a", "ab", "ba", "b", "aba", "".

Input : s = "abc"

Output : 7

Explanation :

The distinct substrings are "a", "ab", "abc", "b", "bc", "c", "".

Input : s = "aaabc"

Output:
10
12
13
15

Submit
Constraints:
1 <= s.length <= 103
s consist of only lowercase English letters.

#BRute Force Approach
Intuition
We can find all distinct substrings of a string by starting at each character and extending to the end, creating every possible substring. Storing these substrings in a set filters out duplicates, ensuring unique substrings are counted.
Approach
Initialize an empty set to store distinct substrings.
Use an outer loop to iterate through each character of the string. This character will serve as the starting point for substrings.
Construct Substrings:
For each starting character, use a nested loop to construct all possible substrings beginning from that character.
The outer loop sets the starting point, while the inner loop iterates over subsequent characters to form the substring.
Add each constructed substring to the set. Since sets only store unique values, duplicates will be automatically filtered out.
After iterating through the string and constructing substrings from each starting character, return the size of the set. This will give the number of distinct substrings of the given string.

class Solution:
    def countDistinctSubstring(self, s: str) -> int:
        substrings = set()
        
        # Iterate through each character of the string
        for i in range(len(s)):
            substring = ""
            #Construct all possible substrings starting from the current character 
            for j in range(i, len(s)):
                substring += s[j]
                substrings.add(substring)
        
        # Include empty substring
        substrings.add("")
        
        # Return number of distinct substrings
        return len(substrings)

# Test the solution
solution = Solution()
input_str = "abc"
print("Number of distinct substrings:", solution.countDistinctSubstring(input_str))

Complexity Analysis
Time Complexity: O(N2 X log M) where N is the size of the string and M is the number of elements in the set. Constructing all possible substrings involves O(N2) operations. Each substring insertion into the set takes O(log M) time due to the balanced tree structure of the set, ensuring uniqueness.

Space Complexity: O(N3), where N is the length of the string. This complexity arises because there can be up to O(N2) distinct substrings, and each substring can be up to N characters long. Storing all these substrings requires O(N2) substrings times O(N) length, resulting in O(N3) space.


#Optiaml Approach
Intuition
Instead of using nested loops in the previous approach, use a Trie data structure which will minimize the number of comparisons required while traversing the substrings. The idea is to store only essential information and reduce redundancy by sharing common prefixes among substrings. This approach is particularly advantageous for long strings with many repeated substrings, as it optimizes space utilization.
Approach
Start by initializing a root node for the Trie.
Iterate through the input string. For each character:
Traverse the Trie, creating new nodes as necessary to represent the substrings formed by the characters seen so far.
Initialize a counter to keep track of the number of distinct substrings.
Iterate through all possible starting positions of the substring.
Begin from the root node for each substring.
For each character in the substring starting from the current position:
Check if the current node has a child node for that character.
If not, insert a new child node and increment the counter, indicating a new substring is found.
Move to the child node corresponding to the current character.
Repeat this process for all substrings starting from the current position.
Finally, return the total count of distinct substrings, adding one to account for the empty string.

class Node:
    def __init__(self):
        self.links = [None] * 26

    def containsKey(self, ch):
        return self.links[ord(ch) - ord('a')] is not None

    def put(self, ch, node):
        self.links[ord(ch) - ord('a')] = node

    def get(self, ch):
        return self.links[ord(ch) - ord('a')]


class Solution:
    # Count number of distinct substrings in string
    def countDistinctSubstring(self, s):
        c = 0
        # Root node of the trie
        root = Node()

        # Iterate all starting positions of substrings
        for i in range(len(s)):
            node = root

            # Iterate through characters
            for j in range(i, len(s)):
                #If the current character is not a child of the current node, insert it as a new child node
                if not node.containsKey(s[j]):
                    c += 1
                    # Insert new child node for character s[j]
                    node.put(s[j], Node())
                # Move to the child node
                node = node.get(s[j])

        # Clean up the allocated memory
        self.deleteTrie(root)
        #Return the total count of distinct substrings including the empty string
        return c + 1

    # Freeing up memory
    def deleteTrie(self, node):
        for i in range(26):
            if node.links[i] is not None:
                self.deleteTrie(node.links[i])


# Main function
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    s1 = "aabbaba"
    print("Input:", s1)
    print("Number of distinct substrings:", solution.countDistinctSubstring(s1))

    # Test case 2
    s2 = "abcdefg"
    print("Input:", s2)
    print("Number of distinct substrings:", solution.countDistinctSubstring(s2))

Complexity Analysis
Time Complexity: O(N^2) where N is the size of the string.This complexity arises because, for each starting position in the string, we iterate through the remaining characters to form substrings. The nested loops result in a quadratic number of operations.

Space Complexity: O(N^2) where N is the size of the string. The space complexity is due to storing all distinct substrings in the trie. In the worst case, the number of distinct substrings can be quadratic relative to the size of the string, leading to O(N^2) space usage.

'''
class Node:
    def __init__(self):
        self.links = [None] * 26

    def containsKey(self, ch):
        return self.links[ord(ch) - ord('a')] is not None

    def put(self, ch, node):
        self.links[ord(ch) - ord('a')] = node

    def get(self, ch):
        return self.links[ord(ch) - ord('a')]
class Solution:
    def countDistinctSubstring(self, s):
        c = 0
        root = Node()
        for i in range(len(s)):
            node = root
            for j in range(i, len(s)):
                if not node.containsKey(s[j]):
                    c += 1
                    node.put(s[j], Node())
                node = node.get(s[j])

        # Clean up the allocated memory
        self.deleteTrie(root)
        return c + 1

    # Freeing up memory
    def deleteTrie(self, node):
        for i in range(26):
            if node.links[i] is not None:
                self.deleteTrie(node.links[i])
