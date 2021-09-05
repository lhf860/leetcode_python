# coding: utf-8


"""

一般的方法：先排序后，然后再选取K个数


便捷方式：采用堆排序，直接获取最大的K个数


实现思路：
1、先向一个列表中放入K个元素，然后调整为堆（小根堆）
2、后续的元素，将每个元素与堆中的最小值进行比较，若大于最小值，移除堆中的最小值，并将该元素加入堆中重新调整为小根堆
3、遍历结束，最后得到的k个元素就是原数组中的最大的K个数

"""


import heapq


def small_k_num(nums, k):

    if len(nums) <= k:
        return nums

    heap = []
    for i in range(len(nums)):
        if i < k:
            heap.append(nums[i])
        else:
            heapq.heapify(heap)
            if heap[0] < nums[i]:
                heapq.heapreplace(heap, nums[i])
    return heap

nums = [10, 2, 12, 3, 5, 7]
k = 4

print(small_k_num(nums, k))




















