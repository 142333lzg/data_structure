class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, element):
        self.stack.append(element)
    
    def pop(self):
        self.stack.pop()
        
    def get_top(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None
        
    def is_empty(self):
        return len(self.stack) == 0

