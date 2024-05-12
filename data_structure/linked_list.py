"""Create a linked list"""

class Node():
    def __init__(self, inputdata) -> None:
        self.data = inputdata
        self.next = None

class Linkedlist:
    def __init__(self) -> None:
        self.head = None
        self.size = 0

    # Add a node to the beginning of the linked list.
    def addNode(self, inputData):
        newNode = Node(inputData) # create a node
        newNode.next = self.head
        self.head = newNode
        self.size += 1

    # Find a node which contains the data matching the value
    def findNode(self, value):
        curr = self.head
        while curr:
            if curr.data == value:
                return curr
            curr = curr.next

        return curr
    
    def printNode(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next

myList = Linkedlist()


for i in range(5):
    myList.addNode(i * 2)

myList.printNode()