'''Given two strings s and t, determine if they are isomorphic. Two strings s and t are isomorphic if the characters in s can be replaced to get t.



All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.


Examples:
Input : s = "egg" , t = "add"

Output : true

Explanation : The 'e' in string s can be replaced with 'a' of string t.

The 'g' in string s can be replaced with 'd' of t.

Hence all characters in s can be replaced to get t.

Input : s = "apple" , t = "bbnbm"

Output : false

Explanation : It can be proved that no solution exists for this example.

All the "b"s in t have to take places of "a", "p", "l", which requires "p" to be mapped to "b", but that makes it impossible for "p" at index 2 (0-indexed) to become "n". Thus no solution exists.

Input : s = "paper" , t = "title"

Output:
true
Constraints:
1 <= s.length <= 103
s.length == t.length
s and t consist of only lowercase English letters.
Intuition:
To determine if two strings are isomorphic, the key insight is to recognize that two strings are isomorphic if the characters in one string can be replaced to get the other string. This can be efficiently checked by ensuring that there is a consistent mapping of characters from the first string to the second string and vice versa. The challenge lies in maintaining this mapping as the strings are traversed, ensuring that each character in the first string maps uniquely to a character in the second string, and that no two characters in the first string map to the same character in the second string.

Approach:
Initialize two arrays of size 256 (to cover all ASCII characters) to store the last seen positions of characters in both strings. This helps in tracking the mapping between characters.
Iterate through each character in the strings simultaneously. For each character, compare the last seen positions stored in the arrays. If the positions do not match, it indicates an inconsistent mapping, and the strings are not isomorphic.
If the positions match, update the arrays with the current index (incremented by 1 to avoid the default value of 0). This ensures that the mapping is consistent throughout the strings.
After completing the iteration, if no inconsistencies in the mappings are found, the strings are confirmed to be isomorphic. If any inconsistency is found during the iteration, return false immediately.
Dry Run:

Solution:
Cpp
Java
Python
Javascript
CSharp
Go


1234567891011121314151617181920212223
Complexity Analysis:
Time Complexity: O(N) where N is the length of the input strings, due to the single loop iterating through each character

Space Complexity: O(k) O(1) since the space used by the arrays is constant (256 fixed size) regardless of input size



My submissions

Status
Language
Code
Advance Analysis
Accepted
May 26, 2025
C++
View





Comment
Community
Mine
Upvoted
MT
Moksh Tehlan
11 months ago

Simple Java Solution without two hasmap

class Solution {
    public boolean isomorphicString(String s, String t) {
        //your code goes here
        Map<Character,Character> map = new HashMap<>();


        for(int i = 0; i < s.length(); i++){
            if(!map.containsKey(s.charAt(i))){


                // check if the value we are going to map
                // isn't mapped to another value of s
                if(map.containsValue(t.charAt(i))) return false;
                map.put(s.charAt(i),t.charAt(i));
            }else if( map.get(s.charAt(i)) != t.charAt(i)){
                return false;
            }
        }
        return true;
    }
}

12

0 replies
R
Radhekanhaji143@
5 months ago

Hey striver how to identify which pattern it is


8

0 replies
AA
Aarfeen Anees
10 months ago

simple C++ solution with std::map (i.e hashing)



class Solution {
public:
    bool isomorphicString(string s, string t) {
        if(s.length() != t.length()) return false;
    
        map<char,char> charmap;
        charmap[s.front()] = t.front();
        for(int i = 0; i<s.length(); i++)
        {
            if(charmap.find(s[i]) != charmap.end()) //if character has been encountered before
            {
                if(charmap[s[i]] != t[i]) return false;
            }
            else charmap[s[i]] = t[i];
        }

        return true; 
    }
};

6

0 replies
KA
Kuderella Abhilash
2 months ago

class Solution {

public:

    bool isomorphicString(string s, string t) {

        //your code goes here

        string sdup=s;

        string tdup=t;

        int cnt1=0;

        int cnt2=0;

        sort(s.begin(),s.end());

        sort(t.begin(),t.end());

        if(s.size()==t.size())

        {

            for(int i=0;i<s.size();i++)

            {

                if(s[i]==s[i+1])

                {

                    cnt1++;

                }

                if(t[i]==t[i+1])

                {

                    cnt2++;

                }

            }

            if(cnt1==cnt2)

            return true;

        return false;

           

        }

        return false;

       

           

       

       



    }

};


2

0 replies
Abhay Yadav
Abhay Yadav
4 months ago

class Solution {

public:

bool isomorphicString(string s, string t) {

int slen = s.length();

int tlen = t.length();

int shash[26] = {0};

int thash[26] = {0};

for (int i = 0; i < slen; i++) {

shash[s[i] - 'a']++;

thash[t[i] - 'a']++;

}

sort(shash, shash + 26, [](int a, int b) { return a > b; });

sort(thash, thash + 26, [](int a, int b) { return a > b; });

for (int i = 0; i < 26; i++) {

if (shash[i] != thash[i]) return false;

}

return true;

}

};


class Solution:
    def isomorphicString(self, s, t):
        # Arrays to store the last seen positions of characters in s and t
        m1, m2 = [0] * 256, [0] * 256
        
        # Length of the string
        n = len(s)
        
        # Iterate through each character in the strings
        for i in range(n):
            # If the last seen positions of the current characters don't match, return false
            if m1[ord(s[i])] != m2[ord(t[i])]:
                return False
            
            # Update the last seen positions
            m1[ord(s[i])] = i + 1
            m2[ord(t[i])] = i + 1
        
        # If all characters match, return true
        return True

# Main method for testing
if __name__ == "__main__":
    solution = Solution()
    s = "egg"
    t = "add"
    if solution.isomorphicString(s, t):
        print("Strings are isomorphic.")
    else:
        print("Strings are not isomorphic.")


'''
class Solution:
    def isomorphicString(self, s, t):
        m1, m2 = [0] * 256, [0] * 256
        n = len(s)
        for i in range(n):
            if m1[ord(s[i])] != m2[ord(t[i])]:
                return False
            m1[ord(s[i])] = i + 1
            m2[ord(t[i])] = i + 1
        return True