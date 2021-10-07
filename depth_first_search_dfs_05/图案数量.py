# coding:utf-8


"""

给定一个二维数组，数组中只包含1和0,1表示涂色的图案，0表示空白，判断给定的二维数组中总共有多少个互相独立的图案。

求有多少个相互独立的图案，每个图案都是由1组成的一个区域，不同图案之间由0相互阻隔。
遍历二维数组，当检测到1时，以该节点为起点进行深度优先搜索，该过程类似于图的遍历。只要发现一个新起点，就一定有一个新的图案，
在遍历二维数组中，需要避免对一个节点的重复访问，故需要另用一个维度相同的二维数组来记录每个节点是否被访问过。遍历过程中发现为1的元素已经被访问过，则跳过该节点。

变量：
grid: 表示一幅画的二维数组
length: 表示二维数组的长度，可以视为画的高度
width: 画的宽度（二维数组的宽度）
directions: 表示4个方向的列表，横纵坐标通过加减该列表中的元素，实现向上下左右4个方向的变化。
marked: 表示每个节点是否已经被访问过的二维数组，维度与grid相同，0表示未被访问过，1表示被访问过
re: 表示图案的数量
x0: 二维数组的横坐标
y0: 二维数组的纵坐标


"""


class Pattern(object):

    def num(self, grid):
        self.length = len(grid)
        if self.length == 0:
            return 0

        self.width = len(grid[0])
        self.directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]

        self.marked = [[0 for _ in range(self.width)] for _ in range(self.length)]

        re = 0

        for i in range(self.length):
            for j in range(self.width):
                if self.marked[i][j] == 0 and grid[i][j] == "1":
                    re += 1
                    self.dfs(grid, i, j)


        return re

    def dfs(self, grid, i, j):
        self.marked[i][j] = 1
        for x in range(4):
            x0 = i + self.directions[x][0]
            y0 = j + self.directions[x][1]
            if 0 <= x0 < self.length and 0 <= y0 < self.width and self.marked[x0][y0] == 0 and grid[x0][y0] == "1":
                self.dfs(grid, x0, y0)






















