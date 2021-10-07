# coding:utf-8

"""

问题描述：
给定一个集合，实现集合中元素的全排列

"""

input_array = [1, 2, 3]

def all_sort():
    temp = []
    dfs(0, temp)

def dfs(position, temp):
    if position == len(input_array):
        print(temp)
    for i in input_array:
        if i not in temp:
            temp.append(i)
            dfs(position + 1, temp)
            temp.pop()

all_sort()




























