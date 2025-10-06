'''
Given are the two distinct words startWord and targetWord, and a list of size N, denoting wordList of unique words of equal size M. Find the length of the shortest transformation sequence from startWord to targetWord.



Keep the following conditions in mind:



A word can only consist of lowercase characters.
Only one letter can be changed in each transformation.
Each transformed word must exist in the wordList including the targetWord.
startWord may or may not be part of the wordList


Note: If there’s no possible way to transform the sequence from startWord to targetWord return 0.


Examples:
Input: wordList = ["des","der","dfr","dgt","dfs"], startWord = "der", targetWord = "dfs"

Output: 3

Explanation: The length of the smallest transformation sequence from "der" to "dfs" is 3 i.e. "der" -> (replace ‘e’ by ‘f’) -> "dfr" -> (replace ‘r’ by ‘s’) -> "dfs". So, it takes 3 different strings for us to reach the targetWord. Each of these strings are present in the wordList.

Input: wordList = ["geek", "gefk"], startWord = "gedk", targetWord= "geek"

Output: 2

Explanation: The length of the smallest transformation sequence from "gedk" to "geek" is 2 i.e. "gedk" -> (replace ‘d’ by ‘e’) -> "geek" .

So, it takes 2 different strings for us to reach the targetWord. Each of these strings are present in the wordList.

Input: wordList = ["hot", "dot", "dog", "lot", "log"], startWord = "hit", targetWord = "cog"

Output:
3
0
2
1

Submit
Constraints:
N= Number of Words
M= Length of Word
1 ≤ N ≤ 100
1 ≤ M ≤ 10

Intuition:
How to identify this as a graph problem?
Consider the following example: 

It can be seen that in order to find the shortest transformation sequence, the level wise fashion helps in determining the shortest steps to go from startWord to targetWord.

Thus, a BFS-traversal will come in use for this problem making it a graph problem.
Understanding:
The levels of the transformation comprises of the words that can be formed from the words of the previous level (by changing only one letter). Thus, the BFS traversal can be performed starting from the startWord, exploring every possible word that can be made by changing one letter during each transformation.

Now consider the following example: 

The first thing that needs to be done is that all the possible transformations from a given word needs to be generated. Out of all the possible words generated, the transformation can be done in only those words which are present in the wordList. Now to check whether a word exists in the wordList or not, a set data structure can be used, which can help find answer this query in O(1) time.
Observation:
Consider a scenario where word "hit" also exist in the wordList and is transformed to "hot" and in the next transformation converted back to "hit". To avoid such unnecessary transformations, once a word is found, it can be deleted from the set which is also a O(1) operation.
The deletion operation is safe because when a word is found via the shortest transformations, there is no use of finding it again through some other path requiring more transformations.
Approach:
Use a queue to store pairs of words and their corresponding transformation steps. Start with the initial word and step count of 1.
Convert the word list into a hash set for efficient word existence checks and removal operations.
While the queue is not empty:
Extract the current word and its step count.
If the current word matches the target word, return the step count.
For each character in the current word, change it to every letter from 'a' to 'z'. For each transformation:
Check if the new word is in the hash set.
If found, remove it from the set, marking it as visited, and add it to the queue with an incremented step count.
If the queue is exhausted without finding the target word, return 0.
Key Points:
BFS ensures the shortest path by exploring all nodes level by level.
Hash set enables O(1) lookups and deletions, making the process efficient.
The algorithm returns the shortest transformation sequence length or 0 if no valid sequence exists.

from collections import deque

class Solution:
    
    # Function to determine number of steps
    # to reach from start ward to target word
    def wordLadderLength(self, startWord, 
                        targetWord, wordList):
                            
        # Queue data structure to store pair:
        # {"word", steps to reach "word"}
        q = deque([(startWord, 1)])

        # Add all the words to a hashset
        st = set(wordList)
        
        # If target word is not there in word list,
        # return 0 as it is not possible to transform
        if targetWord not in st:
            return 0
        
        # Erase the starting word 
        # from set (if it exists)
        st.discard(startWord)
        
        # Until the queue is empty
        while q:
            
            # Get the word from queue
            word, steps = q.popleft()

            # Return steps if target word is achieved
            if word == targetWord:
                return steps
            
            # Iterate on every character
            for i in range(len(word)):
                # Store the original letter 
                original = word[i]
                
                # Replacing current character with
                # letters from 'a' to 'z' to match 
                # any possible word from set
                for ch in range(ord('a'), ord('z') + 1):
                    word = word[:i] + chr(ch) + word[i+1:]
                    
                    # Check if it exists in the set
                    if word in st:
                        
                        # Erase the word from set 
                        st.remove(word)
                        
                        # Add the transition to the queue
                        q.append((word, steps + 1))
                
                # Update the original letter back
                word = word[:i] + original + word[i+1:]
        
        # If no transformation sequence 
        # is found, return 0
        return 0

if __name__ == "__main__":
    
    startWord = "der"
    targetWord = "dfs"
    wordList = ["des", "der", "dfr", "dgt", "dfs"]
    
    # Creating an instance of 
    # Solution class
    sol = Solution()
    
    # Function call to determine number of 
    # steps to reach from start ward to target word
    ans = sol.wordLadderLength(startWord, targetWord, wordList)
    
    # Output
    print("Word ladder length is:", ans)

Complexity Analysis:
Time Complexity: O(N*M*26)
In the worst case, the steps required to reach from startWord to targetWord can go up to N. During each step, all the characters for the word are replaced from 'a' to 'z' taking O(M*26) time.
Adding all the words in wordList takes O(N) time.
Note: If an ordered set is used in place of an unordered set then there will be a logN factor adding to the time complexity, since delete and update operations take O(logN) time for the ordered set.
Space Complexity: O(N)
A Hashset is used to store words in wordList taking O(N) space.

'''
from collections import deque
class Solution:
    def wordLadderLength(self, startWord, targetWord, wordList):
        q = deque([(startWord, 1)])

        # Add all the words to a hashset
        st = set(wordList)
        if targetWord not in st:
            return 0
        st.discard(startWord)
        while q:
            word, steps = q.popleft()
            if word == targetWord:
                return steps
            for i in range(len(word)):
                original = word[i]
                for ch in range(ord('a'), ord('z') + 1):
                    word = word[:i] + chr(ch) + word[i+1:]
                    if word in st:
                        st.remove(word)
                        q.append((word, steps + 1))
                word = word[:i] + original + word[i+1:]
        return 0

