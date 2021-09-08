# coding: utf-8


"""
问题描述：

给定一个包含n个整数的数组array，判断该数组中是否存在3个元素x、y、z，使得x+y+z=0.找出所有符合条件且不重复的三元组，不可以包含重复的三元组。



example:
输入：array=[-1,0,1,2,-1,-4]
输出：[(-1,0,1),(-1,-1,2)]

"""



"""
第一种解法：暴力解法，三层for循环


"""
from typing import List

def three_sum_violent_solution(array: List[int]):
    array.sort()
    length = len(array)
    res = []
    for i in range(length):
        for j in range(i+1, length):
            for k in range(k+1, length):
                if array[i] + array[j] + array[k] == 0:
                    res.append([array[i], array[j], array[k]])

    return res



"""
第二种：双指针解法

前提：可以先将数组排序，避免不必要的遍历

由于x+y+z=0, 即满足x+y=-z, 可以将遍历到的元素视为-z, 在遍历过程中使用左右指针分别指向当前元素的下一个元素及数组的最后一个元素

变量定义：
k: 当前元素的位置
l: 当前元素的下一个元素，初始值为k+1
r: 表示三个数中的第三个数字，其初始值为数组长度减1
res: 表示最终返回的结果，包含所有和为0的不重复的三元组
s: 表示3数之和


"""


def three_sum(array: List[int]):

    array.sort()

    res = []
    for k in range(len(array)-2): # 减2是因为k后要取两个元素l和r索引对应的值

        if array[k] > 0:
            break

        if k > 0 and array[k] == array[k-1]:  # 相同的元素向后移动，因为要求解不同的三元组
            continue

        l, r = k+1, len(array) - 1

        while l < r:
            s = array[k] + array[l] + array[r]
            if s < 0:
                l += 1
                while l < r and array[l] == array[l-1]:  # l先加1， 元素重复向后移动
                    l += 1
            elif s > 0:
                r -= 1
                while l < r and array[r]==array[r+1]:
                    r -= 1
            else:
                res.append([array[k], array[l], array[r]])
                l += 1
                r -= 1
                while l < r and array[l]==array[l-1]:
                    l += 1
                while l < r and array[r]== array[r+1]:
                    r -= 1
        return res





















