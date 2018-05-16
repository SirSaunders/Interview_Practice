# Breath first search
from Interview_Practive.Graphs.Graph import node
from Interview_Practive.StacksQueuesandHeaps.implement_queue import Queue

root_node = None

def BFS(root_node, target):
    queue = Queue()
    visited = set()


    queue.queue(root_node)
    visited.add(root_node.key)

    while len(queue) > 0:
        current_node = queue.dequeue()
        edges = current_node.edges
        for node in edges:
            if node.key not in visited:
                queue.queue(node)
                visited.add(node.key)
                if node.key is target:
                    print('found')
                    print('visited: ' + str(visited))
                    return 'found'
def BFS_traversal():
    queue = Queue()
    visited = set()

    queue.queue(root_node)
    print(queue.queueArry)
    visited.add(root_node.key)

    while len(queue) > 0:
        current_node = queue.dequeue()
        edges = current_node.edges
        for node in edges:
            if node.key not in visited:
                queue.queue(node)
                visited.add(node.key)
        print('current_node: ' + str(current_node.key))
        print('visited: ' + str(visited))
        print('queue : ' + str(queue))


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
BFS_traversal()

print('find target f')
BFS(root_node, 'f')
