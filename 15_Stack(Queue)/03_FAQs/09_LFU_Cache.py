'''
Design and implement a data structure for a Least Frequently Used (LFU) cache.



Implement the LFUCache class with the following functions:



LFUCache(int capacity): Initialize the object with the specified capacity.

int get(int key): Retrieve the value of the key if it exists in the cache; otherwise, return -1.

void put(int key, int value): Update the value of the key if it is present in the cache, or insert the key if it is not already present. If the cache has reached its capacity, invalidate and remove the least frequently used key before inserting a new item. In case of a tie (i.e., two or more keys with the same frequency), invalidate the least recently used key.



A use counter is maintained for each key in the cache to determine the least frequently used key. The key with the smallest use counter is considered the least frequently used.



When a key is first inserted into the cache, its use counter is set to 1 due to the put operation. The use counter for a key in the cache is incremented whenever a get or put operation is called on it.



Ensure that the functions get and put run in O(1) average time complexity.


Examples:
Input:

["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]

[[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]

Output:

[null, null, null, 1, null, -1, 3, null, -1, 3, 4]

Explanation:

// cnt(x) = the use counter for key x

// cache=[] will show the last used order for tiebreakers (leftmost element is most recent)

LFUCache lfu = new LFUCache(2);

lfu.put(1, 1);  // cache=[1,_], cnt(1)=1

lfu.put(2, 2);  // cache=[2,1], cnt(2)=1, cnt(1)=1

lfu.get(1);   // return 1

         // cache=[1,2], cnt(2)=1, cnt(1)=2

lfu.put(3, 3);  // 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2.

         // cache=[3,1], cnt(3)=1, cnt(1)=2

lfu.get(2);   // return -1 (not found)

lfu.get(3);   // return 3

         // cache=[3,1], cnt(3)=2, cnt(1)=2

lfu.put(4, 4);  // Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.

         // cache=[4,3], cnt(4)=1, cnt(3)=2

lfu.get(1);   // return -1 (not found)

lfu.get(3);   // return 3

         // cache=[3,4], cnt(4)=1, cnt(3)=3

lfu.get(4);   // return 4

         // cache=[4,3], cnt(4)=2, cnt(3)=3

Input:

["LFUCache", "put", "put", "put", "put", "put", "get", "get", "get", "get", "get"]

[[3], [5, 7], [4, 6], [3, 5], [2, 4], [1, 3], [1], [2], [3], [4], [5]]

Output:

[null, null, null, null, null, null, 3, 4, 5, -1, -1]

Explanation:

// cnt(x) = the use counter for key x

// cache=[] will show the last used order for tiebreakers (leftmost element is most recent)

LFUCache lfu = new LFUCache(3);

lfu.put(5, 7);  // cache=[5], cnt(5)=1

lfu.put(4, 6);  // cache=[4,5], cnt(4)=1, cnt(5)=1

lfu.put(3, 5);  // cache=[3,4,5], cnt(3)=1, cnt(4)=1, cnt(5)=1

lfu.put(2, 4);  // 5 is the LFU key because cnt(5)=1 is the smallest, invalidate 5.

         // cache=[2,3,4], cnt(2)=1, cnt(3)=1, cnt(4)=1

lfu.put(1, 3);  // 4 is the LFU key because cnt(4)=1 is the smallest, invalidate 4.

         // cache=[1,2,3], cnt(1)=1, cnt(2)=1, cnt(3)=1

lfu.get(1);   // return 3

         // cache=[1,2,3], cnt(1)=2, cnt(2)=1, cnt(3)=1

lfu.get(2);   // return 4

         // cache=[2,1,3], cnt(1)=2, cnt(2)=2, cnt(3)=1

lfu.get(3);   // return 5

         // cache=[3,2,1], cnt(1)=2, cnt(2)=2, cnt(3)=2

lfu.get(4);   // return -1 (not found)

lfu.get(5);   // return -1 (not found)

Input:

["LFUCache", "put", "get", "put", "get", "get"]

[[1], [1, 10], [1], [2, 20], [1], [2]]

Output:
[null, null, 10, null, 20, 20]
[null, null, 10, null, -1, 20]
[null, null, 10, null, -1, -1]
[null, null, -1, null, 10, 20]

Submit
Constraints:
1 <= capacity <= 103
0 <= key <= 104
0 <= value <= 105
At most 105 calls will be made to get and put.

Intuition:
As the name suggests, the data items (key-value pairs) that are least frequently used will be removed from the cache memory. To mark the data items as recently used, a doubly linked list can be used. The most recently used data item will be placed in the front and the least recently used data item will be placed at the end of the doubly linked list.
Why using a Doubly Linked List?
Because doubly linked list data structure makes the insertion and deletion operation on data items in constant time while making sure the order of data items remains.

But in order to implement the get method for LFU cache, the searching operation will take linear time where each data-item needs to be checked. To improve the complexity of get method, a hashmap can be used to store the key and the address of node containing the key (if it exists).

Also, to store the frequencies of different data-items. A Hashmap can be used to store the lists of data-items based on their frequenices.
This way, the two methods can be implemented in constant time:
Get method: Using hashmap, it can be found whether a key exists in the doubly linked list. If it exists, the corresponding value can be returned using the address of node, otherwise, -1 can be returned.
Put method: If the key exists in the doubly linked list, its value can be updated. Otherwise, if the cache limit is reached, the least frequently used data-item can be removed and the current key-value pair can be inserted.
Approach:
The cache is initialized with a specified capacity. Dummy head and tail nodes are created for each list to simplify edge case handling.
Updating Frequency:
When a node is accessed or updated, it is removed from its current frequency list.
If this node was the only node with the minimum frequency, the minimum frequency is incremented.
The node's frequency is incremented, and it is added to the front of the list corresponding to the new frequency.
Both hash maps are updated to reflect these changes.
Get Operation:
Check if the key exists in the keyNode map.
If present, retrieve the node, update its frequency, and return its value. If not present, return -1.
Put Operation:
Check if the key already exists in the keyNode map.
If present, update the node's value, update its frequency, and return. If not present, check if the cache has reached its maximum capacity.
If at capacity, remove the least frequently used node (the node in the list with the minimum frequency and the least recent usage).
Create a new node for the key-value pair, set its frequency to 1, and add it to the front of the frequency list for nodes with frequency 1. Update both hash maps to reflect the addition of the new node.

# To implement a node in doubly linked 
# list that will store data items
class Node:
   def __init__(self, _key, _value):
       self.key = _key
       self.value = _value
       self.cnt = 1
       self.next = None
       self.prev = None

# To implement the doubly linked list
class List:
   def __init__(self):
       self.size = 0  # Size 
       self.head = Node(0, 0)  # Dummy head
       self.tail = Node(0, 0)  # Dummy tail
       self.head.next = self.tail
       self.tail.prev = self.head

   # Function to add node in front 
   def addFront(self, node):
       temp = self.head.next
       node.next = temp
       node.prev = self.head
       self.head.next = node
       temp.prev = node
       self.size += 1

   # Function to remove node from the list
   def removeNode(self, delnode):
       prevNode = delnode.prev
       nextNode = delnode.next
       prevNode.next = nextNode
       nextNode.prev = prevNode
       self.size -= 1

# Class to implement LFU cache
class LFUCache:
   def __init__(self, capacity):
       # Set the capacity
       self.maxSizeCache = capacity
       self.minFreq = 0  # Set minimum frequency
       self.curSize = 0  # Set current frequency
       
       # Hashmap to store the key-nodes pairs
       self.keyNode = {}  
       
       # Hashmap to maintain the lists 
       # having different frequencies
       self.freqListMap = {}

   # Method to update frequency of data-items
   def updateFreqListMap(self, node):
       # Remove from Hashmap
       del self.keyNode[node.key]
       
       # Update the frequency list hashmap
       self.freqListMap[node.cnt].removeNode(node)
       
       # If node was the last node having its frequency
       if (node.cnt == self.minFreq and 
           self.freqListMap[node.cnt].size == 0):
               
           # Update the minimum frequency
           self.minFreq += 1
       
       # Creating a dummy list for next higher frequency
       nextHigherFreqList = List()
       
       # If the next higher frequency list already exists
       if node.cnt + 1 in self.freqListMap:
           
           # Update pointer to already existing list
           nextHigherFreqList = self.freqListMap[node.cnt + 1]
       
       # Increment the count of data-item
       node.cnt += 1
       
       # Add the node in front of higher frequency list
       nextHigherFreqList.addFront(node)
       
       # Update the frequency list map
       self.freqListMap[node.cnt] = nextHigherFreqList
       self.keyNode[node.key] = node

   # Method to get the value of key from LFU cache
   def get(self, key):
       # Return the value if key exists
       if key in self.keyNode:
           node = self.keyNode[key]  # Get the node
           val = node.value  # Get the value
           self.updateFreqListMap(node)  # Update the frequency
           # Return the value
           return val
           
       # Return -1 if key is not found
       return -1

   def put(self, key, value):
       
       # If the size of Cache is 0, 
       # no data-items can be inserted
       if self.maxSizeCache == 0:
           return
       
       # If key already exists
       if key in self.keyNode:
           node = self.keyNode[key]  # Get the node
           node.value = value  # Update the value
           self.updateFreqListMap(node)  # Update the frequency
       else:
           # If cache limit is reached
           if self.curSize == self.maxSizeCache:
               # Remove the least frequently used data-item
               list = self.freqListMap[self.minFreq]
               del self.keyNode[list.tail.prev.key]
               # Update the frequency map
               self.freqListMap[self.minFreq].removeNode(list.tail.prev)
               self.curSize -= 1  # Decrement the current size of cache
           
           self.curSize += 1  # Increment the current cache size
           # Adding new value to the cache, 
           # set its frequency to 1
           self.minFreq = 1  
           
           # Create a dummy list
           listFreq = List()
           
           # If the list already exists
           if self.minFreq in self.freqListMap:
               
               # Update the pointer to already present list
               listFreq = self.freqListMap[self.minFreq]
           
           # Create the node to store data-item
           node = Node(key, value)
           
           # Add the node to dummy list
           listFreq.addFront(node)
           
           # Add the node to Hashmap
           self.keyNode[key] = node
           
           # Update the frequency list map
           self.freqListMap[self.minFreq] = listFreq

# LFU Cache
cache = LFUCache(2)

# Queries
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1), end=" ")
cache.put(3, 3)
print(cache.get(2), end=" ")
print(cache.get(3), end=" ")
cache.put(4, 4)
print(cache.get(1), end=" ")
print(cache.get(3), end=" ")
print(cache.get(4), end=" ")

Complexity Analysis:
Time Complexity: O(N) (where N is the number of queries on the LFU cache)
Each get and put method takes an average of constant time making the overall complexity as O(N).

Space Complexity: O(cap) (where cap is the capacity of LFU cache defined)
At maximum the cache can store the numbers of data-items equal to its capacity taking O(cap) space.

'''
class Node:
   def __init__(self, _key, _value):
       self.key = _key
       self.value = _value
       self.cnt = 1
       self.next = None
       self.prev = None

# To implement the doubly linked list
class List:
   def __init__(self):
       self.size = 0  # Size 
       self.head = Node(0, 0)  # Dummy head
       self.tail = Node(0, 0)  # Dummy tail
       self.head.next = self.tail
       self.tail.prev = self.head

   # Function to add node in front 
   def addFront(self, node):
       temp = self.head.next
       node.next = temp
       node.prev = self.head
       self.head.next = node
       temp.prev = node
       self.size += 1

   # Function to remove node from the list
   def removeNode(self, delnode):
       prevNode = delnode.prev
       nextNode = delnode.next
       prevNode.next = nextNode
       nextNode.prev = prevNode
       self.size -= 1

class LFUCache:
    def __init__(self, capacity):
      self.maxSizeCache = capacity
      self.minFreq = 0  # Set minimum frequency
      self.curSize = 0  # Set current frequency
      
      # Hashmap to store the key-nodes pairs
      self.keyNode = {}  
      
      # Hashmap to maintain the lists 
      # having different frequencies
      self.freqListMap = {}
    def updateFreqListMap(self, node):
       # Remove from Hashmap
      del self.keyNode[node.key]
      
      # Update the frequency list hashmap
      self.freqListMap[node.cnt].removeNode(node)
      
      # If node was the last node having its frequency
      if (node.cnt == self.minFreq and 
          self.freqListMap[node.cnt].size == 0):
              
          # Update the minimum frequency
          self.minFreq += 1
      
      # Creating a dummy list for next higher frequency
      nextHigherFreqList = List()
      
      # If the next higher frequency list already exists
      if node.cnt + 1 in self.freqListMap:
          
          # Update pointer to already existing list
          nextHigherFreqList = self.freqListMap[node.cnt + 1]
      
      # Increment the count of data-item
      node.cnt += 1
      
      # Add the node in front of higher frequency list
      nextHigherFreqList.addFront(node)
      
      # Update the frequency list map
      self.freqListMap[node.cnt] = nextHigherFreqList
      self.keyNode[node.key] = node

    def get(self, key):
      if key in self.keyNode:
          node = self.keyNode[key]  # Get the node
          val = node.value  # Get the value
          self.updateFreqListMap(node)  # Update the frequency
          # Return the value
          return val
      return -1
    
    def put(self, key, value):
      if self.maxSizeCache == 0:
          return
      
      # If key already exists
      if key in self.keyNode:
          node = self.keyNode[key]  # Get the node
          node.value = value  # Update the value
          self.updateFreqListMap(node)  # Update the frequency
      else:
          # If cache limit is reached
          if self.curSize == self.maxSizeCache:
              # Remove the least frequently used data-item
              list = self.freqListMap[self.minFreq]
              del self.keyNode[list.tail.prev.key]
              # Update the frequency map
              self.freqListMap[self.minFreq].removeNode(list.tail.prev)
              self.curSize -= 1  # Decrement the current size of cache
          
          self.curSize += 1  # Increment the current cache size
          # Adding new value to the cache, 
          # set its frequency to 1
          self.minFreq = 1  
          
          # Create a dummy list
          listFreq = List()
          
          # If the list already exists
          if self.minFreq in self.freqListMap:
              
              # Update the pointer to already present list
              listFreq = self.freqListMap[self.minFreq]
          
          # Create the node to store data-item
          node = Node(key, value)
          
          # Add the node to dummy list
          listFreq.addFront(node)
          
          # Add the node to Hashmap
          self.keyNode[key] = node
          
          # Update the frequency list map
          self.freqListMap[self.minFreq] = listFreq