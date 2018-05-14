# Implement a stack with push and pop functions
stack = []

def push(item):
    stack.append(item)

def pop():
    item_index = len(stack)-1
    item = stack[item_index]
    del stack[item_index]
    return item


def t():
    push(2)
    push(3)
    push(4)
    push(5)
    push(6)
    print stack
    print pop()
    print stack

t()