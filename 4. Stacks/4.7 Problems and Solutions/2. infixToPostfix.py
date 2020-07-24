# Convert infix to postfix.

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

def infixToPostfix(expression):
    prec = {}
    prec['*'] = 3
    prec['/'] = 3
    prec['+'] = 2
    prec['-'] = 2
    prec['('] = 1

    stack = Stack()
    postfixExpression = []
    tokenList = expression.split()
    for token in tokenList:
        if token.isalnum():
            postfixExpression.append(token)
        elif token == '(':
            stack.push(token)
        elif token == ')':
            topToken = stack.pop()
            while topToken != '(':
                postfixExpression.append(topToken)
                topToken = stack.pop()
        else:
            while not stack.isEmpty() and prec[stack.top()] >= prec[token]:
                postfixExpression.append(stack.pop())
            stack.push(token)
    while not stack.isEmpty():
        postfixExpression.append(stack.pop())
    return ' '.join(postfixExpression)

exp = input("Infix expression: ")
print("Postfix expression: ", infixToPostfix(exp))