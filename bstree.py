class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None
    
    # insert into a binary search tree
    def insert(self, insert_node):
        # check if insert_node is not null
        if insert_node:
            # check if insert_node is larger than root
            if self.value >= insert_node:
                if self.left:
                    self.left.insert(insert_node)
                else:
                    self.left = Node(insert_node)
            else:
                if self.right:
                    self.right.insert(insert_node)
                else:
                    self.right = Node(insert_node)

    # inorder printing
    def print_inorder(self):
        # print my left subtree
        if self.left:
            self.left.print_inorder()
        # print me
        print(self.value)
        # print my right subtree
        if self.right:
            self.right.print_inorder()

    
    def contains(self, value):
        if self.value == value:
            return True
        # go search left subtree
        if self.value > value:
            if self.left:
                return self.left.contains(value)
            else:
                return False
        # search right subtree
        elif self.value < value:
            if self.right:
                return self.right.contains(value)
            else:
                return False
        # did not find
        else:
            return False


class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if self.root:
            return self.root.insert(value)
        else:
            self.root = Node(value) # make this the root
    

    def print(self):
        if self.root:
            self.root.print_inorder()

    
    def contains(self, value):
        if self.root:
            return self.root.contains(value)



bst = BinarySearchTree()

# insert values into the tree
values = [10, 5, 15, 3, 7, 12, 18]

for value in values:
    bst.insert(value)

bst.insert(100)

bst.print()

contain = bst.contains(100)
print(contain)