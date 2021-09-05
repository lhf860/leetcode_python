# coding:utf-8


"""

1. 颜色分类： 给定一个包含红、白、蓝的一共n个元素的数组，原地对他们进行排序，使相同的元素相邻，并按照红、白、蓝顺序排列。这里使用0、1、2分别表示红、白、蓝。
        1. 计数排序法
        2. 快速排序法

"""



def color_sort_by_count(nums):  # 计数排序
    num0 = 0
    num1 = 1
    num2 = 2

    for num in nums:
        if num0 == num:
            num0 += 1
        elif num1 == num:
            num1 += 1
        else:
            num2 += 1

    for i in range(num0):
        nums[i] = 0

    for i in range(num0, num0+num1):
        nums[i] = 1

    for i in range(num0+num1, len(nums)):
        nums[i] = 2


def color_sort_by_quicksort(nums):
    """
    快速排序的思想：一趟排序之后，左侧的元素比基准元素小，右侧的元素都比基准元素大。而在此题中，可以将数组分为【比1小的元素，1，比1大的元素】，1为基准，进行三路排序。
    给予上述思考：需要三个指针：一个head指针指向数组头部，一个tail指针指向数组尾部，一个指针current指向当前元素，遍历一遍数组即可完成排序。

    :param nums:
    :return:
    """

    head = 0
    tail = len(nums) - 1
    current = 0

    while current <= tail:  # 一趟三路快速排序
        if nums[current] < 1:
            nums[current], nums[head] = nums[head], nums[current]
            head += 1
            current += 1
        elif nums[current] > 1:
            nums[current], nums[tail] = nums[tail], nums[current]
            tail -= 1
        else:
            current += 1

    return nums















