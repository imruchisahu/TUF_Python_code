class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

if __name__ == "__main__":
    arr = [2, 5, 8, 7]

    """ 
    Assigning values to 
    the nodes 
    """
    y1 = Node(arr[0], None)
    y2 = Node(arr[1], None)
    y3 = Node(arr[2], None)
    y4 = Node(arr[3], None)

    """ 
    Linking of 
    Nodes 
    """
    y1.next = y2
    y2.next = y3
    y3.next = y4

    """ 
    Printing Nodes with their 
    values and data 
    """
    print(f"{y1.data} {y1.next}")
    print(f"{y2.data} {y2.next}")
    print(f"{y3.data} {y3.next}")
    print(f"{y4.data} {y4.next}")
