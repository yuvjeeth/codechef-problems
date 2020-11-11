class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None

class LinkedList:
    def __init__(self):
        self.head = None

    def addNode(self, node):
        if(self.head == None):
            self.head = node
        else:
            self.tail.nextNode = node
        self.tail = node

    def printList(self):
        printVal = self.head   
        while(printVal is not None):
            print(printVal.data)
            printVal = printVal.nextNode


node1 = Node("Yuvjeeth")
node2 = Node("Pushpalatha")
node3 = Node("Leyna / Liyush")

linkedList = LinkedList()
linkedList.addNode(node1)
linkedList.addNode(node2)
linkedList.addNode(node3)

linkedList.printList()
print("Linked Lists is working!")
