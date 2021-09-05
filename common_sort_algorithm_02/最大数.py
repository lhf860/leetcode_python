# coding:utf-8


"""
给定一个非负整数，重新排列它们的顺序，使之成为一个最大的整数，因此输出结果可能非常大，所以需要返回一个字符串而不是整数。

示例：
输入：[10, 2]
返回： 210

输入：[3, 30, 34, 5, 9]
返回：9534330


基本思路：
排序的规则是；能够将高位数大的数字放在前面，即让数组按照能使高位最高、第二高、第三高。。。这样的顺序排列，最后拼接成字符串

所以需要首先在一趟排序中找到高位数最大的数组放到前面【遍历所有的数，找到最大，符合冒泡排序】，注意在比较两个数大小的标准不再是数值大小，可以转换成数组按照ASCII的大小进行比较。


"""

def largest_nums(nums):

    nums = [str(i) for i in nums]

    # 冒泡排序：两层for循环
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if int(nums[i] + nums[j]) < int(nums[j] + nums[i]):  # 注意理解这一步
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
    if int(''.join(nums)) == 0:
        return str(0)
    else:
        return "".join(nums)


nums = [3, 30, 34, 5, 9]

print(largest_nums(nums))




"""
简介的方法：

借助sorted
sorted和sort的区别在于是否改变了原数组；sorted函数直接对原数组重新排序，不会另外占用内存空间；而sort函数则需要另外的空间复制了原数组，对复制的数组进行排序，排序后原数组并不会改变。

"""


from functools import cmp_to_key

"""
cmp_to_key： 比较函数，使用方法：传入两个参数x,y, 当x > y时返回1，否则返回-1.在list中的工作机制是：将list中的元素两两比较，当cmp返回正数时交换两元素。

"""


def largest_sort_simple(nums):
    nums = sorted([str(i) for i in nums], key=cmp_to_key(lambda x, y: int(y+x) - int(x+y)))

    if int("".join(nums)) == 0:
        return str(0)
    else:
        return "".join(nums)













