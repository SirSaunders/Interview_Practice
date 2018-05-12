# Find the 2nd largest number in a BST
from Interview_Practive.Trees.BST import insert, node
from Interview_Practive.Trees.print_trees import print_tree_DFS


def find_2nd_largest(root_node):
    current_placements = []  # the current placements highest to lowest
    if not root_node:
        return []  # hit the bottom return
    current_placements += find_2nd_largest(root_node.getRight())  # go to the right when ever possible
    current_placements.append(root_node.value)  # add current node to placements
    current_placements += find_2nd_largest(root_node.getLeft())  # go down the left side
    return current_placements  # return current placements


def populate_tree():
    root = node(4)
    insert(root, node(6))
    insert(root, node(2))
    insert(root, node(9))
    insert(root, node(3))
    insert(root, node(1))
    insert(root, node(5))
    insert(root, node(7))
    insert(root, node(8))
    print('print_DFS')
    print_tree_DFS(root)
    print('finding 2nd largest')
    print (find_2nd_largest(root)[1])


populate_tree()
