# coding:utf-8



def insert_sort_half(nums):

    for i in range(1, len(nums)):

        key = nums[i]

        high = i-1
        low = 0

        while(low <= high):  # 折半查找元素应该插入的位置
            mid = int((low + high)/2)
            if key >= nums[mid]:
                low = mid + 1
            if key < nums[mid]:
                high = mid - 1

        j = i - 1
        while j >= low:
            nums[j+1] =nums[j]
            j -= 1
        nums[low] = key

    return nums

















