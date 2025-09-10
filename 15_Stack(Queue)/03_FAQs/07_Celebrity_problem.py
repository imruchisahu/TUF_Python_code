'''
A celebrity is a person who is known by everyone else at the party but does not know anyone in return. Given a square matrix M of size N x N where M[i][j] is 1 if person i knows person j, and 0 otherwise, determine if there is a celebrity at the party. Return the index of the celebrity or -1 if no such person exists.



Note that M[i][i] is always 0.


Examples:
Input: M = [ [0, 1, 1, 0], [0, 0, 0, 0], [1, 1, 0, 0], [0, 1, 1, 0] ]

Output: 1

Explanation: Person 1 does not know anyone and is known by persons 0, 2, and 3. Therefore, person 1 is the celebrity.

Input: M = [ [0, 1], [1, 0] ]

Output: -1

Explanation: Both persons know each other, so there is no celebrity.

Input: M = [ [0, 1, 0], [0, 0, 0], [0, 1, 0] ]

Output:
0
1
2
3

Submit
Constraints:
  1 <= N <= 3000
  0 <= M[][] <= 1


  #Brute
  Intuition:
A naive approach to solve this problem is to count all the persons that are known for each person and to count all the person that each person knows. This way the celebrity can be identified by finding the person who is known by all other people and who does not know any person.

Approach:
Create two lists to count how many people each person knows and how many people know each person.
Iterate through the matrix to update the counters based on whether a person knows another person.
After populating the counters, iterate through them to find a person who is known by everyone else but does not know anyone. If such a person is found, return their index.
If no such person is found, return -1 indicating there is no celebrity.

class Solution:
    # Function to find the index of celebrity
    def celebrity(self, M):
        
        # Size of given matrix
        n = len(M)
        
        # To store count of people who 
        # know person of index i
        knowMe = [0] * n
        
        # To store count of people who 
        # the person of index i knows
        Iknow = [0] * n
        
        # Traverse on given matrix
        for i in range(n):
            for j in range(n):
                
                # If person i knows person j
                if M[i][j] == 1:
                    knowMe[j] += 1
                    Iknow[i] += 1
        
        # Traverse for all persons to find the celebrity
        for i in range(n):
            
            # Return the index of celebrity
            if knowMe[i] == n - 1 and Iknow[i] == 0:
                return i  
        
        # Return -1 if no celebrity is found
        return -1

if __name__ == "__main__":
    M = [
        [0, 1, 1, 0], 
        [0, 0, 0, 0], 
        [1, 1, 0, 0], 
        [0, 1, 1, 0]
    ]
    
    # Creating an instance of 
    # Solution class
    sol = Solution() 
    
    # Function call to find the index of celebrity
    ans = sol.celebrity(M)
    
    print("The index of celebrity is:", ans)

Complexity Analysis:
Time Complexity: O(N2) (where N is the size of square matrix)
Traversing the given square matrix to populate the two lists takes O(N2) time.
Traversing on the lists to identify the celebrity takes O(N) time.
Space Complexity: O(N)
The two lists to store the count of how many people each person knows and how many people know each person takes O(N) space each.

#Optimal
Intuition:
Since there can be only one celebrity, instead of finding the celebrity, the people that are not celebrity can be determined. If all such people are found, any person left (if it exists) will be the celebrity.
THe two conditions to identify the celebrity is:

The celebrity should be known by every person.
There should be no person that celebrity knows.
Approach:
Set up two pointers, one at the top of the matrix and one at the bottom.
Use the pointers to compare individuals:
If the person at the top pointer knows the person at the bottom pointer, move the top pointer down (as it cannot be the celebrity).
If the person at the bottom pointer knows the person at the top pointer, move the bottom pointer up (as it cannot be the celebrity).
If neither knows the other, increment both pointers (as they both cannot be the celebrity).
After the traversal, check if the remaining candidate pointed by the top pointer is a valid celebrity by ensuring that everyone knows this person and this person knows no one.
If a valid celebrity is found, return the index; otherwise, return -1 indicating there is no celebrity.

class Solution:
    # Function to find the index of celebrity
    def celebrity(self, M):
        
        # Size of given matrix
        n = len(M)
        
        # Top and Down pointers
        top, down = 0, n - 1
        
        # Traverse for all the people
        while top < down:
            
            # If top knows down,
            # it can not be a celebrity
            if M[top][down] == 1:
                top += 1
            
            # If down knows top,
            # it can not be a celebrity
            elif M[down][top] == 1:
                down -= 1
            
            # If both do not know each other,
            # both cannot be the celebrity
            else:
                top += 1
                down -= 1
        
        # Return -1 if no celebrity is found
        if top > down:
            return -1
        
        # Check if the person pointed
        # by top is celebrity
        for i in range(n):
            if i == top:
                continue
            
            # Check if it is not a celebrity
            if M[top][i] == 1 or M[i][top] == 0:
                return -1
        
        # Return the index of celebrity
        return top

if __name__ == "__main__":
    M = [
        [0, 1, 1, 0], 
        [0, 0, 0, 0], 
        [1, 1, 0, 0], 
        [0, 1, 1, 0]
    ]
    
    # Creating an instance of 
    # Solution class
    sol = Solution() 
    
    # Function call to find the index of celebrity
    ans = sol.celebrity(M)
    
    print("The index of celebrity is:", ans)

Complexity Analysis:
Time Complexity: O(N) (where N is the size of given square matrix)
Eliminating persons takes O(N) time.
Checking if the last candidate is a celebrity takes O(N) time.
Space Complexity: O(1)
Using only a couple of variables.


'''
class Solution:
    def celebrity(self, M):
      N=len(M)
      st = [i for i in range(N)]
      while len(st) > 1:
          A = st.pop()
          B = st.pop()
          if M[A][B] == 1:
              st.append(B)
          else:
              st.append(A)
      cand = st.pop()
      for i in range(N):
          if i != cand:
              if M[cand][i] == 1 or M[i][cand] == 0:
                  return -1
      return cand
    