'''
There are n cities numbered from 0 to n-1. Given the array edges where edges[i] = [fromi, toi,weighti] represents a bidirectional and weighted edge between cities fromi and toi, and given the integer distance Threshold. Find out a city with the smallest number of cities that are reachable through some path and whose distance is at most Threshold Distance.



If there are multiple such cities, our answer will be the city with the greatest number.


Examples:


Input : N=4, M=4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4



Output: 3



Explanation: 

The adjacent cities for each city at a distanceThreshold are =

City 0 →[City 1, City 2]

City 1 →[City 0, City 2, City 3]

City 2 →[City 0, City 1, City 3]

City 3 →[City 1, City 2]

Here, City 0 and City 3 have a minimum number of cities 

i.e. 2 within distanceThreshold. So, the result will be the 

city with the largest number. So, the answer is City 3.



Input : N=3, M=2, edges = [[0,1,1],[0,2,3]], distanceThreshold = 2



Output: 2



Explanation: 

City 0 -> City 1,

City 1 → City 0,

City 2 → no City

Hence, 2 is the answer.

Input: N = 3, M = 3, edges = [[0,1,2],[1,2,1],[0,2,4]], distanceThreshold = 2

Output:
2
1
3
4

Submit
Constraints:
1 ≤ n ≤ 100
1 <= m <= n*(n-1)/2
length(edges[i]) == 3
0 <= fromi < toi < n
1 <= weighti , distanceThreshold <= 104
All pairs (fromi, toi) are distinct

Intuition:
To find out which city is having the smallest number of cities that are reachable with at most Threshold distance, we firstly need to find the distance betweeen every two pair of nodes(cities) possible then it can be compared with the threshold distance to get the answer.

In order to find the distance between every two pair of nodes, the Floyd Warshall Algorithm can be used. Once the 2D distance matrix(that contains the shortest paths) is generated, for each node(city), we can count the number of nodes(cities) that can be reached with a distance lesser or equal to the Threshold distance.

Approach:
Represent the cities and the bidirectional weighted edges using an adjacency matrix. Initialize all distances to a large value (infinity) except for the direct edges between cities.
Apply the Floyd-Warshall algorithm to compute the shortest paths between all pairs of cities. This algorithm iteratively updates the distance between any two cities through an intermediate city if it offers a shorter path.
For each city, count the number of cities that are reachable within the given distance threshold.
Identify the city with the smallest number of reachable cities within the threshold. If multiple cities have the same number of reachable cities, choose the city with the greater index.

class Solution:
    
    # Function to find the city with 
    # the smallest number of neighbors.
    def findCity(self, n, m, edges, distanceThreshold):
        
        # Adjacency matrix to store the graph
        adjMat = [[1e9] * n for _ in range(n)]
        
        # Filling up the adjacency matrix
        for it in edges:
            adjMat[it[0]][it[1]] = it[2]
            adjMat[it[1]][it[0]] = it[2]
        
        # Applying Floyd Warshall Algorithm
        
        # For intermediate node k
        for k in range(n):
            
            # node i ---> node j
            for i in range(n):
                for j in range(n):
                    adjMat[i][j] = min(adjMat[i][j], adjMat[i][k] + adjMat[k][j])
        
        # To store the minimum count of neighbors 
        minCount = int(1e9)
        
        # To store the answer (city having 
        # smallest number of neighbors)
        ans = -1
        
        # Check every city
        for i in range(n):
            
            # To count the neighbors of given city 
            # having distance lesser than threshold
            count = 0

            # City i ---> City j
            for j in range(n):
                
                # If the distance to reach city j from 
                # city i is less than threshold
                if i != j and adjMat[i][j] <= distanceThreshold:
                    
                    # Increment count
                    count += 1
            
            # if current count is less than minimum count
            if count < minCount:
                
                # Update minimum count
                minCount = count
                
                # Store the answer
                ans = i
            
            # Else if current count is 
            # equal to minimum count
            elif count == minCount:
                
                # Update the answer (to store 
                # city with greater number)
                ans = i
        
        # Return the resulting city as answer
        return ans

# Main function to test the solution
if __name__ == "__main__":
    N, M = 4, 4
    edges = [
        [0, 1, 3], [1, 2, 1],
        [1, 3, 4], [2, 3, 1]
    ]
    distanceThreshold = 4
    
    # Creating an instance of 
    # Solution class
    sol = Solution()
    
    # Function to find the city with 
    # the smallest number of neighbors.
    ans = sol.findCity(N, M, edges, distanceThreshold)
    
    # Output
    print("The city with smallest number of neighbors (with given threshold) is:", ans)

Complexity Analysis:
Time Complexity: O(N3) (where N is the number of nodes(cities) in graph)
The Floyd Warshall algorithm takes O(N3) time to compute shortest distance between every pair of nodes.
Finding the city having smallest number of neighbors takes O(N2) time.
Space Complexity: O(N2)
The only space used is for the distance matrix taking O(N2) space and for a couple of variables taking O(1) space.

'''
class Solution:
    def findCity(self, n, m, edges, distanceThreshold):
        adjMat = [[1e9] * n for _ in range(n)]
        for it in edges:
            adjMat[it[0]][it[1]] = it[2]
            adjMat[it[1]][it[0]] = it[2]
        
        # Applying Floyd Warshall Algorithm
        
        # For intermediate node k
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    adjMat[i][j] = min(adjMat[i][j], adjMat[i][k] + adjMat[k][j])
        minCount = int(1e9)
        ans = -1
        for i in range(n):
            count = 0
            for j in range(n):
                if i != j and adjMat[i][j] <= distanceThreshold:
                    count += 1
            if count < minCount:
                minCount = count
                ans = i
            elif count == minCount:
                ans = i
        return ans
