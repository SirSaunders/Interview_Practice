# Implement a linked list (with insert and delete functions)
# Find the Nth element in a linked list
# Remove the Nth element of a linked list

class List_element:
    right = None
    value = None

    def __init__(self, value):
        self.value = value

    def set_right(self, list_element):
        self.right = list_element


class Link_List:
    list_start = None
    size = 0

    def insert(self, item):
        list_item = List_element(item)
        if not self.list_start:
            self.list_start = list_item
            print('added')
        else:
            current_list_item = self.list_start
            while current_list_item.right is not None:
                current_list_item = current_list_item.right
            current_list_item.right = list_item
        self.size += 1

    def printList(self):
        current_list_item = self.list_start
        while current_list_item:
            print(current_list_item.value)
            current_list_item = current_list_item.right

    def get(self, index):
        if index < self.size:
            current_list_item = self.list_start
            for i in range(index):
                current_list_item = current_list_item.right
            return current_list_item

    def delete(self, index):
        if index < self.size:
            if index is 0:
                self.list_start = self.list_start.right
            else:
                previous_list_item = self.list_start
                current_list_item = self.list_start
                for i in range(index):
                    previous_list_item = current_list_item
                    current_list_item = current_list_item.right
                previous_list_item.right = current_list_item.right
            self.size -= 1

def t1():
    list = Link_List()
    list.insert(2)
    list.insert(3)
    list.insert(4)
    list.insert(5)
    list.printList()
    print
    print list.get(2).value
    print
    list.delete(1)
    print
    list.printList()


t1()
