# coding:utf-8

"""

问题描述
给定一个二维数组，表示一个迷宫，其中0代表可以走的位置，并且只能水平或者垂直走，不能走斜线；1代表不可以走的位置。
试求从左上角入口能否到达右下角出口，若能够到达，输出路径；若不能，则返回FALSE。

"""

"""广度优先搜索"""


from collections import deque


def gomaze(maze):
    """

    :param maze: 二维数组，代表迷宫
    :return:
    """
    length = len(maze)
    width = len(maze[0])
    visited = [[0 for _ in range(width)] for _ in range(length)]
    step = [[(-1, -1) for _ in range(width)] for _ in range(length)]  # 表示路径子节点和父节点的关系

    directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    queue = deque([(0, 0)])
    visited[0][0] = 1  # 从左上角开始
    result = []

    while queue:
        x, y = queue.popleft()
        if x == length - 1 and y == width - 1:
            break
        for d in directions:
            x1 = x + d[0]
            y1 = y + d[1]
            if x1 < 0 or y1 < 0 or x1 >=length or y1 >= width or visited[x1][y1] == 1 or maze[x1][y1] == 1:
                continue
            step[x1][y1] = (x, y)
            visited[x1][y1] = 1
            queue.append((x1, y1))

    if step[length-1][width-1] == (-1, -1):
        return False

    re_x = length - 1
    re_y = width - 1
    result.append((length-1, width-1))

    while re_x >= 0 and re_y >= 0:
        re_x, re_y = step[re_x][re_y]
        result.append((re_x, re_y))

    return result[::-1][1:]



maze = [[0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0]
        ]
# 输出
#
[(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (3, 4), (4, 4)]


result = gomaze(maze)
print("result: ", result)












