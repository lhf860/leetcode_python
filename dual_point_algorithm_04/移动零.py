# coding:utf-8


"""

问题描述：

    给定一个数组array， 编写一个函数将所有0移动到数组的末尾，同时保持非零元素的相对顺序。
    注意： 必须在原数组上操作，不能复制额外的数组，并且尽量减少操作的次数。

example:

输入： [0, 1, 0, 3, 12]
输出： [, 3, 12, 0, 0]


"""

"""
思路解析：

移动0到末尾，并且保持元素的相对顺序不变，需要遍历数组，且在遍历的过程中堆元素逐个进行处理。从前向后遍历的过程中，定义一个指针current, 一个lastnozero指针。

变量定义：
array: 输入的数组
current: 遍历过程中当前元素的位置
lastnozero: 表示在当前元素之前可以确定的最后一个非零元素的下一个位置。【即lastnozero代表着将非零元素移动前面后的索引，lastnozero索引之前的元素都是非零元素。】


两个指针初始值为0，只要遍历判断当前元素非零，那么就将值赋给lastnozero指针所指向的位置，将0赋给current指针所知的元素，完成一个交换过程。
如此一来， lastnozero指针所指向的位置之前必定都是非零元素，相当于实现了将非零元素逐个移动到0之前。
注意：给current指针所指元素赋值之前，需要判断两个指针指向的是不是同一个位置。如果指向位置 相同，就不能给current指针指向的元素赋0，否则会覆盖非零元素的值。
完成交换之后，要将lastnozero指针自增1，相当远后移一位，以便下次数值交换过程。


"""

from typing import List

def move_zeros(array: List[int]):

    lastnozero = 0
    for current in range(len(array)):
        if array[current] != 0:
            array[lastnozero] = array[current]

        if lastnozero != current:
            array[current] = 0
        lastnozero += 1
    return array
















