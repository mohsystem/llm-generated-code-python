from output.claude.Task151_CLAUDE_claude_3_5_sonnet_20240620 import *

class TestBinarySearchTree:
    def __init__(self):
        self.run_tests()

    def test_insert_and_search(self):
        bst = BinarySearchTree()
        bst.insert(10)
        bst.insert(20)
        bst.insert(5)
        assert bst.search(10) is True, "Failed Test Case 1: test_insert_and_search"
        assert bst.search(20) is True, "Failed Test Case 1: test_insert_and_search"
        assert bst.search(5) is True, "Failed Test Case 1: test_insert_and_search"
        assert bst.search(15) is False, "Failed Test Case 1: test_insert_and_search"

    def test_delete_leaf_node(self):
        bst = BinarySearchTree()
        bst.insert(10)
        bst.insert(5)
        bst.delete(5)
        assert bst.search(5) is False, "Failed Test Case 2: test_delete_leaf_node"

    def test_delete_node_with_one_child(self):
        bst = BinarySearchTree()
        bst.insert(10)
        bst.insert(5)
        bst.insert(7)
        bst.delete(5)
        assert bst.search(5) is False, "Failed Test Case 3: test_delete_node_with_one_child"
        assert bst.search(7) is True, "Failed Test Case 3: test_delete_node_with_one_child"

    def test_delete_node_with_two_children(self):
        bst = BinarySearchTree()
        bst.insert(10)
        bst.insert(5)
        bst.insert(15)
        bst.insert(12)
        bst.delete(15)
        assert bst.search(15) is False, "Failed Test Case 4: test_delete_node_with_two_children"
        assert bst.search(12) is True, "Failed Test Case 4: test_delete_node_with_two_children"

    def test_delete_root(self):
        bst = BinarySearchTree()
        bst.insert(10)
        bst.insert(5)
        bst.insert(15)
        bst.delete(10)
        assert bst.search(10) is False, "Failed Test Case 5: test_delete_root"
        assert bst.search(5) is True, "Failed Test Case 5: test_delete_root"
        assert bst.search(15) is True, "Failed Test Case 5: test_delete_root"

    def test_search_empty_tree(self):
        bst = BinarySearchTree()
        assert bst.search(10) is False, "Failed Test Case 6: test_search_empty_tree"

    def test_insert_multiple_nodes(self):
        bst = BinarySearchTree()
        bst.insert(10)
        bst.insert(5)
        bst.insert(15)
        bst.insert(7)
        bst.insert(12)
        assert bst.search(7) is True, "Failed Test Case 7: test_insert_multiple_nodes"
        assert bst.search(12) is True, "Failed Test Case 7: test_insert_multiple_nodes"

    def test_delete_node_with_no_children(self):
        bst = BinarySearchTree()
        bst.insert(10)
        bst.delete(10)
        assert bst.search(10) is False, "Failed Test Case 8: test_delete_node_with_no_children"

    def test_delete_node_with_left_child(self):
        bst = BinarySearchTree()
        bst.insert(10)
        bst.insert(5)
        bst.insert(3)
        bst.delete(5)
        assert bst.search(5) is False, "Failed Test Case 9: test_delete_node_with_left_child"
        assert bst.search(3) is True, "Failed Test Case 9: test_delete_node_with_left_child"

    def test_delete_node_with_right_child(self):
        bst = BinarySearchTree()
        bst.insert(10)
        bst.insert(15)
        bst.insert(20)
        bst.delete(15)
        assert bst.search(15) is False, "Failed Test Case 10: test_delete_node_with_right_child"
        assert bst.search(20) is True, "Failed Test Case 10: test_delete_node_with_right_child"

    def run_tests(self):
        self.test_insert_and_search()
        self.test_delete_leaf_node()
        self.test_delete_node_with_one_child()
        self.test_delete_node_with_two_children()
        self.test_delete_root()
        self.test_search_empty_tree()
        self.test_insert_multiple_nodes()
        self.test_delete_node_with_no_children()
        self.test_delete_node_with_left_child()
        self.test_delete_node_with_right_child()
        print("All test cases passed!")

def main():
    TestBinarySearchTree()

if __name__ == "__main__":
    main()
