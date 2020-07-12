class Stack:
    
    def __init__(self):
        self.stack = []
        
    def addToStack(self, data):
        if data not in self.stack:
            self.stack.append(data)
        else:
            return False
        
    def removeFromStack(self):
        if len(self.stack) <= 0:
            return ("The stack does not contain any elements")
        else:
            return self.stack.pop()
        
    #Function to look at the top of the stack
    def peek(self):
        return self.stack[-1]

Astack = Stack()
Astack.addToStack(3)
Astack.addToStack(9)
print(Astack.peek())
Astack.addToStack(6)
print(Astack.removeFromStack())
Astack.addToStack(30)
Astack.addToStack(2)
print(Astack.peek())
