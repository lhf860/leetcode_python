# coding: utf-8



def select_sort(nums):

    for i in range(len(nums)-1):
        min_position = i
        for j in range(i+1, len(nums) - 1):
            if nums[j] <nums[i]:
                min_position = j

        if min_position != i:
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
    return nums



















