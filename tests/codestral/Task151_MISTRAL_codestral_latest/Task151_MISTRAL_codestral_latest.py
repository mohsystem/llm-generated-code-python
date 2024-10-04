from output.codestral.Task151_MISTRAL_codestral_latest import *

class TestBinarySearchTree:
    def __init__(self):
        self.run_tests()

    def test_insert_and_search(self):
        root = None
        root = insert(root, 50)
        root = insert(root, 30)
        root = insert(root, 70)
        root = insert(root, 20)
        root = insert(root, 40)
        root = insert(root, 60)
        root = insert(root, 80)
        assert search(root, 50) is not None, "Failed Test Case 1: test_insert_and_search"
        assert search(root, 30) is not None, "Failed Test Case 1: test_insert_and_search"
        assert search(root, 70) is not None, "Failed Test Case 1: test_insert_and_search"
        assert search(root, 20) is not None, "Failed Test Case 1: test_insert_and_search"
        assert search(root, 40) is not None, "Failed Test Case 1: test_insert_and_search"
        assert search(root, 60) is not None, "Failed Test Case 1: test_insert_and_search"
        assert search(root, 80) is not None, "Failed Test Case 1: test_insert_and_search"
        assert search(root, 90) is None, "Failed Test Case 1: test_insert_and_search"

    def test_delete_leaf_node(self):
        root = None
        root = insert(root, 50)
        root = insert(root, 30)
        root = insert(root, 20)
        root = deleteNode(root, 20)
        assert search(root, 20) is None, "Failed Test Case 2: test_delete_leaf_node"

    def test_delete_node_with_one_child(self):
        root = None
        root = insert(root, 50)
        root = insert(root, 30)
        root = insert(root, 20)
        root = insert(root, 25)
        root = deleteNode(root, 20)
        assert search(root, 20) is None, "Failed Test Case 3: test_delete_node_with_one_child"
        assert search(root, 25) is not None, "Failed Test Case 3: test_delete_node_with_one_child"

    def test_delete_node_with_two_children(self):
        root = None
        root = insert(root, 50)
        root = insert(root, 30)
        root = insert(root, 70)
        root = insert(root, 20)
        root = insert(root, 40)
        root = deleteNode(root, 30)
        assert search(root, 30) is None, "Failed Test Case 4: test_delete_node_with_two_children"
        assert search(root, 20) is not None, "Failed Test Case 4: test_delete_node_with_two_children"
        assert search(root, 40) is not None, "Failed Test Case 4: test_delete_node_with_two_children"

    def test_delete_root(self):
        root = None
        root = insert(root, 50)
        root = insert(root, 30)
        root = insert(root, 70)
        root = deleteNode(root, 50)
        assert search(root, 50) is None, "Failed Test Case 5: test_delete_root"
        assert search(root, 30) is not None, "Failed Test Case 5: test_delete_root"
        assert search(root, 70) is not None, "Failed Test Case 5: test_delete_root"

    def test_search_empty_tree(self):
        root = None
        assert search(root, 10) is None, "Failed Test Case 6: test_search_empty_tree"

    def test_insert_multiple_nodes(self):
        root = None
        root = insert(root, 50)
        root = insert(root, 30)
        root = insert(root, 70)
        root = insert(root, 20)
        root = insert(root, 40)
        root = insert(root, 60)
        root = insert(root, 80)
        assert search(root, 20) is not None, "Failed Test Case 7: test_insert_multiple_nodes"
        assert search(root, 40) is not None, "Failed Test Case 7: test_insert_multiple_nodes"
        assert search(root, 60) is not None, "Failed Test Case 7: test_insert_multiple_nodes"
        assert search(root, 80) is not None, "Failed Test Case 7: test_insert_multiple_nodes"

    def test_delete_node_with_no_children(self):
        root = None
        root = insert(root, 50)
        root = deleteNode(root, 50)
        assert search(root, 50) is None, "Failed Test Case 8: test_delete_node_with_no_children"

    def test_delete_node_with_left_child(self):
        root = None
        root = insert(root, 50)
        root = insert(root, 30)
        root = insert(root, 20)
        root = deleteNode(root, 30)
        assert search(root, 30) is None, "Failed Test Case 9: test_delete_node_with_left_child"
        assert search(root, 20) is not None, "Failed Test Case 9: test_delete_node_with_left_child"

    def test_delete_node_with_right_child(self):
        root = None
        root = insert(root, 50)
        root = insert(root, 70)
        root = insert(root, 60)
        root = deleteNode(root, 70)
        assert search(root, 70) is None, "Failed Test Case 10: test_delete_node_with_right_child"
        assert search(root, 60) is not None, "Failed Test Case 10: test_delete_node_with_right_child"

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