# Implement a stack with push and pop functions

class Stack:
    stack = []
    size = 0
    def push(self, item):
        self.stack.append(item)
        self.size +=1

    def pop(self):
        if self.size > 0:
            item_index = len(self.stack) - 1
            item = self.stack[item_index]
            del self.stack[item_index]
            self.size -=1
            return item

    def peak(self):
        if self.size > 0:
            item_index = len(self.stack) - 1
            item = self.stack[item_index]
            return item


def t():
    stack = Stack()
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    stack.push(6)
    print stack
    print stack.pop()
    print stack


# t()
