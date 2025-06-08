import pytest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from bst import BinarySearchTree

class TestTraversals:
    
    def setup_method(self):
        self.bst = BinarySearchTree()
        values = [5, 3, 7, 2, 4, 6, 8]
        for val in values:
            self.bst.insert(val)
    
    def test_inorder_traversal(self):
        result = self.bst.inorder()
        expected = [2, 3, 4, 5, 6, 7, 8]
        assert result == expected
    
    def test_preorder_traversal(self):
        result = self.bst.preorder()
        expected = [5, 3, 2, 4, 7, 6, 8]
        assert result == expected
    
    def test_postorder_traversal(self):
        result = self.bst.postorder()
        expected = [2, 4, 3, 6, 8, 7, 5]
        assert result == expected

class TestTreeProperties:
    
    def test_height_single_node(self):
        bst = BinarySearchTree()
        bst.insert(5)
        assert bst.height() == 1
    
    def test_height_balanced_tree(self):
        bst = BinarySearchTree()
        values = [5, 3, 7, 2, 4, 6, 8]
        for val in values:
            bst.insert(val)
        assert bst.height() == 3
    
    def test_size(self):
        bst = BinarySearchTree()
        values = [5, 3, 7, 2, 4]
        for val in values:
            bst.insert(val)
        assert bst.size() == 5