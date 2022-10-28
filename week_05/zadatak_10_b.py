class Node:
    def __init__(self, name, avg_salary):
        self.value = {"name":"eris", "avg_salary":"20000"}
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root):
        self.root(Node.root)

    # A)
    def _insert(self, data, current_node):
        if data.value["avg_salary"] < current_node.value["avg_salary"]:
            if current_node.left is None:
                current_node.left = Node(data)
            else:
                self._insert(data, current_node.left)
        elif data.value["avg_salary"] > current_node.value["avg_salary"]:
            if current_node.right is None:
                current_node.right = Node(data)
            else:
                self._insert(data, current_node.right)
        else:
            print("The value is already in a tree")

    # B)

    def search_max(self, data, current_node, max_sal,  l=[]):
        current_node = self.root
        if current_node.right > max_sal:
            return current_node.data.value["name"]
        else:
            self.max_salary(data, current_node.right)



    # C)
    def max_salary(self, data, current_node):
        current_node = self.root
        if current_node.right is None:
            return current_node.data.value["name"]
        else:
            self.max_salary(data, current_node.right)


singer1 = Node("Michael", "20000")
singer2 = Node("Kelly", "42000")
singer3 = Node("John", "33000")
singer4 = Node("Jhoe", "11000")











