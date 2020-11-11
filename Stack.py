class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None

class Stack:
    def __init__(self):
        self.top = None

    def stackPush(self, node):
        if(self.top is None):
            self.top = node
        else:
            node.nextNode = self.top
            self.top = node

    def stackPop(self):
        if(self.top is None):
            print("Stack Underflow")
        elif(self.top.nextNode is not None):
            self.top = self.top.nextNode
        else:
            self.top = None

    def showStack(self):
        if(self.top is None):
            print("Empty Stack")
        else:
            printNode = self.top
            print("[",end = " ")
            while(printNode is not None):
                print(printNode.data, end = " ")
                printNode = printNode.nextNode
            else:
                 print("]")

stack = Stack()
node1 = Node("1")
node2 = Node("2")
node3 = Node("3")

stack.stackPush(node1)
stack.stackPush(node2)
stack.stackPush(node3)

stack.showStack()
stack.stackPop()
stack.showStack()
stack.stackPop()
stack.showStack()
stack.stackPop()
stack.showStack()
            
