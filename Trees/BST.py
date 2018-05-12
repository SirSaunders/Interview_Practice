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
        return self.value

    def setValue(self, value):
        self.value = value


root = None


def insert(root, node):
    if not root:
        root = node
    else:
        if root.getValue() > node.getValue():
            rootLeft = root.getLeft()
            if rootLeft:
                insert(rootLeft, node)
            else:
                root.setLeft(node)

        if root.getValue() < node.getValue():
            rootRight = root.getRight()
            if rootRight:
                insert(rootRight, node)
            else:
                root.setRight(node)


def delete(root, node):
    if root.getValue() is node.getValue():
        if root.getLeft() and root.getRight():
            successor = get_successor_node(root.getRight())
            successor.setLeft(root.getLeft())
            if root.getRight().getValue() is not successor.getValue():
                successor.setRight(root.getRight())
            else:
                successor.setRight(None)

            root = successor
            return root
        else:
            if root.getLeft():
                root = root.getLeft()
            elif root.getRight():
                root = root.getRight()
            else:
                root = None
    else:
        if root.getValue() > node.getValue():
            rootLeft = root.getLeft()
            if rootLeft:
                root.setLeft(delete(rootLeft, node))
            else:
                return root
        if root.getValue() < node.getValue():
            rootRight = root.getRight()
            if rootRight:
                root.setRight(delete(rootRight, node))
            else:
                return root
    return root


def get_successor_node(root):
    if root.getLeft():
        succesor = get_successor_node(root.getLeft())
        if(not succesor.getLeft()):
            root.setLeft(succesor.getRight())
        return succesor
    return root


def in_order_print(root):
    if not root:
        return
    in_order_print(root.getLeft())
    print root.getValue()
    in_order_print(root.getRight())


def t():
    root = node(4)
    insert(root, node(6))
    insert(root, node(2))
    insert(root, node(9))
    insert(root, node(3))
    insert(root, node(1))
    insert(root, node(5))
    insert(root, node(6))
    insert(root, node(7))
    insert(root, node(8))
    root = delete(root, node(4))

    in_order_print(root)


#t()
