# Check if the symbols (brackets) in a string are balanced or not.

class Stack:
    def __init__(self):
        self.stack = []
    def isEmpty(self):
        return len(self.stack) <= 0
    def length(self):
        return len(self.stack)
    def push(self, data):
        self.stack.append(data)
    def pop(self):
        if len(self.stack) <= 0:
            return -1
        return self.stack.pop()
    def top(self):
        if len(self.stack) <= 0:
            return -1
        else:
            return self.stack[-1]

def matches(symbol, topSymbol):
    if symbol == ')':
        if topSymbol == '(':
            return True
        else:
            return False
    if symbol == ']':
        if topSymbol == '[':
            return True
        else:
            return False
    if symbol == '}':
        if topSymbol == '{':
            return True
        else:
            return False

def checkSymbolBalance(string):
    symbolStack = Stack()
    balanced = 0
    if not string:
        balanced = 1
    else:
        for symbol in string:
            if symbol in ['(', '[', '{']:
                symbolStack.push(symbol)
            else:
                if symbolStack.length == 0:
                    balanced = 0
                else:
                    topSymbol = symbolStack.pop()
                    if topSymbol == -1:
                        balanced = 0
                        break
                if not matches(symbol, topSymbol):
                    balanced = 0
                else:
                    balanced = 1
    return balanced

print('Balanced') if checkSymbolBalance(input()) else print('Unbalanced')