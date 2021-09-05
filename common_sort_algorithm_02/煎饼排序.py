# coding:utf-8

"""
给定数组A，进行煎饼翻转：选择一些正整数k<=A.length,然后翻转A的前K个元素，目的是：执行零次或者多次煎饼翻转以完成对数组A的排序，返回能够使A排序的煎饼翻转所对应的K值序列。

思路：
变量说明如下
1、res变量：根据题干最终返回的是记录翻转顺序的一个列表
2、index变量： 表示未排序数组中最大值的索引号
3、nums变量：表示输入的数组，list类型

基本思路：
1、找到未排序数组中最大值的索引index，然后将index索引之前的数组翻转，即将最大值翻转到第一个索引索引，然后再将整个数组翻转，这样最大值就落到最后一个索引位置上
2、翻转一次就会将当前未排序数组的最大值放到未排序数组的最后一个位置，因此可以对剩下的子集进行翻转，每轮翻转就会减少一个元素


"""

from typing import List

def pancake_sort(nums: List[int]) -> List[int]:
    res = []
    for i in range(len(nums)-1, -1, -1):
        index = nums.index(max(nums[:i+1]))
        nums[:index+1] = nums[:index+1][::-1]
        res.append(index+1)
        nums[:i+1] = nums[:i+1][::-1]
        res.append(i+1)
    return res



nusms = [3, 2, 4, 1]

print(pancake_sort(nusms))
















