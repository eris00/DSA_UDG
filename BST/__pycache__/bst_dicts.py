from queue import Queue

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = root

    # Funkcija za insert elementa u binarno stablo
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, current_node):
        if data["salary"] < current_node.value["salary"]:
            if current_node.left is None:
                current_node.left = Node(data)
            else:
                self._insert(data, current_node.left)
        elif data["salary"] > current_node.value["salary"]:
            if current_node.right is None:
                current_node.right = Node(data)
            else:
                self._insert(data, current_node.right)
        else:
            print('The value is already in tree')

    def print_tree(self, traversal):
        if traversal == "preorder":
            return self.preorder_print(self.root, "")
        elif traversal == "inorder":
            return self.inorder_print(self.root, "")
        
    def preorder_print(self, current, traversal=""):
        if current:
            traversal += str(current.value['fname']) + ': '
            # traversal += str(current.value['salary']) + ', '
            traversal = self.preorder_print(current.left, traversal)
            traversal = self.preorder_print(current.right, traversal)
        return traversal

    def inorder_print(self, start, traversal):
        # left -> parent -> right
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value['fname']) + '->')
            traversal = self.inorder_print(start.right, traversal)
        return traversal


    def highest_salary(self, current):
        while current.right:
            current = current.right
        return current.value['fname']

    # vraca sve usere koji imaju platu manju od definisanje
    def find(self, current, traversal, max_value=0, l=[]):
        if current:
            traversal = self.find(current.left, traversal, max_value, l)
            if current.value['salary'] < max_value:
                # print (current.value,end=' ')
                l.append(current.value['fname'])
            traversal = self.find(current.right, traversal, max_value, l)
        return traversal, l

    # Youngest user
    def find_youngest_user(self, current, traversal=""):
        if current:
            traversal += str(current.value['fname']) + ': '
            # traversal += str(current.value['salary']) + ', '
            traversal = self.preorder_print(current.left, traversal)
            traversal = self.preorder_print(current.right, traversal)
        return traversal

    # nadji usera po imenu
    def find_fname(self, current, traversal, name='', l=[]):
        if current:
            traversal = self.find_fname(current.left, traversal, name, l)
            if current.value['fname'] == name:
                # print (current.value,end=' ')
                l.append(current.value['fname'])
            traversal = self.find_fname(current.right, traversal, name, l)
        return traversal, l




user1 = Node({'fname':'Eris', 'age':22, 'position':'software engeneer', 'salary':92000})
user2 = Node({'fname':'Petar', 'age':21, 'position':'database developer', 'salary':75000})
user3 = Node({'fname':'Lazar', 'age':23, 'position':'web developer', 'salary':66500})
user4 = Node({'fname':'Milos', 'age':36, 'position':'data scientist', 'salary':112000})
user5 = Node({'fname':'Stevan', 'age':28, 'position':'ai developer', 'salary':97200})

users = BinaryTree(user1)

users.insert(user2.value)
users.insert(user3.value)
users.insert(user4.value)
users.insert(user5.value)

# print(users.print_tree("preorder"))
# print(users.highest_salary(users.root))
# print(users.find_fname(users.root, "", "Eris")[1])
# users.find_youngest_user()
print(users.print_tree("inorder"))