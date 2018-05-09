# Implement a BST with insert and delete functions

class node:
    left = None
    right = None
    value = None

    def __init__(self, val):
        self.value = val

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def setRight(self, node):
        self.right = node

    def setLeft(self, node):
        self.left = node

    def getValue(self):
        self.value

    def setValue(self, value):
        self.value = value


root = None


def insert(root, node):
    if not root:
        root = node
    else:

        if root.getValue > node.value:
            rootLeft = root.getLeft()
            if rootLeft:
                insert(rootLeft, node)
            else:
                root.setLeft(node)

        if root.getValue < node.value:
            rootRight = root.getRight()
            if rootRight:
                insert(rootRight, node)
            else:
                root.setRight(node)
            insert(rootRight, node)
