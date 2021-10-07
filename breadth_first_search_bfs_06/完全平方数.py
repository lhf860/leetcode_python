# coding:utf-8


"""


问题描述
给定一个正整数，找出该整数至少可以由几个平方数累加组成。完全平方数是指整数的平方数，如1、4、9、16等。


思路解析：
抽象成一个从根节点0到叶子结点n的过程，逐层向下累加，直到累加之和为n为止，此时的深度即为完全平方数。
注意：每一层累加时只能加上完全平方数，因此可以缩小范围。当给定n时，只有1到int(n**0.5)的平方数时备选项。

最终输出的是：所需完全平方数的个数，即那个节点所在的深度。

每个节点有两个元素（sum, depth）: 即当前完全平方数的和， depth表示当前节点的深度。

初始根节点为(0, 0)
接下来每一层的操作都是类似的，具体为：
每一层的每个节点为父节点加上 1到int(n**0.5)的平方数， 这样逐层累加，直到合为n。


变量：
n：给定的正整数
selected： 表示1到int(n**0.5)的平方数，即以备累加的平方数
visited: 表示已经出现过的累加和
queue: 表示队列
current: 表示从队列取出头部元素中的累加之和的值
height: 从队列取出头部元素的深度值
sum_: 表示加上完全平方数之后的累加之和，需要检测是否已经存在visited中存在。



"""


"""广度优先搜索算法"""

from collections import deque


def square(n):
    selected = [i**2 for i in range(1, int(n**0.5) + 1)]
    visited = set()

    queue = deque([0, 0])
    while queue:
        current, height = queue.popleft()
        for i in selected:
            sum_ = current + i
            if sum_ == n:
                return height + 1
            if sum_ < n and sum_ not in visited:
                visited.add(sum_)
                queue.append([sum_,height+1])





"""动态规划法"""


def square_dp(n):
    dp = [i for i in range(n+1)]
    for i in range(4, n+1):
        for j in range(int(n**0.5), 0, -1):
            if i >= j**2:
                dp[i] = min(dp[i], dp[i-j*j]+1)
    return dp[n]
















