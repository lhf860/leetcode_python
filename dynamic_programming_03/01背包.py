# coding:utf-8

"""有n个物品，他们有各自对应的质量和价值，现在给定容量的背包， 求如何让物品装进背包具有最大价值的方案


example:
weights = [1, 3, 2, 5]
values = [200, 240,140, 150]
max_weight = 5

输出：440

解决思路：
1、动态规划是否合适，是否有最子结构，是否有重叠子问题
   将子问题的最优解结合得到原始问题的最优解，要知道最大容量下如何在n个物品中选择，使背包价值最大，就得考虑一件件物品，容量一步步扩大，考虑每一件物品是否放入；
   而子问题与子问题的解决思路是相同的，因此满足最优子结构和重叠子问题
2、动态规划最重要的一步：找状态和状态转移方程
   每一个都要考虑是否放入，放入之后的价值是否更高；那么就需要直到放入该物品时背包的最大价值和不放入该物品时背包的最大价值，然后进行比较。
   因此需要一个二维数组来保存考虑当前考虑前i件物品时，背包容量为j时，背包中的最大价值是多少

3、约束条件，就是背包的最大容量

4、初始化问题（最容易忽略的问题，但也是很重要的问题）
   本题中背包容量为0时，价值均为0，其他也为0


递归公式：

   每一步更新时，需要考虑是否将第i个物品放入到容量为j的背包内，就要比较放入第i个物品和不放入的物品总价值，选择总价值最高的放入方式，可以得到递归关系：

   当j >=weights[i]时， dp[i][j] = dp[i-1][j]   # 不放入时的总价值
   当j < weights[i]时， dp[i][j] = max(dp[i-][j], dp[i-1][j-weights[i]] + value[i]])  # 放入第i件物品，需要有value[i]的空间才能放下



"""

from typing import List


def bag(weight: List, value: List, max_weight: int):

    weight.insert(0, 0)
    value.insert(0, 0)

    thing_num = len(weight)

    # 建立一个thing_num * (max_weight + 1)的二维数组

    dp = []

    for i in range(thing_num):
        dp.append([0] * (max_weight+1))

    for i in range(1, thing_num):
        for j in range(1, max_weight+1):
            dp[i][j] = dp[i-1][j]
            if j >= weight[i]:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight[i]] + value[i])
    return dp[thing_num-1][max_weight]



















