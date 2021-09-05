# coding: utf-8



import heapq

def heap_sort(nums):

    result = []
    for i in range(len(nums)):
        heapq.heapify(nums)  # 调整为小根堆, nums的第一个元素是最小的
        # print(nums)
        result.append(nums[0])  # 获取最小元素放入到结果列表中【第一个元素】
        nums.remove(nums[0])  # 移除nums中的最小元素
    return result



nums = [2, 6, 4, 3, 8, 10, 1]

print(heap_sort(nums))



