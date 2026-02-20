class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)

        # Empty linked list and new node becomes the head
        if not self.head: 
            self.head = new_node
            return
        
        # traverse to the end of the linked list and insert the new node
        current = self.head
        while current.next:
            current = current.next

        current.next = new_node
    
    def display(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        # Print None at the end of the linked list
        print("None")

    def delete(self, key):
        current = self.head
        if current and current.value == key:
            self.head = current.next
            return
        previous = None
        while current and current.value != key:
            previous = current
            current = current.next

        if current:
            previous.next = current.next

def main():
    linked_list = LinkedList()
    linked_list.insert(1)
    linked_list.insert(2)
    linked_list.insert(3)

    print("Linked List:")
    
    linked_list.insert(6)
    linked_list.display()
    
    linked_list.delete(2)
    linked_list.display()

if __name__ == "__main__":
    main()