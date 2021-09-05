# coding:utf-8

"""


"""

class Queue(object):

    def __init__(self):
        self.list = []

    def enqueue(self, item):
        """入队"""
        self.list.append(item)

    def dequeue(self):
        """出队"""
        self.list.pop(0)

    def is_empty(self):
        return self.list == []

    def size(self):
        return len(self.list)



"""或者借助Python中自带的队列数据结构"""

from queue import Queue

q = Queue(maxsize=10)
q.put(1)
q.put(2)
print(q.qsize())
print(q.empty())
print(q.full())









