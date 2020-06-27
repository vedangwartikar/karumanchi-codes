class Node:
    def insertAtEnd(self, data):
        """
        def setData(self, data):
            self.data = data
    
        def setNext(self, next):
            self.next = next

        def getNext(self):
            return self.next
        """
        newNode = Node()
        newNode.setData(data)

        current = self.head

        while current.getNext() != None:
            current = current.getNext()

        current.setNext(newNode)
        self.length += 1