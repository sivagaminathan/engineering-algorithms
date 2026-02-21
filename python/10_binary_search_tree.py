class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    # INSERT 
    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if not node:
            return TreeNode(value)
        
        if value <= node.value:
            node.left = self._insert(node.left, value)
        else:
            node.right = self._insert(node.right, value)
        return node
    
    # SEARCH 
    def search(self, value):
        return self._search(self.root, value)

    def _search(self, node, value):
        if not node:
            return False
        if node.value == value:
            return True
        elif value > node.value:
            return self._search(node.right, value)
        else:
            return self._search(node.left, value)
        
    # DELETE 
    def delete(self, value):
        self.root = self._delete(self.root, value)

    def _delete(self, node, value):
        if not node: 
            return node
        
        if value < node.value:
            node.left = self._delete(node.left, value)

        elif value > node.value:
            node.right = self._delete(node.right, value)

        else: 
            # Case 1 - No child
            if not node.left and not node.right:
                return None
            
            # Case 2 - One child 
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            
            # Case 3 - Two children 
            temp = self._min_value_node(node.right)
            node.value = temp.value 
            node.right = self._delete(node.right, temp.value)

        return node
    
    def _min_value_node(self, node):
        while node.left:
            node = node.left
        return node
    
    # HEIGHT 
    def height(self, node):
        if not node:
            return -1
        return 1 + max(self.height(node.left), self.height(node.right))
    
    # MIRROR 
    def mirror(self, node):
        if node is None:
            return None
        
        right_mirror = self.mirror(node.right)
        left_mirror = self.mirror(node.left)
        
        node.left = right_mirror
        node.right = left_mirror
        return node

    # TRAVERSALS 

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.value, end=" ")
            self.inorder(node.right)

    def preorder(self, node):
        if node:
            print(node.value, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)
        
    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.value, end=" ")

def main():

    bst = BinarySearchTree()
    values = [5, 3, 7, 2, 4, 6, 8]
    for value in values:
        bst.insert(value)

    print("Inorder Traversal: ", end="")
    bst.inorder(bst.root)  # Output: 2 3 4 5 6 7 8

    print("\nPreorder Traversal: ", end="")
    bst.preorder(bst.root)  # Output: 5 3 2 4 7 6 8 

    print("\nPostorder Traversal: ", end="")
    bst.postorder(bst.root)  # Output: 2 4 3 6 8 7 5    

    print("\nSearch for 4: ", bst.search(4))  # Output: True
    print("\nSearch for 10: ", bst.search(10))  # Output: False

    print("\nHeight of BST: ", bst.height(bst.root))  # Output: 2
    
    bst.delete(3)
    print("\nInorder Traversal after deleting 3: ", end="")
    bst.inorder(bst.root)  # Output: 2 4 5 6 7 8

    bst.mirror(bst.root)
    print("\nInorder Traversal of Mirrored BST: ", end="")
    bst.inorder(bst.root)  # Output: 8 7 6 5 4 2
    

if __name__ == "__main__":
    main()
