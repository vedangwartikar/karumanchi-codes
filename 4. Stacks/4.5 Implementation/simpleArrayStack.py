# Simple Array Implementation using fixed limit array
class Stack(object):
    def __init__(self, limit = 10):
        self.stack = []
        self.limit = limit

    def isEmpty(self):
        return len(self.stack) <= 0

    def isFull(self):
        return len(self.stack) >= self.limit

    def push(self, item):
        if len(self.stack) >= self.limit:
            print('Stack Overflow!')
        else:
            self.stack.append(item)
        print('Stack after push: ', self.stack)
    
    def pop(self):
        if len(self.stack) <= 0:
            print('Stack Underflow!')
            return 0
        else:
            return self.stack.pop()
    
    def top(self):
        if len(self.stack) <= 0:
            print('Stack Underflow!')
            return 0
        else:
            return self.stack[-1]
        
    def size(self):
        return len(self.stack)

our_stack = Stack(5)
our_stack.push(10)
our_stack.push(20)
our_stack.push(30)
print(our_stack.pop())
print(our_stack.top())
print(our_stack.size())

#Time Complexity for all operations: O(1)