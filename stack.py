class Stack:
    def __init__(self):
        self.items = []

    def isEmty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmty():
            return self.items.pop()
        return None
    
    def peek(self):
        if not self.isEmty():
            return self.items[-1]
        return None
    
    def size(self):
        return len(self.items)
