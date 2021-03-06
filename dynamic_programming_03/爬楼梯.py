# coding:utf-8


"""
是一维动态规划的应用题

问题描述：
    假设你正在爬楼梯，需要n阶才能到达楼顶，每次你可以爬1个或者2个台阶，你有多少种不同的方法可以爬到楼顶


思路：
   若想爬到楼顶n处，只有两种可能：1）从n-1层楼顶向上爬一层， 这种只需要计算到达n-1层的方法数
                               2） 从n-2层向上爬2层，这种方法只需要计算爬n-2层的方法数，之后将二者相加即可。


   计算到达n层的方法数=到达n-1层的方法数 + 到达n-2层的方法数；
   计算n-1层的方法数=到达n-2层方法数 + 到达n-3层的方法数
   ......

   包含重叠子问题，大的问题的解由小问题的解构成


"""


def climb_stairs(n):

    count = [0, 1, 2]
    for i in range(3, n+1):
        count.append(count[i-1] + count[i-2])
    return count[n]

n = 10  # 代表楼梯的层数

print(climb_stairs(n))












