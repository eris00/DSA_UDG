""" prebrojati cvorove u listi """

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:

    def __init__(self, root):
        self.root = Node(root)

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, current_node):
        if data < current_node.value:
            if current_node.left is None:
                current_node.left = Node(data)
            else:
                self._insert(data, current_node.left)
        elif data > current_node.value:

            if current_node.right is None:
                current_node.right = Node(data)
            else:
                self._insert(data, current_node.right)
        else:
            print("The value is already in a tree")

    def count_cvor(self, cvor):
        if cvor is None:
            return 0
        return 1 + self.count_cvor(cvor.left) + self.count_cvor(cvor.right)



stablo = BinaryTree(6)

stablo.insert(4)
stablo.insert(7)
stablo.insert(2)
stablo.insert(6)
stablo.insert(9)

stablo.count_cvor(stablo)