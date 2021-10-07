# coding:utf-8


"""

二叉树最大、最小深度
解决方法：深度优先搜索，广度优先搜索

本章节使用广度优先搜素。

最大深度思路解析：
广大优先搜索是逐层搜索，需要用到一个变量累计深度，就可最终返回最大深度。

借助队列结构完成广度优先搜索，若想用一个变量累计深度，那么每次要访问某一层的所有节点。可想而知：在迭代的while循环中，再嵌套一层while循环用于访问某一层的全部节点之后，对深度自变量自增，而后执行下一层循环。


变量：
root: 二叉树根节点
queue: 队列
tmp: 表示访问盖层时，该层节点的子节点集合，每次迭代更新tmp为空列表，list类型。
ans: 表示最终返回的最大深度，初始值为0


"""

from collections import deque

def max_depth(root):

    if not root:
        return 0

    ans = 0
    queue = deque([root])
    while queue:
        tmp = []
        while queue:
            node = queue.popleft()
            if node.left:
                tmp.append(node.left)
            if node.right:
                tmp.append(node.right)
        queue.extend(tmp)
        ans += 1
    return ans


"""

最小深度思路解析

从上到下访问，只要访问到一个叶子节点，证明已经到达了与根节点距离最近的叶节点处，此叶节点的深度为最小深度。借助队列，如果当前节点为叶子节点，则返回该节点的深度为最终结果。
如果当前节点不满足上述判断且不为空节点，即存在子节点，则将其子节点依次入队。

"""



def min_depth(root):

    if not root:
        return 0
    queue = deque([(1, root)])

    while queue:
        depth, node = queue.popleft()
        if node and not node.left and node.right:   
            return depth

        if node:
            queue.append((depth+1, node.left))
            queue.append((depth+1, node.right))











