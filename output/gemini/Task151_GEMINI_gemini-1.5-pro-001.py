class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert(self.root, data)

    def _insert(self, node, data):
        if node is None:
            return Node(data)
        if data < node.data:
            node.left = self._insert(node.left, data)
        elif data > node.data:
            node.right = self._insert(node.right, data)
        return node

    def delete(self, data):
        self.root = self._delete(self.root, data)

    def _delete(self, node, data):
        if node is None:
            return node
        if data < node.data:
            node.left = self._delete(node.left, data)
        elif data > node.data:
            node.right = self._delete(node.right, data)
        else:
            if node.left is None:
                temp = node.right
                del node
                return temp
            elif node.right is None:
                temp = node.left
                del node
                return temp
            temp = self.minValue(node.right)
            node.data = temp
            node.right = self._delete(node.right, temp)
        return node

    def minValue(self, node):
        minv = node.data
        while node.left is not None:
            minv = node.left.data
            node = node.left
        return minv

    def search(self, data):
        return self._search(self.root, data)

    def _search(self, node, data):
        if node is None:
            return False
        if data == node.data:
            return True
        if data < node.data:
            return self._search(node.left, data)
        return self._search(node.right, data)

    def levelOrderTraversal(self):
        if self.root is None:
            return
        queue = []
        queue.append(self.root)
        while len(queue) > 0:
            node = queue.pop(0)
            print(node.data, end=" ")
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

    def printTree(self):
        print("Level Order Traversal: ")
        self.levelOrderTraversal()
        print()


if __name__ == "__main__":
    tree = BinarySearchTree()
    tree.insert(50)
    tree.insert(30)
    tree.insert(20)
    tree.insert(40)
    tree.insert(70)
    tree.insert(60)
    tree.insert(80)
    tree.printTree()

    print("Search for 40: ", tree.search(40))
    print("Search for 100: ", tree.search(100))

    print("Delete 20")
    tree.delete(20)
    tree.printTree()

    print("Delete 50")
    tree.delete(50)
    tree.printTree()