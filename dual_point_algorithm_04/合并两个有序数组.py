# coding: utf-8


"""

合并两个有序数组：

有序数组arr1和arr2，


"""

def merge(array1, array2):
    a = len(array1)
    b = len(array2)

    array_ = array1[:a]
    array1[:] = []

    p1 = p2 = 0
    while p1 < a and p2 < b:
        if array_[p1] < array2[p2]:
            array1.append(array_[p1])
            p1 += 1
        else:
            array1.append(array2[p2])
            p2 += 1
    if p1 < a:
        array1[p1+p2:]=array_[p1:]
    if p2 < b:
        array1[p1+p2:] = array2[p2:]
    return array1




