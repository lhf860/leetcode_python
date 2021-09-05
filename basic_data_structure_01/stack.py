# coding:utf-8


"""自定义栈"""



class Stack(object):

    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def push(self, item):
        self.data.append(item)

    def get_top(self):
        if self.is_empty():
            return None
        return self.data[-1]

    def pop(self):
        if self.is_empty():
            return None
        return self.data.pop()










