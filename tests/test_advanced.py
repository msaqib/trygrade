import pytest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from bst import BinarySearchTree

class TestDeletion:
    
    def test_delete_leaf_node(self):
        bst = BinarySearchTree()
        values = [5, 3, 7, 2, 4]
        for val in values:
            bst.insert(val)
        
        bst.delete(2)
        assert bst.search(2) == False
        assert bst.inorder() == [3, 4, 5, 7]
    
    def test_delete_node_with_one_child(self):
        bst = BinarySearchTree()
        values = [5, 3, 7, 8]
        for val in values:
            bst.insert(val)
        
        bst.delete(7)
        assert bst.search(7) == False
        assert bst.inorder() == [3, 5, 8]
    
    def test_delete_node_with_two_children(self):
        bst = BinarySearchTree()
        values = [5, 3, 7, 2, 4, 6, 8]
        for val in values:
            bst.insert(val)
        
        bst.delete(3)
        assert bst.search(3) == False
        # Should still maintain BST property
        result = bst.inorder()
        assert result == sorted(result)

class TestValidation:
    
    def test_valid_bst(self):
        bst = BinarySearchTree()
        values = [5, 3, 7, 2, 4, 6, 8]
        for val in values:
            bst.insert(val)
        
        assert bst.is_valid_bst() == True
    
    def test_empty_tree_valid(self):
        bst = BinarySearchTree()
        assert bst.is_valid_bst() == True