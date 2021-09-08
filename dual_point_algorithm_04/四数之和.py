# coding:utf-8


"""
问题描述：
    给定一个包含n个整数的数组array和一个目标值sum_, 判断数组中是否存在4个数x、y、z和w, 使用x+y+z+w=sum_，找出所有满足条件且不重复的四元组。


example:

array = [1, 0, -1, 0, -2, 2]
sum_ = 0

输出：
[
   [-1, 0, 0, 1],
   [-2, -1, 1, 2],
   [-2, 0, 0, 2]
]


"""

"""

思路解析：

使用的是：双指针法，但是比三数之和多一个数字，因此多一层循环，时间复杂度O(N^3)

类推：
   三数之和的实例中，通过固定一个数，双指针指向两个数的方式找和为0的三个数。 本题是四个数，因此固定两个数，双指针指向两个数的方式来找和为目标值的4个数。
   
   
变量定义：
array: 输入数组
res: 表示返回的最终列表，包含不重复的额四元组
sum_：表示4个数的目标和
i: 表示固定的第1个数，范围从0到数组长度减3
j: 表示固定的第2个数，范围从0到数组长度为2.






"""

from typing import List

def four_sum(array: List[int], sum_: int):
    array.sort()

    res = []
    length = len(array)

    for i in range(length-3):
        if i!=0 and array[i]==array[i-1]:
            continue

        for j in range(i+1, length-2):
            if j!=i+1 and array[j] == array[j-1]:
                continue

            l = j+1
            r = length - 1
            while l < r:
                s = array[i] + array[j] + array[l] + array[r]
                if s == sum_ and [array[i], array[j], array[l], array[r]] not in res:
                    res.append([array[i], array[j], array[l], array[j]])
                    l += 1
                    r -= 1
                    while l < r and array[l] == array[l-1]:  # 排序后相同的数字，移动索引。
                        l += 1

                    while l < r and array[r] == array[r+1]:
                        r -= 1
                elif s >sum_:
                    r -= 1
                else:
                    l += 1
    return res










