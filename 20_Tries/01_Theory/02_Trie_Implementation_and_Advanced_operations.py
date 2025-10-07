'''
Implement "TRIE” data structure from scratch with the following functions.



Trie(): Initialize the object of this “TRIE” data structure.


insert(“WORD”): Insert the string “WORD” into this “TRIE” data structure.


countWordsEqualTo(“WORD”): Return how many times this “WORD” is present in this “TRIE”.


countWordsStartingWith(“PREFIX”): Return how many words are there in this “TRIE” that have the string “PREFIX” as a prefix.


erase(“WORD”): Delete one occurrence of the string “WORD” from the “TRIE”.

Examples:
Input : ["Trie", "insert", "countWordsEqualTo", "insert", "countWordsStartingWith", "erase", "countWordsStartingWith"]

[ "apple", "apple", "app", "app", "apple", "app" ]



Output : [null, null, 1, null, 2, null, 1]



Explanation :

Trie trie = new Trie()

trie.insert("apple")

trie.countWordsEqualTo("apple")  // return 1

trie.insert("app") 

trie.countWordsStartingWith("app") // return 2

trie.erase("apple")

trie.countWordsStartingWith("app")   // return 1

Input : ["Trie", "insert", "countWordsEqualTo", "insert", "erase", "countWordsStartingWith"]

[ "mango", "apple", "app", "app", "mango" ]



Output : [null, null, 0, null, null, 1]



Explanation :

Trie trie = new Trie()

trie.insert("mango")

trie.countWordsEqualTo("apple")  // return 0

trie.insert("app") 

trie.erase("app")

trie.countWordsStartingWith("mango") // return 1

Input : ["Trie", "insert", "insert", "erase", "countWordsEqualTo", "insert", "countWordsStartingWith"]

["abcde","fghij","abcde", "bcde", "abcde", "fgh"]

Output:
[null, null, null, null, 0, null, 1]
[null, null, null, null, 0, 0, null]
[null, null, null, 0, null, null, 0]
[null, null, null, 0, null, 0, null]

Submit
Constraints:
1 <= word.length , prefix.length <= 2000
word and prefix consist only of lowercase English letters.
At most 3*104 calls in total will be made to insert, countWordsEqualTo , countWordsStartingWith and erase.

Intuition
Refer to this article to get the basic idea about Tries.

Approach
To Insert a Node in the Prefix Trie
Begin at the root node.
Iterate through each character in the word. For each character:
Verify if a child node for that character exists.
If it doesn't, create a new node for the character and link it to the current node.
Increase the prefix count for each node.
Finally, increase the end count for the last node of the word.

To Count the Number of Words Equal to the Given Word in the Trie
Begin at the root node.
Iterate through each character in the word. For each character:
Traverse down the Trie by following the characters of the word.
If any character is not found, return 0 (indicating the word is not in the Trie).
Once all characters are found, return the end count of the node corresponding to the last character.

To Count the Number of Words Starting with the Given Word in the Trie
Begin at the root node.
Iterate through each character in the prefix. For each character:
Move down the Trie by following the characters of the prefix.
If any character is not found, return 0 (indicating no words start with the given prefix).
Once all characters are found, return the prefix count of the node corresponding to the last character.

To Erase the Given Word from the Trie
Begin at the root node.
Iterate through each character in the word. For each character, move down the Trie following the characters of the word and at each node:
Decrease the prefix count.
It is assumed that the word to be erased is always present in the Trie.
Once the end of the word is reached, decrease the end count.

class Node:
    def __init__(self):
        # Array to store links to child nodes,
        # each index represents a letter
        self.links = [None] * 26
        # Counter for number of words
        # that end at this node
        self.cntEndWith = 0
        # Counter for number of words
        # that have this node as a prefix
        self.cntPrefix = 0

    # Check if the node contains
    # a specific key (letter)
    def containsKey(self, ch):
        # Check if the link corresponding
        # to the character exists
        return self.links[ord(ch) - ord('a')] is not None

    # Get the node with a specific
    # key (letter) from the Trie
    def get(self, ch):
        # Return the link
        # corresponding to the character
        return self.links[ord(ch) - ord('a')]

    # Insert a new node with a specific
    # key (letter) into the Trie
    def put(self, ch, node):
        # Set the link corresponding to
        # the character to the provided node
        self.links[ord(ch) - ord('a')] = node

    # Increment the count of words
    # that end at this node
    def increaseEnd(self):
        # Increment the counter
        self.cntEndWith += 1

    # Increment the count of words
    # that have this node as a prefix
    def increasePrefix(self):
        # Increment the counter
        self.cntPrefix += 1

    # Decrement the count of words
    # that end at this node
    def deleteEnd(self):
        # Decrement the counter
        self.cntEndWith -= 1

    # Decrement the count of words
    # that have this node as a prefix
    def reducePrefix(self):
        # Decrement the counter
        self.cntPrefix -= 1

class Trie:
    def __init__(self):
        # Constructor to initialize the
        # Trie with an empty root node
        self.root = Node()

    # Inserts a word into the Trie
    # Time Complexity O(len), where len
    # is the length of the word
    def insert(self, word):
        # Start from the root node
        node = self.root
        # Iterate over each
        # character in the word
        for ch in word:
            if not node.containsKey(ch):
                # Create a new node
                # for the character
                node.put(ch, Node())
            # Move to the child node
            # corresponding to the character
            node = node.get(ch)
            # Increment the prefix
            # count for the node
            node.increasePrefix()
        # Increment the end count
        # for the last node of the word
        node.increaseEnd()

    # Returns the number of words
    # equal to a given word
    def countWordsEqualTo(self, word):
        # Start from the root node
        node = self.root
        # Iterate over each character in the word
        for ch in word:
            if node.containsKey(ch):
                # Move to the child node
                # corresponding to the character
                node = node.get(ch)
            else:
                # Return 0 if the
                # character is not found
                return 0
        # Return the count of
        # words ending at the node
        return node.cntEndWith

    # Returns the number of words
    # starting with a given prefix
    def countWordsStartingWith(self, word):
        # Start from the root node
        node = self.root
        # Iterate over each character in the prefix
        for ch in word:
            if node.containsKey(ch):
                # Move to the child node
                # corresponding to the character
                node = node.get(ch)
            else:
                # Return 0 if the
                # character is not found
                return 0
        # Return the count of
        # words with the prefix
        return node.cntPrefix

    # Erases a word from the Trie
    def erase(self, word):
        # Start from the root node
        node = self.root
        # Iterate over each character in the word
        for ch in word:
            if node.containsKey(ch):
                # Move to the child node
                # corresponding to the character
                node = node.get(ch)
                # Decrement the prefix
                # count for the node
                node.reducePrefix()
            else:
                # Return if the
                # character is not found
                return
        # Decrement the end count
        # for the last node of the word
        node.deleteEnd()

# Testing the Trie class
trie = Trie()
trie.insert("apple")
trie.insert("apple")
print("Inserting strings 'apple' twice into Trie")
print("Count Words Equal to 'apple':", trie.countWordsEqualTo("apple"))
print("Count Words Starting With 'app':", trie.countWordsStartingWith("app"))
print("Erasing word 'apple' from Trie")
trie.erase("apple")
print("Count Words Equal to 'apple':", trie.countWordsEqualTo("apple"))
print("Count Words Starting With 'app':", trie.countWordsStartingWith("app"))
print("Erasing word 'apple' from Trie")
trie.erase("apple")
print("Count Words Starting With 'app':", trie.countWordsStartingWith("app"))

Complexity Analysis
Time Complexity: O(N) where N is the length of the word or prefix being processed.
Each method (inserting a word, counting words equal to a given word, counting words starting with a prefix, and erasing a word) involves traversing the Trie for each character of the input word or prefix.
Thus, the time complexity is linear relative to the length of the word or prefix being processed.

Space Complexity: O(N) where N is the total number of characters across all words inserted into the Trie. The space complexity depends on the number of unique words added to the Trie and the average length of these words.

'''
class Node:
    def __init__(self):
        self.links = [None] * 26
        self.cntEndWith = 0
        self.cntPrefix = 0

    def containsKey(self, ch):
        return self.links[ord(ch) - ord('a')] is not None

    def get(self, ch):
        return self.links[ord(ch) - ord('a')]

    def put(self, ch, node):
        self.links[ord(ch) - ord('a')] = node

    def increaseEnd(self):
        self.cntEndWith += 1

    def increasePrefix(self):
        self.cntPrefix += 1

    def deleteEnd(self):
        self.cntEndWith -= 1

    def reducePrefix(self):
        self.cntPrefix -= 1

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        node = self.root
        for ch in word:
            if not node.containsKey(ch):
                node.put(ch, Node())
            node = node.get(ch)
            node.increasePrefix()
        node.increaseEnd()

    def countWordsEqualTo(self, word):
        node = self.root
        for ch in word:
            if node.containsKey(ch):
                node = node.get(ch)
            else:
                return 0
        return node.cntEndWith

    def countWordsStartingWith(self, word):
        node = self.root
        for ch in word:
            if node.containsKey(ch):
                node = node.get(ch)
            else:
                return 0
        return node.cntPrefix

    def erase(self, word):
        node = self.root
        for ch in word:
            if node.containsKey(ch):
                node = node.get(ch)
                node.reducePrefix()
            else:
                return 
        node.deleteEnd()


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)