import pytest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from bst import BinarySearchTree

class TestBasicOperations:
    
    def test_insert_single_node(self):
        bst = BinarySearchTree()
        bst.insert(5)
        assert bst.root is not None
        assert bst.root.val == 5
    
    def test_insert_multiple_nodes(self):
        bst = BinarySearchTree()
        values = [5, 3, 7, 2, 4, 6, 8]
        for val in values:
            bst.insert(val)
        
        # Check structure
        assert bst.root.val == 5
        assert bst.root.left.val == 3
        assert bst.root.right.val == 7
    
    def test_search_existing(self):
        bst = BinarySearchTree()
        values = [5, 3, 7, 2, 4]
        for val in values:
            bst.insert(val)
        
        assert bst.search(3) == True
        assert bst.search(7) == True
        assert bst.search(2) == True
    
    def test_search_non_existing(self):
        bst = BinarySearchTree()
        values = [5, 3, 7]
        for val in values:
            bst.insert(val)
        
        assert bst.search(10) == False
        assert bst.search(1) == False