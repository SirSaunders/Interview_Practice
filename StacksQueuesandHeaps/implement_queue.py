# Implement a queue with queue and dequeue functions
class Queue:
    def __init__(self):
        pass

    queueArry = []
    _data_len = 0

    def queue(self, item):
        self.queueArry.append(item)
        self._data_len += 1

    def dequeue(self):
        if len(self.queueArry) > 0:
            item = self.queueArry[0]
            del self.queueArry[0]
            self._data_len -= 1

            return item
        return None

    def __len__(self):
        return self._data_len

    def __str__(self):
        return str(self.queueArry)


def t():
    queue = Queue()
    queue(1)
    queue(2)
    queue(3)
    queue(4)
    print(queue.queueArry)
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.queueArry)

# t()
