# coding:utf-8

"""

救生艇人员分配问题，即在每一艘救生艇承重有限的情况下，需要用多少艘救生艇才能容纳所有人。
该问题利用左右指针算法解决。


问题定义：
第i个人的重量为people[i], 每艘救生艇可以承载的最大重量为weight。每艘救生艇最多可以同时载两人，但是条件时这些人的重量之和最多为weight。要求每个人都有救生艇可乘坐，求至少需要多少艘救生梯。


example：
输入：people=[1, 2], weight=3
输出： 1


思路解析：
一艘救生梯最多乘坐两个人，应当先将体重的数组从小到大进行排序，然后双指针分别指向第一个人和最后一个人，通过不断判断指针所指的两个人是否可以安排到一艘救生艇来不断计算所需救生艇的数量。
同时移动两个指针，直至两个指针相遇。


"""


def rescue_boats(people, weight):
    people.sort()
    left = 0
    right = len(people) - 1
    res = 0

    while(left <= right):
        res += 1
        if people[left] + people[right] <= weight:
            left += 1
        right -= 1
    return res
