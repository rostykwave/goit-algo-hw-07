class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
            return
        
        current = self.root
        while True:
            if key < current.val:
                if current.left is None:
                    current.left = Node(key)
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = Node(key)
                    return
                current = current.right
    
    def find_max(self):
        if self.root is None:
            return None
        
        current = self.root
        while current.right:
            current = current.right
        
        return current.val
    
    def find_min(self):
        if self.root is None:
            return None
        
        current = self.root
        while current.left:
            current = current.left
        
        return current.val
    
    def sum_values(self):
        def _sum_recursive(node):
            if node is None:
                return 0
            return node.val + _sum_recursive(node.left) + _sum_recursive(node.right)
        
        return _sum_recursive(self.root)
    
    def inorder_traversal(self):
        result = []
        def _inorder(node):
            if node:
                _inorder(node.left)
                result.append(node.val)
                _inorder(node.right)
        
        _inorder(self.root)
        return result
