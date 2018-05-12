# Find the smallest element in a BST
from Interview_Practive.Trees.BST import insert, node
from Interview_Practive.Trees.print_trees import print_tree_BFS, print_tree_DFS


def find_smallest_item_bst(root_node):
    if not root_node:
        return # hit bottom of tree
    smallest = find_smallest_item_bst(root_node.getLeft()) # smallest should be all the way to the left
    if smallest is None: # if the return is None we are at the bottom to the left
        smallest = root_node.getValue() # at bottom to the left assign as smallest
    return smallest # return smallest up the stack



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
    print('finding smallest')
    print (find_smallest_item_bst(root))

populate_tree()