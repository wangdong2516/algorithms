"""
    希尔排序
        希尔排序是一种分组插入排序算法
        1. 首先取一个整数d1 = n / 2,将元素分为d1个组，每组相邻两个元素之间的距离为d1,在各组内进行直接插入排序
        2. 取第二个整数d2=d1/2,重复上述分组排序过程，直到di=1,即所有元素在同一组内进行直接插入排序
        3. 希尔排序每趟并不使某些元素有序，而是使整体数据越来越接近有序，最后一趟排序使得所有数据有序
"""

from typing import List


def insert_sort_gap(li: List, gap: int) -> None:
    """
        带gap的插入排序
    """
    
    # 摸到的牌的下标
    for i in range(gap, len(li)):
        
        # 手里最后一张牌的下标
        j = i - gap
        
        # 摸到的牌
        tmp = li[i]

        while li[j] > tmp and j >= 0:
            li[j + gap] = li[j]
            j -= gap
        li[j + gap] = tmp


def shell_sort(li: List):
    """
        希尔排序
    """

    d = len(li) // 2

    while d >= 1:
        insert_sort_gap(li, d)
        d //= 2


li = [2, 5, 1, 9, 3, 6, 4, 8, 7]
shell_sort(li)
print(li)
