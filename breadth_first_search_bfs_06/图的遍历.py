# coding: utf-8


"""

图的遍历
图的存储：邻接矩阵表示，二维数组




"""

from collections import deque



graph = [[0, 1, 0, 1, 1],
         [1, 0, 1, 0, 0],
         [0, 1, 0, 0, 0],
         [1, 0, 0, 0, 1],
         [1, 0, 0, 1, 0]]

point = [1, 2, 3, 4, 5]


class Graph(object):

    def __init__(self, point, graph):
        self.point = point
        self.graph = graph
        self.visited = [0 for _ in range(len(graph))]

    def bfs(self, n):
        queue = deque([n])
        self.visited[n] = 1

        while queue:
            node_index = queue.popleft()
            print(self.point[node_index])

            for i in range(len(self.graph)):
                if self.graph[node_index][i] == 1 and self.visited[i] == 0:
                    queue.append(i)
                    self.visited[i] = 1

Graph(point, graph).bfs(0)















