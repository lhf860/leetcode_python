# coding: utf-8


"""

问题描述
给定一个二维数组表示一个迷宫，其中1为可达节点，0为不可达节点。假设迷宫中的每个可达节点都有一个玩家，求有多少玩家无论怎么走都不能到达迷宫的边界（迷宫的边界指二维数组的第一行、第一列、最后一行、最后一列）

思路；
如果从边界入手，对边界上的可达节点进行深度优先搜索，相当于将从内向外探索变成了从外向内的搜索，其达到的效果是相同的。
对边界上可达节点可以访问到的玩家位置做标记，那么最终只要统计未被标记的节点个数，即为不能到达边界的玩家数量。

变量：
array: 迷宫的二维数组， 1为可达节点，并且各有一个玩家位于此处，0表示不可达节点。
m: 二维数组的长度，高度
n: 二维数组每一维的长度，宽度

directions: 表示上下左右方向的列表
re: 不可走出迷宫的玩家数量，默认为0
x0: 横坐标
y0: 纵坐标


"""



class Player(object):

    def num(self, array):
        self.directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        m = len(array)
        n = len(array[0])
        re = 0

        for i in range(0, n):
            if array[0][i] == 1:
                array[0][i] = 0
                self.dfs(0, i, array, m, n)
            if array[m-1][i] == 1:
                array[m-1][i] = 0
                self.dfs(m-1, i, array, m, n)

        for j in range(0, m-1):
            if array[j][0] == 1:
                array[j][0] = 0
                self.dfs(j, 0, array, m, n)
            if array[j][n-1] == 1:
                array[j][n-1] = 0
                self.dfs(j, n-1, array, m, n)

        for arr in array:
            re += arr.count(1)
        return re



    def dfs(self, i, j, array, m, n):
        for l in self.directions:
            x0 = i + l[0]
            y0 = j + l[1]
            if 0 <= x0 < m and  0 <= y0 < n and array[x0][y0] == 1:
                array[x0][y0] = 0
                self.dfs(x0, y0, array, m, n)














