# coding: utf-8

"""
问题描述： 给定m个非负整数表示每个宽度为1的柱子的高度图，计算按此排列的柱子，下雨之后能存储多少水。

"""


def water(height):

    left = 0
    right = len(height) - 1
    leftmax = rightmax =0
    res = 0
    while(left < right):
        if height[left] < height[right]:
            if height[left] >= leftmax:
                leftmax =height[left]
            else:
                res += leftmax - height[left]
            left += 1
        else:
            if height[right] >= rightmax:
                rightmax = height[right]
            else:
                res += rightmax - height[right]
            right -= 1
    return res
