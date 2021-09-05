# coding: utf-8


def bubble_sort(nums):

    for i in range(len(nums)-1):
        flag = 0
        for j in range(len(nums) - 1 - i):
            if nums[j] > nums[j+1]:   # 较大元素后移
                temp = nums[j]
                nums[j+1] =nums[j]
                nums[j] = temp
                flag = 1
        if flag == 0:
            break
    return nums











