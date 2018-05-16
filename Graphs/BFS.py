# Breath first search
from Interview_Practive.Graphs.Graph import node
from Interview_Practive.StacksQueuesandHeaps.implement_queue import Queue

queue = Queue()
root_node = None
visited = set()


def BFS():
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

    root_node.edges = (b)
    b.edges = (c)
    c.edges = D
    root_node.edges = (b)
    root_node.edges = (e)
    b.edges = (c)
    b.edges = (g)
    c.edges = (e)
    g.edges = (f)
    f.edges = (root_node)


populate_graph()
BFS()
