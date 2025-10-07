'''
Implement the Trie class:



Trie(): Initializes the trie object.


void insert (String word): Inserts the string word into the trie.


boolean search (String word): Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.


boolean startsWith (String prefix): Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

Examples:
Input : ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]

[ [] , "apple", "apple", "app", "app", "app", "app" ]



Output : [null, null, true, false, true, null, true]



Explanation :

Trie trie = new Trie()

trie.insert("apple")

trie.search("apple")  // return True

trie.search("app")   // return False

trie.startsWith("app") // return True

trie.insert("app")

trie.search("app")   // return True

Input : ["Trie" , "insert" , "insert" , "startsWith" , "search" ]

[ [] , "takeu" , "banana" , "bana" , "takeu" ]



Output : [null, null, null, true, true]



Explanation :

Trie trie = new Trie()

trie.insert("takeu")

trie.insert("banana")

trie.startsWith("bana") // return True

trie.search("takeu")   // return True

Input : ["Trie" , "insert" , "insert" , "startsWith" , "search" ]

[ [] , "caterpiller" , "cat" , "cat" , "cat" ]

Output:
[null, null, null, false, true]
[null, null, null, false, false]
[null, null, null, true, false]
[null, null, null, true, true]

Submit
Constraints:
1 <= word.length , prefix.length <= 2000
word and prefix consist only of lowercase English letters.
At most 3*104 calls in total will be made to insert, search and startsWith.

Intuition
A Trie is a specialized tree-like data structure that organizes and stores words in an efficient manner. Each node in a Trie represents a single character of a word, allowing for efficient addition, retrieval, and deletion of words.
In simpler terms, a Trie is an advanced information retrieval data structure. It outperforms more conventional data structures like Hashmaps and Trees in terms of the time complexity for various operations, making it particularly useful for tasks involving large sets of strings or words.
The Trie data structure is designed to store and quickly retrieve a collection of strings.
It arranges strings so that shared prefixes are stored once, which makes it very efficient for operations like searching for words with a specific prefix. This ability to quickly find all strings that start with a given prefix makes Tries particularly useful for applications like autocomplete and predictive text. Trie Node Structure
A Trie node is a fundamental element used to build a Trie. Each node consists of the following parts:

Child Node Links: A Trie node has an array of pointers, often referred to as "links" or "children pointers," for every letter of the lowercase alphabet. These pointers create connections to child nodes that represent each letter of the alphabet. For example, the link at index 0 corresponds to the child node for the letter 'a', the link at index 1 corresponds to 'b', and so on.
End-of-Word Flag: Each Trie node includes a boolean flag that signifies whether the node marks the end of a word. This flag is crucial for differentiating between prefixes and full words stored in the Trie.

Each node in the Trie supports several key operations:

Contains Key: This operation checks if a specific letter (or key) exists as a child node of the current Trie node. It returns true if the letter is present, indicating a valid path in the Trie.
Get Child Node: Given a letter, this operation retrieves the corresponding child node from the current Trie node. If the letter is present, it returns a pointer to the child node; otherwise, it returns null, indicating the letter is absent.
Put Child Node: This operation creates a link between the current Trie node and a child node representing a specific letter. It sets the link at the corresponding index to point to the given child node.
Set End Flag: This operation marks the current Trie node as the end of a word. This flag is essential for determining if a string stored in the Trie ends at this node, indicating a complete word.
Is End of Word: This operation checks if the current Trie node marks the end of a word by examining the end flag. It returns true if the node signifies the end of a word; otherwise, it returns false.

Approach
To insert a Node in The Trie
Begin at the root node.
For each character in the word:
Check if the current node has a child node for the character.
If the child node doesn't exist, create a new node and link it to the current node.
Move to the child node that corresponds to the character.
After inserting all characters, mark the end of the word by setting the end flag of the last node to true.

To search for a word in Trie
Begin at the root node.
For each character in the word:
Verify if the current node has a child node for the character.
If not, the word is not present in the Trie.
Move to the child node corresponding to the character.
After processing all characters, check if the end flag of the last node is set to true. If it is, the word is found; if not, the word is not in the Trie.

Check if Trie contains Prefix
Begin at the root node.
For each character in the prefix:
Check if the current node has a child node for the character.
If it doesn't, there is no word with the given prefix.
Move to the child node that corresponds to the character.
If all characters of the prefix are found, return true to indicate that there are words with the given prefix.

# Node Structure for Trie
class Node:
    """ Array to store links to child nodes,
    each index represents a letter """
    def __init__(self):
        self.links = [None] * 26

        """ Flag indicating if 
        the node marks the end 
        of a word """
        self.flag = False

    """ Check if the node contains
    a specific key (letter) """
    def containsKey(self, ch):
        return self.links[ord(ch) - ord('a')] is not None

    """ Insert a new node with a specific
    key (letter) into the Trie """
    def put(self, ch, node):
        self.links[ord(ch) - ord('a')] = node

    """ Get the node with a specific
    key (letter) from the Trie """
    def get(self, ch):
        return self.links[ord(ch) - ord('a')]

    """ Set the current node
    as the end of a word """
    def setEnd(self):
        self.flag = True

    """ Check if the 
    current node marks 
    the end of a word """
    def isEnd(self):
        return self.flag

# Trie class
class Trie:
    """ Constructor to 
    initialize the
    Trie with an 
    empty root node """
    def __init__(self):
        self.root = Node()

    """ Inserts a word into the Trie
    Time Complexity O(len), where len
    is the length of the word """
    def insert(self, word):
        node = self.root
        for ch in word:
            if not node.containsKey(ch):
                """ Create a new node for
                the letter if not present """
                node.put(ch, Node())
            # Move to the next node
            node = node.get(ch)
        # Mark the end of the word
        node.setEnd()

    """ Returns if the word
    is in the trie """
    def search(self, word):
        node = self.root
        for ch in word:
            if not node.containsKey(ch):
                """ If a letter is 
                not found, the word 
                is not in the Trie """
                return False
            # Move to the next node
            node = node.get(ch)
        """ Check if the last node
        marks the end of a word """
        return node.isEnd()

    """ Returns if there is any word in the
    trie that starts with the given prefix """
    def startsWith(self, prefix):
        node = self.root
        for ch in prefix:
            if not node.containsKey(ch):
                """ If a letter is not 
                found, there is
                no word with the 
                given prefix """
                return False
            # Move to the next node
            node = node.get(ch)
        # Prefix Found
        return True

# Driver Code
trie = Trie()
operations = ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
arguments = [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]

output = []
for i in range(len(operations)):
    if operations[i] == "Trie":
        output.append("null")
    elif operations[i] == "insert":
        trie.insert(arguments[i][0])
        output.append("null")
    elif operations[i] == "search":
        result = trie.search(arguments[i][0])
        output.append("true" if result else "false")
    elif operations[i] == "startsWith":
        result = trie.startsWith(arguments[i][0])
        output.append("true" if result else "false")

for res in output:
    print(res)

    
        self.flag = True

    """ Check if the 
    current node marks 
    the end of a word """
    def isEnd(self):
        return self.flag

# Trie class
class Trie:

Complexity Analysis
Time Complexity:
Insertion: O(N), where N is the length of the word being inserted. This is because we need to go through each letter of the word to either find its corresponding node or create a new node as needed.
Search: O(N), where N is the length of the word being searched for. During a Trie search, we traverse each letter of the word starting from the root, checking if the current node has a child node at the position of the next letter. This continues until we either reach the end of the word or find a missing letter node.
Prefix Search: O(N), where N is the length of the prefix being searched for. Just like in word search, we go through each letter of the prefix to find its corresponding node.


Space Complexity: O(N) where N is the total number of characters across all unique words inserted into the Trie. For each character in a word, a new node might need to be created, 
resulting in space usage that is proportional to the total number of characters.
'''

class Node:
    def __init__(self):
        self.links = [None] * 26
        self.flag = False
    def containsKey(self, ch):
        return self.links[ord(ch) - ord('a')] is not None
    def put(self, ch, node):
        self.links[ord(ch) - ord('a')] = node
    def get(self, ch):
        return self.links[ord(ch) - ord('a')]
    def setEnd(self):
        self.flag = True
    def isEnd(self):
        return self.flag

# Trie class
class Trie:
    def __init__(self):
        self.root = Node()
    def insert(self, word):
        node = self.root
        for ch in word:
            if not node.containsKey(ch):
                node.put(ch, Node())
            node = node.get(ch)
        node.setEnd()

    def search(self, word):
        node = self.root
        for ch in word:
            if not node.containsKey(ch):
                return False
            node = node.get(ch)
        return node.isEnd()

    def startsWith(self, prefix):
        node = self.root
        for ch in prefix:
            if not node.containsKey(ch):
                return False
            node = node.get(ch)
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
