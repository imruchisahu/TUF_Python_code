'''
Given a string array nums of length n. A string is called a complete string if every prefix of this string is also present in the array nums.



Find the longest complete string in the array nums.



If there are multiple strings with the same length, return the lexicographically smallest one and if no string exists, return "None" (without quotes).


Examples:
Input : nums = [ "n", "ni", "nin", "ninj" , "ninja" , "nil" ]

Output : ninja

Explanation :

The word "ninja" is the longest word which has all its prefixes present in the array.

Input : nums = [ "ninja" , "night" , "nil" ]

Output : None

Explanation :

There is no string that has all its prefix present in array. So we return None.

Input : nums = [ "cat" , "car" , "cow", "c", "ca", "t", "r", "w" ]

Output:
cat
car
cow
c

Submit
Constraints:
1 <= n <= 105
1 <= nums[i].length <= 105
1 <= sum(nums[i].length) <= 105
nums[i] consist only of lowercase English characters

Intuition
By building a Trie from the array of words, checking prefixes becomes much easier. In a Trie, each node stands for a character, and the paths from the root to the nodes represent the prefixes found in the array. This setup quickly checks if a prefix exists by following the path in the Trie, making the process much faster and more efficient.
Approach
Iterate through each word in the input list and insert it into the Trie.
Initialize an empty string to represent the longest complete string found so far.
Iterate through each word in the input list again and check if all its prefixes are present in the Trie.
If all prefixes are present: Compare the current word's length and lexicographical order with the current longest complete string.
Update the longest complete string if the current word is longer or comes earlier alphabetically.
If no complete string is found, return an empty string. Otherwise, return the longest complete string found.


Finding the complete string
class Node:
    def __init__(self):
        # To store references to child nodes
        self.links = [None] * 26
        # Flag to indicate end of a word
        self.flag = False

    # Checks if the current character link exists
    def containsKey(self, ch):
        return self.links[ord(ch) - ord('a')] is not None

    # Returns the next node corresponding to the character
    def get(self, ch):
        return self.links[ord(ch) - ord('a')]

    # Creates a link to the next node for the current character
    def put(self, ch, node):
        self.links[ord(ch) - ord('a')] = node

    # Marks the end of a word
    def setEnd(self):
        self.flag = True

    # Checks if the current node is the end of a word
    def isEnd(self):
        return self.flag


class Trie:
    def __init__(self):
        # Root node of the Trie
        self.root = Node()

    # Inserts a word into the Trie
    def insert(self, word):
        node = self.root
        for char in word:
            if not node.containsKey(char):
                node.put(char, Node())
            node = node.get(char)
        # Marks the end of the inserted word
        node.setEnd()

    # Checks if all prefixes of the given word exist in the Trie
    def checkIfAllPrefixExists(self, word):
        node = self.root
        for char in word:
            if node.containsKey(char):
                node = node.get(char)
                if not node.isEnd():
                    # Prefix is incomplete, return false
                    return False
            else:
                # Return false if a character link is missing
                return False
        # All prefixes exist
        return True


class Solution:
    def completeString(self, nums):
        # Create a new Trie
        trie = Trie()

        # Insert all words into the Trie
        for word in nums:
            trie.insert(word)

        longest = ""  # Stores the longest valid word

        # Check each word to find the longest one where all prefixes exist
        for word in nums:
            if trie.checkIfAllPrefixExists(word):
                if len(word) > len(longest):
                    longest = word
                elif len(word) == len(longest) and word < longest:
                    longest = word  # Lexicographically smaller word

        # Return result or "None"
        return longest if longest else "None"


if __name__ == "__main__":
    # Hardcoded test cases
    test_cases = [
        ("Test Case 1", ["n", "ni", "nin", "ninj" , "ninja" , "nil"]),
        ("Test Case 2", ["z", "zu", "zur", "zuri"]),
        ("Test Case 3", ["not", "none", "no", "on"]),
        ("Test Case 4", ["abcd", "ab", "a"]),
        ("Test Case 5", ["hello", "he", "hell", "hel", "h"])
    ]

    for test_case, words in test_cases:
        print(test_case)
        print("Words:", words)

        sol = Solution()
        ans = sol.completeString(words)
        print("Longest complete string with all prefixes:", ans)
        print()  # Blank line for better readability

        # Check each word to find the longest one where all prefixes exist
        for word in nums:
            if trie.checkIfAllPrefixExists(word):
                if len(word) > len(longest):
                    longest = word
                elif len(word) == len(longest) and word < longest:
                    longest = word  # Lexicographically smaller word

        # Return result or "None"
        return longest if longest else "None"


Complexity Analysis
Time Complexity: O(N*M), where N is the number of words given and M is the average length of a word.
Each word is inserted into the Trie, and each insertion involves traversing the length of the word and potentially adding new nodes to the Trie taking O(N*M) time.
For each word, the code checks if every prefix of the word exists in the Trie as a complete word. This involves traversing each character in the word and checking if it leads to a node marked as an end of a valid prefix (or word) which again will take O(N*M) time.

Space Complexity: O(N)
Each node in the Trie contains an array of pointers to child nodes, typically 26 pointers for lowercase English letters.
The number of nodes created will be proportional to the number of characters in all unique words, resulting in a space complexity of O(N).

'''
class Node:
    def __init__(self):
        self.links = [None] * 26
        self.flag = False

    def containsKey(self, ch):
        return self.links[ord(ch) - ord('a')] is not None

    def get(self, ch):
        return self.links[ord(ch) - ord('a')]

    def put(self, ch, node):
        self.links[ord(ch) - ord('a')] = node

    def setEnd(self):
        self.flag = True

    def isEnd(self):
        return self.flag


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        node = self.root
        for char in word:
            if not node.containsKey(char):
                node.put(char, Node())
            node = node.get(char)
        node.setEnd()

    def checkIfAllPrefixExists(self, word):
        node = self.root
        for char in word:
            if node.containsKey(char):
                node = node.get(char)
                if not node.isEnd():
                    return False
            else:
                return False
        return True


class Solution:
    def completeString(self, nums):
        trie = Trie()
        for word in nums:
            trie.insert(word)

        longest = ""  
        for word in nums:
            if trie.checkIfAllPrefixExists(word):
                if len(word) > len(longest):
                    longest = word
                elif len(word) == len(longest) and word < longest:
                    longest = word  # Lexicographically smaller word
        return longest if longest else "None"