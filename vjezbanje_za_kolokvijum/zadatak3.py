""" prebrojati cvorove koji su veci od neke zadate vrijednosti """

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

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(self.root, "")
        elif traversal_type == "inorder":
            return self.inorder_print(self.root, "")
        elif traversal_type == "postorder":
            return self.postorder_print(self.root, "")
        elif traversal_type == "levelorder":
            return self.levelorder_print(self.root, "")
        else:
            return "Invalid traversal type!"

    def preorder_print(self, start, traversal):
        # parent -> left -> right
        if start:
            traversal += (str(start.value) + "->")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

        def _size(self, current):
            low = 4
            hig = 7
            if current is None:
                return 0
            else:
                while current > low and current < hig:
                    return self._size(current.left) + self._size(current.right) + 1

        def size(self):
            return self._size(self.root)


bin_tree = BinaryTree(6)

bin_tree.insert(3)
bin_tree.insert(7)
bin_tree.insert(2)
bin_tree.insert(5)
bin_tree.insert(9)

print(bin_tree.print_tree("preorder"))
bin_tree.size()