'''
Given two distinct words startWord and targetWord, and a list denoting wordList of unique words of equal lengths. Find all shortest transformation sequence(s) from startWord to targetWord. You can return them in any order possible.



In this problem statement, we need to keep the following conditions in mind:



A word can only consist of lowercase characters.

Only one letter can be changed in each transformation.

Each transformed word must exist in the wordList including the targetWord.

startWord may or may not be part of the wordList.

Return an empty list if there is no such transformation sequence.


Examples:
Input: startWord = "der", targetWord = "dfs", wordList = ["des", "der", "dfr", "dgt", "dfs"]



Output: [ [ “der”, “dfr”, “dfs” ], [ “der”, “des”, “dfs”] ]



Explanation: The length of the smallest transformation sequence here is 3.

Following are the only two shortest ways to get to the targetWord from the startWord :

"der" -> ( replace ‘r’ by ‘s’ ) -> "des" -> ( replace ‘e’ by ‘f’ ) -> "dfs".

"der" -> ( replace ‘e’ by ‘f’ ) -> "dfr" -> ( replace ‘r’ by ‘s’ ) -> "dfs".

Input: startWord = "gedk", targetWord= "geek", wordList = ["geek", "gefk"]



Output: [ [ “gedk”, “geek” ] ]



Explanation: The length of the smallest transformation sequence here is 2.

Following is the only shortest way to get to the targetWord from the startWord :

"gedk" -> ( replace ‘d’ by ‘e’ ) -> "geek".

Input: startWord = "abc", targetWord = "xyz", wordList = ["abc", "ayc", "ayz", "xyz"]

Output:
[["abc","ayz", "ayc", "xyz"]]
[["abc", "ayc", "abc", "xyz"]]
[]
[["abc", "ayc", "ayz", "xyz"]]

Submit
Constraints:
N= Number of Words
M= Length of Word
1 ≤ N ≤ 100
1 ≤ M ≤ 10


#Word_ladder_part_1
Intuition:
In this problem, all the possible transformations from the startWord to endWord must be found. Hence, in contrary to the previous problem, we do not stop the traversal on the first occurrence of endWord,but rather continue it for as many occurrences of the word as possible as we need all the shortest possible sequences in order to reach the end word.

Modification:
In the previous solution, whenever a word was matched from the given wordList, it was immediately erased from the Hashmap to avoid visiting it via a longer path. But since, here all the possible transformations must be returned, erasing it from the Hashmap might lose some of the possible transformations leading through it.

Thus, instead of erasing the word immediately when it is found, the erase/delete operation can be performed after the traversal for all the words for a particular level is completed allowing exploration of all the paths.
Understanding:
In order to form the different sequences for transformations in a particular level, the concept of Backtracking can be used.
After adding the new word to a sequence, it is immediately removed (backtracked) to restore the sequence to its original state after the sequence is added to the queue.
This backtracking step ensures that the original sequence can be used to try other possible transformations at the current level of the BFS.
Approach:
Use a queue for breadth-first search (BFS) to handle sequences of word transformations. Add all words from the word list to a set for quick lookup. Start with the initial word and add it to the queue.
Perform BFS level by level. For each word in the current level:
Check if it matches the target word and add the sequence to the results. Generate all possible single-letter transformations.
If a transformed word exists in the set, add it to the current sequence and push the sequence into the queue for further exploration.
Mark words to be removed after the current level to prevent revisiting.
After adding a transformed word to the sequence, immediately remove it to restore the sequence for the next transformation.
Remove words marked during the level traversal from the set to prevent revisiting. Exit early if any sequences reaching the target word are found.
Return the list of resulting sequences.
from collections import deque

class Solution:
    
    # Function to determine number of steps
    # to reach from start word to target word
    def findSequences(self, beginWord, endWord, wordList):
        # To store the answer
        ans = []
        
        # Queue data structure to store 
        # the sequence of transformations
        q = deque()
        
        # Add all the words to a hashset
        st = set(wordList)
        
        # Add the sequence containing starting word to queue
        q.append([beginWord])
        
        # Erase starting word from set if it exists
        st.discard(beginWord)
        
        # Set to store the words that must be deleted 
        # after traversal of a level is complete
        toErase = set()
        
        # Until the queue is empty
        while q:
            
            # Size of queue
            size = len(q)
            
            # Traversing all words in current level
            for _ in range(size):
                
                # Sequence 
                seq = q.popleft()
                
                # Last added word in sequence
                word = seq[-1]
                
                # If the last word same as end word
                if word == endWord:
                    # Add the sequence to the answer
                    if not ans:
                        ans.append(seq)
                    elif len(ans[-1]) == len(seq):
                        ans.append(seq)
                
                # Iterate on every character
                for pos in range(len(word)):
                    
                    # Original letter
                    original = word[pos]
                    
                    # Replacing current character with
                    # letters from 'a' to 'z' to match 
                    # any possible word from set
                    for ch in 'abcdefghijklmnopqrstuvwxyz':
                        word = word[:pos] + ch + word[pos + 1:]
                        
                        # Check if it exists in the set
                        if word in st:
                            # Update the sequence
                            seq.append(word)
                            
                            # Push in the queue
                            q.append(list(seq))
                            
                            # Add the word to erase map
                            toErase.add(word)
                            
                            # Backtracking step
                            seq.pop()
                    
                    # Update the original letter back
                    word = word[:pos] + original + word[pos + 1:]
            
            # Erase all the words in set after
            # traversal of a level is completed
            for it in toErase:
                st.discard(it)
            toErase.clear()
            
            # If answer is found, break
            if ans:
                break
        
        # Return the result found
        return ans

if __name__ == "__main__":
    
    beginWord = "der"
    endWord = "dfs"
    wordList = ["des", "der", "dfr", "dgt", "dfs"]
    
    # Creating an instance of 
    # Solution class
    sol = Solution()
    
    # Function call to determine number of 
    # steps to reach from start word to target word
    ans = sol.findSequences(beginWord, endWord, wordList)
    
    # Output
    print("The different sequences are:")
    for sequence in ans:
        print(" ".join(sequence))

Complexity Analysis:
Time Complexity: O(N*M*26)
In the worst case, the steps required to reach from startWord to targetWord can go up to N. During each step, all the characters for the word are replaced from 'a' to 'z' taking O(M*26) time.
Adding all the words in wordList takes O(N) time.
Each word is enqueued and dequeued at most once, leading to O(N) queue operations.
Checking if a word exists in the set and removing a word from the set takes O(1) on average. If there are N words, there are O(N) set operations.
Note: If an ordered set is used in place of an unordered set then there will be a logN factor adding to the time complexity, since delete and update operations take O(logN) time for the ordered set.
Space Complexity: O(N*M)
A HashSet is used to store words in wordList taking O(N) space. In the worst case, the queue will store all possible sequences leading to a space requirement of O(N*M). Storing the result in a list will take O(N*M) space.


#Word_ladder_part_2
Intuition:
A more efficient way to find all the shortest possible transformations from the Start Word to End Word is by using a combination of BFS traversal for level-order traversal and DFS for backtracking.

Understanding:
Breadth-First Search (BFS): BFS is used to find the shortest path from beginWord to endWord. BFS explores all words level by level, ensuring that the shortest path is found first. The re-processing of nodes can be avoided by using a map to track the shortest distance to each word.
Depth-First Search (DFS): After the BFS completes, DFS can be used to backtrack from endWord to beginWord. DFS helps to reconstruct all the shortest paths found by BFS.
This approach avoids redundant transformations and unnecessary path explorations by combining BFS and DFS. BFS ensures that the shortest paths are discovered first, while DFS backtracks efficiently to generate all valid sequences.
Edge Cases:
If it not possible to reach the target word from the start word, the Backtracking step can be skipped and an empty list can be returned as the answer.

Approach:
Create a set containing all words from the provided word list and a queue to facilitate BFS traversal. Additionally, use a map to keep track of the minimum steps needed to reach each word from the start word.
Start from the initial word and perform BFS. For each word, explore all possible transformations by changing each character to every letter from 'a' to 'z'.
If a transformed word is found in the word list set, it is added to the queue and the map with incremented steps. The word is then removed from the set to prevent revisiting.
After BFS completes, check if the target word is present in the map. If not, return an empty list as there is no transformation sequence.
If the target word is found, use DFS to backtrack from the target word to the start word. The DFS reconstructs all shortest transformation sequences by following the steps stored in the map.
Store the valid sequences found by DFS in a result list and return it.

from collections import deque

class Solution:
    
    def dfs(self, word, beginWord, seq, mpp, ans):
        # If the sequence is complete
        if word == beginWord:
            
            # Reverse the sequence
            seq.reverse()
            
            # Store in the result
            ans.append(list(seq))
            
            # Reverse again for other possible sequences
            seq.reverse()
            
            # Return
            return
        
        # Steps to reach the word
        val = mpp[word]
        
        # Try all possible transformations
        for i in range(len(word)):
            original = word[i]
            
            for ch in range(ord('a'), ord('z') + 1):
                transformed_word = word[:i] + chr(ch) + word[i + 1:]
                
                # If a possible transformation is found
                if (transformed_word in mpp and 
                    mpp[transformed_word] + 1 == val):
                    
                    # Update the sequence
                    seq.append(transformed_word)
                    
                    # Make recursive DFS call
                    self.dfs(transformed_word, beginWord, seq, mpp, ans)
                    
                    # Pop back for backtracking
                    seq.pop()
            
            # Restore original word
            word = word[:i] + original + word[i + 1:]

    def findSequences(self, beginWord, endWord, wordList):
        
        # Length of words
        len_word = len(beginWord)
        
        # Add all the words to a hashset
        st = set(wordList)
                                  
        # Hash map to store the minimum steps needed to reach a word
        mpp = {}
        
        # Queue for BFS traversal
        q = deque([beginWord])
        
        # Erasing the initial word from the set if it exists
        if beginWord in st:
            st.remove(beginWord)
        
        # Step count
        steps = 1
        
        # Storing the initial pair in map
        mpp[beginWord] = steps
        
        # Until the queue is empty
        while q:
            
            # Get the word and steps
            word = q.popleft()
            steps = mpp[word]

            # Check for every possible transformation
            for i in range(len_word):
                original = word[i]
                
                for ch in range(ord('a'), ord('z') + 1):
                    transformed_word = word[:i] + chr(ch) + word[i + 1:]
                    
                    # If a possible transformation is found
                    if transformed_word in st:
                        
                        # Store it in map
                        mpp[transformed_word] = steps + 1
                        
                        # Push in the queue
                        q.append(transformed_word)
                        
                        # Erase word from list
                        st.remove(transformed_word)
                
                # Restore original word
                word = word[:i] + original + word[i + 1:]

        # Return an empty list if reaching 
        # the target word is not possible
        if endWord not in mpp:
            return []
        
        # To store the answer
        ans = []
        
        # To store the possible sequence of transformations
        seq = [endWord]
        
        # Backtracking step
        self.dfs(endWord, beginWord, seq, mpp, ans)
        
        # Return the computed result
        return ans

if __name__ == "__main__":
    beginWord = "der"
    endWord = "dfs"
    wordList = ["des", "der", "dfr", "dgt", "dfs"]
    
    # Creating an instance of Solution class
    sol = Solution()
    
    # Function call to determine number of steps 
    # to reach from start word to target word
    ans = sol.findSequences(beginWord, endWord, wordList)
    
    # Output
    print("The different sequences are:")
    for seq in ans:
        print(" ".join(seq))

Complexity Analysis:
Time Complexity: O(N*M)

Creating a set from the word list takes O(N).
The queue can contain up to N words in the worst case. For each word, all possible M character positions are changed to 26 different letters taking overall O(N*M*26) time.
In the worst case, the DFS might explore all possible sequences from the target word back to the start word.
Space Complexity: O(N2*M)
The set and map will store all the words each having M length taking O(N*M) space. The queue space will also be O(N*M) in the worst case. In the worst case, the result list will store all possible transformations ( which is N in the worst case) making the space requirement of O(N2*M)


'''
from collections import deque
class Solution:
    def findSequences(self, beginWord, endWord, wordList):
        ans = []
        q = deque()
        st = set(wordList)
        q.append([beginWord])
        st.discard(beginWord)
        toErase = set()
        while q:
            size = len(q)
            for _ in range(size): 
                seq = q.popleft()
                word = seq[-1]
                if word == endWord:
                    if not ans:
                        ans.append(seq)
                    elif len(ans[-1]) == len(seq):
                        ans.append(seq)
                for pos in range(len(word)):
                    original = word[pos]
                    for ch in 'abcdefghijklmnopqrstuvwxyz':
                        word = word[:pos] + ch + word[pos + 1:]
                        if word in st:
                            seq.append(word)
                            q.append(list(seq))
                            toErase.add(word)
                            seq.pop()
                    word = word[:pos] + original + word[pos + 1:]
            for it in toErase:
                st.discard(it)
            toErase.clear()
            if ans:
                break
        return ans