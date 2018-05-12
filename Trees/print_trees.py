# Print a tree using BFS and DFS

from BST import insert
from Interview_Practive.Trees.BST import node


def print_tree_BFS(tree):
    thislevel = [tree] # root is top level, aka level1
    while thislevel: # while you have items in the level keep looping
        nextlevel = list() # prep for next level list
        for n in thislevel: # get every item in this level
            print n.value, # print the item, comman prints on same line
            if n.left:
                nextlevel.append(n.left) # put the left item in the list for the new level
            if n.right:
                nextlevel.append(n.right) # put the right item in the list for the new level
        print# print new line to show new level
        thislevel = nextlevel # next level is now this level


def print_tree_DFS(tree):
    if not tree:
        return
    print_tree_DFS(tree.left)
    print (tree.value)
    print_tree_DFS(tree.right)


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
    print('print_BFS')
    print_tree_BFS(root)
    print('print_DFS')
    print_tree_DFS(root)



populate_tree()
