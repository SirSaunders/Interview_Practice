# depth first search
from Interview_Practive.Graphs.Graph import node
from Interview_Practive.StacksQueuesandHeaps.implement_stack import Stack

root_node = None


def DFS(root_node, target, path):
    path.add(root_node.key)
    if root_node.key is target:
        print('found')
        print('path: ' + str(path))
        return True
    found = False
    for node in root_node.edges:
        if node.key not in path and not found:
            path.add(node.key)
            found = DFS(node, target, path)
    return found




def DFS_taversal():
    stack = Stack()
    visited = set()
    stack.push(root_node)
    visited.add(root_node.key)
    while len(stack) > 0:
        current_node = stack.pop()
        edges = current_node.edges
        for node in edges:
            if node.key not in visited:
                stack.push(node)
                visited.add(node.key)
        print('current_node: ' + str(current_node.key))
        print('visited: ' + str(visited))
        print('queue : ' + str(stack))


def populate_graph():
    global root_node
    root_node = node('a')
    b = node('b')
    c = node('c')
    D = node('d')
    e = node('e')
    f = node('f')
    g = node('g')

    b.edges = (c)
    c.edges = D
    root_node.edges = (e)
    b.edges = (c)
    b.edges = (g)
    c.edges = (e)
    g.edges = (f)
    b.edges = e


populate_graph()
#DFS_taversal()

print('find target c')
DFS(root_node, 'c', set())
