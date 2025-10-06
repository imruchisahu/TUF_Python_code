'''
Given a list of accounts where each element account [i] is a list of strings, where the first element account [i][0] is a name, and the rest of the elements are emails representing emails of the account.



Now, merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.



After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order.


Examples:
Input: N = 4,

accounts =

[["John","johnsmith@mail.com","john_newyork@mail.com"],

["John","johnsmith@mail.com","john00@mail.com"],

["Mary","mary@mail.com"],

["John","johnnybravo@mail.com"]]



Output: [["John","john00@mail.com","john_newyork@mail.com", "johnsmith@mail.com"],

["Mary","mary@mail.com"],

["John","johnnybravo@mail.com"]]



Explanation: The first and the second John are the same person as they have a common email. But the third Mary and fourth John are not the same as they do not have any common email. The result can be in any order but the emails must be in sorted order. The following is also a valid result:

[['Mary', 'mary@mail.com'],

['John', 'johnnybravo@mail.com'],

['John', 'john00@mail.com' , 'john_newyork@mail.com', 'johnsmith@mail.com' ]]

Input: N = 6,

accounts =

[["John","j1@com","j2@com","j3@com"],

["John","j4@com"],

["Raj",”r1@com”, “r2@com”],

["John","j1@com","j5@com"],

["Raj",”r2@com”, “r3@com”],

["Mary","m1@com"]]



Output: [["John","j1@com","j2@com","j3@com","j5@com"],

["John","j4@com"],

["Raj",”r1@com”, “r2@com”, “r3@com”],

["Mary","m1@com"]]



Explanation: The first and the fourth John are the same person here as they have a common email. And the third and the fifth Raj are also the same person. So, the same accounts are merged.

Input: N = 3,



accounts = [

  ["Alice", "alice@mail.com", "alice_work@mail.com"],

  ["Bob", "bob@gmail.com"],

  ["Alice", "alice_personal@mail.com", "alice@mail.com"]

]

Output:
[['Alice', 'alice@mail.com', 'alice_personal@mail.com'], ['Alice', 'alice_personal@mail.com' ,alice_work@mail.com'], ['Bob', bob@gmail.com']]
[['Alice', 'alice@mail.com', 'alice_personal@mail.com'], ['Alice', 'alice_work@mail.com'], ['Bob', bob@gmail.com']]
[['Alice', 'alice@mail.com', 'alice_personal@mail.com', 'alice_work@mail.com'], ['Bob', bob@gmail.com']]
[['Alice', 'alice@mail.com'], ['Alice', 'alice_personal@mail.com', 'alice_work@mail.com'], ['Bob', bob@gmail.com']]

Submit
Constraints:
·  1 <= N <= 1000

·  2 <= accounts[i].size <= 15

·  1 <= accounts[i][j].size <= 30

·  accounts[i][0] consists of English letters.

Intuition:
To identify if two accounts have a common email, iterating over two accounts of the same name and checking each email can be costly.
A more efficient way involves visualizing the set of emails of each account as a graph, forming various connected components. Set of emails belonging to a person form a single node. Each mail can be placed under a set representing that the email belongs to that person. If an email is found to be already associated with some other person, a common email is found, which means all the emails in both the sets belong to a single person and thus, merging of accounts(sets) must be done.

How to handle merging of accounts?
The data structure that is the best fit when it comes to handling merge/union operation is Disjoint Set. Hence, whenever the two sets(accounts) are found to have a common email, the merge operation can be performed in constant time.
Understanding:
To store the mails belonging to a single person, a hashmap can be used which will provide constant look-up time which will be efficient to check if the mails already belonging to a person or not.
Approach:
Initialize a DSU structure to keep track of connected components (emails belonging to the same person).
Traverse through each account and its emails. For each email, if it's seen for the first time, map it to the current account index. If the email has been seen before, union the current account index with the previously mapped account index.
Create a list to collect emails for each connected component.
Traverse the email-to-node mapping to collect all emails under their ultimate parent node.
For each component, sort the emails and prepend the owner's name. Collect all the accounts and sort them by name.

class DisjointSet:
    # To store the ranks, parents and 
    # sizes of different set of vertices
    def __init__(self, n):
        self.rank = [0] * (n + 1)
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)
    
    # Function to find ultimate parent
    def findUPar(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.findUPar(self.parent[node])
        return self.parent[node]
    
    # Function to implement union by rank
    def unionByRank(self, u, v):
        ulp_u = self.findUPar(u)
        ulp_v = self.findUPar(v)
        if ulp_u == ulp_v: return
        if self.rank[ulp_u] < self.rank[ulp_v]:
            self.parent[ulp_u] = ulp_v
        elif self.rank[ulp_v] < self.rank[ulp_u]:
            self.parent[ulp_v] = ulp_u
        else:
            self.parent[ulp_v] = ulp_u
            self.rank[ulp_u] += 1
    
    # Function to implement union by size
    def unionBySize(self, u, v):
        ulp_u = self.findUPar(u)
        ulp_v = self.findUPar(v)
        if ulp_u == ulp_v: return
        if self.size[ulp_u] < self.size[ulp_v]:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v] += self.size[ulp_u]
        else:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]

# Solution class
class Solution:
    
    # Function to merge the accounts
    def accountsMerge(self, accounts):
        n = len(accounts) # Number of accounts
        
        # Disjoint Set data structure
        ds = DisjointSet(n)
        
        # Hashmap to store the pair: {mails, node}
        mapMailNode = {}
        
        # Iterate on all the accounts
        for i in range(n):
            
            # Iterate on all the mails of the person
            for j in range(1, len(accounts[i])):
                
                # Get the mail
                mail = accounts[i][j]
                
                # If this mail was not already existing
                if mail not in mapMailNode:
                    
                    # Add it to the hashmap
                    mapMailNode[mail] = i
                
                # Otherwise join it with the previous component
                else:
                    # Unite the components
                    ds.unionBySize(i, mapMailNode[mail])
        
        # To store the merged mails
        mergedMail = [[] for _ in range(n)]
        
        # Iterate on the Hashmap
        for mail, node in mapMailNode.items():
            root = ds.findUPar(node)
            mergedMail[root].append(mail)
        
        # To return the result
        ans = []
        
        # Iterate on all list of merged mails
        for i in range(n):
            
            # If a person has no mails, skip the iteration
            if not mergedMail[i]:
                continue
            
            # Otherwise, add all the merged mails of person
            mergedMail[i].sort()
            temp = [accounts[i][0]] + mergedMail[i]
            ans.append(temp)
        
        ans.sort()
        return ans

if __name__ == "__main__":
    n = 4
    accounts = [
        ["John","johnsmith@mail.com","john_newyork@mail.com"],
        ["John","johnsmith@mail.com","john00@mail.com"],
        ["Mary","mary@mail.com"],
        ["John","johnnybravo@mail.com"]
    ]

    # Creating instance of Solution class
    sol = Solution()
    
    # Function call to merge the accounts
    ans = sol.accountsMerge(accounts)
    
    # Output
    print("The merged accounts are:")
    for account in ans:
        print(" ".join(account))

Complexity Analysis:
Time Complexity: O(N+E) + O(E*4ɑ) + O(N*(ElogE + E)) (where E = no. of emails)
Visiting all the emails takes O(N+E) time.
In the worst case, all the accounts can be merged taking O(E*4ɑ) time.
All the emails to the result list and Sorting the emails take O(N*(ElogE + E)) times.
Space Complexity: O(N+E)

The hashmap will store all the emails taking O(E) space.
The disjoint set data structure uses parent and size/rank arrays taking O(N) space.
The resulting list will take up O(E) space.

'''
class DisjointSet:
    def __init__(self, n):
        self.rank = [0] * (n + 1)
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)
    
    # Function to find ultimate parent
    def findUPar(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.findUPar(self.parent[node])
        return self.parent[node]
    
    # Function to implement union by rank
    def unionByRank(self, u, v):
        ulp_u = self.findUPar(u)
        ulp_v = self.findUPar(v)
        if ulp_u == ulp_v: return
        if self.rank[ulp_u] < self.rank[ulp_v]:
            self.parent[ulp_u] = ulp_v
        elif self.rank[ulp_v] < self.rank[ulp_u]:
            self.parent[ulp_v] = ulp_u
        else:
            self.parent[ulp_v] = ulp_u
            self.rank[ulp_u] += 1

class Solution:
    def accountsMerge(self, accounts):
        n=len(accounts)
        ds=DisjointSet(n)
        mapMailNode={}
        for i in range(n):
            for j in range(1, len(accounts[i])):
                mail = accounts[i][j]
                if mail not in mapMailNode:
                    mapMailNode[mail] = i
                else:
                    ds.unionByRank(i, mapMailNode[mail])
        mergedMail = [[] for _ in range(n)]
        for mail, node in mapMailNode.items():
            root = ds.findUPar(node)
            mergedMail[root].append(mail)
        ans =[]
        for i in range(n):
            if not mergedMail[i]:
                continue
            mergedMail[i].sort()
            temp = [accounts[i][0]] + mergedMail[i]
            ans.append(temp)
        ans.sort()
        return ans