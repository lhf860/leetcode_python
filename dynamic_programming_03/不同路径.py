# coding: utf-8


"""
问题描述：

  一个机器人位于m*n的网格的左上角， 机器人每次只能向下或者向右移动一步，机器人需要到达网格的右下角，总共有多少路径？


"""


"""
思路解析：

分析：当到达其中一个网格中时，其要么来自上方的网格，要么来自左侧的网格。因此到达当前网格的路径数=到达上方网格的路径数+到达左侧网格的路径【递归公式】，
      具有重叠子问题和最优子结构的问题，采用动态规划


"""


"""

变量定义：
1、dp：二维数组，dp[i][j]表示到达网格i行j列网格的路径数
   初始化： 到达第一行或者第一列的网络都只有一种路径，所以dp[0][:] = 1， dp[:][0] = 1, 其余位置初始化为0.

2、递归公式
   dp[i][j] = dp[i-1][j] + dp[i][j-1]

3、结果获取：dp[m][n]



"""




def unique_paths(m, n):

    dp = []
    for i in range(m):
        dp.append([0] * n)


    for row_index in range(m):
        dp[row_index][0] = 1

    for col_index in range(n):
        dp[0][col_index] = 1

    dp[0] = [1] * n

    for i in range(1, m):   # 从1开始，因此第一行已经初始化过了
        for j in range(1, n):    # 从1开始，因此第一列已经初始化过了
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[m-1][n-1]


m = 3  # 3 行
n = 7  # 7 列

print(unique_paths(m, n))





























