# coding: utf-8



def quick_sort(nums, low, hight):
    i = low
    j = hight
    keys = nums[i]

    while(i < j):  # 一趟快速排序
        while(i < j and keys <= nums[j]):
            j -= 1
        nums[i] = nums[j]

        while(i<j and keys >= nums[i]):
            i += 1
        nums[j] = nums[i]
    nums[i] = keys

    quick_sort(nums, low, i-1)
    quick_sort(nums, i+1, hight)
















