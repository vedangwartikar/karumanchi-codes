class Node:
    """
    def setData(self, data):
        self.data = data
    def setNext(self, next):
        self.next = next
    """
    def insertAtBeginning(self, data):
        newNode = Node()
        newNode.setData(data)
        if self.length == 0:
            self.head = newNode
        else:
            newNode.setNext(self.head)
            self.head = newNode
        self.length += 1