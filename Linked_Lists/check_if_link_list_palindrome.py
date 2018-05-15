# Check whether a link list is a palindrome
from Interview_Practive.Linked_Lists.implement_linked_list import Link_List
from Interview_Practive.StacksQueuesandHeaps.implement_stack import Stack


def check_is_palindrome(link_list):
    current_item = link_list.list_start
    stack = Stack()
    midPoint = -1
    if link_list.size % 2 is not 0: # check if list is odd number
        midPoint = link_list.size // 2 # find mid point if its odd
    cnt = 0
    print midPoint
    while current_item:
        if cnt is not midPoint:
            if stack.peak() is not current_item.value: # if the item is not at the top of the stack push it
                stack.push(current_item.value)
            else: # item is the same pop it
                stack.pop()
            print stack.stack
        current_item = current_item.right
        cnt += 1
    return len(stack.stack) is 0 # if stack is empty it must be a palindrome


def t():
    list = Link_List()

    list.insert('r')
    list.insert('a')
    list.insert('c')
    list.insert('e')
    list.insert('c')
    list.insert('a')
    list.insert('r')
    print check_is_palindrome(list)



t()
