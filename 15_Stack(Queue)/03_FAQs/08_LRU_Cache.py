'''
Design a data structure that follows the constraints of Least Recently Used (LRU) cache.



Implement the LRUCache class:



LRUCache(int capacity): We need to initialize the LRU cache with positive size capacity.

int get(int key): Returns the value of the key if the key exists, otherwise return -1.

void put(int key,int value): Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.



The functions get and put must each run in O(1) average time complexity.


Examples:
Input:

 ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]

 [ [2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4] ]

Output:

 [null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation:

LRUCache lRUCache = new LRUCache(2);

lRUCache.put(1, 1); // cache is {1=1}

lRUCache.put(2, 2); // cache is {1=1, 2=2}

lRUCache.get(1);  // return 1

lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}

lRUCache.get(2);  // returns -1 (not found)

lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}

lRUCache.get(1);  // return -1 (not found)

lRUCache.get(3);  // return 3

lRUCache.get(4);  // return 4

Input:

["LRUCache", "put", "put", "get", "put", "get", "put", "get"]

[[1], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [3]]

Output:

[null, null, null, -1, null, -1, null, -1]

Explanation:

LRUCache lRUCache = new LRUCache(1);

lRUCache.put(1, 1); // cache is {1=1}

lRUCache.put(2, 2); // evicts key 1, cache is {2=2}

lRUCache.get(1);  // returns -1 (not found)

lRUCache.put(3, 3); // evicts key 2, cache is {3=3}

lRUCache.get(2);  // returns -1 (not found)

lRUCache.put(4, 4); // evicts key 3, cache is {4=4}

lRUCache.get(3);  // returns -1 (not found)

Input:

["LRUCache", "put", "put", "get", "put", "put", "get", "get"]

[[2], [1, 1], [2, 2], [1], [3, 3], [4, 4], [2], [4]]

Output:
[null, null, null, 1, null, null, -1, 4]
[null, null, null, 1, null, null, 1, 4]
[null, null, null, 1, null, null, -1, -1]
[null, null, null, -1, null, null, -1, 4]

Submit
Constraints:
1 <= capacity <= 1000
0 <= key <= 104
0 <= value <= 105
At most 105 calls will be made to get and put.

Intuition:
As the name suggests, the data items (key-value pairs) that are least recently used will be staying in the cache memory. To mark the data items as recently used, a doubly linked list can be used. The most recently used data item will be placed in the front and the least recently used data item will be placed at the end of the doubly linked list.
Why using a Doubly Linked List?
Because doubly linked list data structure makes the insertion and deletion operation on data items in constant time while making sure the order of data items remains.

But in order to implement the get method for LRU cache, the searching operation will take linear time where each data-item needs to be checked. To improve the complexity of get method, a hashmap can be used to store the key and the address of node containing the key (if it exists).

This way, the two methods can be implemented in constant time:
Get method: Using hashmap, it can be found whether a key exists in the doubly linked list. If it exists, the corresponding value can be returned using the address of node, otherwise, -1 can be returned.
Put method: If the key exists in the doubly linked list, its value can be updated. Otherwise, the least recently used data-item can be removed and the current key-value pair can be inserted.
Approach:
The cache is initialized with a given capacity. Two dummy nodes, head and tail, are created to mark the start and end of cache. The head's next points to the tail, and the tail's previous points to the head.
Get operation:
Check if the key exists in the hash map.
If the key is present, retrieve the corresponding node, move it to the front (mark it as recently used), and return its value.
If the key is not present, return -1.
Put operation:
Check if the key already exists in the hash map.
If the key is present, update the node's value, move it to the front (mark it as recently used). If the key is not present, check if the cache has reached its capacity.
If at capacity, remove the least recently used node (node right before the tail) from both the hash map and the doubly linked list.
Insert the new key-value pair as a new node at the front (mark it as recently used) and add it to the hash map.
There are two helper functions:
DeleteNode: This function removes a given node from the doubly linked list by adjusting the pointers of its previous and next nodes.
InsertAfterHead: This function inserts a given node right after the head, marking it as the most recently used.

# Class to implement Nodes of a doubly linked list
class Node:
    def __init__(self, key=-1, val=-1):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

# Class implementing LRU cache
class LRUCache:

    def __init__(self, capacity):
        self.mpp = {} # Map data structure
        self.cap = capacity # Capacity
        self.head = Node() # Dummy head pointer
        self.tail = Node() # Dummy tail pointer

        # Make the connections
        self.head.next = self.tail
        self.tail.prev = self.head

    # Private method to delete node from doubly linked list
    def deleteNode(self, node):
        # Get the previous and next pointers
        prevNode = node.prev
        nextNode = node.next

        # Remove pointers to node
        prevNode.next = nextNode
        nextNode.prev = prevNode

    # Private method to insert node after head
    def insertAfterHead(self, node):
        nextNode = self.head.next
        self.head.next = node
        nextNode.prev = node
        node.prev = self.head
        node.next = nextNode

    # Method to get the key from cache
    def get(self, key_):
        # Return -1 if it is not present in cache
        if key_ not in self.mpp:
            return -1

        node = self.mpp[key_] # Get the node
        val = node.val # Get the value

        # Delete the node
        self.deleteNode(node)
        # Insert this node to front as it was recently used
        self.insertAfterHead(node)

        # Return the stored value
        return val

    # Method to update value if key exists, otherwise insert the key-value pair
    def put(self, key_, value):
        # Update the value if key is already present
        if key_ in self.mpp:
            node = self.mpp[key_] # Get the node
            node.val = value # Update the value

            # Delete the node
            self.deleteNode(node)
            # Insert this node to front as it was recently used
            self.insertAfterHead(node)

            return

        # Check if the capacity limit has reached
        if len(self.mpp) == self.cap:
            # Get the least recently used node
            node = self.tail.prev

            # Delete node from map
            del self.mpp[node.key]

            # Delete node from doubly linked list
            self.deleteNode(node)

        # Create a new node
        newNode = Node(key_, value)

        # Insert it in map
        self.mpp[key_] = newNode

        # Insert in doubly linked list
        self.insertAfterHead(newNode)


# LRU Cache
cache = LRUCache(2)

# Queries
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1), end=" ")
cache.put(3, 3)
print(cache.get(2), end=" ")
cache.put(4, 4)
print(cache.get(1), end=" ")
print(cache.get(3), end=" ")
print(cache.get(4), end=" ")

Complexity Analysis:
Time Complexity: O(N) (where N is the number of queries)
Since the Put and Get method takes an average of constant time, the overall complexity to process all the queries is O(N) time.

Space Complexity: O(cap) (where cap is the capacity of the LRU cache)
Since the doubly linked list can store at most of the capacity number of key-value pairs, this takes O(cap) space.

'''
# Class to implement Nodes of a doubly linked list
class Node:
    def __init__(self, key=-1, val=-1):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

# Class implementing LRU cache
class LRUCache:

    def __init__(self, capacity):
        self.mpp = {} # Map data structure
        self.cap = capacity # Capacity
        self.head = Node() # Dummy head pointer
        self.tail = Node() # Dummy tail pointer

        # Make the connections
        self.head.next = self.tail
        self.tail.prev = self.head

    # Private method to delete node from doubly linked list
    def deleteNode(self, node):
        # Get the previous and next pointers
        prevNode = node.prev
        nextNode = node.next

        # Remove pointers to node
        prevNode.next = nextNode
        nextNode.prev = prevNode

    # Private method to insert node after head
    def insertAfterHead(self, node):
        nextNode = self.head.next
        self.head.next = node
        nextNode.prev = node
        node.prev = self.head
        node.next = nextNode

    # Method to get the key from cache
    def get(self, key_):
        # Return -1 if it is not present in cache
        if key_ not in self.mpp:
            return -1

        node = self.mpp[key_] # Get the node
        val = node.val # Get the value

        # Delete the node
        self.deleteNode(node)
        # Insert this node to front as it was recently used
        self.insertAfterHead(node)

        # Return the stored value
        return val

    # Method to update value if key exists, otherwise insert the key-value pair
    def put(self, key_, value):
        # Update the value if key is already present
        if key_ in self.mpp:
            node = self.mpp[key_] # Get the node
            node.val = value # Update the value

            # Delete the node
            self.deleteNode(node)
            # Insert this node to front as it was recently used
            self.insertAfterHead(node)

            return

        # Check if the capacity limit has reached
        if len(self.mpp) == self.cap:
            # Get the least recently used node
            node = self.tail.prev

            # Delete node from map
            del self.mpp[node.key]

            # Delete node from doubly linked list
            self.deleteNode(node)

        # Create a new node
        newNode = Node(key_, value)

        # Insert it in map
        self.mpp[key_] = newNode

        # Insert in doubly linked list
        self.insertAfterHead(newNode)


