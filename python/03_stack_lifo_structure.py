# ====================================
# Stack (Last In, First Out) Structure
# Implemented using a list in Python
# ====================================

from symtable import Class


class Stack:
    def __init__(self):
        self.items = []

    # push (Add) an element 
    def push(self, item):
        self.items.append(item)

    # pop (Remove) the last element
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None
        
    # peek 
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    # is empty check
    def is_empty(self):
        return len(self.items) == 0
    
    # size of the stack 
    def size(self):
        return len(self.items)

# Usage Example 

stack = Stack()
stack.push(1)
stack.push(2)

print("Peek top element:", stack.peek())
print("Stack size:", stack.size())
print("Popped element:", stack.pop())
print("Is stack empty?", stack.is_empty())
print("Stack elements:", stack.items)