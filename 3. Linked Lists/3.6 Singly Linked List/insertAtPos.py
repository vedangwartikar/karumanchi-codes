#Method for inserting a new node at any position in a Linked List
class Node:
    def insertAtPos(self, pos, data):
        if pos > self.length or pos < 0:
            return
        else:
            if pos == 0:
                self.insertAtBeginning(data)
            else:
                if pos == self.length:
                    self.insertAtEnd(data)
                else:
                    newNode = Node()
                    newNode.setData(data)
                    count = 0
                    current = self.head
                    while count < pos-1:
                        count += 1
                        current.setNext(current.getNext())
                newNode.setNext(current.getNext())
                current.setNext(newNode)
                self.length += 1

#Time Complexity: O(n), worst case insert at end
#Space Complexity: O(1), temp var count
                    
