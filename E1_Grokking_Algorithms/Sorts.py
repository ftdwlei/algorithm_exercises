# coding=utf-8
"""
@Author : captain
@Email: 
@createtime : 2022/10/27 0:06
@Note:
"""


def selectSort(list):
    res_list = []
    while list:
        smallindex = 0
        for j in range(1, len(list)):
            if list[j] < list[smallindex]:
                smallindex = j
        res_list.append(list.pop(smallindex))
    return res_list


def quickSort(list):
    if list:
        left = 0
        right = len(list) - 1
        mid = (left + right) // 2
        # print(f"left:{left},right:{right},mid:{mid}")
        left_arr, right_arr, mid_arr = [], [], []
        for i in range(len(list)):
            if list[i] < list[mid]:
                left_arr.append(list[i])
            elif list[i] > list[mid]:
                right_arr.append(list[i])
            else:
                mid_arr.append(list[i])
        # print(f"left_arr:{left_arr},mid_arr:{mid_arr},right_arr:{right_arr}")
        return quickSort(left_arr) + mid_arr + quickSort(right_arr)
    else:
        return []


list1 = [2, 33, 55, 4, 42, 21, 332, 77]
print(selectSort(list1))
list2 = [2, 33, 55, 4, 42, 21, 332, 77]
print(quickSort(list2))
