class Node:
    def listLength(self):
        """
        def getNext(self):
        return self.next
        """
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count

#Time Complexity: O(n), list of length n
#Space Complexity: O(1), temp variable count