# ==================================
# Queue - First In First Out (FIFO)
# ==================================

from collections import deque


class Queue:
    def __init__(self):
        self.items = deque()
    
    # Enqueue 
    def enqueue(self, item):
        self.items.append(item)

    # Dequeue 
    def dequeue(self):
        if not self.is_empty():
            return self.items.popleft()
        else:
            return None
        
    # is empty 
    def is_empty(self):
        return len(self.items) == 0
    
    # Size 
    def size(self):
        return len(self.items)
    
    # Peek
    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return None
        
# Usage Example

def main():

    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    print(queue.items)
    print(queue.size())
    print("Queue peek element : : ", queue.peek())

    print(queue.dequeue())  # Output: 1

# Code does not execute when imported as a module, only when run directly
if __name__ == "__main__":
    main()