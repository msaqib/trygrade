class TreeNode:
    """Node class for Binary Search Tree"""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinarySearchTree:
    """Binary Search Tree implementation"""
    
    def __init__(self):
        self.root = None
    
    # Task 1: Insert operation
    def insert(self, val):
        """Insert a value into the BST"""
        # TODO: Implement insertion
        pass
    
    # Task 2: Search operation
    def search(self, val):
        """Search for a value in the BST"""
        # TODO: Implement search
        pass
    
    # Task 3: Traversals
    def inorder(self):
        """Return inorder traversal as list"""
        # TODO: Implement inorder traversal
        pass
    
    def preorder(self):
        """Return preorder traversal as list"""
        # TODO: Implement preorder traversal
        pass
    
    def postorder(self):
        """Return postorder traversal as list"""
        # TODO: Implement postorder traversal
        pass
    
    # Task 4: Delete operation
    def delete(self, val):
        """Delete a value from the BST"""
        # TODO: Implement deletion
        pass
    
    # Task 5: Tree properties
    def height(self):
        """Return height of the tree"""
        # TODO: Implement height calculation
        pass
    
    def size(self):
        """Return number of nodes in tree"""
        # TODO: Implement size calculation
        pass
    
    # Task 6: Validation
    def is_valid_bst(self):
        """Check if tree maintains BST property"""
        # TODO: Implement BST validation
        return True