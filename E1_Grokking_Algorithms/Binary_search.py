# coding=utf-8
"""
@Author : captain
@Email: 
@createtime : 2022/10/27 0:01
@Note:
"""


def binary_search(list, item):
    left = 0
    right = len(list) - 1
    while left < right:
        mid = (left + right) // 2
        if list[mid] == item:
            return mid
        elif list[mid] < item:
            left = mid + 1
        else:
            right = mid - 1
    return None


list = [2, 3, 4, 5, 33, 49, 72, 245]
print(binary_search(list, 3))
print(binary_search(list, 34))
