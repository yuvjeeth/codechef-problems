class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, node):
        if(self.rear is None):
            self.rear = node
            self.front = node
        else:
            self.rear.nextNode = node
            self.rear = self.rear.nextNode
            

    def dequeue(self):
        if(self.front is None):
            print("Queue Empty")
        elif(self.rear == self.front):
            self.rear = None
            self.front = None
        else:
            self.front = self.front.nextNode

    def showQueue(self):
        if(self.front is None):
            print("Queue Empty")
        else:
            printNode = self.front
            print("[",end = " ")
            while(printNode is not None):
                print(printNode.data, end = " ")
                printNode = printNode.nextNode
            else:
                print("]")

queue = Queue()
node1 = Node("1")
node2 = Node("2")
node3 = Node("3")
node4 = Node("4")

queue.enqueue(node1)
queue.enqueue(node2)
queue.enqueue(node3)

queue.showQueue()

queue.dequeue()

queue.showQueue()

queue.enqueue(node4)
queue.showQueue()



            
            
