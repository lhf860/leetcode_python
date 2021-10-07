# coding: utf-8


"""
图的遍历：
图的存储需要使用邻接矩阵，比如：
array = [[0, 1, 0, 1, 1],
         [1, 0, 1, 0, 0],
         [0, 1, 0, 0, 0],
         [1, 0, 0, 0, 1],
         [1, 0, 0, 1, 0]]

point = [1, 2, 3, 4, 5]

变量:
sum： 表示到目前为止共访问了多少个节点，int类型
visited: 表示目标为止哪些节点访问过则为1， 未被访问则为0， list类型， 默认初始值为0

"""



array = [[0, 1, 0, 1, 1],
         [1, 0, 1, 0, 0],
         [0, 1, 0, 0, 0],
         [1, 0, 0, 0, 1],
         [1, 0, 0, 1, 0]]


point = [1, 2, 3, 4, 5]


class Graph(object):
    def __init__(self, point, graph):
        self.graph = graph
        self.point = point
        self.sum = 0
        self.visited = [0 for _ in range(len(graph))]

    def dfs(self, n):
        self.visited[n] = 1
        print(self.point[n])
        self.sum += 1
        if self.sum == len(self.visited):
            return

        for i in range(len(self.graph)):
            if self.graph[n][i] == 1 and self.visited[i] == 0:
                self.dfs(i)

Graph(point, array).dfs(0)


