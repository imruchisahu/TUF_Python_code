'''You are given a string s. Return the array of unique characters, sorted by highest to lowest occurring characters.

If two or more characters have same frequency then arrange them in alphabetic order.


Examples:
Input : s = "tree"

Output : ['e', 'r', 't' ]

Explanation : The occurrences of each character are as shown below :

e --> 2

r --> 1

t --> 1.

The r and t have same occurrences , so we arrange them by alphabetic order.

Input : s = "raaaajj"

Output : ['a' , 'j', 'r' ]

Explanation : The occurrences of each character are as shown below :

a --> 4

j --> 2

r --> 1

Input : s = "bbccddaaa"

Output:
['a', 'b', 'c', 'd']
Constraints:
1 <= s.length <= 105
s consist of only lowercase English characters.
Intuition
The task at hand involves sorting characters based on their frequency in a string. Intuitively, the solution can be broken down into two parts: counting the occurrences of each character and sorting the characters based on these counts. It is essential to focus on two sorting criteria — first, prioritize higher frequencies, and second, in cases of equal frequency, sort the characters alphabetically. Therefore, the thought process revolves around using an efficient frequency counting technique and a custom sorting mechanism to produce the required result.

Approach
Create a frequency array where each element is a pair of an integer (frequency) and its associated character. Initialize this array for all lowercase alphabetic characters.
Traverse the string, incrementing the frequency of the respective character in the frequency array.
Sort the frequency array using a custom comparator that orders elements first by descending frequency and then by alphabetical order for characters with equal frequency.
Generate the output by iterating over the sorted array and collecting characters that have a non-zero frequency.
Dry Run


Complexity Analysis
Time Complexity: The time complexity of this solution is O(n + k log k) where n is the length of the string and k is the constant 26 for the alphabet

Space Complexity: The space complexity is O(k), where k is the constant 26 for the frequency array.





class Solution:
    def frequencySort(self, s):
        # Frequency array for characters 'a' to 'z'
        freq = [(0, chr(i + ord('a'))) for i in range(26)]

        # Count frequency of each character
        for ch in s:
            index = ord(ch) - ord('a')
            freq[index] = (freq[index][0] + 1, ch)

        # Sort by frequency (descending) and alphabetically (ascending)
        freq.sort(key=lambda x: (-x[0], x[1]))

        # Collect characters with non-zero frequency
        result = [ch for f, ch in freq if f > 0]
        return result

# Main method to test the function
if __name__ == "__main__":
    sol = Solution()
    s = "tree"
    result = sol.frequencySort(s)
    print(result)


'''
from collections import Counter
class Solution:
    def frequencySort(self, s):
        #your code goes here
        freq = Counter(s)
        sorted_chars = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
        return [char for char, count in sorted_chars]