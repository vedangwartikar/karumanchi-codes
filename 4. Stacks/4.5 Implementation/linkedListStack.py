# Linked List Implementation of Stack
class Node:
    def __init__(self):
        self.data = None
        self.next = None
    
    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data
    
    def setNext(self, next):
        self.next = next

    def getNext(self):
        return self.next
    
    def hasNext(self):
        return self.next != None

class Stack(object):
    def __init__(self, data = None):
        self.head = None
        if data:
            for data in data:
                self.push(data)
    
    def push(self, data):
        temp = Node()
        temp.setData(data)
        temp.setNext(self.head)
        self.head = temp

    def pop(self):
        if self.head == None:
            raise IndexError
        temp = self.head.getData()
        self.head = self.head.getNext()
        return temp

    def top(self):
        if self.head == None:
            raise IndexError
        return self.head.getData()

our_list = ['first', 'second', 'third']
our_stack = Stack(our_list)
print(our_stack.pop())
print(our_stack.top())
our_stack.push('schwifty')
print(our_stack.top())

# Time Complexity for all but delete entire stack operation: O(1)
"""
Clearing the memory for each individual node of stack
will require O(n) time.
"""