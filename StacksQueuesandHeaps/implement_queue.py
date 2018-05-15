# Implement a queue with queue and dequeue functions

queueArry = []


def queue(item):
    queueArry.append(item)


def dequeue():
    if len(queueArry) > 0:
        item = queueArry[0]
        del queueArry[0]
        return item
    return None

def t():
    queue(1)
    queue(2)
    queue(3)
    queue(4)
    print queueArry
    print dequeue()
    print dequeue()
    print dequeue()
    print queueArry



t()
