'''
Given the root of a binary tree, the value of a target node target, and an integer k. Return an array of the values of all nodes that have a distance k from the target node.



The answer can be returned in any order (N represents null).



Note: Although input shows target as a value, internally it refers to the TreeNode with that value.


Examples:
Input : root = [3, 5, 1, 6, 2, 0, 8, N, N, 7, 4] , target = 5, k = 2

Output : [1, 4, 7]

Explanation : The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.



Input : root = [3, 5, 1, 6, 2, 0, 8, N, N, 7, 4] , target = 5, k = 3

Output : [0, 8]

Explanation : The nodes that are a distance 3 from the target node (with value 5) have values 0, 8.



Input : root =[1, 2, 3, 4, null, 5, 6], target = 6, k = 2

Output:
[1, 5]
Constraints:
1 <= Number of Nodes <= 103
-104 <= Node.val <= 104
All the values Node.val are unique.
target is the value of one of the nodes in the tree
0 <= k <= 103

Intuition
To tackle the problem of finding all nodes at a specific distance 'K' from a given node in a binary tree, we need to understand the spatial distribution of nodes around the target node. Nodes that are exactly 'K' steps away from the target node can be thought of as forming a concentric pattern around it, with each level of distance increasing by one step. To efficiently traverse the tree and find these nodes, access not only the direct child nodes but also the parent nodes. While child nodes can be accessed via pointers, the parent node access requires constructing a mapping from each node to its parent. This involves three main phases: constructing the parent-child relationships using a breadth-first search (BFS), identifying and storing the target node, and then performing a depth-first search (DFS) to explore nodes at the required distance 'K' from the target node.



Approach
Traverse the tree to create a mapping from each node to its parent.
Use a queue to perform a breadth-first search starting from the target node.
Explore neighbors of the current node in three directions: left child, right child, and parent.
Keep track of visited nodes to prevent revisiting and cycles.
Continue the search until reaching nodes at distance K, then collect and return their values.
from collections import deque, defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Solution:
    def distanceK(self, root, target, k):
        # Step 1: Create a map to store the parent of each node
        parent_map = {}
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node.left:
                parent_map[node.left] = node
                queue.append(node.left)
            if node.right:
                parent_map[node.right] = node
                queue.append(node.right)

        # Step 2: Use BFS to find all nodes at distance k from the target
        result = []
        visited = set()
        queue = deque([target])
        visited.add(target)
        current_distance = 0

        # Continue BFS until the desired distance is reached
        while queue:
            if current_distance == k:
                # Collect all nodes at distance k
                result.extend(node.data for node in queue)
                return result
            for _ in range(len(queue)):
                node = queue.popleft()
                # Check left child
                if node.left and node.left not in visited:
                    visited.add(node.left)
                    queue.append(node.left)
                # Check right child
                if node.right and node.right not in visited:
                    visited.add(node.right)
                    queue.append(node.right)
                # Check parent
                if node in parent_map and parent_map[node] not in visited:
                    visited.add(parent_map[node])
                    queue.append(parent_map[node])
            current_distance += 1

        return result

# Helper function to create a binary tree from a list
def create_tree(nodes, index=0):
    if index < len(nodes) and nodes[index] is not None:
        root = TreeNode(nodes[index])
        root.left = create_tree(nodes, 2 * index + 1)
        root.right = create_tree(nodes, 2 * index + 2)
        return root
    return None

def main():
    nodes = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    root = create_tree(nodes)
    target = root.left  # Node with value 5
    k = 2

    sol = Solution()
    result = sol.distanceK(root, target, k)

    print(f"Nodes at distance {k} from target node are: {result}")

if __name__ == "__main__":
    main()

Complexity Analysis
Time Complexity: Traversing the tree to create the parent hashmap requires visiting each node once (O(N)), exploring all nodes at a distance of 'K' in the worst case is O(N), and the logarithmic lookup time for the hashmap is O(log N). Therefore, the overall time complexity simplifies to O(N).

Space Complexity: The space complexity is determined by the data structures used: O(N) for the parent hashmap, O(N) for the DFS queue, and O(N) for the visited hashmap. Thus, the total space complexity is O(N).


'''
from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def distanceK(self, root, target, k):
        # Step 1: Create a map to store the parent of each node
        parent_map = {}
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node.left:
                parent_map[node.left] = node
                queue.append(node.left)
            if node.right:
                parent_map[node.right] = node
                queue.append(node.right)

        # Step 2: Use BFS to find all nodes at distance k from the target
        result = []
        visited = set()
        queue = deque([target])
        visited.add(target)
        current_distance = 0

        # Continue BFS until the desired distance is reached
        while queue:
            if current_distance == k:
                # Collect all nodes at distance k
                result.extend(node.data for node in queue)
                return result
            for _ in range(len(queue)):
                node = queue.popleft()
                # Check left child
                if node.left and node.left not in visited:
                    visited.add(node.left)
                    queue.append(node.left)
                # Check right child
                if node.right and node.right not in visited:
                    visited.add(node.right)
                    queue.append(node.right)
                # Check parent
                if node in parent_map and parent_map[node] not in visited:
                    visited.add(parent_map[node])
                    queue.append(parent_map[node])
            current_distance += 1

        return result